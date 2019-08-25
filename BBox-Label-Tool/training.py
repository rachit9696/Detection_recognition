import glob, os
# directory obj is in data folder of darknet which contains both images and labels
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Directory where the data will reside, relative to 'darknet.exe'
current_data = '/home/rachit/BBox-Label-Tool/Multi-train/'
# Percentage of images to be used for the test set
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.JPEG")):
    title,ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(current_data + title + '.JPEG' + "\n")
    else:
        file_train.write(current_data + title + '.JPEG' + "\n")
        counter = counter + 1
