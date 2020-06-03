from distutils.core import setup, Extension

setup(name="PackageName",
      version="1.0",
      description="this is a package for matrix",
      ext_modules=[Extension("matrix", sources=["matrix.c"])])