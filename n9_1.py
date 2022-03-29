from datetime import date, datetime, timedelta,time
from hashlib import new
from re import I, T
from time import strftime 
import sys
import logging

from click import echo

logging.basicConfig(filename = 'n9_1.logs',level = logging.INFO)


def main(argv) ->list:
    logging.info("main with %d arguments", len(argv))
    if len(argv) > 1:
        logging.info("main with argument: %s", argv[1])

    if 'newyear'in argv:
        today = datetime.today()
        nye = datetime(today.year+1,1,1)
        t2ny = nye - today
        days_to_newyear = t2ny.days
       
        if '--hours' in argv:
            hours_to_newyear = int(t2ny.seconds/3600)
            print(days_to_newyear, 'days', hours_to_newyear, 'hours' )
            logging.info("%d days %d hours", days_to_newyear, hours_to_newyear)
        else:
            print(days_to_newyear,'days')
            logging.info("%d days", days_to_newyear)


if __name__ == "__main__":
    
    main_list = sys.argv
    #main_list.append('newyear')
    #main_list.append('--hours')
    main(main_list)
    








    





