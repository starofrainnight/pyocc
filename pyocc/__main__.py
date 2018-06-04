#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for pyocc."""

import click
from pyocc import PyOCC


@click.group()
@click.pass_context
def main(ctx):
    """PyOCC command line program. Use for demonstrate how to use PyOCC
    library."""
    ctx.obj = PyOCC()


@main.group()
@click.pass_context
def show(ctx):
    """Display details about how to invoke PyOCC.
    """
    pass


@show.command()
@click.pass_context
def configs(ctx):
    """Display configs we supported
    """
    occ = ctx.obj

    click.echo(list(occ.configs))


@show.command()
@click.pass_context
def executable(ctx):
    """Display executable we found
    """
    occ = ctx.obj

    click.echo(occ.executable)


if __name__ == "__main__":
    main()
