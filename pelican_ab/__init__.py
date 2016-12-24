# pylint: disable=protected-access,missing-docstring,invalid-name
import os

import jinja_ab

from pelican import signals
from pelican.writers import Writer
from pelican.contents import Content
from pelican.urlwrappers import URLWrapper

_orig_content_url = Content.url
_orig_urlwrapper_url = URLWrapper.url


class PelicanAbExperimentWriter(Writer):
    """
        This writer knows how to write templates, which
        contain A/B experiments markup.

        Each experiment is written under a separate directory
        structure, duplicating output/ only with this experiment
        values. To use execute

        AB_EXPERIMENT=v1 make html
    """
    def __init__(self, output_path, settings=None):
        if settings['DELETE_OUTPUT_DIRECTORY']:
            raise RuntimeError('DELETE_OUTPUT_DIRECTORY is set to True. \
                                See pelican-ab/README.rst!')

        super(PelicanAbExperimentWriter, self).__init__(output_path, settings)

        experiment = os.environ.get(jinja_ab._ENV, jinja_ab._ENV_DEFAULT)
        if experiment != jinja_ab._ENV_DEFAULT:
            # all Content and URLWrapper objects are saved under $experiment/
            # and their URLs are updated as well. Static content and SITEURL
            # are not affected by this! Only HTML files are!
            self.output_path = os.path.join(self.output_path, experiment)
            # pylint: disable=no-member
            Content.url = property(lambda s: experiment + '/' +
                                   _orig_content_url.fget(s))
            URLWrapper.url = property(lambda s: experiment + '/' +
                                      _orig_urlwrapper_url.fget(s))
        else:
            # restore the monkey patch. This is useful in unit-tests
            # and also if this module has been loaded and kept in memory
            # but Pelican.run() will be executed multiple times.
            # Without this block the default properties will not be restored
            # once we try to render the control variant if another experiment
            # has been rendered before that!
            Content.url = _orig_content_url
            URLWrapper.url = _orig_urlwrapper_url


def pelican_experiment_plugin(_sender):
    """ Return the writer to be used by Pelican. """
    return PelicanAbExperimentWriter


def add_jinja2_ext(pelican):
    """ Add JinjaExperimentExtension to Pelican settings. """
    # Pelican >= 3.7.0
    if 'JINJA_ENVIRONMENT' in pelican.settings:
        if 'extensions' in pelican.settings['JINJA_ENVIRONMENT']:
            pelican.settings['JINJA_ENVIRONMENT']['extensions'].append(
                jinja_ab.JinjaAbExperimentExtension)
        else:
            pelican.settings['JINJA_ENVIRONMENT']['extensions'] = [
                jinja_ab.JinjaAbExperimentExtension]
    else:
        # Pelican < 3.7.0
        pelican.settings['JINJA_EXTENSIONS'].append(
            jinja_ab.JinjaAbExperimentExtension)


def register():
    """ Register this plugin with Pelican. """
    signals.initialized.connect(add_jinja2_ext)
    signals.get_writer.connect(pelican_experiment_plugin)
