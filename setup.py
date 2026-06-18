"""setup.py

Used for installing Yeller via pip.
"""

from setuptools import setup


def repo_file_as_string(file_path: str) -> str:
    with open(file_path, "r") as repo_file:
        return repo_file.read()


def get_version():
    version_globals = {}
    with open("version.py", "r") as version_file:
        exec(version_file.read(), version_globals)
    return version_globals["yeller_version"]

setup(
    name='yeller',
    version=get_version(),
    long_description=repo_file_as_string("README.md"),
    long_description_content_type="text/markdown",
    author="Josh Moulder",
    author_email="josh.moulder12@gmail.com",
    url="https://github.com/oimoulder/yeller",
    python_requires=">=3.10",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Terminals",
        "Topic :: Utilities"
    ],
    keywords="cli automation devops sre plugin",
    py_modules=[
        'yeller',
        'version',
        'hello',
        'install_dev',
        'new_tf_project',
    ],
    install_requires=[
        "click>=8.1.8,<9",
        "jinja2>=3.1.6,<4",
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
        'scripts/windows.ps1',
        'scripts/ubuntu.sh',
        'scripts/redhat.sh',
        'scripts/rocky.sh',
    ],
)
