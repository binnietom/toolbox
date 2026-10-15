from setuptools import Extension, setup

setup(
    name="hello",
    version="0.1.0",
    ext_modules=[
        Extension(
            name="hello",
            sources=["hello.cpp", "hello_module.cpp"],
            language="c++",
        )
    ],
)
