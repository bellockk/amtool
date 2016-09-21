#!/usr/bin/python
# encoding: utf-8
"""
amt-init -- Artifact Management Tool initialization.

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
__all__ = ['add']

import os
import sys
import uuid

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(SCRIPT_PATH, '..', '..')
sys.path.insert(0, LIB_PATH)

from amt.file_io import safe_dump

def add(targets, verbose=1):
    for target in targets:
        dirname = os.path.dirname(target)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        f_obj = open(target, 'w')
        f_obj.write(safe_dump({'uid': str(uuid.uuid4())},
                              default_flow_style=False))
        f_obj.close()
    return 0
