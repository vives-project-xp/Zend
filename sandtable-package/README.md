<!-- Aan te vullen -->

To do's als functionaliteit toegevoegd is:

in Command line - in sandtable-package directory:
- python3 -m pip install --upgrade build
- python3 -m build
- python3 -m pip install --upgrade twine
-  python3 -m twine upload dist/*
    * username: __token__
    * password: token from PyPI

In command line van interface directory:
- python3 -m pip install vives-sandtable_package_zend

In main.py van de server: from vives-sandtable_package_zend import [klassenaam]