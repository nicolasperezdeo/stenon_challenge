import os
import typing
import logging
import math
import csv

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def read_csv_data(filename: str, delimiter: str) -> pd.DataFrame:
    """
    Function that loads a given  .csv file using Pandas library and return it in a DataFrame object.
    :param filename: String containing the filename.
    :param delimiter: String of the csv delimiter.
    :return: Pandas DataFrame
    """
    df = pd.read_csv(filename, sep=delimiter)

    return df


def main():
    # Get current working directory
    current_path = os.getcwd()

    # Defining the filename
    filename = 'challenge_juniorDS_feb2021.csv'

    file_path = os.path.join(current_path, filename)

    # Loading data from the given file
    raw_data = read_csv_data(file_path, ';')

    sensor_data = raw_data[raw_data.columns[:-8]]

    print(raw_data.head())


if __name__ == '__main__':
    main()
