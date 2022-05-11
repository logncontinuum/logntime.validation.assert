# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'logn.validation.assertions'
copyright = '2022, David B F Garcia Chavez'
author = 'David B F Garcia Chavez'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

extensions = [
    'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc'
]

html_css_files = [
    'css/custom.css'
]

autodoc_typehints_format = "short"
add_module_names = False

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'furo'
html_static_path = ['_static']
