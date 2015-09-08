# -*- coding: utf-8 -*-

"""
logger_utils module contains some functions for logging management:
    - Logger wrapper
    - Fuctions for pretty print:
        - log_print_request
        - log_print_response

This code is based on:
     https://pdihub.hi.inet/fiware/fiware-iotqaUtils/raw/develop/iotqautils/iotqaLogger.py
"""

__author__ = "Telefonica I+D, @jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"


import logging
import logging.config
from xml.dom.minidom import parseString
import json
import os
from qautils.http.headers_utils import HEADER_CONTENT_TYPE, HEADER_REPRESENTATION_XML, HEADER_REPRESENTATION_JSON


# Load logging configuration from file if it exists
if os.path.exists("./settings/logging.conf"):
    logging.config.fileConfig("./settings/logging.conf")


def get_logger(name):
    """
    Create new __logger__ with the given name
    :param name: Name of the __logger__
    :return: Logger
    """

    logger = logging.getLogger(name)
    return logger


def _get_pretty_body(headers, body):
    """
    Return a pretty printed body using the Content-Type header information
    :param headers: Headers for the request/response (dict)
    :param body: Body to pretty print (string)
    :return: Body pretty printed (string)
    """

    if HEADER_CONTENT_TYPE in headers:
        if HEADER_REPRESENTATION_XML == headers[HEADER_CONTENT_TYPE]:
            xml_parsed = parseString(body)
            pretty_xml_as_string = xml_parsed.toprettyxml()
            return pretty_xml_as_string
        else:
            if HEADER_REPRESENTATION_JSON in headers[HEADER_CONTENT_TYPE]:
                parsed = json.loads(body)
                return json.dumps(parsed, sort_keys=True, indent=4)
            else:
                return body
    else:
        return body


def log_print_request(logger, method, url, query_params=None, headers=None, body=None):
    """
    Log an HTTP request data.
    :param logger: Logger to use
    :param method: HTTP method
    :param url: URL
    :param query_params: Query parameters in the URL
    :param headers: Headers (dict)
    :param body: Body (raw body, string)
    :return: None
    """

    log_msg = '>>>>>>>>>>>>>>>>>>>>> Request >>>>>>>>>>>>>>>>>>> \n'
    log_msg += '\t> Method: %s\n' % method
    log_msg += '\t> Url: %s\n' % url
    if query_params is not None:
        log_msg += '\t> Query params: {}\n'.format(str(query_params))
    if headers is not None:
        log_msg += '\t> Headers: {}\n'.format(str(headers))
    if body is not None:
        log_msg += '\t> Payload sent:\n {}\n'.format(_get_pretty_body(headers, body))

    logger.debug(log_msg)


def log_print_response(logger, response):
    """
    Log an HTTP response data
    :param logger: __logger__ to use
    :param response: HTTP response ('Requests' lib)
    :return: None
    """

    log_msg = '<<<<<<<<<<<<<<<<<<<<<< Response <<<<<<<<<<<<<<<<<<\n'
    log_msg += '\t< Response code: {}\n'.format(str(response.status_code))
    log_msg += '\t< Headers: {}\n'.format(str(dict(response.headers)))
    try:
        log_msg += '\t< Payload received:\n {}'.format(_get_pretty_body(dict(response.headers), response.content))
    except ValueError:
        log_msg += '\t< Payload received:\n {}'.format(_get_pretty_body(dict(response.headers), response.content.text))

    logger.debug(log_msg)
