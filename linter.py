#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Clifton Kaznocha
# Copyright (c) 2015 Clifton Kaznocha
#
# License: MIT
#

"""This module exports the ProtocGenLint plugin class."""
from SublimeLinter.lint import Linter, util, highlight


class ProtocGenLint(Linter):
    """Provides an interface to protoc-gen-lint."""

    syntax = 'protobuf'
    cmd = 'protoc --lint_out=. -I=/'
    regex = r'''(?xi)
        ^.+\.proto:(?P<line>\d+):(?P<col>\d+):\s(?P<message>(\'(?P<near>.*)\')?.*)$
    '''
    error_stream = util.STREAM_BOTH
    default_type = highlight.WARNING
    tempfile_suffix = 'proto'
