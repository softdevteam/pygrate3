import unittest
import sys
from test.support.warnings_helper import check_py2x_warnings
import warnings
from test import test_support

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
            
    def test_dict(self):
        expected = [
            "dict_values() returns a view in 3.x, not a list. Use list(dict_values()) instead"
            "dict_keys() returns a view in 3.x, not a list. Use list(dict_keys()) instead"
            "dict_items() returns a view in 3.x, not a list. Use list(dict_items()) instead"
        ]
        test = {"a":1}
        
        with check_py2x_warnings() as w:
            self.assertWarning(test.values(), w, expected[0])
            w.reset()
            self.assertWarning(test.keys(), w, expected[1])
            w.reset()
            self.assertWarning(test.items(), w, expected[2])
            

if __name__ == '__main__':
    unittest.main()
