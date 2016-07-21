"""Test oxymorons.misc"""
from __future__ import absolute_import

from .check import Check

from proselint.checks.oxymorons import misc as chk


class TestCheck(Check):
    """The test class for oxymoron.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for preferred_forms_check."""
        assert not self.passes("""It was an organized mess""")
        assert self.passes("""It was a terrible mess""")
            
