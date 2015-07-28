# -*- coding: utf-8 -*-

"""
    remote_tail_utils module contains utilities for reading remote logs using 'tail'.
        - start_tailer: Starts a new thread reading the remote file.
        - stop_tailer: Stop the capturing.
"""

__author__ = "@jframos"
__project__ = "python-qautils [https://github.com/qaenablers/python-qautils]"
__copyright__ = "Copyright 2015"
__license__ = " Apache License, Version 2.0"
__version__ = "1.1.0"

import time
import threading

from sshtail import SSHTailer, load_dss_key
from qautils.logger.logger_utils import get_logger


__logger__ = get_logger(__name__)

# Delay period just after starting remote tailers
TIMER_DELAY_PERIOD = 3

# Grace period when stopping thread. 3 seconds by default
TIMER_GRACE_PERIOD = 3

# Global flag
_tail_terminate_flag = False


class RemoteTail:

    def __init__(self, remote_host_ip, remote_host_user, remote_log_path, remote_log_file_name, local_log_target,
                 private_key):
        """
        Init RemoteTail class
        :param remote_host_ip: Remote Host IP
        :param remote_host_user: Remote host User name
        :param remote_log_path: Remote log path location
        :param remote_log_file_name: Remote log filename to be tailed
        :param local_log_target: Local path where remote logs will be captured
        :param private_key: Private key to use in the SSH connection.
        If no path's specified for the private key file name, it automatically prepends /home/<current_user>/.ssh/
        and for RSA keys, import load_rsa_key instead.
        :return: None
        """

        self.tailer = None
        self.tail_terminate_flag = False
        self.thread = None
        self.local_capture_file_descriptor = None

        self.remote_host_ip = remote_host_ip
        self.remote_host_user = remote_host_user
        self.remote_log_path = remote_log_path
        self.remote_log_file_name = remote_log_file_name
        self.local_log_target = local_log_target
        self.private_key = private_key

    def init_tailer_connection(self):
        """
        Create a ssh connection to host and init tail on the file.
        :return: None
        """

        private_key_loaded = load_dss_key(self.private_key)
        connection_host = self.remote_host_user + '@' + self.remote_host_ip
        target_log_path = self.remote_log_path + self.remote_log_file_name
        __logger__.info("Remote Tailer: Connecting to remote host [host: %s, path: %s", connection_host,
                    target_log_path)
        self.tailer = SSHTailer(connection_host, target_log_path, private_key_loaded)

        # Open local output file
        local_capture_path = self.local_log_target + self.remote_log_file_name
        __logger__.debug("Remote Tailer: Opening local file to save the captured logs")
        self.local_capture_file_descriptor = open(local_capture_path, 'w')

    @staticmethod
    def _read_tailer(tailer, local_capture_file_descriptor):
        """
        Execute a 'tail' on remote log file until tail_terminate_flag will be True
        :param tailer: Created and initialized sshtail connection
        :param local_capture_file_descriptor: Opened descriptor to local file where remote logs will be captured
        :return: None
        """

        global _tail_terminate_flag
        _tail_terminate_flag = False

        try:
            while not _tail_terminate_flag:
                for line in tailer.tail():
                    local_capture_file_descriptor.writelines(line + "\n")
                    local_capture_file_descriptor.flush()

                # wait a bit
                time.sleep(0.5)

            __logger__.debug("Remote Tailer: Remote capture finished")
        except:
            __logger__.error("Remote Tailer: Error when reading remote log lines")

        __logger__.debug("Remote Tailer: Closing connections and file descriptors")
        tailer.disconnect()
        local_capture_file_descriptor.close()

    def start_tailer(self):
        """
        This method starts a new thread to execute a tailing on the remote log file
        :return: None
        """

        __logger__.debug("Remote Tailer: Launching thread to capture logs")
        self.thread = threading.Thread(target=self._read_tailer,
                                       args=[self.tailer, self.local_capture_file_descriptor])
        self.thread.start()
        __logger__.debug("Delay timer before starting: " + str(TIMER_DELAY_PERIOD))
        time.sleep(TIMER_DELAY_PERIOD)

    def stop_tailer(self):
        """
        This method will stop the tailer process after a grace time period
        :return: None
        """

        __logger__.info("Remote Tailer: Stopping tailers")
        __logger__.debug("Grace period after stopping: " + str(TIMER_GRACE_PERIOD))
        time.sleep(TIMER_GRACE_PERIOD)
        global _tail_terminate_flag
        _tail_terminate_flag = True
