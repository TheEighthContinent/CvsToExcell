import pandas as pd
import os
from tkinter.filedialog import askdirectory

path = askdirectory(title='Select Folder')
os.chdir(path)

data = []
header = []
for unnecessary, unneeded, filenames in os.walk(path):
    for i in filenames:
        name = os.path.splitext(i)
        ## stops errors
        if name[1] != ".csv":
            pass
        else:
            col_names = ["sct_col", name[0], ]
            df = pd.read_csv(i, names=col_names)
            header.append([x for x in df["sct_col"]])
            data_sub = [x for x in df[name[0]]]
            data_sub.insert(0, name[0])
            data.append(data_sub)
header[0].insert(0, "0,0")
data.insert(0, header[0])
pd \
    .DataFrame(data) \
    .T \
    .to_excel("Result.xlsx", index=False, header=False)
