# -*- coding: utf-8 -*-

"""Console script for amtool."""
import sys
import click
import logging
import click_log
import yaml
from amt import canonical as canon
from amt import load
from amt import uid as amtuid
from amt import MetaDict
from amt import MetaList
from pkg_resources import iter_entry_points
from click_plugins import with_plugins


click_log.basic_config()


@with_plugins(iter_entry_points('amt.plugins'))
@click.group()
@click_log.simple_verbosity_option(default='WARNING')
def main(args=None):
    """Console script for amtool."""
    logging.info('A message')
    return 0


@main.command()
@click.argument('PATH')
def canonical(path):
    canon(path)
    return 0


@main.command()
@click.argument('PATH')
def dump(path):
    yaml.add_representer(MetaDict,
                         lambda dumper, data: dumper.represent_mapping(
                             'tag:yaml.org,2002:map', data.items()))
    yaml.add_representer(MetaList,
                         lambda dumper, data: dumper.represent_sequence(
                             'tag:yaml.org,2002:seq', data))
    click.echo(yaml.dump(load(path), default_flow_style=False))
    return 0


@main.command()
@click.argument('PATH')
def uid(path):
    yaml.add_representer(MetaDict,
                         lambda dumper, data: dumper.represent_mapping(
                             'tag:yaml.org,2002:map', data.items()))
    yaml.add_representer(MetaList,
                         lambda dumper, data: dumper.represent_sequence(
                             'tag:yaml.org,2002:seq', data))
    click.echo(yaml.dump(amtuid(path), default_flow_style=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
