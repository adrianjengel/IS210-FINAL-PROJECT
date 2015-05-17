#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program that allows me to generate bills for my clients."""

import csv
import clientdata
import datetime


def confirmation():
    """A function to ask the user a confirmation question.

    Example:
        >>> confirmation()
        Would you like to try again/enter more time? Yes or No
        no
        Ok, good bye.

    """
    conf_input = raw_input('Would you like to try again? Yes or No\n')

    if conf_input.lower()[0] == 'y':
        createbill()

    else:
        print 'Ok, good bye.'
        raise SystemExit()


def createbill():
    """A function to create a customer bill.

    Returns:
        bill (str): The bill containing the total time worked in the last 30
        days and the amount owed.

    Examples:
    >>>Welcome. Please enter the client ID you would like to print a bill for.
    101
    Dear Brandon,

    The total time I worked on your case(s) is 360 mins and the
    total cost is $2030.0.

    >>>Welcome. Please enter the client ID you would like to print a bill for.
    103
    Dear Betty,

    The total time I worked on your case(s) is 70 mins and the
    total cost is $366.67.

    """
    total_time = 0
    cost = 0
    today = datetime.date.today()
    diff = datetime.timedelta(30)

    client_input = int(raw_input('Please enter the client ID you would like to \
print a bill for.\n'))

    if client_input not in clientdata.CLIENTS.keys():
        print 'Sorry this client ID is not valid.'
        confirmation()

    with open('clientdb.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            day = int(row['date'][8:])
            month = int(row['date'][5:7])
            year = int(row['date'][0:4])
            date_entry = datetime.date(year, month, day)
            firstname = clientdata.CLIENTS[client_input]['first']
            email = clientdata.CLIENTS[client_input]['email']
            if row['client_id'] == str(client_input) and \
               (date_entry + diff > today):
                total_time += int(row['time'])
                rate = (clientdata.HOURLY_RATE[int(row['code'])][1] / 60)
                cost += (rate * (int(row['time'])))

    print ''
    print 'To: {}\n'.format(email)
    print ''
    print 'Today\'s date is: {}'.format(today)
    print ''
    print 'Dear {},\n'.format(firstname)
    print 'The total time I worked on your case(s) is {} mins and the total \
cost is ${}.'.format(total_time, round(cost, 2))
    print ''
    print 'You have until {} to pay this amount.'.format(today + diff)

    csvfile.close()

if __name__ == '__main__':
    createbill()
