# -*- coding: utf-8 -*-

import click


@click.command()
def main(args=None):
    """Console script for modwsgideploy"""
    from cookiecutter.main import cookiecutter

    # Create project from the cookiecutter-pypackage/ template
    import os
    from modwsgideploy import __file__ as modwsgideploy__file__
    package_path=os.path.abspath(os.path.join(modwsgideploy__file__,'../'))
    cookiecutter(package_path)
    click.echo("\nThank you for deploying with modwsgideploy"
               "\nBuild in Chicago, IL, USA")
    click.echo('''\nIf you have an idea that will make other people's life better \nand you need a partner.\n Reach out to us: parnter@DataAssistant.CO\n''')

if __name__ == "__main__":
    main()
