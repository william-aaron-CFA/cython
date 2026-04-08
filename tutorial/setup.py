from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        ["primes.py",
         "primes_python_compiled.py"],
          annotate=True, force=True),
    py_modules = ['primes_python.py']
)