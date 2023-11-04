import click
from dotenv import dotenv_values


@click.command()
@click.option('-e', '--env', type=str, help='relative path to the .env file', default='.env')
@click.option('-o', '--output', type=str, help='relative path to the output .env.example, will be created if not found',
              default='.env.example')
def cli(env, output):
    env = dotenv_values(env)
    env_example = dotenv_values(output)
    if len(env) == 0:
        warn('env file not found')
        return
    new_variables = set(env.keys()) - set(env_example.keys())
    deleted_variables = set(env_example.keys()) - set(env.keys())
    for i in deleted_variables:
        del env_example[i]
    for i in new_variables:
        env_example[i] = ''
    print_env(env_example, output)

def warn(message: str = "generic warning"):
    click.echo(click.style(message, fg='red'))


def print_env(env, filename):
    print("Hello Python!", file=open('output.txt', 'w'))
    with open(filename, "w") as file:
        for i in env.keys():
            file.write(i + "=" + env[i] + "\n")
    click.echo("done")
