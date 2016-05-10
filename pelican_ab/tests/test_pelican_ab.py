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
OUTPUT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'output'))
INPUT_PATH = os.path.join(CURRENT_DIR, "content")


class TestPelicanAB(unittest.TestCase):
    def setUp(self):
        self.temp_path = mkdtemp(prefix='pelican-ab.')
        pelican_ab_path, _ = os.path.join(os.path.split(pelican_ab.__file__))
        self.pelican_ab_static = os.path.join(pelican_ab_path, 'static')
        self.settings = read_settings(path=None,
                                      override={
                                          'PATH': INPUT_PATH,
                                          'OUTPUT_PATH': self.temp_path,
                                          'PLUGINS': [pelican_ab]})
        self.pelican = Pelican(self.settings)
        self.pelican.run()
        pass

    def tearDown(self):
        rmtree(self.temp_path)
        pass

    def test_jinja_ab_extension_is_added_to_settings(self):
        """
            WHEN this plugin is configured,
            THEN JINJA_EXTENSIONS settings are updated
        """
        added = any([issubclass(x, jinja_ab.JinjaExperimentExtension)
                    for x in self.pelican.settings['JINJA_EXTENSIONS']])
        self.assertTrue(added)
