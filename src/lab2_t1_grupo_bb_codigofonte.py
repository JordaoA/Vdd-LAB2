# -*- coding: utf-8 -*-
"""LAB2-T1_Grupo_BB-CodigoFonte

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1220umDcI8PMm95z38tlIn1Ef-Nh4VvdJ
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

plane_data = pd.read_csv('/content/drive/MyDrive/vdd/lab2/data/airplane_crashes_dataset_since_1908 - airplane_crashes_dataset_since_1908.csv')
plane_data.head(10)

plane_data.replace('?', np.nan)

def format_time(val):
  neo_val = ''
  for c in val:
    if c.isdigit():
      neo_val = neo_val + c
  

  val_format = int(neo_val) if val != '' else None
  
  if val_format >= 600 and val_format <= 1759:
    return 'dia'
  else: return 'noite'

def format_date(val):
  date_format = val.split(', ')[1]
  return date_format[:3] + '0'

used_data = plane_data[['date', 'time']]
used_data.replace('?', np.nan,inplace = True)
used_data.dropna(inplace = True)
used_data.head()

used_data['dn'] = used_data['time'].apply(format_time)
used_data['decada'] = used_data['date'].apply(format_date)

used_data.head()

dia = used_data[used_data['dn']=='dia']
noite = used_data[used_data['dn']=='noite']

dia.head()

noite.head()

dia_list = list(dia.groupby('decada').count()['dn'])
noite_list =  [0] + list(noite.groupby('decada').count()['dn'])

data = [dia_list,
noite_list]



X = np.arange(len(dia_list))
fig = plt.figure(figsize=(16,12))
ax = fig.add_axes([0,0,1,1])


ax.bar(X + 0.00, data[0], color = 'skyblue', width = 0.25, label = 'dia')
ax.bar(X + 0.25, data[1], color = 'mediumpurple', width = 0.25, label = 'noite')
decadas = list(used_data['decada'].unique())
print(decadas)
plt.legend()

plt.xticks([i  for i in range(len(decadas))], decadas)

plt.ylabel("Quantidade de acidentes", fontdict={"fontsize": "16", "fontweight" : "6"})
plt.xlabel("Décadas", fontdict={"fontsize": "16", "fontweight" : "6"})
plt.title("A falta de luz natural é fator determinante para um maior número de acidentes aéreos?", fontdict={"fontsize": "20", "fontweight" : "6"})
plt.grid(axis='y', linewidth=0.3)