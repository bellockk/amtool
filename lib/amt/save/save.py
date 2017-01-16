"""
amt-save -- Artifact Management Tool Reader

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import os
import sys

__all__ = ['save']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(SCRIPT_PATH, '..', '..')
sys.path.insert(0, LIB_PATH)

from amt.file_io import safe_dump


def save(data, pth, verbose=1):
    for key, value in data.iteritems():
        if '__file__' not in value:
            newpth = os.path.join(pth, key)
            os.makedirs(newpth)
            save(value, newpth, verbose)
        else:
            write_data = value.copy()
            del write_data['__file__']
            f_obj = open(os.path.join(pth, value['__file__']), 'w')
            f_obj.write(safe_dump(write_data, default_flow_style=False))
