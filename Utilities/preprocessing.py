import numpy as np
import cv2
import json
import os
import time
import gzip



if __name__ == "__main__":

    folderpath = 'images/'
    # images = load_images(folderpath)
    for filename in os.listdir(folderpath):
        filepath = folderpath+filename
        label_file_dir = 'labels/'+filename.split('.')[0]+ '.npy.gz'
        
        
        try:
            with open('labels/centers.json','r') as file:
                data = json.load(file)
            
            f=gzip.open(label_file_dir, mode='rb')
            data1 = np.load(file=f)
            f.close()

            print(data[filename])
            print(data1.shape())
        
        
        except:
            img = cv2.imread(filepath)
            with open('cfg/config.txt','r') as file:
                data = json.load(file)
                no_of_colors = data[filename]
            
            # reshape and convert to np.float32
            Z = img.reshape((-1,3))
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            # 10 - no of iterations, 1.0 - required accuracy
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            _,label,center = cv2.kmeans(Z, no_of_colors, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
            label = label.reshape((img.shape[:-1]))
            label = label.astype(np.uint8)
            center = center.astype(np.uint8)
            with open('labels/centers.json', 'r') as file:
                data = json.load(file)

            data[filename] = center.tolist()

            with open('labels/centers.json', 'w+') as file:
                json.dump(data,file)

            
            f = gzip.GzipFile(label_file_dir, "w")
            np.save(file=f, arr=label)
            f.close()
        else:
            print("{} is recorded in the database".format(filename))