# Configuration file for the Sphinx documentation builder.

project = 'VectorGrid Data Collection Tools'
copyright = '2026, VectorGrid Africa Consortium'
author = 'VectorGrid Team'
release = '1.0.0'
html_title = 'VectorGrid Data Collection Tools'

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'style_external_links': False,
}
