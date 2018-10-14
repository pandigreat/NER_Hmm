import os
import jieba
import nltk
import random
#import numpy as np


class Data_Process:
    def __init__(self, mark_type_file, split_char='/', term='char', file_name, split_percent=0.9):
        self.mark_dic = self.process_mark_type(mark_type_file)
        self.term = term
        self.split_char = split_char

    def process_mark_type(self, mark_type_file):
        mark_dic = {}
        with open(mark_type_file, 'r') as file_p:
            for line in file_p:
                key, val = line.split('|')
                mark_dic[key] = val.split(' ')

        return mark_dic

    def replace_mark_in_data(self, file_name):



    def shuffle(self, data, split_percenet=self.split_percent):
        random.shuffle(data)
        n_len = len(data)
        return (data[:n_len*split_percenet], data[n_len*split_percenet:])




