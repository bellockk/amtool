#!/usr/bin/env python
import unittest
import logging
import os
import sys

# Set Paths
TEST_PATH = os.path.dirname(os.path.realpath(__file__))
SUT_PATH = os.path.dirname(TEST_PATH)
DATA_PATH = os.path.join(TEST_PATH, 'data')

# Import SUT's
sys.path.append(SUT_PATH)
from load import load


class Test_AMT(unittest.TestCase):
    def test_load0(self):
        expected = {'__file__': os.path.join(
            DATA_PATH, 'test1', 'test1.yaml'), 'foo': 'bar'}
        actual = load(os.path.join(DATA_PATH, 'test1', 'test1.yaml'))
        logging.info('Expected: %s', str(expected))
        logging.info('Actual: %s', str(actual))
        self.assertEqual(expected, actual, 'File only')

    def test_load1(self):
        expected = {'test1': {'__file__': os.path.join(
            DATA_PATH, 'test1', 'test1.yaml'), 'foo': 'bar'}}
        actual = load(os.path.join(DATA_PATH, 'test1'))
        logging.info('Expected: %s', str(expected))
        logging.info('Actual: %s', str(actual))
        self.assertEqual(expected, actual, 'File only')

    def test_load2(self):
        expected = {'say': {'test1': {'__file__': os.path.join(
            DATA_PATH, 'test2', 'say', 'test1.yaml'), 'foo': 'bar'}}}
        actual = load(os.path.join(DATA_PATH, 'test2'))
        logging.info('Expected: %s', str(expected))
        logging.info('Actual: %s', str(actual))
        self.assertEqual(expected, actual, 'Directory with File')

    def test_load3(self):
        expected = {'you': {'say': {'test1': {'__file__': os.path.join(
            DATA_PATH, 'test3', 'you', 'say', 'test1.yaml'), 'foo': 'bar'}}}}
        actual = load(os.path.join(DATA_PATH, 'test3'))
        logging.info('Expected: %s', str(expected))
        logging.info('Actual: %s', str(actual))
        self.assertEqual(expected, actual,
                         'Directory with Directory with file')


if __name__ == '__main__':
    unittest.main()
