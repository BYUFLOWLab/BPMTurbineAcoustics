#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='BPM_Acoustic_Model',
    version='2.0.0',
    description='BPM acoustic model for turbine noise prediction',
    author='Eric B. Tingey',
    author_email='ebtingey@byu.edu',
    url='https://github.com/byuflowlab/bpm-turbine-acoustics',
    package_dir={'': 'acoustic_model'},
    packages=['data'],
    py_modules=['BPM_Acoustic_Model'],
    license='MIT License',
    zip_safe=False
)

from numpy.distutils.core import setup, Extension
setup(
    name='bpmacoustic',
    version='2.0.0',
    package_dir={'': 'acoustic_model'},
    ext_modules=[Extension('_bpmacoustic', ['acoustic_model/BPM_Acoustic_Model.f90'], extra_compile_args=['-O2'])],
)
