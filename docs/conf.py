# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

import os
import sys
import traceback
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "PyThaiNLP"
copyright = "2019, pythainlp_builders"
author = "pythainlp_builders"

curyear = datetime.today().year
copyright = f"2017-{curyear}, {project} (Apache Software License 2.0)"


# -- Get version information and date from Git ----------------------------

try:
    from subprocess import check_output, STDOUT

    current_branch = (
        os.environ["CURRENT_BRANCH"]
        if "CURRENT_BRANCH" in os.environ
        else check_output(
            ["git", "symbolic-ref", "HEAD"], shell=False, stderr=STDOUT
        )
        .decode()
        .strip()
        .split("/")[-1]
    )
    release = (
        os.environ["RELEASE"]
        if "RELEASE" in os.environ
        else check_output(
            ["git", "describe", "--tags", "--always"],
            shell=False,
            stderr=STDOUT,
        )
        .decode()
        .strip()
        .split("-")[0]
    )
    today = (
        os.environ["TODAY"]
        if "TODAY" in os.environ
        else check_output(
            ["git", "show", "-s", "--format=%ad", "--date=short"],
            shell=False,
            stderr=STDOUT,
        )
        .decode()
        .strip()
    )
except Exception as e:
    traceback.print_exc()
    release = "<unknown>"
    today = "<unknown date>"
    current_branch = "<unknown>"

# The short X.Y version
version = f"{current_branch} ({release}) <br /> Published date: {today}"

# The full version, including alpha/beta/rc tags
release = release


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
]
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"display_version": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pythainlpdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "pythainlp.tex",
        "PyThaiNLP Documentation",
        "pythainlp\\_builders",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pythainlp", "PyThaiNLP Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "pythainlp",
        "PyThaiNLP Documentation",
        author,
        "pythainlp",
        "Python library for Thai language processing",
        "Manual",
    )
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "NLTK": ("http://www.nltk.org", None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Markdown

# from recommonmark.parser import CommonMarkParser
# source_parsers = {'.md': CommonMarkParser}
# source_suffix = ['.rst', '.md']
