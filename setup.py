from distutils.core import setup

setup(
    name = "pylru",
    version = "1.0.6",
    py_modules=['pylru'],
    description = "A least recently used (LRU) cache implementation",
    author = "Jay Hutchinson",
    author_email = "jlhutch+pylru@gmail.com",
    url = "http://github.com/jlhutch/pylru",
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description=open('README.txt').read())


