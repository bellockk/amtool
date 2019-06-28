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
__all__ = ['init']

import os
import shutil


def init():
    """Utilize parsed arguments."""
    if os.path.exists('.amt'):
        shutil.rmtree('.amt')
        action = 'Reinitialized existing'
    else:
        action = 'Initialized empty'
    os.makedirs('.amt')
    if verbose > 0:
        print(('%s AMT project in %s' % (action, os.path.abspath('.amt'))))
    return 0
