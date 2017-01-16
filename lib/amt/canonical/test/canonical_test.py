#!/usr/bin/env python
import shutil
import tempfile
import unittest
import os
import sys
from filecmp import dircmp

# Set Paths
TEST_PATH = os.path.dirname(os.path.realpath(__file__))
SUT_PATH = os.path.dirname(TEST_PATH)
DATA_PATH = os.path.join(TEST_PATH, 'data')

# Import SUT's
sys.path.append(SUT_PATH)
from canonical import canonical


class Test_AMT(unittest.TestCase):
    def test_canonical1(self):
        test_description = 'File Only'
        expected = os.path.join(DATA_PATH, 'test1_canonical')
        temp_directory = tempfile.mkdtemp()
        actual = os.path.join(temp_directory, 'test1')
        shutil.copytree(os.path.join(DATA_PATH, 'test1'),
                        actual)
        canonical(actual)
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(temp_directory)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)

    def test_canonical2(self):
        test_description = 'Directory with File'
        expected = os.path.join(DATA_PATH, 'test2_canonical')
        temp_directory = tempfile.mkdtemp()
        actual = os.path.join(temp_directory, 'test2')
        shutil.copytree(os.path.join(DATA_PATH, 'test2'),
                        actual)
        canonical(actual)
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(temp_directory)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)

    def test_canonical3(self):
        test_description = 'Directory with Directory with file'
        expected = os.path.join(DATA_PATH, 'test3_canonical')
        temp_directory = tempfile.mkdtemp()
        actual = os.path.join(temp_directory, 'test3')
        shutil.copytree(os.path.join(DATA_PATH, 'test3'),
                        actual)
        canonical(actual)
        dcmp = dircmp(expected, actual)
        dcmp.report()
        shutil.rmtree(temp_directory)
        self.assertEqual([], dcmp.diff_files, test_description)
        self.assertEqual([], dcmp.left_only, test_description)
        self.assertEqual([], dcmp.right_only, test_description)


if __name__ == '__main__':
    unittest.main()
