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
import uuid
import yaml


def add(targets, verbose=1):
    for target in targets:
        f_obj = open(target, 'w')
        f_obj.write(yaml.dump({'uid': str(uuid.uuid4())},
                              default_flow_style=False))
        f_obj.close()
    return 0
