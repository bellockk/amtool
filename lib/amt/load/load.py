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


def _d(d, l):
    if l[0] not in d:
        d[l[0]] = {}
    if l[1:]:
        return _d(d[l[0]], l[1:])
    else:
        return d[l[0]]


def load(target, verbose=1):
    result = {}
    for root, directories, files in os.walk(target):
        for f in files:
            if f.lower().endswith('.yaml'):
                base = [d for d in os.path.relpath(
                    root, target).split(os.sep) if d != '.'] + [
                        os.path.splitext(f)[0]]
                dictionary_to_update = _d(result, base)
                f_obj = open(os.path.join(root, f), 'r')
                dictionary_to_update.update(safe_load(f_obj.read()))
                dictionary_to_update['__file__'] = f
                f_obj.close()
    return result
