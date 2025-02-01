import pandas as pd
import ast


point_dict = {}

df = pd.read_csv('points.csv')
for i,r in df.iterrows():
    l = ast.literal_eval(r['Points'])
    if not l: continue
    point_dict[r['Video Name']] = l
    

    
