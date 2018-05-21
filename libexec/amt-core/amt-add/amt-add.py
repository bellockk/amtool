"""
amt-add -- add artifact

amt is a Tool for managing software artifacts

@author:     Kenneth E. Bellock

@copyright:

@contact:    ken@bellock.net
"""
import sys
import os
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(
        SCRIPT_PATH))), 'lib')
sys.path.insert(0, LIB_PATH)
from amt import add
from amt import CLIError
from amt import _main

__version__ = '0.0.1'
__date__ = '2013-11-13'
__updated__ = '2013-11-13'
DEBUG = 0
TESTRUN = 0
PROFILE = 0


def _apply_args(args):
    """Utilize parsed arguments."""
    verbose = args.verbose

    if verbose > 0:

        print("Verbose mode on")

    if not os.path.exists('.amt'):
        # print('Not within an AMT managed folder')
        # return 1
        pass
    return add(args.FILE)


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
    _main(__version__, __updated__, __date__, _fill_parser, _apply_args,
          DEBUG, TESTRUN, PROFILE)
