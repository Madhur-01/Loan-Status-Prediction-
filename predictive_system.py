# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model

loaded_model = pickle.load(open(r"C:/Users/madhu/Dropbox/My PC (LAPTOP-9DI2D1AT)/Documents/GitHub/Loan-Status-Prediction-/trained_model.sav", 'rb'))
input_data = [[1,1,0,0,0,9083,0,228,360,1,1]]   
prediction = loaded_model.predict(input_data)      


if(prediction[0]==0):
    print('NO')
else :
    print('YES')