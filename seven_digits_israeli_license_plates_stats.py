# -*- coding: utf-8 -*-
"""
Reads the Ministry of Transport csv of car details.
Creates a statistics JSON file with details for each plate number suffix.
Usage: seven_digits_israeli_license_plates_stats.py -i INPUT -o OUTPUT

Options:
  -i The CSV file downloaded from the Ministry of Transport website.
  -o Output path for the JSON stats file.

"""
import json
import pandas

from collections import defaultdict
from docopt import docopt
from typing import DefaultDict

from utils import convert_manufacturer_to_hebrew

FIRST_EIGHT_DIGITS_PLATE_NUMBER = 10000000
FILE_ENCODING = 'ISO-8859-1'


def get_license_plate_number_suffix_stats(
        license_plates_data: pandas.DataFrame
) -> DefaultDict[str, DefaultDict[str, DefaultDict[str, int]]]:
    suffix_years = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for _, row in license_plates_data.iterrows():
        plate_number = row['mispar_rechev']
        print(f'Working on {plate_number}')
        manufacturer = convert_manufacturer_to_hebrew(row['tozeret_nm'])
        year = row['shnat_yitzur']
        if int(plate_number) < FIRST_EIGHT_DIGITS_PLATE_NUMBER:
            suffix_years[str(plate_number)[-2:]][year][manufacturer] += 1

    return suffix_years


def main(input_file_path: str, output_file_path: str):
    license_plates_data = pandas.read_csv(
        input_file_path,
        delimiter='|',
        encoding=FILE_ENCODING,
        on_bad_lines='skip'
    )

    suffix_years = get_license_plate_number_suffix_stats(license_plates_data)

    with open(output_file_path, 'w', encoding=FILE_ENCODING) as output_file:
        output_file.write(json.dumps(suffix_years))


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments['-i'], arguments['-o'])
