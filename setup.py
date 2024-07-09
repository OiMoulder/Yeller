"""setup.py

Used for installing Yeller via pip.
"""

from setuptools import setup
from version import yeller_version

def repo_file_as_string(file_path: str) -> str:
    with open(file_path, "r") as repo_file:
        return repo_file.read()

setup(
    name='yeller',
    version=yeller_version,
    long_description=repo_file_as_string("README.md"),
    long_description_content_type="text/markdown",
    author="Josh Moulder",
    author_email="josh.moulder12@gmail.com",
    url="https://github.com/oimoulder/yeller",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Terminals",
        "Topic :: Utilities"
    ],
    keywords="cli automation devops sre plugin",
    py_modules=['yeller'],
    install_requires=[
        'Click',
    ],
    package_data={
        '': ['README.md'],
    },
    entry_points={
        'console_scripts': [
            'yeller=yeller:cli',
        ],
    },
    scripts=[
        'hello.py',
        'install_dev.py',
    ],
)
