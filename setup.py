from setuptools import setup

setup(
    name='gpandas',
    version = '0.1',
    url='https://github.com/ebravofm/gpandas',
    keywords = 'pandas dataframes google-sheets google-spreadsheets python data data-science data-analytics google sheets oauth2',
    author='Emilio Bravo',
    author_email='ebravofm@gmail.com',
    packages=['gpandas'],
    install_requires=['pandas', 'requests', 'xlrd'],
    version='0.1',
    license = 'Apache License 2.0',
    description='Simple tool for quickly reading a public google spreasheet. Does not require Google OAuth.',
)