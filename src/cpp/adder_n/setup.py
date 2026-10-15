from setuptools import Extension, setup

setup(
    name="adder",
    version="0.1.0",
    ext_modules=[
        Extension(
            name="adder",
            sources=["adder.c"],
        )
    ],
)