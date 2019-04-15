import numpy as np
from skimage import exposure

def distance(point1,point2):
    return  ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

def EDH(img):# edge distance descriptor, point = rag._node[i]['centroid']

    row,column = img.shape
    center = (row//2,column//2)
    points = []
    dis = []
    des = [0 for _ in range(9)]#9 bins
    for i in range(row):
        for j in range(column):
            if img[i,j]!=255:
                points.append((i,j))
    while points:
        dis.append(distance(points.pop(),center))
    MAX = max(dis)
    MIN = min(dis)
    interval = (MAX-MIN)/9
    #print(MIN, MAX,interval)
    for d in dis:
        if MIN<=d<MIN+interval:
            des[0]+=1
        if MIN+interval<=d<MIN+2*interval:
            des[1]+=1
        if MIN+2*interval<=d<MIN+3*interval:
            des[2]+=1
        if MIN+3*interval<=d<MIN+4*interval:
            des[3]+=1
        if MIN+4*interval<=d<MIN+5*interval:
            des[4]+=1
        if MIN+5*interval<=d<MIN+6*interval:
            des[5]+=1
        if MIN+6*interval<=d<MIN+7*interval:
            des[6]+=1
        if MIN+7*interval<=d<MIN+8*interval:
            des[7]+=1
        else:
            des[8]+=1
    #print(des)
    des = np.array(des).reshape(9,1).astype(np.float32)
    des = des/sum(des)
    ##add two histogram values
    his,cp = exposure.histogram(img,nbins=2)
    h = np.array([his[0],his[-1]]).astype(np.float32)
    h = h/sum(h)
    des = np.append(des,h)
    return des