#!/usr/bin/env python3
"""yeller

Author:
    Josh Moulder <josh.moulder12@gmail.com>
"""

import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

HELP_TEXT = """
Yeller is the Yell CLI toolset -- a single command with multiple subcommands for automating 
repeatable tasks.
"""

VERSION_NUMBER = "#{VERSION}#"
"""The version number of the application, to print when calling with --version."""

def cli():
    print("Hello World")