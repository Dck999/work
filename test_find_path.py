import os


dirPath = os.getcwd()
target_path = os.path.join(dirPath,"tcxo_temp\TCXO_TEMP_FREQ")
TCXO_PHASE_NOISE_path = os.path.join(dirPath,"tcxo_temp\TCXO_PHASE_NOISE")
start_up_freq_path = os.path.join(dirPath,"tcxo_temp\TCXO_START_UP_FREQ")

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
    
    
