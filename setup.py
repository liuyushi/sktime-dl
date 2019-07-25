#! /usr/bin/env python
"""Install script for sktime"""

from setuptools import find_packages
from setuptools import setup
import codecs
import os
import re
import sys
import platform

try:
    import numpy as np
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("No module named 'numpy'. Please install "
                              "numpy first using `pip install numpy`.")

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(HERE, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


# raise warning for Python versions prior to 3.6
if sys.version_info < (3, 6):
    raise RuntimeError("sktime-dl requires Python 3.6 or later. The current"
                       " Python version is %s installed in %s."
                       % (platform.python_version(), sys.executable))

DISTNAME = 'sktime-dl'
DESCRIPTION = 'deep learning extension toolbox for sktime, a scikit-learn compatible toolbox for learning with time series/panel data'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'F. Király'
MAINTAINER_EMAIL = 'fkiraly@turing.ac.uk'
URL = 'https://github.com/uea-machine-learning/sktime-dl'
LICENSE = 'BSD-3-Clause'
DOWNLOAD_URL = 'https://pypi.org/project/sktime-dl/#files'
PROJECT_URLS = {
    'Issue Tracker': 'https://github.com/uea-machine-learning/sktime-dl/issues',
    'Documentation': 'https://uea-machine-learning.github.io/sktime-dl/',
    'Source Code': 'https://github.com/uea-machine-learning/sktime-dl'
}
VERSION = find_version('sktime_dl', '__init__.py')
INSTALL_REQUIRES = [
    'keras_contrib @ git+https://github.com/keras-team/keras-contrib.git@master',
    'sktime>=0.2.0',
    'keras>=2.2.4',
    'tensorflow>=1.8.0'  # and/or tensorflow-gpu 1.8.0
]
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib'
    ]
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      include_dirs=[np.get_include()]
      )
