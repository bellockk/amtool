#!/usr/bin/python
# encoding: utf-8
"""
amt-add -- Artifact Management Tool add artifact.

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""

import sys
import os
import shutil
import yaml
import uuid

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = '0.0.1'
__date__ = '2013-11-13'
__updated__ = '2013-11-13'

DEBUG = 0
TESTRUN = 0
PROFILE = 0


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

        # Add command line arguments
        _fill_parser(parser,
                     program_version_message=program_version_message)

        # Process arguments
        args = parser.parse_args()

        # Apply arguments
        return _apply_args(args)

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


def _apply_args(args):
    """Utilize parsed arguments."""
    verbose = args.verbose

    if verbose > 0:

        print("Verbose mode on")

    if not os.path.exists('.amt'):
        # print('Not within an AMT managed folder')
        # return 1
        pass

    for f in args.FILE:
        f_obj = open(f, 'w')
        f_obj.write(yaml.dump({'uid': str(uuid.uuid4())},
                              default_flow_style=False))
        f_obj.close()

    return 0


def _fill_parser(parser, **kw):
    """Fill parser with commands."""
    parser.add_argument("FILE", help="target list", nargs='+')
    parser.add_argument("-v",
                        "--verbose",
                        dest="verbose",
                        action="count",
                        default=0,
                        help="set verbosity level [default: %(default)s]")
    if 'program_version_message' in kw:
        parser.add_argument('-V',
                            '--version',
                            action='version',
                            version=kw['program_version_message'])


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
