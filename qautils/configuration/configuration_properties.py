# -*- coding: utf-8 -*-

"""
configuration_properties module has some functions to manage project configuration
    - This file contains a set of constants with the name of the properties used in examples/settings/settings.json
"""

__author__ = "@jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"


# Env properties.
PROPERTIES_FILE = "./conf/settings.json"
PROPERTIES_CONFIG_ENV = "environment"
PROPERTIES_CONFIG_ENV_NAME = "name"

# Remote logs properties
PROPERTIES_CONFIG_REMOTE_LOGS = "remote_logs"
PROPERTIES_CONFIG_REMOTE_LOGS_CAPTURE_LOCAL_PATH = "capture_local_path"

# Generic API service properties
PROPERTIES_CONFIG_SERVICE_PROTOCOL = "protocol"
PROPERTIES_CONFIG_SERVICE_HOST = "host"
PROPERTIES_CONFIG_SERVICE_PORT = "port"
PROPERTIES_CONFIG_SERVICE_RESOURCE = "resource"

# Generic API service properties
PROPERTIES_CONFIG_SERVICE_PROTOCOL = "protocol"
PROPERTIES_CONFIG_SERVICE_HOST = "host"
PROPERTIES_CONFIG_SERVICE_PORT = "port"
PROPERTIES_CONFIG_SERVICE_RESOURCE = "resource"

# Generic HOST access (where service is running) properties
PROPERTIES_CONFIG_SERVICE_HOST_USER = "host_user"
PROPERTIES_CONFIG_SERVICE_HOST_PASSWORD = "host_password"
PROPERTIES_CONFIG_SERVICE_HOST_PKEY = "host_private_key_location"
PROPERTIES_CONFIG_SERVICE_LOG_PATH = "service_log_path"
PROPERTIES_CONFIG_SERVICE_LOG_FILES = "service_log_file_names"

# Generic API service properties: OpenStack credentials
PROPERTIES_CONFIG_SERVICE_OS_USERNAME = "os_username"
PROPERTIES_CONFIG_SERVICE_OS_PASSWORD = "os_password"
PROPERTIES_CONFIG_SERVICE_OS_TENANT_ID = "os_tenant_id"
PROPERTIES_CONFIG_SERVICE_OS_TENANT_NAME = "os_tenant_name"
PROPERTIES_CONFIG_SERVICE_OS_DOMAIN_NAME = "os_domain_name"
PROPERTIES_CONFIG_SERVICE_OS_AUTH_URL = "os_auth_url"
