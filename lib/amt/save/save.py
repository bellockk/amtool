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
import tempfile
import shutil
from filecmp import dircmp

__all__ = ['save']
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(SCRIPT_PATH, '..', '..')
sys.path.insert(0, LIB_PATH)

from amt.file_io import safe_dump


def _d(pth, data, verbose=1):
    for key, value in data.iteritems():
        if '__file__' not in value:
            newpth = os.path.join(pth, key)
            if not os.path.isdir(newpth):
                os.makedirs(newpth)
            save(newpth, value, verbose)
        else:
            write_data = value.copy()
            del write_data['__file__']
            f_obj = open(os.path.join(pth, value['__file__']), 'w')
            f_obj.write(safe_dump(write_data, default_flow_style=False))
            f_obj.close()


def _d2(dcmp):
    for f in dcmp.left_only:
        if os.path.isdir(f):
            shutil.rmtree(f)
        elif os.path.isfile(f):
            os.remove(f)
    for fname in list(set(dcmp.right_only + dcmp.diff_files)):
        f = os.path.join(dcmp.right, fname)
        if os.path.isfile(f):
            relpath = os.path.relpath(f, dcmp.right)
            target = os.path.join(dcmp.left, relpath)
            target_dirname = os.path.dirname(target)
            if not os.path.isdir(target_dirname):
                os.makedirs(target_dirname)
            shutil.copy2(f, target)
        elif os.path.isdir(f):
            shutil.copytree(os.path.join(dcmp.right, fname),
                            os.path.join(dcmp.left, fname))
    for key, value in dcmp.subdirs.iteritems():
            _d2(value)


def save(pth, data, header=None, footer=None, verbose=1):
    if pth.lower().endswith('.yaml'):
        write_data = data.copy()
        # TODO: Recursively remove all instances of '__file__'
        f_obj = open(pth, 'w')
        if header:
            f_obj.write(header)
        f_obj.write(safe_dump(write_data, default_flow_style=False))
        if footer:
            f_obj.write(footer)
        f_obj.close()
    else:
        tmp = tempfile.mkdtemp()
        _d(tmp, data, verbose)
        _d2(dircmp(pth, tmp))
        shutil.rmtree(tmp)
