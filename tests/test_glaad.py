"""Test GLAAD Guidelines."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.glaad import terms as chk


class TestCheck(Check):
    """The test class for glaad.terms."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk