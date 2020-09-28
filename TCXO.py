import pandas as pd
from test_find_path import *
import matplotlib.pyplot as plt
import numpy as np


def collect_tcxo_temp_vs_freq():
    dict = {}
    index = 0
    for file in show_csv_file_nam(target_path):

        arrary1 = []
        arrary2 = []
        arrary3 = []
     
        df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ' + file,names=['column1','column2','column3'])
        for freq in df['column1']:
            arrary1.append(freq)
        for temp in df['column2']:
            arrary2.append(temp)
        for ppm in df['column3']:
            arrary3.append(ppm)  
        
        dict[str(index)] = arrary1
        index = index + 1
        dict[str(index)] = arrary2
        index = index + 1
        dict[str(index)] = arrary3
        index = index + 1
        
    df = pd.DataFrame(dict)
    print(df)
    df.to_csv('tcxo_temp/result.csv')


def plot_tcxo_temp_ppm():
    index=0
    brandname=['Ref.','TXC8','TXC7','TXC6','TXC4','TXC3','TXC2','TXC1']
    brandname_index = 0
    
    plt.figure(figsize=(20,10)) #控制視窗大小
    for i in range(8):

        arrary1 = []
        arrary2 = []
        
        df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/result.csv')
        df.drop(['Unnamed: 0'],axis=1,inplace=True)
        df.drop([0,1,2],axis=0,inplace=True)
        
        for Temp in df[str(index+1)]:
            arrary1.append(float(Temp))
        for ppm in df[str(index+2)]:
            arrary2.append(float(ppm))
            
        plt.plot(arrary1,arrary2,label=brandname[brandname_index]) #將每一組plot
        plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.) #將每一組的lable 放到外面
        index = index +3
        brandname_index = brandname_index + 1
    
    plt.xlim(-40, 100) #設定x軸範圍
    plt.ylim(-0.5, 0.5)#設定y軸範圍
    
    my_x_ticks = np.arange(-40, 100, 5) #設定x軸刻度
    my_y_ticks = np.arange(-0.5, 0.5,0.1)  #設定y軸刻度
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    
    plt.grid(b=True, which='major', color='#666666', linestyle='-.') # 格線
    
    plt.title("Temperature - Frequency Deviation",fontsize=20) #lable
    plt.xlabel("Temperature (Degree C)",fontsize=20)
    plt.ylabel("Temperature Deviation (ppm)",fontsize=20)
    
    plt.show()
#===================================================================================
def plt_setting():
    plt.xlim(-40, 100) 
    plt.ylim(-0.5, 0.5)
    my_x_ticks = np.arange(-40, 100, 5) 
    my_y_ticks = np.arange(-1, 1.1,0.1) 
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.grid(b=True, which='major', color='#666666', linestyle='-.')
    plt.title("Temperature - Frequency Deviation",fontsize=20)
    plt.xlabel("Temperature (Degree C)",fontsize=20)
    plt.ylabel("Temperature Deviation (ppm)",fontsize=20)
#===================================================================================
#temp_freq:

def temp_ppm_single(filename,colors):   
    arrary1 = []
    arrary2 = []
    df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+filename,names=['0','1','2'])
    df.drop(['0'],axis=1,inplace=True)
    df.drop([0,1,2],axis=0,inplace=True)
    for Temp in df['1']:
        arrary1.append(float(Temp))
    for ppm in df['2']:
        arrary2.append(float(ppm))
    plt.plot(arrary1,arrary2,label=filename,color = colors)
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt_setting()
    plt.show()
   
def temp_ppm_All(colors):
    color_index = 0
    for file in show_csv_file_nam(target_path):
        
        arrary1 = []
        arrary2 = []
        df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+file,names=['0','1','2'])
        df.drop(['0'],axis=1,inplace=True)
        df.drop([0,1,2],axis=0,inplace=True)
        for Temp in df['1']:
            arrary1.append(float(Temp))
        for ppm in df['2']:
            arrary2.append(float(ppm))
        plt.plot(arrary1,arrary2,label=file,color = colors[color_index])
        color_index = color_index + 1
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt_setting()
    plt.show()
    
def temp_slope_single(filename,colors):
    arrary1=[]
    arrary2=[]
    df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+filename,names=['0','1','2'])
    df.drop(['0'],axis=1,inplace=True)
    df.drop([0,1,2],axis=0,inplace=True)
    for i in range(len(df['1'])-1):
        
        arrary1.append(float(df['1'][i+4]))
            
        if abs(float(df['1'][i+4])-float(df['1'][i+3])) > 0:
            arrary2.append(round((float(df['2'][i+4])-float(df['2'][i+3]))/abs(float(df['1'][i+4])-float(df['1'][i+3])),3))
        else:
            arrary2.append(0)
    plt.plot(arrary1,arrary2,label=filename,color = colors)
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt_setting()
    plt.show()
    
def temp_slope_all(colors):
    color_index = 0
    for file in show_csv_file_nam(target_path):
        arrary1=[]
        arrary2=[]
        df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+file,names=['0','1','2'])
        df.drop(['0'],axis=1,inplace=True)
        df.drop([0,1,2],axis=0,inplace=True)
        for i in range(len(df['1'])-1):
            
            arrary1.append(float(df['1'][i+4]))
                
            if abs(float(df['1'][i+4])-float(df['1'][i+3])) > 0:
                arrary2.append(round((float(df['2'][i+4])-float(df['2'][i+3]))/abs(float(df['1'][i+4])-float(df['1'][i+3])),3))
            else:
                arrary2.append(0)
        plt.plot(arrary1,arrary2,label=file,color = colors[color_index])
        color_index = color_index + 1
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)   
    plt_setting()
    plt.show()
    
    
