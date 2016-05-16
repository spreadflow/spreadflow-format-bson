# -*- coding: utf-8 -*-
# pylint: disable=too-many-public-methods

"""
Unit tests for BSON message builder.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import unittest

from spreadflow_format_bson import MessageBuilder

class BsonBuilderTestCase(unittest.TestCase):
    """
    Unit tests for BSON message builder.
    """

    def test_build_message(self):
        """
        Tests BSON message builder.
        """
        builder = MessageBuilder()

        result = builder.message({'msg': 'hello world'})
        self.assertEquals(b'\x1a\x00\x00\x00\x02msg\x00\x0c\x00\x00\x00hello world\x00\x00', result)

        result = builder.message({'x': 42})
        self.assertEquals(b'\x0c\x00\x00\x00\x10x\x00*\x00\x00\x00\x00', result)
