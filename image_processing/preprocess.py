import requests
import random
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
import urllib
import cv2
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

x=[]
z=[]
#set the path for the file
file = 'path to json file'
a=[]
w=[]
width=[]
height=[]
#creating the list for the specific contents present in the file
with open(file) as f:
    for line in f:
        y=(json.loads(line))
        x.append(y['content'])
        z.append(y['annotation'])
        a.append(y['extras'])
        

        
print(x)
print(z)
print(a)
l=len(z)
c=y['annotation']
p=[]
o=[]
for i in range(l):
    for j in c:
        p.append(j['label'])
        o.append(j['points'])
        width.append(j['imageWidth'])
        height.append(j['imageHeight'])
#printing the attributes of the json file
print(p)
print(o)
print(width)
print(height)

#Creating a file for the coordinates providedin json file
with open('point.txt', 'w') as f:
    for item in o:
        f.write("%s\n" % item)

       
