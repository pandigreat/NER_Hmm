from Utils import *
import traceback
import numpy as np
import os


'''
    Hmm Model to tag on NER
    @author pandigreat
    @sup_params_file the file contains the super_parameters
'''

Class HmmTagger(object):

    def __init__(self, sup_params_file):
        self.utils = Utils(sup_params_file)
        self.indicator = Indicator()
        self.emission_prob = self.utils.emission_prob
        self.transition_prob = self.utils.transition_prob
        self.start_prob = self.utils.start_prob
        self.hidden_state = self.utils.hidden_state
        self.ner_type = self.utils.ner_type

    def Estimate(self):
        data_iter = self.utils.LoadTestData()
        dict_eval = self.indicator
        try:
            for data, labels in data_iter:
                dict_eval += len(lables.keys())
                pass
                test_prob, tag_seq = self.viterbi(data)
                




        except Exception:
            traceback.print_exc()
        finally:
            self.indicator = Indicator(dict_eval)

    def Extract_From_Tags(self):


    def viterbi(self, data):
        return data,data
        pass

    def Access_Result(self):
        pass
