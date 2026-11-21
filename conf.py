# Configuration file for the Sphinx documentation builder.

project = 'VectorGrid Data Collection Tools'
copyright = '2026, VectorGrid Africa Consortium'
author = 'VectorGrid Team'
release = '1.0.0'
html_title = 'VectorGrid Data Collection Tools'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
]

html_context = {
    'default_mode': 'light',
}

html_theme_options = {
    'use_repository_button': False,
    'use_download_button': False,
    'use_fullscreen_button': True,
    'home_page_in_toc': False,
    'show_navbar_depth': 1,
    'max_navbar_depth': 3,
}
