#!/usr/bin/env python
import click
from .utils import s

@click.command()
@click.option("--url",required=True,type=str,default=None,help="Url to be explored")
def crawl(url):
    click.echo("Starting web scrapping")
    s.start(url)
    s.reset()
    


