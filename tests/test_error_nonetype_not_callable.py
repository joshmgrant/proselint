"""Test version number."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
import subprocess


class TestCheck(Check):
    """Test class for version number."""

    __test__ = True

    def test_demo(self):
        """Make sure the version number is correct."""
        out = subprocess.check_output("proselint --demo", shell=True)
        assert "Exception TypeError" not in out
