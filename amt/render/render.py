"""
amt-render -- Artifact Management Tool Reader

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import os
import sys
import logging

__all__ = ['render']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(SCRIPT_PATH), 'load'))
from load import load


def render(target, engine='mako'):
    """
    Render a set of artifacts.

    The `target` can be a directory or file, and can contain plain yaml, or
    canonicalized artifact data.  If a directory is specified, it will be
    walked recursively and all files will be loaded into the return data
    structure.

    Args:
        target (str): The directory or file to be loaded.

    Kwargs:
        verbose (int): Level to perform logging at.

    Returns:
        dict.  The fully read data structure containing all artifacts from the
        loaded target.
    """
    logging.debug('Rendering Target: %s', target)
    return load(target)
