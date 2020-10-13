#!/usr/bin/env python3

import dateutil.parser


class ValueParsers():

    @staticmethod
    def parse_char64(val):
        """
        Test val is exactely 64 characters. Can be anything that can be handled
        by str()
        """
        val = str(val)
        if(len(val) != 64):
            return ("This field expects a string of lenght 64 but the lenght "
                    "of the string is {}. The string is: {}"
                    .format(len(val), val))

    @staticmethod
    def parse_date(val):
        """
        Test str(val) can be converted using dateutil.parser.isoparse()
        """
        try:
            # If the date is just a year it might be an integer (ex. 2018)
            dateutil.parser.isoparse(str(val))
        except ValueError:
            return ("Date format not recognised. Date format must adhere to "
                    "the ISO 8601 format (YYYY-MM-DD). Provided value was: {}"
                    .format(val))

    @staticmethod
    def parse_integer(val):
        """
        Test that val is an integer
        """
        try:
            val = int(float(val))
        except ValueError:
            return "Value must be an integer. Value was: {}".format(val)

    @staticmethod
    def parse_percentage(val):
        """
        Test that val is between 0 and 100.
        """
        try:
            val = float(val)
        except ValueError:
            return "Value must be a number. Value was: {}".format(val)
        if(val < 0 or val > 100):
            return ("Percentage value must be between 0 and 100. The value "
                    "was: {}".format(val))

    @staticmethod
    def parse_string(val):
        try:
            val = str(val)
        except ValueError:
            return "Value could not be converted to a string."

    @staticmethod
    def parse_float(val):
        try:
            val = float(val)
        except ValueError:
            return "Value must be a float. Value was: {}".format(val)