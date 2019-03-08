"""
amt -- Artifact Management Tool.

amt is a Tool for managing software artifacts

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net

"""
import sys
import os
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(
        SCRIPT_PATH))), 'lib')

sys.path.insert(0, LIB_PATH)
from amt import CLIError
from amt import _main

__all__ = []
__version__ = '0.0.1'
__date__ = '2013-11-13'
__updated__ = '2013-11-13'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.dirname(SCRIPT_PATH)


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
        subparsers = parser.add_subparsers(title='commands', metavar='',
                                           dest='tool')
        tools = {}
        for cmd in sorted(commands):
            tools[cmd] = {}
            tools[cmd]['Namespace'] = {'__file__':  __file__}
            exec(compile(open(os.path.join(
                ROOT_PATH,
                'amt-%s' % cmd,
                'amt-%s.py' % cmd)).read(), os.path.join(
                    ROOT_PATH,
                    'amt-%s' % cmd,
                    'amt-%s.py' % cmd), 'exec'), tools[cmd]['Namespace'])
            sp = subparsers.add_parser(cmd, help=tools[cmd][
                'Namespace']['__doc__'].split('\n')[1].split(' -- ')[1])
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
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise
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


if __name__ == "__main__":
    _main(debug=DEBUG, testrun=TESTRUN, profile=PROFILE, main=main)
