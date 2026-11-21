# Configuration file for the Sphinx documentation builder.

project = 'VectorGrid Data Collection Tools'
copyright = '2026, VectorGrid Africa Consortium'
author = 'VectorGrid Team'
release = '1.0.0'
html_title = 'VectorGrid Data Collection Tools'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
]

html_theme_options = {
    'top_of_page_buttons': [],
    'light_css_variables': {
        'font-stack': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif',
        'font-stack--headings': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif',
        'font-stack--monospace': 'Consolas, Monaco, "Liberation Mono", monospace',
        'font-size--normal': '95%',
        'color-brand-primary': '#1d4e89',
        'color-brand-content': '#1d4e89',
        'color-table-header-background': '#f8fafc',
        'sidebar-item-font-size': '0.875rem',
        'sidebar-item-spacing-vertical': '0.35rem',
    },
    'dark_css_variables': {
        'color-brand-primary': '#60a5fa',
        'color-brand-content': '#60a5fa',
    },
}
