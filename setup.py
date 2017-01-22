"""Setup script for Contour."""
from setuptools import setup


setup(
    name = 'contour',
    version = '0.1',
    packages = ['contour'],
    install_requires = [
        'click',
        'appdirs',
        'configobj',
        'requests',
        'bson',
    ],
    entry_points = '''
        [console_scripts]
        contourauthority=contour.authorityconsole:cli
        contourauditor=contour.auditorconsole:cli
    ''',
)