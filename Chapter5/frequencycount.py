#! /usr/bin/env python3
import re
import math
from matplotlib import pyplot


class WordRanker:
    """Reads text files and counts the frequency of words in the text"""
    default_word_dict = {'freq': None, 'rank': None}

    def __init__(self, filename):
        self.freq_map = {}
        self.read_file(filename)
        # Need to rank after reading, or all ranks will be none
        self.rank_words()

    def read_file(self, filename):
        """
        Reads the text file named in filename, and counts the frequency,
        stripping out any punctuation
        """
        with open(filename) as in_file:
            for line in in_file:
                line_list = line.split()
                # Clean up punctuation
                line_list = [re.sub('[-.!?:"]', '', s) for s in line_list]
                for word in line_list:
                    # Just convert everything to lowercase for now
                    word = word.lower()
                    if not word in self.freq_map:
                        self.freq_map[word] = self.default_word_dict.copy()
                        self.freq_map[word]['freq'] = 1
                    else:
                        self.freq_map[word]['freq'] += 1

    def rank_words(self):
        """Adds ranks for each word to freq_map"""
        ranked_words = sorted(
            self.freq_map,
            key=lambda x: self.freq_map[x]['freq'],
            reverse=True
        )
        for rank, word in enumerate(ranked_words):
            self.freq_map[word]['rank'] = rank + 1

    def graph_zipf(self):
        ranked_words = sorted(
            self.freq_map,
            key=lambda x: self.freq_map[x]['rank']
        )
        log_freqs = []
        log_ranks = []
        for word in ranked_words:
            word_stats = self.freq_map[word]
            log_f = math.log(word_stats['freq'])
            log_r = math.log(word_stats['rank'])
            log_freqs.append(log_f)
            log_ranks.append(log_r)
        pyplot.plot(log_ranks, log_freqs)
        pyplot.xlabel('Word rank (log(rank))')
        pyplot.ylabel('Word frequency (log(freq))')
        pyplot.show()


def test_hist(filename):
    print("Reading in file")
    hist = WordRanker(filename)
    print("Done!")
    ordered = sorted(hist.freq_map, key=lambda x: hist.freq_map[x]['rank'])
    for rank in range(20):
        print(ordered[rank])


def test_graph(filename):
    hist = WordRanker(filename)
    hist.graph_zipf()

if __name__ == '__main__':
    test_graph('SherlockHolmes.txt')
