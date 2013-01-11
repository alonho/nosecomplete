from setuptools import setup

setup(name='nosecomplete',
      version='0.1.0',
      description='nosecomplete is a nose plugin used for completing test names from the command line, it supports both python 2 and 3.',
      author='Alon Horev',
      author_email='alon@horev.net',
      url='https://github.com/alonho/nosecomplete',
      classifiers = ["Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "Operating System :: POSIX :: Linux",
                     "Operating System :: MacOS :: MacOS X"],
      license='BSD',
      py_modules=['nosecomplete'],
      install_requires=['nose'],
      entry_points={'console_scripts': ['nosecomplete=nosecomplete:main']})
