# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.append(os.path.abspath('..'))

project = 'CASA-FITS'
copyright = '2025, akimasanishida'
author = 'akimasanishida'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
]

napoleon_google_docstring = True
autosummary_generate = True
add_module_names = False
autodoc_member_order = 'bysource'

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_favicon = 'https://raw.githubusercontent.com/skrbcr/skrbcr.github.io/refs/heads/main/docs/favicon.png'
