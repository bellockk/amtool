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
__all__ = ['CLIError']


class CLIError(Exception):

    """Generic exception to raise and log different fatal errors."""

    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "Error: %s" % msg

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


def main(name, version, build_data, version_message, shortdesc, epilog, license, argv=None, DEBUG=False, TESTRUN=False):  # IGNORE:C0111
    """Command line options."""

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

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
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
