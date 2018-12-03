import os
import random

neg = os.listdir('neg')
pos = os.listdir('pos')


sent = []
labs = []

for i in neg:
 with open('neg/'+i,'r') as f:
  lines = f.readlines()
  for j in lines:
   if len(j.split(' '))> -1:
    sent.append(j)
    labs.append('Negative')


for i in pos:
 with open('pos/'+i,'r') as f:
  lines = f.readlines()
  for j in lines:
   if len(j.split(' '))> -1:
    sent.append(j)
    labs.append('Positive')


with open('rev','w') as f:
 for i in sent:
  f.write(i)

with open('lab','w') as f:
 for i in labs:
  f.write(i+'\n')


