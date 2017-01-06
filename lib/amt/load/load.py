"""
amt-load -- Artifact Management Tool Reader

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import os
import sys

__all__ = ['load']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(SCRIPT_PATH, '..', '..')
sys.path.insert(0, LIB_PATH)

from amt.file_io import safe_load


def load(target, verbose=1):
    result = {}
    for root, directories, files in os.walk(target):
        for f in files:
            if f.lower().endswith('.yaml'):
                base = [d for d in os.path.relpath(
                    root, target).split(os.sep) if d != '.']
                print base
                print safe_load(os.path.join(root, f))
    return result
