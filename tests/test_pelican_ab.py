# -*- coding: utf-8 -*-
import os
import unittest

import jinja_ab
import pelican_ab

from shutil import rmtree
from tempfile import mkdtemp

from pelican import Pelican
from pelican.settings import read_settings


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(CURRENT_DIR, "content")
THEME_PATH = os.path.join(CURRENT_DIR, "themes")


class TestPelicanAB(unittest.TestCase):
    """
        Experiments are defined in themes/simple/templates/article.html
    """
    def _render(self, run=True):
        self.temp_path = mkdtemp(prefix='pelican-ab.')
        settings = read_settings(path=None,
                                 override={
                                    'PATH': INPUT_PATH,
                                    'OUTPUT_PATH': self.temp_path,
                                    'THEME': os.path.join(THEME_PATH,
                                                          'simple'),
                                    'PLUGINS': [pelican_ab]})
        self.pelican = Pelican(settings)
        if run:
            self.pelican.run()

    def setUp(self):
        self.temp_path = None

    def tearDown(self):
        if jinja_ab._ENV in os.environ:
            del os.environ[jinja_ab._ENV]

        if self.temp_path:
            rmtree(self.temp_path)

    def test_jinja_ab_extension_is_added_to_settings(self):
        """
            WHEN this plugin is configured,
            THEN JINJA_EXTENSIONS settings are updated
            NOTE: In Pelican 3.7.0 and later the setting is
                JINJA_ENVIRONMENT['extensions']
        """
        self._render(False)
        # Pelican 3.6.x
        if 'JINJA_EXTENSIONS' in self.pelican.settings:
            added = any([issubclass(x, jinja_ab.JinjaAbExperimentExtension)
                        for x in self.pelican.settings['JINJA_EXTENSIONS']])
        else:
            # Pelican >= 3.7.0
            added = any([issubclass(x, jinja_ab.JinjaAbExperimentExtension)
                        for x in self.pelican.settings[
                                    'JINJA_ENVIRONMENT'
                                ]['extensions']])

        self.assertTrue(added)

    def test_render_the_control_experiment(self):
        """
            WHEN AB_EXPERIMENT is not configured,
            THEN the control experiment is rendered
        """
        self._render()
        sample_output = open(os.path.join(self.temp_path,
                                          'a-sample-page.html'), 'r').read()
        # verify correct text is rendered
        self.assertTrue('This is the control experiment' in sample_output)
        self.assertFalse('This is v1 experiment' in sample_output)
        # verify URLs are not changed
        self.assertTrue('href="/a-sample-page.html"' in sample_output)
        self.assertTrue('href="/author/mr-senko.html"' in sample_output)

    def test_render_experiment_v1(self):
        """
            WHEN AB_EXPERIMENT is configured,
            THEN that particular experiment is rendered

            NOTE: for mutation testing 'c1' < 'control' < 'v1'
        """
        v1 = 'v1'
        os.environ[jinja_ab._ENV] = v1

        self._render()
        sample_output = open(os.path.join(self.temp_path, v1,
                                          'a-sample-page.html'), 'r').read()
        # verify correct text is rendered
        self.assertFalse('This is the control experiment' in sample_output)
        self.assertTrue('This is v1 experiment' in sample_output)
        # verify URLs have been changed to point to objects from the experiment
        # NOTE:
        # a-simple-page.html is {{ article.url }} aka Content.url
        # author/mr-senko.html is {{ author.url }} aka URLWrapper.url
        # both are monkey-patched by this plugin and tested here
        self.assertTrue('href="/%s/a-sample-page.html"' % v1 in sample_output)
        self.assertTrue('href="/%s/author/mr-senko.html"' % v1 in
                        sample_output)

    def test_if_DELETE_OUTPUT_DIRECTORY_is_true_then_raise(self):
        """
            WHEN DELETE_OUTPUT_DIRECTORY is True
            THEN we'll raise an exception
        """
        settings = read_settings(path=None,
                                 override={
                                    'DELETE_OUTPUT_DIRECTORY': True,
                                    'PLUGINS': [pelican_ab]})
        pelican = Pelican(settings)
        with self.assertRaises(RuntimeError):
            pelican.run()

    def test_render_experiment_c1(self):
        """
            WHEN AB_EXPERIMENT is configured,
            THEN that particular experiment is rendered

            NOTE: for mutation testing 'c1' < 'control' < 'v1'
        """
        c1 = 'c1'
        os.environ[jinja_ab._ENV] = c1

        self._render()
        sample_output = open(os.path.join(self.temp_path, c1,
                                          'a-sample-page.html'), 'r').read()
        # verify correct text is rendered
        self.assertFalse('This is the control experiment' in sample_output)
        self.assertTrue('This is c1 experiment' in sample_output)
        # verify URLs have been changed to point to objects from the experiment
        # NOTE:
        # a-simple-page.html is {{ article.url }} aka Content.url
        # author/mr-senko.html is {{ author.url }} aka URLWrapper.url
        # both are monkey-patched by this plugin and tested here
        self.assertTrue('href="/%s/a-sample-page.html"' % c1 in sample_output)
        self.assertTrue('href="/%s/author/mr-senko.html"' % c1 in
                        sample_output)
