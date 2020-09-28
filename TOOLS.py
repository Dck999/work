import tkinter as tk
from tkinter.ttk import *
#from tkinter import ttk
from TCXO import temp_ppm_single, temp_ppm_All, temp_slope_single, temp_slope_all, temp_slope_single_each_temp_record, temp_slope_All_each_temp_record, phase_noise_single_plot, phase_noise_all_plot, start_up_frequency,freq_deviation_form20second
from Livegraphtest import *
from test_find_path import *


LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='news')
        


        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(quickPrint):
    print(quickPrint)
       
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.test = 0
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Wellcome to AE tools", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button = tk.Button(self, text="TCXO TEST PLAN", command=lambda: controller.show_frame(PageOne))
        button.pack()
        
        button2 = tk.Button(self, text="CC/CV Log", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        self.test = 1
        tk.Frame.__init__(self,parent)
        
        def clicked_plot_single_file():
            temp_ppm_single(combo.get(),combo2.get())

        def clicked_plot_all_file():
            temp_ppm_All(color_arrary)
            
        def clicked_plot_single_file_ppm_slope():
            temp_slope_single(combo.get(),combo2.get())

        def clicked_plot_all_file_ppm_slope():
            temp_slope_all(color_arrary)

        def click_plot_single_file_each_temp_ppm():
            temp_slope_single_each_temp_record(combo.get(),combo2.get())

        def click_plot_all_file_each_temp_ppm():
            temp_slope_All_each_temp_record(color_arrary)

        def click_plot_single_phase_noise():
            phase_noise_single_plot(combo.get(),combo2.get())
        
        def click_plot_all_phase_noise():
            phase_noise_all_plot(color_arrary)
            
        def click_plot_single_start_up_frequency():
            start_up_frequency(combo.get(),combo2.get())
            
        def click_plot_single_freq_drift(): #還沒有 建立相關按鈕
            freq_deviation_form20second(combo.get(),combo2.get())

        def clicked_show_file():
            combo['values']= show_csv_file_nam(target_path)
        
        def clicked_show_file2():
            combo['values']= show_csv_file_nam(TCXO_PHASE_NOISE_path)
        
        def clicked_show_file3():
            combo['value'] = show_log_file_nam(start_up_freq_path)
        
        
        label = tk.Label(self,text="TCXO test plan", font = LARGE_FONT)
        label.pack()
        
        
        combo = Combobox(self)
        combo.pack()
        
        combo2 = Combobox(self)
        combo2.pack()
        combo2['values'] = ['black','red','darkorange','gold','forestgreen','teal','blue','magenta']
        color_arrary=['black','red','darkorange','gold','forestgreen','teal','blue','magenta']
        
        btn_show_file1 = Button(self,text="Scan(Temp&Freq)", command=clicked_show_file )
        btn_show_file1.pack()
        
        btn_show_file2 = Button(self,text="Scan(phase noise)", command=clicked_show_file2 )
        btn_show_file2.pack()

        btn_show_file3 = Button(self,text="Scan(start up freq)", command=clicked_show_file3 )
        btn_show_file3.pack()
            
        btn_plot_single = Button(self,text="clicked plot single temp_ppm",command = clicked_plot_single_file)
        btn_plot_single.pack()

        btn_plot_single_ppm_slope = Button(self,text="clicked plot single ppm slope file",command = clicked_plot_single_file_ppm_slope)
        btn_plot_single_ppm_slope.pack()


        btn_plot_single_ppm_slope = Button(self,text="clicked plot single each temp_ppm_slope file",command = click_plot_single_file_each_temp_ppm)
        btn_plot_single_ppm_slope.pack()

        btn_plot_single_phase_noise = Button(self,text="clicked plot single phase noise file",command = click_plot_single_phase_noise)
        btn_plot_single_phase_noise.pack()
        
        btn_plot_start_up_freq = Button(self,text="clicked plot start up freq",command = click_plot_single_start_up_frequency)
        btn_plot_start_up_freq.pack()
        
        btn_plot_freq_drift_after_20sec = Button(self,text="clicked plot freq drift after 20sec",command = click_plot_single_freq_drift)
        btn_plot_freq_drift_after_20sec.pack()
        
        lb_line1 = Label(self, text="=================================")
        lb_line1.pack()

        btn_plot_all_file = Button(self,text="clicked plot all temp_ppm file",command = clicked_plot_all_file)
        btn_plot_all_file.pack()

        btn_plot_all_ppm_slope = Button(self,text="clicked plot all ppm_slope",command = clicked_plot_all_file_ppm_slope)
        btn_plot_all_ppm_slope.pack()

        btn_plot_all_each_temp_ppm_slope = Button(self,text="clicked plot all each_temp_ppm_slope",command = click_plot_all_file_each_temp_ppm)
        btn_plot_all_each_temp_ppm_slope.pack()
        
        btn_plot_all_phase_noise = Button(self,text="clicked plot all phase noise",command = click_plot_all_phase_noise)
        btn_plot_all_phase_noise.pack()
        
        
        
        button = tk.Button(self, text="Back to Home",command = lambda:controller.show_frame(StartPage))
        button.pack()
        
        
        
    
        
        
        
        

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        self.test = 2
        tk.Frame.__init__(self,parent)
        
        def click_start_cc_cv_app():
            start_cc_cv_app()
        
        
        
        label_1 = tk.Label(self,text="CC/CV App with IATE AND Tera term.", font = LARGE_FONT)
        label_1.pack()
        
        btn_start_app = Button(self,text="Start App",command=click_start_cc_cv_app)
        btn_start_app.pack()
        
        button = tk.Button(self, text="Back to Home",command = lambda:controller.show_frame(StartPage))
        button.pack()
        
        
        
        

app = SeaofBTCapp()
app.title("AE Tools")
app.geometry('350x500')

app.mainloop()

