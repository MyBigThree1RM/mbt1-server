import os
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import LSTM, Dense,ZeroPadding3D
from keras.models import Sequential

def read_csv_to_np(csv_file):
    test_dataset=[]
    li = []
    for row in csv_file.iterrows():
        d = row[1][0]
        if(pd.isnull(d)):
            test_dataset.append(np.asarray(li).astype('float32'))   
            li = []
        else :
            d = np.asarray(list(map(float,d.split(',')))).astype('float32')
            li.append(d)
  
    test_dataset = tf.keras.preprocessing.sequence.pad_sequences(test_dataset, padding = "pre")
    #print(test_dataset)
    return np.asarray(test_dataset).astype('float32')
