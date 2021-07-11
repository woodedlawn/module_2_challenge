# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(csvpath, csvdata):
    """Saves the data as a CSV file to path provided.

    Args:
        csvpath (Path): The csv file path.
        csvdata (list of lists): The csv data to save

    Returns:
        None

    """
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile)

        # add the CSV header
        csvwriter.writerow(["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"])

        # write the CSV data
        for row in csvdata:
            csvwriter.writerow(row)
    return None