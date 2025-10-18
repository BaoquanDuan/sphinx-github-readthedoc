# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
# 把项目根目录放进 sys.path，这样autodoc才能import到package
sys. path.insert(0, os.path.abspath('../..'))  # 根据实际目录调整

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



language = 'zh_CN'

templates_path = ['_templates']
exclude_patterns = ['recommonmark']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

<<<<<<< HEAD
=======
html_theme = 'sphinx_rtd_theme'
>>>>>>> fae03db2c18ef14198079983e285fc9bb716c510
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
