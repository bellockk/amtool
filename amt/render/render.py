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
import copy
import logging
from mako.template import Template

__all__ = ['render']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(SCRIPT_PATH), 'load'))
sys.path.insert(0, os.path.join(os.path.dirname(SCRIPT_PATH), 'uid'))
from load import load
from uid import uid


def _render(artifacts, uids):
    """
    Recursive helper function for diving into dictionaries of dictionaries
    searching for unique id's.

    Args:
        artifacts (dict): Input dictionary.

    Returns:
        dict: returned dictionary
    """
    if isinstance(artifacts, dict):
        for key, value in artifacts.items():
            if isinstance(value, (dict, list, tuple)):
                _render(value, uids)
            elif isinstance(value, str):
                artifacts[key] = Template(value).render(UID=uids)
    elif isinstance(artifacts, (list, tuple)):
        for index, value in enumerate(artifacts):
            if isinstance(value, (dict, list, tuple)):
                _render(value, uids)
            elif isinstance(value, str):
                artifacts[index] = Template(value).render(UID=uids)


def render(source, engine='mako'):
    """
    Render a set of artifacts.

    The `target` can be a directory or file, and can contain plain yaml, or
    canonicalized artifact data.  If a directory is specified, it will be
    walked recursively and all files will be loaded into the return data
    structure.

    Args:
        source (str): The directory or file to be loaded.

    Kwargs:
        verbose (int): Level to perform logging at.

    Returns:
        dict.  The fully read data structure containing all artifacts from the
        loaded target.
    """
    logging.debug('Rendering: %s', source)
    if isinstance(source, str):
        data = load(source)
    else:
        data = copy.deepcopy(source)
    _render({'': data}, uid(source))
    return data
