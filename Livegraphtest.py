import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as md
import datetime
import pandas as pd

def start_cc_cv_app():

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax2 = ax1.twinx()



    def animate(i):
        arrary_I2=[]
        arrary_I2_time=[]
        arrary_V0=[]
        arrary_V0_time=[]
        data = pd.read_table('teraterm.log',sep=' ',names=['0','1','2'])
        for index in range(len(data['2'])):
            if (data['2'][index][4]+data['2'][index][5]) == 'I0':
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
        """
        print(f"arrary_I2 = {arrary_I2}")
        print("========================================")
        print(f"arrary_I2_time = {arrary_I2_time}")
        print("========================================")
        print(f"arrary_V0 = {arrary_V0}")
        print("========================================")
        print(f"arrary_V0_time = {arrary_V0_time}")
        print("========================================")
        """
        ax1.clear()
        ax2.clear()
        ax1.plot(arrary_I2_time,arrary_I2,'g-')
        ax2.plot(arrary_V0_time,arrary_V0,'b-')

    ani = animation.FuncAnimation(fig, animate, interval=500)
    plt.show()