def temp_slope_single_each_temp_record(filename,colors):
    arrary1 = []
    arrary2 = []
    df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+filename,names=['0','1','2'])
    df.drop(['0'],axis=1,inplace=True)
    df.drop([0,1,2],axis=0,inplace=True)
    for i in range(len(df['1'])-1):
        arrary1.append(float(df['1'][i+4]))
        arrary2.append(round(float(df['2'][i+4])-float(df['2'][i+3]),3))
    plt.plot(arrary1,arrary2,label=filename,color = colors)
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)   
    plt_setting()
    plt.show()
    

def temp_slope_All_each_temp_record(colors):
    color_index = 0
    for file in show_csv_file_nam(target_path):
        arrary1 = []
        arrary2 = []
        df = pd.read_csv('tcxo_temp/TCXO_TEMP_FREQ/'+file,names=['0','1','2'])
        df.drop(['0'],axis=1,inplace=True)
        df.drop([0,1,2],axis=0,inplace=True)
        for i in range(len(df['1'])-1):
            arrary1.append(float(df['1'][i+4]))
            arrary2.append(round(float(df['2'][i+4])-float(df['2'][i+3]),3))
        
        
        plt.plot(arrary1,arrary2,label=file,color = colors[color_index])
        color_index = color_index + 1
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)   
    plt_setting()
    plt.show()
#===================================================================================
#phase noise

def phase_noise_single_plot(filename,colors):
    arrary1 = []
    arrary2 = []
    df = pd.read_csv('tcxo_temp/TCXO_PHASE_NOISE/'+filename,names=['0','1'])
    df.drop([0],axis=0,inplace=True)
    for freq in df['0']:
        arrary1.append(round(float(freq),3))
    for  db in df['1']:
        arrary2.append(round(float(db),3))
    plt.semilogx(arrary1,arrary2,lw=2,label=filename,color = colors)
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt.ylim(-160, -50)
    plt.xlabel("log(x)")
    plt.ylabel("y")
    plt.grid(b=True, which='major', color='#666666', linestyle='-.')
    plt.title("phase_noise",fontsize=20)
    plt.show()

def phase_noise_all_plot(colors):
    color_index = 0
    for file in show_csv_file_nam(TCXO_PHASE_NOISE_path):
        arrary1 = []
        arrary2 = []
        df = pd.read_csv('tcxo_temp/TCXO_PHASE_NOISE/'+file,names=['0','1'])
        df.drop([0],axis=0,inplace=True)
        for freq in df['0']:
            arrary1.append(round(float(freq),3))
        for  db in df['1']:
            arrary2.append(round(float(db),3))
        plt.semilogx(arrary1,arrary2,lw=2,label=file,color = colors[color_index])
        color_index = color_index +1
        plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
        plt.ylim(-160, -50)
        plt.xlabel("log(x)")
        plt.ylabel("y")
        plt.grid(b=True, which='major', color='#666666', linestyle='-.')
        plt.title("phase_noise",fontsize=20)
    plt.show()

def start_up_frequency(filename,colors):
    arrary1 = []
    arrary1_freq2subfreq1 = []
    temp_max = 0
    data = pd.read_table('tcxo_temp/TCXO_START_UP_FREQ/'+filename,sep=' ',names=['0','1','2'])
    #print(data)
    #print(data['1'][0][6]+data['1'][0][7])
    for index,value in enumerate(data['2']):
        if index < 15:
            if float(value)>temp_max:
                temp_max = round(value,3)
        if index == 15:
            arrary1.append(temp_max)
        if index > 15:
            if int(data['1'][index][6:8]) != int(data['1'][index-1][6:8]):
                arrary1.append(round(float(data['2'][index]),3))

   
    for index in range(1,len(arrary1)):
        arrary1_freq2subfreq1.append(round(arrary1[index-1]-arrary1[index],3))
    #print(arrary1_freq2subfreq1)
    arrary2 = list(range(len(arrary1_freq2subfreq1)))
    
    plt.plot(arrary2,arrary1_freq2subfreq1,lw=2,label=filename,color = colors)    
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt.ylim(-1,1.0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(b=True, which='major', color='#666666', linestyle='-.')
    plt.title("frequency slope",fontsize=20)
    plt.show()
    
    
    
def freq_deviation_form20second(filename,colors):
    arrary1 = []
    arrary1_freq2subfreq1 = []
    temp_max = 0
    data = pd.read_table('tcxo_temp/TCXO_START_UP_FREQ/'+filename,sep=' ',names=['0','1','2'])
    #print(data)
    #print(data['1'][0][6]+data['1'][0][7])
    for index,value in enumerate(data['2']):
        if index < 15:
            if float(value)>temp_max:
                temp_max = round(value,3)
        if index == 15:
            arrary1.append(temp_max)
        if index > 15:
            if int(data['1'][index][6:8]) != int(data['1'][index-1][6:8]):
                arrary1.append(round(float(data['2'][index]),3))
                
    for index in range(21,len(arrary1)):
        arrary1_freq2subfreq1.append(round(arrary1[20]-arrary1[index],3))
    #print(arrary1_freq2subfreq1)           
    #print(arrary1)
    arrary2 = list(range(len(arrary1_freq2subfreq1)))
    
    plt.plot(arrary2,arrary1_freq2subfreq1,lw=2,label=filename,color = colors)    
    plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.)
    plt.ylim(-2,2.0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(b=True, which='major', color='#666666', linestyle='-.')
    plt.title("frequency slope",fontsize=20)
    plt.show()
    
    
    

    
    