# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Javet'
copyright = '2021. caoccao.com Sam Cao'
author = 'Sam Cao'

# The full version, including alpha/beta/rc tags
release = '1.0.7'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_inline_tabs',
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en, zh-CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '_static',
    '_templates',
    'Thumbs.db',
    '.DS_Store',
    '.history',
    '.gradle',
    '.idea',
    '.vscode',
    'node_modules',
    'scripts',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_show_sphinx = False
html_copy_source = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['resources']
html_css_files = [
    'css/custom.css',
]

html_logo = 'resources/images/logo.png'
html_favicon = 'resources/images/logo.ico'

extlinks = {
    'extsource0': ('https://github.com/caoccao/Javet/tree/main/%s', '%s'),
    'extsource1': ('https://github.com/caoccao/Javet/tree/main/1/%s', '%s'),
    'extsource2': ('https://github.com/caoccao/Javet/tree/main/1/2/%s', '%s'),
    'extsource3': ('https://github.com/caoccao/Javet/tree/main/1/2/3/%s', '%s'),
}
