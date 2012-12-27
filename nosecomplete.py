import os
import sys
    
def _generate_tests(suite):
    from nose.suite import ContextSuite
    from nose.case import Test
    for context in suite._tests:
        if isinstance(context, Test):
            yield context
            continue
        assert isinstance(context, ContextSuite)
        for test in _generate_tests(context):
            yield test

def _get_test_name(test_wrapper):
    from nose.case import FunctionTestCase
    test = test_wrapper.test
    if isinstance(test, FunctionTestCase):
        return test.test.__name__
    return test.__class__.__name__ + '.' + test._testMethodName

def _generate_test_names(suite):
    from itertools import imap
    return imap(_get_test_name, _generate_tests(suite))

def get_module_tests(module):
    import nose
    loader = nose.loader.defaultTestLoader()
    return _generate_test_names(loader.loadTestsFromName(module))

def _get_prefixed(strings, prefix):
    for string in strings:
        if string.startswith(prefix):
            yield string.replace(prefix, '')

def _get_py_or_dirs(directory, prefix):
    for entry in os.listdir(directory or '.'):
        path = os.path.join(directory, entry)
        if entry.startswith(prefix) and (os.path.isdir(path) or entry.endswith('.py')):
            yield entry.replace(prefix, '')

def _complete(thing):
    if ':' in thing:
        # complete a test
        module, test_part = thing.split(':')
        tests = list(get_module_tests(module))
        if '.' in test_part:
            # complete a method
            return _get_prefixed(strings=tests, prefix=test_part)
        funcs = [test for test in tests if test.count('.') == 0]
        classes = [test.split('.')[0] for test in tests if '.' in test]
        if test_part in classes:
            # indicate a method should be completed
            return ['.']
        return _get_prefixed(strings=funcs + classes, prefix=test_part)
    if os.path.isdir(thing):
        # complete directory contents
        if thing != '.' and not thing.endswith('/'):
            return ['/']
        return os.listdir(thing)
    if os.path.exists(thing):
        # add a colon to indicate search for specific class/func
        return [':']
    # path not exists, complete a partial path
    directory, file_part = os.path.split(thing)
    return _get_py_or_dirs(directory, file_part)

def complete(thing):
    for option in _complete(thing):
        sys.stdout.write(thing + option + ' ') # avoid print for python 3

def main():
    if len(sys.argv) == 1:
        complete('./')
    else:
        complete(sys.argv[1])

if __name__ == '__main__':
    main()