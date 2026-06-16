"""Tests for `toolbox` package."""

import toolbox

from toolbox.testwrapper import hello as hello_py

hello_py()

def test_import():
    """Verify the package can be imported."""
    assert toolbox
