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
import yaml

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(SCRIPT_PATH), 'meta'))
from meta import MetaDict
from meta import MetaList
yaml.add_representer(MetaDict,
                     lambda dumper, data: dumper.represent_mapping(
                         'tag:yaml.org,2002:map', data.items()))
yaml.add_representer(MetaList,
                     lambda dumper, data: dumper.represent_sequence(
                         'tag:yaml.org,2002:seq', data))

__all__ = ['save']


def _d(pth, data, verbose=1):
    for key, value in data.items():
        try:
            with open(os.path.join(pth, value._file), 'w') as f_obj:
                f_obj.write(yaml.dump(value, default_flow_style=False))
        except:
            newpth = os.path.join(pth, key)
            if not os.path.isdir(newpth):
                os.makedirs(newpth)
            save(newpth, value, verbose)


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
    for key, value in dcmp.subdirs.items():
            _d2(value)


def save(pth, data, header=None, footer=None, verbose=1):
    if pth.lower().endswith('.yaml'):
        write_data = data.copy()
        f_obj = open(pth, 'w')
        if header:
            f_obj.write(header)
        f_obj.write(yaml.dump(write_data, default_flow_style=False))
        if footer:
            f_obj.write(footer)
        f_obj.close()
    else:
        tmp = tempfile.mkdtemp()
        _d(tmp, data, verbose)
        _d2(dircmp(pth, tmp))
        shutil.rmtree(tmp)
