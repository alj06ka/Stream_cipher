from distutils.core import setup, Extension

cpp_args = ['-std=c++11']

module = Extension("binaryEncipher",
                   sources=['binaryEncipher.cpp'],
                   language="c++",
                   extra_compile_args=cpp_args)

setup(name="binaryEncipher",
      version="1.0",
      description="Binary Encipher",
      ext_modules=[module])
