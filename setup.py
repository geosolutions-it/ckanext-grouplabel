from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ckanext-grouplabel',
    version = '0.1',
    description="Replaces group wording as category",
    long_description="Replaces group wording as category",
    author="Emanuele Tajariol",
    author_email="info@geosolutionsgroup.com",
    url='https://github.com/geosolutions-it/ckanext-grouplabel',
    license='AGPL',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext', 'ckanext.grouplabel'],
    include_package_data=True,
    package_data={},
    data_files=[],
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        grouplabel = ckanext.grouplabel.plugin:GroupLabelPlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',

    # Translations
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
