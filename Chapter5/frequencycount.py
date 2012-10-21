#! /usr/bin/env python3
import re


class Hist:
    """Reads text files and counts the frequency of words in the text"""

    def __init__(self, filename):
        self.freq_map = {}
        self.read_file(filename)

    def read_file(self, filename):
        """
        Reads the text file named in filename, and counts the frequency,
        stripping out any punctuation
        """
        with open(filename) as in_file:
            for line in in_file:
                line_list = line.split()
                # Clean up puncuation
                line_list = [re.sub('[-.!?:"]', '', s) for s in line_list]
                for word in line_list:
                    # Just convert everything to lowercase for now
                    word = word.lower()
                    if not word in self.freq_map:
                        self.freq_map[word] = 1
                    else:
                        self.freq_map[word] += 1


def test_hist(filename):
    print("Reading in file")
    hist = Hist(filename)
    print("Done!")
    order = sorted(hist.freq_map, key=lambda x: hist.freq_map[x], reverse=True)
    for i in range(100):
        print(order[i], ": ", hist.freq_map[order[i]])


if __name__ == '__main__':
    test_hist('SherlockHolmes.txt')
