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
import yaml

__all__ = ['load']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


def _d(d, l):
    if l[0] not in d:
        d[l[0]] = {}
    if l[1:]:
        return _d(d[l[0]], l[1:])
    else:
        return d[l[0]]


def _load_file(result, filename, verbose=1):
    f_obj = open(filename, 'r')
    result.update(yaml.load(f_obj.read()))
    result['__file__'] = filename
    f_obj.close()


def load(target, verbose=1):
    result = {}
    if os.path.isfile(target):
        _load_file(result, target, verbose)
    elif os.path.isdir(target):
        for root, directories, files in os.walk(target):
            for f in files:
                if f.lower().endswith('.yaml'):
                    base = [d for d in os.path.relpath(
                        root, target).split(os.sep) if d != '.'] + [
                            os.path.splitext(f)[0]]
                    dictionary_to_update = _d(result, base)
                    _load_file(dictionary_to_update, os.path.join(
                        root, f), verbose)
    return result
