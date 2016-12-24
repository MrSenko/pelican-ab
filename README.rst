Pelican A/B testing plugin
--------------------------

.. image:: https://img.shields.io/travis/MrSenko/pelican-ab/master.svg
   :target: https://travis-ci.org/MrSenko/pelican-ab
   :alt: Build status


This is an A/B testing plugin for Pelican. It allows you to encode
experiments in your templates and renders the experiment selected by
the ``AB_EXPERIMENT`` environment variable. 'control' is the default
experiment name if ``AB_EXPERIMENT`` is not specified!

To install::

    pip install pelican-ab


Enable the plugin in ``pelicanconf.py`` like this::


    PLUGIN_PATHS = ['path/to/pelican-ab']
    PLUGINS = ['pelican_ab']

``PLUGIN_PATHS`` can be a path relative to your settings file or an absolute
path. Alternatively, if plugins are in an importable path, you can omit
``PLUGIN_PATHS`` and list them::

    PLUGINS = ['pelican_ab']

or you can ``import`` the plugin directly and give the module name instead::

    import pelican_ab
    PLUGINS = [pelican_ab]


The template syntax is provided by the
`jinja-ab <https://github.com/MrSenko/jinja-ab>`_ extension
which is automatically loaded::

    {% experiment control %}This is the control{% endexperiment %}
    {% experiment v1 %}This is version 1{% endexperiment %}

Alternative syntax is also supported::

    {% ab control %}This is the control{% endab %}
    {% ab v1 %}This is version 1{% endab %}

You can also mix the two tags in a single template::

    {% experiment control %}This is the control{% endexperiment %}
    {% ab v1 %}This is version 1{% endab %}

Single and double quoted names are also supported!


How to test and publish experiments
===================================

For local development use the command::

    AB_EXPERIMENT="xy" make regenerate

or::

    AB_EXPERIMENT="xy" make html

together with ``make serve`` to review the experiments.
When you are ready to publish them online use::

    rm -rf output/
    make github
    AB_EXPERIMENT="01" make github
    AB_EXPERIMENT="02" make github

See the section about ``DELETE_OUTPUT_DIRECTORY`` for more info.

Output files
============

After encoding your experiments into the theme templates you can generate the
resulting HTML files like this::

    AB_EXPERIMENT="v1" make html

When rendering experiments the resulting HTML files are saved under
``OUTPUT_PATH`` plus the experiment name. For example 'output/v1', 'output/v2',
etc. The control experiments are rendered directly under ``OUTPUT_PATH``.

This plugin automatically updates the ``Content.url`` and ``URLWrapper.url``
class properties from Pelican so that things like ``{{ article.url }}``
and ``{{ author.url }}``
will point to URLs from the same experiment. In other words each experiment
produces its own HTML and URL structure, using the experiment name as
prefix. For example 'blog/about-me.html' becomes 'v1/blog/about-me.html'.


DELETE_OUTPUT_DIRECTORY
========================

By default ``publishconf.py`` has ``DELETE_OUTPUT_DIRECTORY`` set to True
which causes pelican-ab to raise an exception. The problem is that you need to
execute ``make publish`` or ``make github`` for each experiment you'd like to
publish online. When ``DELETE_OUTPUT_DIRECTORY`` is True the previous
contents will be deleted and **ONLY** that variation will be published!
This will break your website because everything will be gone!

CHANGELOG
=========

* v0.2.4 (Dec 25th 2016)
    - add more tests
    - enable pylint during testing
    - fix bad ``super()`` call
* v0.2.3 (Dec 13th 2016)
    - rebuilt for Pelican v3.7.0 which now expects
      Jinja2 extensions in the ``JINJA_ENVIRONMENT`` setting instead of
      ``JINJA_EXTENSIONS``.
* v0.2.2 (May 12th 2016)
    - raise RuntimeError if ``DELETE_OUTPUT_DIRECTORY`` is set to True
* v0.2.1 (May 11th 2016)
    - updated README
* v0.2.0 (May 10th 2016)
    - initial release


Contributing
============

Source code and issue tracker are at https://github.com/MrSenko/pelican-ab


Commercial support
==================

`Mr. Senko <http://MrSenko.com>`_ provides commercial support for open source
libraries, should you need it!
