#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program that allows me to generate a work report."""

import csv
import clientdata
import datetime


def createreport():
    """A function that takes no input and creates a work report showing all
    entries for the past 30 days and the total billed amount.

    Returns:
        report (str): The report containing the total time worked in a given
        time period.

    Example:
    >>>
    A list of your work entries for the last 30 days:

    {'date': '2015-05-17', 'code': '4', 'client_id': '103', 'time': '15'}
    {'date': '2015-05-17', 'code': '5', 'client_id': '101', 'time': '20'}
    {'date': '2015-05-17', 'code': '4', 'client_id': '101', 'time': '90'}
    {'date': '2015-05-17', 'code': '6', 'client_id': '101', 'time': '90'}
    {'date': '2015-05-17', 'code': '2', 'client_id': '107', 'time': '110'}
    {'date': '2015-05-17', 'code': '6', 'client_id': '107', 'time': '200'}
    {'date': '2015-05-17', 'code': '1', 'client_id': '106', 'time': '20'}

    You worked a total of 9 hours in the past 30 days.

    You billed a total amount of $2813.332.

    """

    total_time = 0
    cost = 0
    today = datetime.date.today()
    diff = datetime.timedelta(30)

    print 'A list of your work entries for the last 30 days:\n'

    with open('clientdb.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            day = int(row['date'][8:])
            month = int(row['date'][5:7])
            year = int(row['date'][0:4])
            date_entry = datetime.date(year, month, day)

            if date_entry + diff > today:
                rate = (clientdata.HOURLY_RATE[int(row['code'])][1] / 60)
                total_time += int(row['time'])
                cost += round((rate * (int(row['time']))), 3)
                print row

    print ''
    print 'You worked a total of {} hours in the past 30 \
days.\n'.format(total_time / 60)
    print 'You billed a total amount of ${}.\n'.format(cost)

    csvfile.close()

if __name__ == '__main__':
    createreport()
