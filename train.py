from read_data import read_csv_to_np
import pandas as pd    
import matplotlib.pyplot as plt
import tensorflow as tf

def predict(event,user):
  dir = './personalData/'+event+'/'
  test_file = pd.read_csv(dir+user+'_data.csv',skip_blank_lines=False,sep="\n")
  X = read_csv_to_np(test_file)
  print(X.shape)
  imported = tf.saved_model.load('./saved_model/'+user+'/'+event)

  print(imported(X))


def train_model(event,user):
  dir = './personalData/'+event
  test_file = pd.read_csv(dir+user+'_data.csv',skip_blank_lines=False,sep="\n")
  out_file = pd.read_csv(dir+user+'_result.csv',sep="\n")

  X = read_csv_to_np(test_file)
  Y = read_csv_to_np(out_file)

  print(X.shape)
  print(Y.shape)

  for x in X:
    plt.plot(x)
    plt.xlabel('frames')
    plt.ylabel('angle')
  plt.show()