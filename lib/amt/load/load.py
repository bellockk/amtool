"""
amt-load -- Artifact Management Tool Reader

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import os
import yaml
import logging

__all__ = ['load', 'MetaDict', 'MetaList']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


def _d(d, l):
    if l[0] not in d:
        d[l[0]] = {}
    if l[1:]:
        return _d(d[l[0]], l[1:])
    else:
        return d[l[0]]


class MetaDict(dict):
    pass


class MetaList(list):
    pass


def _load_file(filename):
    """
    Loads a file into the specified node of the artifacts tree.

    This function is a helper function to `load`.  It processes a single
    artifact file for inclusion into the overall artifacts tree.

    Args:
        result: (dict): Node to load artifacts into.

        filename: (str): File to load artifacts from.

    Kwargs:
        verbose (int): Level to perform logging at.
    """
    logging.debug('Loading File: %s', filename)
    with open(filename, 'r') as f_obj:
        loaded_file_content = yaml.load(f_obj)
    logging.debug('Loaded File Content: %s', loaded_file_content)
    if isinstance(loaded_file_content, dict):
        metadict = MetaDict()
        metadict.update(loaded_file_content)
        metadict._file = filename
        return metadict
    if isinstance(loaded_file_content, (list, set, tuple)):
        metadict = MetaList()
        metadict.extend(loaded_file_content)
        metadict._file = filename
        return metadict


def load(target, verbose=1):
    """
    Load a directory or file containing artifacts.

    The `target` can be a directory or file, and can contain plain yaml, or
    canonicalized artifact data.  If a directory is specified, it will be walked
    recursively and all files will be loaded into the return data structure.

    Args:
        target (str): The directory or file to be loaded.

    Kwargs:
        verbose (int): Level to perform logging at.

    Returns:
        dict.  The fully read data structure containing all artifacts from the
        loaded target.
    """
    logging.debug('Loading Target: %s', target)
    if os.path.isfile(target):
        result = _load_file(target)
    elif os.path.isdir(target):
        for root, directories, files in os.walk(target):
            for f in files:
                if f.lower().endswith('.yaml'):
                    base = [d for d in os.path.relpath(
                        root, target).split(os.sep) if d != '.'] + [
                            os.path.splitext(f)[0]]
                    print('Result: %s' % result)
                    print('Base: %s' % base)
                    dictionary_to_update = _d(result, base)
                    _load_file(dictionary_to_update, os.path.join(
                        root, f), verbose)
    return result
