# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Freightol'
copyright = '2021, Freightol'
author = 'Freightol'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'notfound.extension',
    'hoverxref.extension',
    'sphinx_search.extension',
    'sphinxemoji.sphinxemoji',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
