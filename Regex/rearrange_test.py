#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange (unittest.TestCase):
    def test_basic(self):
        testcase = "piplai, ashok"
        expected = "ashok piplai"
        
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_invalid_name(self):
        self.assertRaises(ValueError, rearrange_name, "ashok")

unittest.main()

        
