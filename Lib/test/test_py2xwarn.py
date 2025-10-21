import unittest
import sys
from test.support.warnings_helper import check_py2x_warnings
import warnings
from test import test_support
import tempfile


if not sys.py2x_warning:
    raise unittest.SkipTest('%s must be run with the -2 flag' % __name__)


class TestPy2xWarnings(unittest.TestCase):

    def assertWarning(self, _, warning, expected_message):
        self.assertEqual(str(warning.message), expected_message)

    def assertNoWarning(self, _, recorder):
        self.assertEqual(len(recorder.warnings), 0)

    def test_next(self):
        marks = [65, 71, 68, 74, 61]
        iterator_marks = iter(marks)
        expected = "The attribute 'x.next' is not supported in 3.x: use 'x.__next__'."

        with check_py2x_warnings() as w:
            self.assertWarning(iterator_marks.next(), w, expected)
            w.reset()
            self.assertNoWarning(iterator_marks.__next__(), w)
            
    def test_truncate0(self):
        expected = "Calling truncate(0) on text stream without seek(0)" + \
        " may produce inconsistent results. Use seek(0) before truncate(0)"
        with check_py2x_warnings(("", Py2xWarning)) as w:
            with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=True) as f:
                f.write("test")
                f.truncate(0)
                self.assertWarning((), w, expected)
            

if __name__ == '__main__':
    unittest.main()
