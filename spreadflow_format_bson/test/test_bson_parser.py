# -*- coding: utf-8 -*-
# pylint: disable=too-many-public-methods

"""
Unit tests for BSON message parser.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import unittest

from spreadflow_format_bson import MessageParser

class BsonParserTestCase(unittest.TestCase):
    """
    Unit tests for BSON message parser.
    """

    def test_parse_messages(self):
        """
        Tests BSON message parser.
        """
        parser = MessageParser()

        msg1 = b'\x1a\x00\x00\x00\x02msg\x00\x0c\x00\x00\x00hello world\x00\x00'
        msg2 = b'\x0c\x00\x00\x00\x10x\x00*\x00\x00\x00\x00'

        parser.push(msg1)
        self.assertEquals([{'msg': 'hello world'}], list(parser.messages()))

        parser.push(msg2)
        self.assertEquals([{'x': 42}], list(parser.messages()))

    def test_parse_partial_msgs(self):
        """
        Tests that BSON message parser accepts partial messages.
        """
        parser = MessageParser()

        msg = b''.join([
            b'\x1a\x00\x00\x00\x02msg\x00\x0c\x00\x00\x00hello world\x00\x00',
            b'\x0c\x00\x00\x00\x10x\x00*\x00\x00\x00\x00'
        ])

        chunk_size = 8

        actual_messages = []
        for pos in range(0, len(msg), chunk_size):
            parser.push(msg[pos:pos+chunk_size])
            for parsed_message in parser.messages():
                actual_messages.append(parsed_message)

        self.assertEquals([{'msg': 'hello world'}, {'x': 42}], actual_messages)

    def test_buffer_exceeded(self):
        """
        Tests that BSON message parser raises an exception when its buffer
        limit is exceeded.
        """
        parser = MessageParser(8)

        msg = b'\x1a\x00\x00\x00\x02msg\x00\x0c\x00\x00\x00hello world\x00\x00'

        self.assertRaises(RuntimeError, parser.push, msg)
