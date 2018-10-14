#!- encoding:utf-8
import json
import numpy as np

''' The Utils is a class type ot load Hmm model
    @author pandigreat
    @:param sup_params the file that includes super_paramaters in json format
'''
class Utils:
    def __init__(self, sup_params_file):
        self.raw_data = open(sup_params_file, 'r').read()
        self.sup_params = json.loads(self.raw_data)
        self.emission_prob = {}
        self.transition_prob = {}
        self.hidden_state = {}
        self.start_prob = {}
        self.ner_type = {}
        self.Load_Params_of_Hmm()

    '''
        Load Params of Hmm model
    '''
    def Load_Params_of_Hmm(self):
        emisson_prob_file = self.sup_params['emission_prob_file']
        start_prob_file = self.sup_params['start_prob_file']
        transition_prob_file = self.sup_params['transition_prob_file']
        ner_type = self.sup_params['ner_type_file']

        start_prob = {}
        emission_prob = {}
        transition_prob = {}
        hidden_state = []

        with open(start_prob_file, 'r') as file_d:
            for line in file_d:
                state, times, state_prob = line.strip().split(' ')
                start_prob[state] = np.array(state_prob, dtype=np.float64)
                hidden_state.append(state)
        for state in hidden_state:
            transition_prob[state] = {}
            for sec_state in hidden_state:
                transition_prob[state][sec_state] = np.array(0, dtype=np.float64)
            emission_prob[state] = {}
        with open(transition_prob_file, 'r') as file_d:
            for line in file_d:
                start_state, end_state, count, trans_prob = line.strip().split(" ")
                transition_prob[start_state][end_state] = np.array(trans_prob, dtype=np.float64)
        with open(emisson_prob_file, 'r') as file_d:
            for line in file_d:
                state, ob_word, count, emi_prob = line.strip().split(' ')
                emission_prob[state][ob_word] = np.array(emi_prob, dtype=np.float64 )


        self.start_prob = start_prob
        self.hidden_state = hidden_state
        self.emission_prob = emission_prob
        self.transition_prob = transition_prob
        self.ner_type = ner_type

    '''
        @return start_prob, emission_prob, transition_prob, hidden_state
    '''
    def GetHmmModel(self):
        return (self.start_prob, self.emission_prob,self.transition_prob, self.hidden_state)

    '''
        process the test data and the lable in test data file
        @:param data the data string from test data file
    '''
    def TestDataFormatProcess(self, data):
        pass
        for line in data:
            raw_data, label = line.strip().split(' ')
            yield  (raw_data, json.loads(label))

    '''
        @:return return a generator to get test data
    '''
    def LoadTestData(self):
        test_data_file = self.sup_params['test_data']
        test_data = open(test_data_file).read()
        return self.TestDataFormatProcess(test_data)

'''
    The Indicator that maintain the evaluation value and calculate f1 score 
    @:param indicator_dict the dictionary from the hmm model of which value can be to eval
    the f1 score
'''

class Indicator(object):
    def __init__(self, indicator_dict=None):
        self.total, self.true_positive, self.false_positive,self.false_negative, \
        self.true_negative = 0,0,0,0,0
        if indicator_dict != None:
            self.total = indicator_dict['total']
            self.true_positive = indicator_dict['t2t']
            self.false_negative = indicator_dict['t2f']
            self.false_positive = indicator_dict['f2t']
            self.true_negative = indicator_dict['f2f']


    def get_recall(self):
        return float(self.true_positive)/(self.true_positive+self.false_negative)

    def get_precision(self):
        return float(self.true_positive)/(self.true_positive+self.false_positive)
    def get_accuracy(self):
        return float(self.true_positive+self.true_negative)/ \
               (self.true_negative+self.true_positive+self.false_negative+self.false_positive)
    def get_f1_value(self):
        return 2*(self.get_precision()+self.get_recall()) / \
               (self.get_recall()+self.get_precision())


'''

if __name__ == '__main__':
    sup_params_file = './sup_params.txt'
    utils_u = Utils(sup_params_file)
    (a,b,c,d) = utils_u.GetHmmModel()
    print(a)

'''

