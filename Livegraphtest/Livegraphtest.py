import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import datetime
import time
import pandas as pd



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate():
    arrary_I2=[]
    arrary_I2_time=[]
    arrary_V0=[]
    arrary_V0_time=[]
    
    
    data = pd.read_table('teraterm.log',sep=' ',names=['0','1','2'])
    
    print(data)
    """
    for value in data['2']:
        if (value[4]+value[5]) == 'I2':
            I2 = ""
            I2_time = ""
            for index in range(7,len(value)):
                I2 = I2+value[index]
                I2_time = I2_time
            arrary_I2.append(round(float(I2),3))
        if (value[4]+value[5]) == 'V0':
            V0 = ""
            for index in range(7,len(value)):
                V0 = V0+value[index]
            arrary_V0.append(round(float(V0),3))
    """
    for index in range(len(data['2'])):
        
        if (data['2'][index][4]+data['2'][index][5]) == 'I2':
            arrary_times = []
            arrary_num_times = []
            I2 = ""
            I2_time = ""
            I2_time = I2_time +data['0'][index]+" "+data['1'][index]
            I2_time = I2_time.replace("-"," ")
            I2_time = I2_time.replace(":"," ")
            I2_time = I2_time.replace("[","")
            I2_time = I2_time.replace("]","")
            I2_time = I2_time.replace("."," ")
            arrary_times = I2_time.split(" ")
            dt=datetime.datetime(int(arrary_times[0]),int(arrary_times[1]),int(arrary_times[2]),int(arrary_times[3]),int(arrary_times[4]),int(arrary_times[5]),int(arrary_times[6]))
            
            for index2 in range(7,len(data['2'][index])):
                I2 = I2+data['2'][index][index2]
                
            arrary_I2.append(round(float(I2),3))
            arrary_I2_time.append(md.date2num(dt))
        if (data['2'][index][4]+data['2'][index][5]) == 'V0':
            arrary_times = []
            arrary_num_times = []
            V0 = ""
            V0_time = ""
            V0_time = V0_time + data['0'][index]+" "+data['1'][index]
            V0_time = V0_time.replace("-"," ")
            V0_time = V0_time.replace(":"," ")
            V0_time = V0_time.replace("[","")
            V0_time = V0_time.replace("]","")
            V0_time = V0_time.replace("."," ")
            arrary_times = V0_time.split(" ")
            dt=datetime.datetime(int(arrary_times[0]),int(arrary_times[1]),int(arrary_times[2]),int(arrary_times[3]),int(arrary_times[4]),int(arrary_times[5]),int(arrary_times[6]))
            
            
            for index2 in range(7,len(data['2'][index])):
                V0 = V0+data['2'][index][index2]
                
            arrary_V0.append(round(float(V0),3))
            arrary_V0_time.append(md.date2num(dt))
    
    print(f"arrary_I2 = {arrary_I2}")
    print("========================================")
    print(f"arrary_I2_time = {arrary_I2_time}")
    print("========================================")
    print(f"arrary_V0 = {arrary_V0}")
    print("========================================")
    print(f"arrary_V0_time = {arrary_V0_time}")
    print("========================================")
    plt.plot(arrary_I2_time,arrary_I2)
    plt.plot(arrary_V0_time,arrary_V0)
    plt.show()
    
    for index_time in range(len(data['1'])):
        time_temp = (data['0'][index_time]+" "+data['1'][index_time])
        time_temp = time_temp.replace("-"," ")
        time_temp = time_temp.replace(":"," ")
        time_temp = time_temp.replace("[","")
        time_temp = time_temp.replace("]","")
        time_temp = time_temp.replace("."," ")
        arrary_times = time_temp.split(" ")
        dt=datetime.datetime(int(arrary_times[0]),int(arrary_times[1]),int(arrary_times[2]),int(arrary_times[3]),int(arrary_times[4]),int(arrary_times[5]),int(arrary_times[6]))
        arrary_num_times.append(md.date2num(dt))
        
    print(arrary_num_times)
        
        
def test():
    i=2010;j=8;k=6
    d2=datetime.datetime(i,j,k,10,53,54)
    n1 = md.date2num(d2)
    print(type(d2))
    print(n1)

def test2():
    datetime_dt = datetime.datetime.today()
    print(type(datetime_dt))






animate()



