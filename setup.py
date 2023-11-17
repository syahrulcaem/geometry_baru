from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'MyGeometry is a simple Python library for calculating the area and perimeter of basic geometric shapes'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="mygeometri_hanifaslam",
    version=VERSION,
    author="hanifaslam",
    author_email="<aslamhanif141@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/syahrulcaem/new_mygeometry14',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['mal', 'myanimelist'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)