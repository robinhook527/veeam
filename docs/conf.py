project = 'veeam'
author = 'veeam'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="msvalidate.01" content="ED7B3FDEFFA814A0FDE88335A1C1C2E6" />
    """
}

# Base URL for sitemap
html_baseurl = 'https://veeam.readthedocs.io/en/latest/'
