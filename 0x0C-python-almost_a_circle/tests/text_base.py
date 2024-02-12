#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCsv - line 404
    TestBaseLoadFromFileCsv - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

