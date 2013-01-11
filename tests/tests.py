import unittest
import nosecomplete

FIXTURES = {
    'basic': 'tests/fixtures/basic.py',
}

class _BaseTestFinderTestCase(unittest.TestCase):

    def test_basic(self):
        actual = list(self.finder.get_module_tests(FIXTURES['basic']))
        expected = [
            'AwesomeTestCase.test_green',
            'AwesomeTestCase.test_yellow',
            'test_red',
            'test_blue',
        ]
        self.assertEqual(set(actual), set(expected))

class NoseTestFinderTestCase(_BaseTestFinderTestCase):
    finder = nosecomplete.NoseTestFinder()
    
class PythonTestFinderTestCase(_BaseTestFinderTestCase):
    finder = nosecomplete.PythonTestFinder()
