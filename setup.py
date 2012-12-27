from setuptools import setup

setup(name='nosecomplete',
      version='0.0.2',
      description='nosecomplete is a nose plugin used for completing test names from the command line',
      author='Alon Horev',
      author_email='alon@horev.net',
      url='https://github.com/alonho/nosecomplete',
      classifiers = ["Development Status :: 3 - Alpha",
                     "Intended Audience :: Developers",
                     "Operating System :: POSIX :: Linux",
                     "Operating System :: MacOS :: MacOS X",
                     "Programming Language :: Python :: 2.7"],
      license='BSD',
      py_modules=['nosecomplete'],
      install_requires=['nose'],
      entry_points={'console_scripts': ['nosecomplete=nosecomplete:main']})
