import click
import requests
import validators

def validate_positive_int(ctx, param, value):
    if value < 1:
        raise click.BadParameter(f"{param} should be positive integer greater than 0")
    return value


def validate_url(ctx, param, value):
    if not validators.url(value):
        response = requests.get(f'http://{value}')
        if response.status_code == 200:
            return f'http://{value}'
        response = requests.get(f'https://{value}')
        if response.status_code == 200:
            return f'https://{value}'
        raise click.BadParameter(f"{param}: {value} is not a valid url")

    return value