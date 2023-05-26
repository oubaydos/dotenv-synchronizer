
import click
from dotenv import dotenv_values




@click.command()
@click.option('-e', '--env', type=str, help='relative path to the .env file', default='.env')
@click.option('-o', '--output', type=str, help='relative path to the output .env.example, will be created if not found', default='.env.example')
def cli(env, output):
    env = dotenv_values(env)
    click.echo(f'Hello {env}!')
