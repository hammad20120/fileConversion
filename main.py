import pandas as pd;
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(file)

catlist = ['grading', 'knowledge', 'presentation', 'counselling', 'punctuality', 'favoritism']
##file = r'5-22-42-29.csv'

with open(file, 'r', encoding="utf8") as f:
    lines = f.readlines()

index = []

for l in lines[1:]:
    l = l.strip()
    txt = l.split('\t')
    category = txt[0]
    polarity = txt[1]
    reviewID = txt[2]
    text = txt[3]
    if not any(text in s for s in index):
        index.append(text)

attrib = [[] for i in range(len(index))]
for i in range(len(attrib)):
    for j in range(len(catlist)):
        attrib[i].append('')

ind = 0
for l in lines[1:]:
    l = l.strip()
    txt = l.split('\t')
    category = txt[0]
    catIndex = catlist.index(category)
    polarity = txt[1]
    text = txt[3]
    if text != index[ind]:
        ind = ind + 1
    if polarity == 'positive':
        attrib[ind][catIndex] = 'positive'
    else:
        attrib[ind][catIndex] = 'negative'


df = pd.DataFrame(attrib, columns=catlist, index=index)
file = file[:len(file)-4]
file = file + '-formatted.csv'
export_csv = df.to_csv(file)
print(df)
