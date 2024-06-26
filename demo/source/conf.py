# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '.'
copyright = '2024, aidan'
author = 'aidan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['quantinuum_docs_theme']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'quantinuum_docs_theme'
html_theme_options = {
     "navTextLinks": [
        {
            "title": "API Docs",
            "href": "/api-docs",
            "pathMatch": "somewhere",
        },
        {
            "title": "Examples",
            "href": "/examples",
            "pathMatch": "somewhere",
        },
        {
            "title": "Blog",
            "href": "/blog/",
            "pathMatch": "somewhere",
        },
        {
            "title": "User Manual",
            "href": "/user-manual",
            "pathMatch": "somewhere",
        },
    ],
    "navProductName": "TKET",
    "navIconLinks": [
        {
            "title": "TKET Github",
            "href": "https://github.com/CQCL/tket",
            "pathMatch": "somewhere",
            "iconImageURL": "/_static/github.svg",
        },
        {
            "title": "TKET Slack Channel",
            "href": "https://tketusers.slack.com/",
            "pathMatch": "somewhere",
            "iconImageURL": "/_static/slack.svg",
        },
        {
            "title": "TKET Stack Exchange",
            "href": "https://quantumcomputing.stackexchange.com/questions/tagged/pytket",
            "pathMatch": "somewhere",
            "iconImageURL": "/_static/stack.svg",
        },
    ],
}
html_static_path = ['_static']
