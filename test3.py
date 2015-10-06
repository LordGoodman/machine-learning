import pandas as pd
years = range(1880,2011)

pieces = []
colums = ['name','sex','births']

for year in years:
    path = 'H:\ingridient/pydata-book-master/ch02/names/yob%d.txt' %year
    frame = pd.read_csv(path,names=colums)
    
    frame ['year'] = year
    pieces.append(frame)
    
names = pd.concat(pieces,ignore_index=True)

def add_prop(group):
    births = group.births
    group['prop'] = births/births.sum()
    return group
    
namess = names.groupby(['year','sex']).apply(add_prop)    