import pandas as pd
from test_find_path import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



def baro_data_collect():
    
    color_arrary=['black','red','darkorange','gold','forestgreen','teal','blue','magenta']
    for index_file,file in enumerate(showfile(os.path.join(dirPath,"baro_function\\rawdata"))):
        time_array = []
        baro_value = []
        print(file)
        #print(df)
        df = pd.read_csv('baro_function/rawdata/' +file ,names=['column1','column2','column3','column4'])
        df.drop([0],axis=0,inplace=True)
        
        for index,time in enumerate(df['column1']):
            time_array.append(datetime.strptime(time,"%m-%d-%Y %H:%M:%S"))
            baro_value.append(float(df['column3'][index+1]))
        #use scatter to clean or find the reason of the strange line
        plt.plot(time_array,baro_value,color=color_arrary[index_file])
    plt.show()
    
def baro_data_plot_single(file,color_file):
    time_array = []
    baro_value = []
    df = pd.read_csv('baro_function/rawdata/' +file ,names=['column1','column2','column3','column4'])
    df.drop([0],axis=0,inplace=True)
        
    for index,time in enumerate(df['column1']):
        time_array.append(datetime.strptime(time,"%m-%d-%Y %H:%M:%S"))
        baro_value.append(float(df['column3'][index+1]))
    #use scatter to clean or find the reason of the strange line
    plt.plot(time_array,baro_value,label=file,color=color_file)
    plt.xlim(time_array[0],time_array[-1]) 
    plt.grid(b=True, which='major', color='#666666', linestyle='-.')
    plt.title("Baro log",fontsize=18)
    plt.xlabel("time",fontsize=18)
    plt.ylabel("Baro(PA)",fontsize=18)
    plt.legend(loc=4)
    
    
    plt.show()

#baro_data_plot_single('Baro_goleden_1.csv','black')