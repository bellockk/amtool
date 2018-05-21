#!/usr/bin/python
# encoding: utf-8
"""
amt-init -- Artifact Management Tool initialization.

amt is a Tool for managing software artifacts

It defines classes_and_methods and a command line interface

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import os
import sys
import logging
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
__all__ = ['CLIError', '_main']


class CLIError(Exception):
    """
    Generic exception to raise and log different fatal errors
    """

    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "Error: %s" % msg

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


def _startup(version, updated, date, fill_parser, apply_args, debug=False,
          testrun=False, profile=False, argv=None):  # IGNORE:C0111
    if argv is None:
        argv = sys.argv
    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % version
    program_build_date = str(updated)
    program_version_message = '%%(prog)s %s (%s)' % (program_version,
                                                     program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_epilog = ''
    program_license = '''%s

  Created by Kenneth E. Bellock on %s.

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(date))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                epilog=program_epilog,
                                formatter_class=RawDescriptionHelpFormatter)

        # Add command line arguments
        fill_parser(parser,
                    program_version_message=program_version_message)

        # Process arguments
        args = parser.parse_args()

        # Apply arguments
        return apply_args(args)

    except KeyboardInterrupt:
        return 0
    except Exception as e:
        if debug or testrun:
            raise(e)
        indent = len(program_name) * " "
        logging.error(program_name + ": " + repr(e) + "\n")
        logging.error(indent + "  for help use --help")
        return 2


def _main(*args, **kwargs):
    if 'debug' in kwargs and kwargs['debug']:
        sys.argv.append("-v")
    if 'testrun' in kwargs and kwargs['testrun']:
        import doctest
        doctest.testmod()
    if 'profile' in kwargs and kwargs['profile']:
        import cProfile
        import pstats
        basename = os.path.splitext(os.path.basename(__file__))[0]
        profile_filename = '%s_profile.txt' % basename
        cProfile.run('_main()', profile_filename)
        statsfile = open("%s_profile_stats.txt" % basename, "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    if 'main' in kwargs and kwargs['main']:
        sys.exit(kwargs['main']())
    else:
        sys.exit(_startup(*args, *kwargs))
