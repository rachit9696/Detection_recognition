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
import os, sys

path = "set path for image extracted"
dirs = os.listdir( path )
#Resizing the image according to the width and height provided in the json file
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
        imResize = im.resize((395,147), Image.ANTIALIAS)
        imResize.save(f + '.jpeg', 'JPEG')
        resize()
