import pandas as pd
from test_find_path import *
import matplotlib.pyplot as plt
import numpy as np

def cn_log_getsetting():
    showfile((os.path.join(dirPath,"cn_log\\csv_file_getsetting")))
    df = pd.read_csv('cn_log/csv_file_getsetting/3970081200_golden.csv')
    print(df)
    
#cn_log_getsetting()
print(cn_log_getsetting())