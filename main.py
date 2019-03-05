import pandas as pd;
from pandas import DataFrame, read_csv;

catlist = ['grading', 'knowledge', 'presentation', 'counselling', 'punctuality', 'favoritism']
file = r'5-22-42-29.csv'

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

for i in attrib:
    print(i)

print(index)

df = pd.DataFrame(attrib, columns=catlist, index=index)
export_csv = df.to_csv(r'formatted.csv')
print(df)
