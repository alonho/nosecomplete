import unittest
import nosecomplete

FIXTURES = {
    'basic': 'tests/fixtures/basic.py',
}


class NoseTestFinderTestCase(unittest.TestCase):
    def test_basic(self):
        finder = nosecomplete.NoseTestFinder()
        actual = list(finder.get_module_tests(FIXTURES['basic']))
        expected = [
            'AwesomeTestCase.test_green',
            'AwesomeTestCase.test_yellow',
            'test_red',
            'test_blue',
        ]
        self.assertEqual(actual, expected)


class PythonTestFinderTestCase(unittest.TestCase):
    def test_basic(self):
        finder = nosecomplete.PythonTestFinder()
        actual = list(finder.get_module_tests(FIXTURES['basic']))
        expected = [
            'test_red',
            'AwesomeTestCase.test_yellow',
            'AwesomeTestCase.test_green',
            'test_blue',
        ]
        self.assertEqual(actual, expected)
