import unittest
import sys
from test.support.warnings_helper import check_py2x_warnings
import warnings

if not sys.py2x_warning:
    raise unittest.SkipTest('%s must be run with the -2 flag' % __name__)

class TestPy2xWarnings(unittest.TestCase):

    def assertWarning(self, _, warning, expected_message):
        self.assertEqual(str(warning.message), expected_message)

    def assertNoWarning(self, _, recorder):
        self.assertEqual(len(recorder.warnings), 0)
