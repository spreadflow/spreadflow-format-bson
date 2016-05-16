# -*- coding: utf-8 -*-

"""
BSON message interchange format for SpreadFlow metadata extraction and
processing engine.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import struct

from bson import BSON

class MessageParser(object):
    """
    BSON message parser.

    Args:
        buffer_max_len (int): The maximum number of bytes buffered while
            parsing a stream of incoming messages. Defaults to 32768.
    """

    MAX_LENGTH = 32768

    def __init__(self, buffer_max_len=MAX_LENGTH):
        self._buffer_max_len = buffer_max_len
        self._buffer = b''

    def push(self, data):
        """
        Push data onto the message parser buffer.

        Args:
            data (bytes): Data as received from the network. Partial messages
            are allowed.

        Raises:
            RuntimeError: If the buffer is full.
        """
        if len(self._buffer) + len(data) > self._buffer_max_len:
            raise RuntimeError('Buffer length exceeded')

        self._buffer += data


    def messages(self):
        """
        Iterate over all available messages.

        Yields:
            object: The next decoded message.
        """
        doc_start = 0

        while doc_start + 4 < len(self._buffer):
            # http://bsonspec.org/spec.html
            (doc_len, ) = struct.unpack(b'<l', self._buffer[doc_start:doc_start + 4])
            if doc_start + doc_len > len(self._buffer):
                break

            doc = BSON(self._buffer[doc_start:doc_start + doc_len])
            yield doc.decode()

            doc_start += doc_len

        self._buffer = self._buffer[doc_start:]

class MessageBuilder(object):
    """
    Message builder for the BSON stream format.
    """

    def message(self, msg):
        return BSON.encode(msg)
