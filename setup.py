from setuptools import setup
from setuptools.extension import Extension
# TODO: include generated c and include switches if cython is not available ->
# https://stackoverflow.com/questions/4505747/how-should-i-structure-a-python-package-that-contains-cython-code
from Cython.Distutils import build_ext
# TODO: bootstrap numpy ->
# https://stackoverflow.com/questions/19919905/how-to-bootstrap-numpy-installation-in-setup-py
import numpy
import scipy
import sys

if sys.platform == 'win32':
    ext_modules = [
        Extension("c_matrix",
                  ["glotaran/models/kinetic/c_matrix.pyx"],
                  include_dirs=[numpy.get_include(), scipy.get_include()],
                  extra_compile_args=["-O3", "-ffast-math", "-march=native",
                                      "-fopenmp"],
                  extra_link_args=['-fopenmp']),
        Extension("c_matrix_gaussian_irf",
                  ["glotaran/models/kinetic/c_matrix_gaussian_irf.pyx"],
                  include_dirs=[numpy.get_include(), scipy.get_include()],
                  extra_compile_args=["-O3", "-ffast-math", "-march=native",
                                      "-fopenmp"],
                  extra_link_args=['-fopenmp'])
                  ]
else:
    ext_modules = [
        Extension("c_matrix",
                  ["glotaran/models/kinetic/c_matrix.pyx"],
                  include_dirs=[numpy.get_include(), scipy.get_include()],
                  libraries=["m"],
                  extra_compile_args=["-O3", "-ffast-math", "-march=native",
                                      "-fopenmp"],
                  extra_link_args=['-fopenmp']),
        Extension("c_matrix_gaussian_irf",
                  ["glotaran/models/kinetic/c_matrix_gaussian_irf.pyx"],
                  include_dirs=[numpy.get_include(), scipy.get_include()],
                  libraries=["m"],
                  extra_compile_args=["-O3", "-ffast-math", "-march=native",
                                      "-fopenmp"],
                  extra_link_args=['-fopenmp'])
                  ]


setup(
    name="glotaran",
    version="0.1.0",
    description='The Glotaran fitting engine.',
    url='http://glotaran.org',
    author='Joris Snellenburg, Stefan Schuetz, Joern Weissenborn',
    author_email="""j.snellenburg@vu.nl,
                    YamiNoKeshin@gmail.com,
                    joern.weissenborn@gmail.com""",
    license='GPLv3',
    packages=[
              'glotaran.datasets',
              'glotaran.model',
              'glotaran.models.kinetic',
              'glotaran.models.kinetic.c_matrix_opencl',
              'glotaran.specification_parser'
              ],
    install_requires=[
        'numpy',
        'scipy',
        'lmfit',
        'pyyaml',
    ],
    package_data={'glotaran.models.kinetic.c_matrix_opencl':
                  ['*.cl']},
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    test_suite='nose.collector',
    tests_require=['nose'],
)
