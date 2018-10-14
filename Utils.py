#!- encoding:utf-8
import json
import numpy as np

class Utils:
    def __init__(self, sup_params_file):
        self.raw_data = open(sup_params_file, 'r').read()
        self.sup_params = json.loads(self.raw_data)
        self.emisson_prob = {}
        self.transition_prob = {}
        self.hidden_state = {}
        self.start_prob = {}
        self.Load_Params_of_Hmm()


    def Load_Params_of_Hmm(self):
        emisson_prob_file = self.sup_params['emission_prob_file']
        start_prob_file = self.sup_params['start_prob_file']
        transition_prob_file = self.sup_params['transition_prob_file']

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
            emission_prob[state] = {}
        with open(transition_prob_file, 'r') as file_d:
            for line in file_d:
                start_state, end_state, count, trans_prob = line.strip().split(" ")
                transition_prob[start_state][end_state] = np.array(trans_prob, dtype=np.float64)
        with open(emisson_prob_file, 'r') as file_d:
            for line in file_d:
                state, ob_word, count, emi_prob = line.strip().split(' ')
                emission_prob[state][ob_word] = emi_prob


        self.start_prob = start_prob
        self.hidden_state = hidden_state
        self.emission_prob = emission_prob
        self.transition_prob = transition_prob

    def GetHmmModel(self):
        return (self.start_prob, self.emisson_prob,self.transition_prob, self.hidden_state)
'''

if __name__ == '__main__':
    sup_params_file = './sup_params.txt'
    utils_u = Utils(sup_params_file)
    (a,b,c,d) = utils_u.GetHmmModel()
    print(a)

'''

