from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Version and Description
VERSION = '0.1.0'
DESCRIPTION = 'A Python library for quantitative finance.'

# Setting up
setup(
    name="quantspy",
    license='MIT',
    version=VERSION,
    author="Eric YE Rongjun",
    author_email="<yerongjun03@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'scipy', 'matplotlib', "statsmodels", "cvxpy"],
    keywords=['python', 'quantitative', 'finance', 'mathematical models', 'statistics', 'mathematics', 'data analysis', 'visualization', 'data analytics', 'data science'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# python setup.py sdist bdist_wheel
# twine upload dist/*