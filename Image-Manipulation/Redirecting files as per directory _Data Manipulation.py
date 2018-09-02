import numpy as np
import math
import pandas as pd
import csv
import os , glob, shutil 
from os.path import join
from tqdm import tqdm

#Read csv
location ="C:/Users/Sravani/Desktop/IWR_DATA_arrange/Diseases file.csv"
df = pd.read_csv(location,header=None, dtype='str')

records=len(df.index)

with open(location, mode='r',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    
#print(mydict)




def test():

	#image_path = "C:/Users/Sravani/Desktop/IWR_DATA_arrange/images_002/"
	#img_files = os.listdir("C:/Users/Sravani/Desktop/IWR_DATA_arrange/images_001/")
	image_path = "E:/softies/Deep Learning Project IWR/NIHCC Dataset TB/images-processed/image1/"
	img_files = os.listdir("E:/softies/Deep Learning Project IWR/NIHCC Dataset TB/images-processed/image1")
	for img in mydict.keys():
		if img in img_files:
			dest_dir = "E:/softies/Deep Learning Project IWR/Diseases_split/"+str(mydict.get(img))
			if not os.path.exists(dest_dir):
				os.mkdir(dest_dir)
			shutil.copy(image_path+img,dest_dir)


test()
print("done...with 1!")
#segregate()




