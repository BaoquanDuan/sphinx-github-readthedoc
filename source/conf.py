# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
# 把项目根目录放进 sys.path，这样autodoc才能import到package
sys.path.insert(0, os.path.abspath('../..'))  # 根据实际目录调整

project = 'CHESS'
copyright = '2025, SunPeng'
author = 'SunPeng'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",                # 支持 Markdown（MyST）
    "sphinx.ext.autodoc",         # 自动从 docstring 生成 API
    "sphinx.ext.viewcode",        # 在文档中添加源码链接
    "sphinx.ext.autosummary",     # 可生成 API 概览表（配合 autosummary_generate）
]
extensions = [
'sphinx_markdown_tables',    
'sphinx_rtd_theme',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', 'rest', '.md']



html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

language = 'zh_CN'

templates_path = ['_templates']
exclude_patterns = ['recommonmark']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
