#!/usr/bin/env python
import shutil
import tempfile
import unittest
import logging
import os
import sys
from filecmp import dircmp

# Set Paths
TEST_PATH = os.path.dirname(os.path.realpath(__file__))
SUT_PATH = os.path.dirname(TEST_PATH)
DATA_PATH = os.path.join(TEST_PATH, 'data')

# Import SUT's
sys.path.append(SUT_PATH)
from save import save

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(SCRIPT_PATH))), 'amt', 'meta'))
from meta import MetaDict
from meta import MetaList


class Test_AMT(unittest.TestCase):
    def test_save1(self):
        test_description = 'File Only'
        expected = os.path.join(DATA_PATH, 'test1')
        actual = tempfile.mkdtemp()
        metadict = MetaDict([('foo', 'bar')])
        metadict._file = 'test1.yaml'
        save(actual, {'test1': metadict})
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(actual)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)

    def test_save2(self):
        test_description = 'Directory with File'
        expected = os.path.join(DATA_PATH, 'test2')
        actual = tempfile.mkdtemp()
        metadict = MetaDict([('foo', 'bar')])
        metadict._file = 'test1.yaml'
        save(actual,
             {'say': {'test1': metadict}})
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(actual)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)

    def test_save3(self):
        test_description = 'Directory with Directory with file'
        expected = os.path.join(DATA_PATH, 'test3')
        actual = tempfile.mkdtemp()
        metadict = MetaDict([('foo', 'bar')])
        metadict._file = 'test1.yaml'
        save(actual, {'you': {'say': {'test1': metadict}}})
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(actual)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)


if __name__ == '__main__':
    unittest.main()
