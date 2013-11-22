#!/usr/bin/python
# encoding: utf-8
"""
amt -- Artifact Management Tool.

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""

import sys
import os
import re

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = '0.0.1'
__date__ = '2013-11-13'
__updated__ = '2013-11-13'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.dirname(SCRIPT_PATH)


class CLIError(Exception):

    """Generic exception to raise and log different fatal errors."""

    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "Error: %s" % msg

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


def main(argv=None):  # IGNORE:C0111
    """Command line options."""

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version,
                                                     program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_epilog = ''
    program_license = '''%s

  Created by Kenneth E. Bellock on %s.

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:

        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                epilog=program_epilog,
                                formatter_class=RawDescriptionHelpFormatter)

        # Add parsing options
        _fill_parser(parser, program_version_message=program_version_message)

        # Create subparsers for each tool
        commands = [d[len('amt-'):] for d in os.listdir(ROOT_PATH) if
                    d.startswith('amt-')]
        # Note: The metavar being set to an empty string removes the redundant
        # listing of subcommands.
        subparsers = parser.add_subparsers(title='commands', metavar='', dest='tool')
        tools= {}
        for cmd in commands:
            tools[cmd] = {}
            tools[cmd]['Namespace'] = {'__file__':  __file__}
            execfile(os.path.join(ROOT_PATH,
                                  'amt-%s' % cmd,
                                  'amt-%s.py' % cmd), tools[cmd]['Namespace'])
            sp = subparsers.add_parser(cmd, help=tools[cmd]['Namespace']['__doc__'].split('\n')[1].split(' -- ')[1])
            tools[cmd]['Parser'] = sp
            tools[cmd]['Namespace']['_fill_parser'](sp)

        # Process arguments
        args = parser.parse_args()

        tools[args.tool]['Namespace']['_apply_args'](args)

        verbose = args.verbose

        if verbose > 0:
            print("Verbose mode on")

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


def _fill_parser(parser, **kw):
    """Fill a command line parser."""
    parser.add_argument("-v",
                        "--verbose",
                        dest="verbose",
                        action="count",
                        default=0,
                        help="set verbosity level [default: %(default)s]")
    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version=kw['program_version_message'])


def _replacemany(adict, astring, prefix='<', suffix='>'):
    """
    Replace keys within a string using the given dictionary of key:value pairs.

    Parameters
    ----------
    adict : dictionary
        Dictionary of replace key - replace value pairs.
    astring : string
        String to perform the replacement on.

    Returns
    -------
    result : string
        Input string with replacements performed.

    """
    re_obj = re.compile('|'.join(re.escape(
        '%s%s%s' % (prefix, s, suffix)) for s in adict))
    return re_obj.sub(lambda m: str(
        adict[m.group()[len(prefix):len(m.group()) - len(suffix)]]), astring)

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-v")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'filltemplates_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
