import pandas as pd
import numpy as np
import pickle


with open('model.pkl', 'rb') as handle:
    model = pickle.load(handle)
