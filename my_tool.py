import click
from dotenv import dotenv_values
import os

@click.command()
@click.option('-e', '--env', type=str, help='Relative path to the .env file', default='.env')
@click.option('-o', '--output', type=str, help='Relative path to the output .env.example', default='.env.example')
def cli(env, output):
    try:
        env = dotenv_values(env)
        env_example = dotenv_values(output)
        
        if not env:
            click.echo("Warning: .env file is empty or not found.")
            return

        new_variables = set(env.keys()) - set(env_example.keys())
        deleted_variables = set(env_example.keys()) - set(env.keys())

        if new_variables or deleted_variables:
            if click.confirm("Do you want to update the output file?"):
                update_env_file(output, env, new_variables, deleted_variables)
            else:
                click.echo("No changes were made.")
        else:
            click.echo("No changes found between the files.")
    
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

def update_env_file(filename, env, new_variables, deleted_variables):
    try:
        for var_name in deleted_variables:
            del env[var_name]
        for var_name in new_variables:
            env[var_name] = ''

        with open(filename, "w") as file:
            for key, value in env.items():
                file.write(f"{key}={value}\n")
        
        click.echo("Changes saved to the output file.")
    except Exception as e:
        click.echo(f"Failed to update the output file: {str(e)}")

if __name__ == '__main__':
    cli()
