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


Output files
============

When rendering experiments the resulting HTML files are saved under
``OUTPUT_PATH`` plus the experiment name. For example 'output/v1', 'output/v2',
etc. The control experiments are rendered directly under ``OUTPUT_PATH``.

This plugin automatically updates the ``Content.url`` and ``URLWrapper.url``
class properties from Pelican so that things like ``{{ article.url }}``
and ``{{ author.url }}``
will point to URLs from the same experiment. In other words each experiment
produces its own HTML and URL structure, using the experiment name as
prefix. For example 'blog/about-me.html' becomes 'v1/blog/about-me.html'.


Contributing
============

Source code and issue tracker are at https://github.com/MrSenko/pelican-ab


Commercial support
==================

`Mr. Senko <http://MrSenko.com>`_ provides commercial support for open source
libraries, should you need it!
