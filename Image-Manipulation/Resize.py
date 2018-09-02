from glob import glob
from threading import Thread
import cv2
import numpy as np
import threading
import _thread

def transform(ext,img_paths):
	for i in range(0,len(img_paths)):
		img= cv2.imread(img_paths[i])
#		print(img.shape)
		height, width,channel = img.shape
		res= cv2.resize(img, (512,512))
		name = img_paths[i].split('/')[-1];
		print(name);
		cv2.imwrite('images-processed/'+ext+'/'+name,res)
		i=i+1


def run(self):
      print ("Starting run")


imgloc1 = "E:/softies/Deep Learning Project IWR/NIHCC Dataset TB/images_001/"
img_paths1 = glob(imgloc1+'*.png')
print("starting 1")

imgloc2 = "E:/softies/Deep Learning Project IWR/NIHCC Dataset TB/images_002/"
img_paths2 = glob(imgloc2+'*.png')
print("starting 2")


try:
   _thread.start_new_thread( transform, ("image1",img_paths1))
   #_thread.start_new_thread( transform, ("image2",img_paths2))
   #thread.start_new_thread( transform,  ("image9",img_paths9))
   #thread.start_new_thread( transform, ("image10",img_paths10))
except ValueError:
   print ("Error: unable to start thread"+ ValueError)

while 1:
   pass

print("end")