from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        [
            Extension(
                "toolbox.testwrapper",
                ["src/toolbox/testwrapper.pyx", "src/cpp/hello.cpp"],
                include_dirs=["src/cpp"],
                language="c++",
            )
        ]
    )
)
