import numpy as np


class InputFileReader:
    def readContent(self, fileName):
        read_data = ''
        with open(fileName) as f:
            read_data = f.read()

        return read_data.split('\n')
