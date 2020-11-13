import os


dirPath = os.getcwd()
target_path = os.path.join(dirPath,"tcxo_temp\TCXO_TEMP_FREQ")
TCXO_PHASE_NOISE_path = os.path.join(dirPath,"tcxo_temp\TCXO_PHASE_NOISE")
start_up_freq_path = os.path.join(dirPath,"tcxo_temp\TCXO_START_UP_FREQ")

""" these function can be combined to one function """
def show_csv_file_nam(target_path):
    csv_list = []
    for file in os.listdir(target_path):
        if file[-3:] == "csv":
            csv_list.append(file)
    
    return csv_list


def show_log_file_nam(target_path):
    log_list = []
    for file in os.listdir(target_path):
        if file[-3:] == "log":
            log_list.append(file)
    return log_list

#add path like this: os.path.join(dirPath,"baro_function\\rawdata")

def showfile(dirPath):
    csv_file = []
    for file in os.listdir(dirPath):
        if file[-3:] == "csv":
            csv_file.append(file)
    return  csv_file      
    


