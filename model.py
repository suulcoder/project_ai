#import libraries
import csv
import PIL.Image
import matplotlib.pyplot as plt
import os.path
import numpy as np
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from sklearn import neighbors, datasets
from sklearn.manifold import TSNE
from matplotlib.colors import ListedColormap
from PIL import Image

data = []
samples = []
size = 100

def img_into_matrix(img, hasPath=True):
    filename = img
    if(hasPath):
        filepath = os.path.join(
            os.getcwd(), 'Data/train'
        )
        filename = os.path.join(
            filepath, img
        )
    print(filename)
    image = Image.open(filename)
    matrix = np.asarray(image.resize((size,size)), dtype=np.float32)
    new_matrix = []

    for i in matrix:
        value = 0
        total = 0
        for j in i:
            for k in j:
                value += k
                total += 1
        new_matrix.append(value/total)
    return(new_matrix)

#LoadData
with open('./Data/train.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        if(i!=0):
            data.append(img_into_matrix(row[0]))
            samples.append(row[0])
        i+=1

#get 10 related neighbors
def get_related(img,number=10):
    matrix = img_into_matrix(img,False)
    model = NearestNeighbors(n_neighbors=number)
    model.fit(data)
    result = model.kneighbors([matrix])
    my_result = []
    for i in result[1][0]:
        my_result.append(samples[i])
    return(my_result,result[0][0])


