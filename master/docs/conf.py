# -*- coding: utf-8 -*-
#
# Buildbot documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 10 15:13:31 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import textwrap

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'bbdocs.ext'
]
todo_include_todos=True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Buildbot'
copyright = u'Buildbot Team Members'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

if 'VERSION' in os.environ:
    version = os.environ['VERSION']
else:
    gl = {'__file__': '../buildbot/__init__.py'}
    execfile('../buildbot/__init__.py', gl)
    version = gl['version']
# The full version, including alpha/beta/rc tags.
release = version

# add a loud note for anyone looking at the latest docs
if release == 'latest':
    rst_prolog = textwrap.dedent("""\
    .. caution:: This page documents the latest, unreleased version of
        Buildbot.  For documentation for released versions, see
        http://docs.buildbot.net/.

    """)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'release-notes/*.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

intersphinx_mapping = {
    'python': ('http://python.readthedocs.org/en/latest/', None),
    'sqlalchemy': ('http://sqlalchemy.readthedocs.org/en/latest/', None),
}

extlinks = {
    'bug': ('http://trac.buildbot.net/ticket/%s', 'bug #'),
    'pull': ('https://github.com/buildbot/buildbot/pull/%s', 'pull request '),
    'src': ('https://github.com/buildbot/buildbot/blob/master/%s', None)
}

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'qtile'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'stickysidebar': 'true'}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [
    '_themes'
]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join('_images', 'header-text-transparent.png')

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = os.path.join('_static', 'buildbot.ico')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['searchbox.html', 'localtoc.html', 'relations.html', 'sourcelink.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

html_use_index = True
html_use_modindex = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Buildbotdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Buildbot.tex', u'Buildbot Documentation',
     u'Brian Warner', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = os.path.join('_images', 'header-text-transparent.png')

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = True

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'buildbot', u'Buildbot Documentation',
     [u'Brian Warner'], 1)
]


# Monkey-patch Sphinx to treat unhiglighted code as error.
import sphinx
import sphinx.highlighting

from pkg_resources import parse_version
from sphinx.errors import SphinxWarning

# Versions of Sphinx below changeset 1860:19b394207746 (before v0.6.6 release)
# won't work due to different PygmentsBridge interface.
required_sphinx_version = '0.6.6'
sphinx_version_supported = \
    parse_version(sphinx.__version__) >= parse_version(required_sphinx_version)

# This simple monkey-patch allows either fail on first unhighlighted block or
# print all unhighlighted blocks and don't fail at all.
# First behaviour is useful for testing that all code is highlighted, second ---
# for fixing lots of unhighlighted code.
fail_on_first_unhighlighted = True


class UnhighlightedError(SphinxWarning):
    pass

# PygmentsBridge.unhighlighted() added in Sphinx in changeset 574:f1c885fdd6ad
# (0.5 release).


def patched_unhighlighted(self, source):
    indented_source = '    ' + '\n    '.join(source.split('\n'))

    if fail_on_first_unhighlighted:
        msg = textwrap.dedent(u"""\
            Block not highlighted:

            %s

            If it should be unhighlighted, please specify explicitly language of
            this block as "none":

            .. code-block:: none

                ...

            If this block is Python example, then it probably contains syntax
            errors, such as unmatched brackets or invalid indentation.

            Note that in most places you can use "..." in Python code as valid
            anonymous expression.
            """) % indented_source
        raise UnhighlightedError(msg)
    else:
        msg = textwrap.dedent(u"""\
            Unhighlighted block:

            %s

            """) % indented_source
        sys.stderr.write(msg.encode('ascii', 'ignore'))

        return orig_unhiglighted(self, source)

# Compatible with PygmentsBridge.highlight_block since Sphinx'
# 1860:19b394207746 changeset (v0.6.6 release)


def patched_highlight_block(self, *args, **kwargs):
    try:
        return orig_highlight_block(self, *args, **kwargs)
    except UnhighlightedError, ex:
        msg = ex.args[0]
        if 'warn' in kwargs:
            kwargs['warn'](msg)

        raise

if sphinx_version_supported:
    orig_unhiglighted = sphinx.highlighting.PygmentsBridge.unhighlighted
    orig_highlight_block = sphinx.highlighting.PygmentsBridge.highlight_block

    sphinx.highlighting.PygmentsBridge.unhighlighted = patched_unhighlighted
    sphinx.highlighting.PygmentsBridge.highlight_block = patched_highlight_block
else:
    msg = textwrap.dedent("""\
        WARNING: Your Sphinx version %s is too old and will not work with
        monkey-patch for checking unhighlighted code.  Minimal required version
        of Sphinx is %s.  Check disabled.
        """) % (sphinx.__version__, required_sphinx_version)
    sys.stderr.write(msg)
