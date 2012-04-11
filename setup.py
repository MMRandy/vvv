"""

    Yo dawg

"""

from setuptools import setup

LONG_DESCRIPTION = open("README.rst").read()

setup(name = "vvv",
    version = "0.1",
    long_description = LONG_DESCRIPTION,
    description = "A convenience utility for software source code validation and linting",
    author = "Mikko Ohtamaa",
    author_email = "mikko@opensourcehacker.com",
    url = "https://github.com/miohtama/vvv",
    install_requires = ["setuptools", 
        "PyYAML==3.10",
        "plac==0.9.0",
        "requests==0.11.1"
    ],
    packages = ['vvv'],
    classifiers=[
        "Programming Language :: Python",
    ],     
    license="GPL",
    include_package_data = True,
    entry_points="""
      # -*- Entry points: -*-
      [vvv]
      tabs=vvv.validators.tabs:TabsPlugin
      linelength = vvv.validators.linelength:LineLengthPlugin
      css = vvv.validators.css:CSSPlugin
      jshint = vvv.validators.jshint:JSHintPlugin
      pylint = vvv.validators.pylint:PylintPlugin
      pdb = vvv.validators.pdb:PdbPlugin
      rst = vvv.validators.rst:RestructuredTextPlugin

      [console_scripts]
      vvv = vvv.main:entry_point
      vvv-install-git-pre-commit-hook = vvv.hooks.git:setup_hook
      vvv-validate-rst = vvv.scripts.validaterst:run
      vvv-expand-tabs = vvv.scripts.expandtabs:run
      """,        
) 