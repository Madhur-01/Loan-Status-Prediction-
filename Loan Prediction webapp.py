# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:36:52 2023

@author: madhu
"""
import numpy as np
import pickle
import streamlit

loaded_model = pickle.load(open(r"C:\Users\madhu\Dropbox\My PC (LAPTOP-9DI2D1AT)\Documents\GitHub\Stock-Price-Predction\trained_model.sav", 'rb'))
