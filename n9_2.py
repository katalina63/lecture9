from datetime import date, datetime, timedelta,time
from hashlib import new
from re import I, T
from time import strftime 
import sys
import click
import enum
import random
import logging

logging.basicConfig(filename = 'n9_2.logs',level = logging.DEBUG)

class Toy(enum.Enum):
    Blue_ball = 0
    Purple_angel = 1
    
@click.group()
def main():
    pass
    
@main.command()
@click.option('--hours', default=False, is_flag=True)
def newyear(hours):
    logging.info(f'Newyear: hours={hours}')
    today = datetime.today()
    nye = datetime(today.year+1,1,1)
    t2ny = nye - today
    days_to_newyear = t2ny.days
    
    if hours:
        hours_to_newyear = int(t2ny.seconds/3600)
        click.echo(f'{days_to_newyear} days {hours_to_newyear} hours')
    else:
        click.echo(f'{days_to_newyear} days')

@main.command()
def toy()->None:
    logging.debug(f'Toy: start')
    last_index = len(Toy) - 1
    r = random.randint(0,last_index)
    logging.debug(f'Toy: {r}')
    toy = Toy(r)
    logging.info(f'Toy: {str(toy)}')
    click.echo(f'{str(toy).removeprefix("Toy.").replace("_"," ")}')

if __name__ == '__main__':
    main()








    





