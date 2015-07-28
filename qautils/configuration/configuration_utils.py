# -*- coding: utf-8 -*-

"""
configuration_utils module has some functions to manage project configuration
    - set_up: Loads properties from properties.json file and configures the project.
              By default, properties file should be located at ./settings/settings.json
"""

__author__ = "@jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"


import os
import sys
import json

from qautils.logger.logger_utils import get_logger


__logger__ = get_logger(__name__)

# Env properties.
PROPERTIES_FILE = "./settings/settings.json"
PROPERTIES_CONFIG_ENV = "environment"
PROPERTIES_CONFIG_ENV_NAME = "name"

# Remote logs properties
PROPERTIES_CONFIG_REMOTE_LOGS = "remote_logs"
PROPERTIES_CONFIG_REMOTE_LOGS_CAPTURE_LOCAL_PATH = "capture_local_path"

# Generic service properties
PROPERTIES_CONFIG_SERVICE_PROTOCOL = "protocol"
PROPERTIES_CONFIG_SERVICE_HOST = "host"
PROPERTIES_CONFIG_SERVICE_PORT = "port"
PROPERTIES_CONFIG_SERVICE_RESOURCE = "resource"


# Loaded configuration
config = None


def _load_project_properties():
    """
    Parse the JSON configuration file located in the src folder and
    store the resulting dictionary in the config global variable.
    """

    __logger__.info("Loading project properties from %s", PROPERTIES_FILE)
    try:
        with open(PROPERTIES_FILE) as config_file:
            try:
                global config
                config = json.load(config_file)
            except Exception, e:
                __logger__.error('Error parsing config file: %s' % e)
                sys.exit(1)
    except IOError, e:
        __logger__.error('%s properties file CANNOT be opened: %s', PROPERTIES_FILE, e)

    __logger__.debug("Properties loaded: %s", config)


def set_up_project():
    """
    Setup execution and configure global test parameters and environment.
    :return: None
    """

    __logger__.info("Setting up test execution")
    _load_project_properties()

    """
    Make sure the logs path exists and create it otherwise.
    """
    if PROPERTIES_CONFIG_REMOTE_LOGS in config:
        __logger__.debug("Creating directory for remote log capturing defined in CONF.%s.%s",
                         PROPERTIES_CONFIG_REMOTE_LOGS,
                         PROPERTIES_CONFIG_REMOTE_LOGS_CAPTURE_LOCAL_PATH)
        log_path = config[PROPERTIES_CONFIG_REMOTE_LOGS][PROPERTIES_CONFIG_REMOTE_LOGS_CAPTURE_LOCAL_PATH]
        if not os.path.exists(log_path):
            os.makedirs(log_path)

    # Overrides if you need more project configurations
