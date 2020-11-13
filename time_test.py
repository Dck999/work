import pandas as pd
import numpy as np
from datetime import datetime

current_datetime = "2020-10-29 11:59:40.672610"
time = datetime.strptime("2020-10-29 11:59:40","%Y-%m-%d %H:%M:%S")
print(current_datetime)
print(type(current_datetime))
print(time)
print(type(time))
#print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
