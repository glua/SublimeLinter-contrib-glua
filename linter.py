#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Lua plugin class."""

from SublimeLinter.lint import Linter, util


class Lua(Linter):

    """Provides an interface to gluac -p."""

    syntax = 'lua'
    cmd = 'gluac -p * -'
    regex = r'^.+?:.+?:(?P<line>\d+): (?P<message>.+?(?:near (?P<near>\'.+\')|$))'
    error_stream = util.STREAM_STDOUT
