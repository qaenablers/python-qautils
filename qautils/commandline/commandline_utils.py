# -*- coding: utf-8 -*-

"""
    commandline_utils module contains utilities for executing local commands in the system
        - execute_command: Executes a new command
"""

__author__ = "@jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"

import subprocess
from subprocess import CalledProcessError

from qautils.logger.logger_utils import get_logger


__logger__ = get_logger(__name__)


def execute_command(command):
    """
    Execute the given command. Wait for command ends.
    :param command (String): The sequence of program arguments.
    :return (String): The command output when command has finished.
    """
    __logger__.debug("Executing command: '%s'", command)

    result = None
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except CalledProcessError, e:
        result = e.output
        __logger__.warning("Command execution failed. Command: '%s'; Output: '%s'", command, e.output)

    return result
