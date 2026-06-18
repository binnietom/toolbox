# toolbox

![PyPI version](https://img.shields.io/pypi/v/toolbox.svg)

A numerical toolbox for mathematical methods in science, engineering and beyond.

* [GitHub](https://github.com/binnietom/toolbox/) | [PyPI](https://pypi.org/project/toolbox/) | [Documentation](https://binnietom.github.io/toolbox/)
* Created by [Thomas Binnie](https://audrey.feldroy.com/) | GitHub [@binnietom](https://github.com/binnietom) | PyPI [@binnietom](https://pypi.org/user/binnietom/)
* MIT License

## Features

Tested the wrapping template.
Checked c++ tests and some bit shifting examples in cpp_tests

TODO Test wrapping template passes parameters.


## Installation & Usage

pip install cython
cd toolbox
python setup.py build_ext --inplace
pip install -e .
python tests/test_toolbox.py

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://binnietom.github.io/toolbox/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/toolbox.git
cd toolbox

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `toolbox`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Notes

Wrt accuracy I think it helps to understand floating point representation. Integers are easily represented in bits. S x M x B^(E-e) = any number, where S is a sign bit, M the mantissa (binary integer), and another integer that represents the digits beyond the decimal point.
From this all combinations of numbers up to a precision can be represented e.g. (-1)^S x 1.F x 2^(E-e), where floats have e = 127, double e = 1023.
Note that +/- 0 are different and +/- infty are the maximum 255-127 or 2047-1022. Nan is defined with digits beyond the resolution (i.e. an infty with non-zero F.

Floating point maths has some pitfalls TODO, give examples.

## Author

toolbox was created in 2026 by Thomas Binnie.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
