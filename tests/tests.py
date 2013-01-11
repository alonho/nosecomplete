import unittest
import nosecomplete

FIXTURES = {
    'basic': 'tests/fixtures/basic.py',
}

class _BaseTestFinderTestCase(unittest.TestCase):

    def test_complete(self):
        # this prints to the screen.. just make sure the code's not broken
        nosecomplete.complete(self.finder, FIXTURES['basic'])
    
    def test_basic(self):
        actual = list(self.finder.get_module_tests(FIXTURES['basic']))
        expected = [
            'AwesomeTestCase.test_green',
            'AwesomeTestCase.test_yellow',
            'test_red',
            'test_blue',
        ]
        self.assertEqual(set(actual), set(expected))
        
    def _assert_complete(self, thing, options):
        self.assertEqual(set(nosecomplete._complete(self.finder, thing)),
                         set(options))

    def test_dir_prefix(self):
        self._assert_complete('tests/fixtures', ['/'])
        
    def test_dir(self):
        try:
            options = ['fixtures/', '__init__.py:', 'tests.py:']
            self._assert_complete('tests/', options)
        except AssertionError:
            options.append('__pycache__/') # py3 leaves these around
            self._assert_complete('tests/', options)
                
    def test_partial_filename(self):
        self._assert_complete('tests/fixtures/ba', ['sic.py:'])
        
    def test_filename(self):
        self._assert_complete('tests/fixtures/basic.py', [':'])

    def test_partial_case(self):
        self._assert_complete('tests/fixtures/basic.py:test', ['_red', '_blue'])

    def test_partial_class(self):
        self._assert_complete('tests/fixtures/basic.py:AwesomeTestCase', ['.'])

    def test_partial_method(self):
        self._assert_complete('tests/fixtures/basic.py:AwesomeTestCase.',
                              ['test_green',
                               'test_yellow'])
        
class NoseTestFinderTestCase(_BaseTestFinderTestCase):
    finder = nosecomplete.NoseTestFinder()
    
class PythonTestFinderTestCase(_BaseTestFinderTestCase):
    finder = nosecomplete.PythonTestFinder()

