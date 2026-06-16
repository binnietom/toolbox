# toolbox

![PyPI version](https://img.shields.io/pypi/v/toolbox.svg)

A numerical toolbox for mathematical methods in science, engineering and beyond.

* [GitHub](https://github.com/binnietom/toolbox/) | [PyPI](https://pypi.org/project/toolbox/) | [Documentation](https://binnietom.github.io/toolbox/)
* Created by [Thomas Binnie](https://audrey.feldroy.com/) | GitHub [@binnietom](https://github.com/binnietom) | PyPI [@binnietom](https://pypi.org/user/binnietom/)
* MIT License

## Features

* TODO

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

## Author

toolbox was created in 2026 by Thomas Binnie.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
