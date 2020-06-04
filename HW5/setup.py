from distutils.core import setup, Extension


def main():
      setup(name="PackageName",
            version="1.0",
            description="this is a package for matrix",
            ext_modules=[Extension("matrix", sources=["matrix.c"])])


if __name__ == '__main__':
      main()
