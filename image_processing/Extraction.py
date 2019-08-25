import matplotlib.pyplot as plt
import urllib
import cv2
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

file = 'path to json file'
#Extracting the images from the list appended from the json file
for index, url in enumerate(list_of_URL):
    link = urllib.request.urlopen(url)
    try:
        name = "%s.jpeg" % (index+1)
        with open(name, "wb") as output:
            output.write(link.read())
    except IOError:
        print ("Unable to create %s" % name)
