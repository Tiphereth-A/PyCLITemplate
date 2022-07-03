#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
import coloredlogs

from libs.decorator import withlog


@click.group()
@click.option('-l', '--level', type=click.Choice(['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']), help='log level',
              default='INFO')
def cli(level: str):
    coloredlogs.install(level=level,
                        fmt='%(asctime)s:%(msecs)03d %(levelname)s %(programname)s::%(name)s [%(process)d] %(message)s',
                        field_styles={'asctime': {'color': 'green'},
                                      'msecs': {'color': 'green'},
                                      'hostname': {'color': 'red'},
                                      'levelname': {'bold': True, 'color': 'magenta'},
                                      'name': {'faint': True, 'color': 'blue'},
                                      'programname': {'bold': True, 'color': 'cyan'},
                                      'process': {'faint': True, 'color': 'green'},
                                      'username': {'color': 'yellow'}},
                        level_styles={'critical': {'bold': True, 'color': 'red'},
                                      'debug': {'color': 'cyan'},
                                      'error': {'color': 'red'},
                                      'info': {'bright': True, 'color': 'white'},
                                      'notice': {'color': 'magenta'},
                                      'spam': {'color': 'green', 'faint': True},
                                      'success': {'bold': True, 'color': 'green'},
                                      'verbose': {'color': 'blue'},
                                      'warning': {'bright': True, 'color': 'yellow'}})


@cli.command('run')
@click.option('-m', '--message', type=str, prompt='Message', help='Message')
def _run(message: str):
    """run"""

    @withlog
    def run(_message: str, **kwargs):
        kwargs.get('logger').info('Started running')
        print('Hello world!')
        print(_message)
        kwargs.get('logger').info('Finished')

    run(message)


if __name__ == '__main__':
    cli()
