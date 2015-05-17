#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A program that allows me to enter my billable time."""

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
    conf_input = raw_input('Would you like to try again/enter \
more time? Yes or No\n')

    if conf_input.lower()[0] == 'y':
        timeentry()

    else:
        print 'Ok, good bye.'
        raise SystemExit()


def timeentry():
    """A function to enter billable time.

    Example:
        >>>Please enter client id:
        101
        Please enter work code:
        2
        Please enter the work minutes:
        30
        The information has been saved.
        Would you like to enter more time? Yes or No
        no
        Ok, good bye.

    """
    clientdb = {}
    todayvar = datetime.date.today()

    print 'Please enter billable time only for active clients.'
    print 'Your current active client\'s are:'
    for keys, values in clientdata.CLIENTS.iteritems():
        print keys, values['first'], values['last']
    print ''
    print 'Your current work codes and their respective hourly rates are:'
    for keys, values in clientdata.HOURLY_RATE.iteritems():
        print keys, values
    print ''

    client_input = raw_input('Please enter client id:\n')

    if int(client_input) not in clientdata.CLIENTS.keys():
        print 'Sorry this client ID is not valid.'
        confirmation()

    code_input = raw_input('Please enter work code:\n')

    if int(code_input) not in clientdata.HOURLY_RATE.keys():
        print 'Sorry this work code is not valid.'
        confirmation()

    time_input = raw_input('Please enter the work minutes:\n')

    clientdb.update({client_input: dict(code=code_input, time=time_input)})

    with open('clientdb.csv', 'a') as csvfile:
        fieldnames = ['client_id', 'code', 'time', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'client_id': client_input, 'code': code_input,
                         'time': time_input, 'date': todayvar})
        csvfile.close()
        print 'The information has been saved.'

    confirmation()

if __name__ == '__main__':
    timeentry()
