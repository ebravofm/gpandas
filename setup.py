from setuptools import setup

setup(
    name='gpandas',
    url='https://github.com/ebravofm/gpandas',
    author='Emilio Bravo',
    author_email='ebravofm@gmail.com',
    packages=['gpandas'],
    install_requires=['pandas', 'requests', 'xlrd'],
    version='0.1',
    license='MIT',
    description='Read Google Sheets excel as pandas DataFrame.',
)