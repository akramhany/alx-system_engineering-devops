#!/usr/bin/python3

"""
A module in which I would make requests to a fake API.
"""
import sys
import csv

utilty = __import__('0-gather_data_from_an_API')


def convertJsonToCsv(data, file_name):
    "Takes json data and convert it to csv, then write it to a file"

    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        for item in data:
            csv_writer.writerow(item.values())


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: ./file_name employeeId')
        exit(1)

    csv_file_name = 'USER_ID.csv'
    convertJsonToCsv(utilty.retrieveInfo(sys.argv[1]), csv_file_name)
