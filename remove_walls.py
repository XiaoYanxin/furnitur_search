from skimage import measure,morphology
import numpy as np
import cv2
from matplotlib import pyplot as plt

def removewalls(apartment):
    # img = cv2.imread('../project pics/testroom.jpg',0)
    img = apartment
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,data = cv2.threshold(img,240,255,cv2.THRESH_BINARY_INV)
    data = morphology.thin(data).astype(np.uint8)
    ret1,data = cv2.threshold(data,0,255,cv2.THRESH_BINARY_INV)
    # cv2.imshow('pic2', data)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ##打断墙的连通性
    row,column = data.shape
    i1,j1 = 0,0
    while data[i1,j1]==255:
        i1+=1
        j1+=1
    i2 = row-1
    j2 = column-1
    while data[i2,j2]==255:
        i2-=1
        j2-=1
    i3 = row-1
    j3 = 0
    while data[i3,j3]==255:
        i3-=1
        j3+=1
    i4 = 0
    j4 = column-1
    while data[i4,j4]==255:
        i4+=1
        j4-=1
    labels=measure.label(data,connectivity=1,background=-1)#针对线条连通域需设background
    w_label1 = labels[i1,j2]
    w_label2 = labels[i2,j2]
    w_label3 = labels[i3,j3]
    w_label4 = labels[i4,j4]
    wall_ps = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            if labels[x,y]==w_label1 or labels[x,y]==w_label2 or labels[x,y]==w_label3 or labels[x,y]==w_label4:
                wall_ps.append((x,y))
    for wp in wall_ps:
        data[wp]=255
    ##对背景所在连通域进行填黑色
    labels=measure.label(data,connectivity=1,background = -1)
    background_label = labels[0,0]
    for i in range(row):
        for j in range(column):
            if labels[i,j]==background_label:
                data[i,j]=0
    # labels = measure.label(data, connectivity=1, background=-1)
    # background_label = labels[0, 0]
    # bgps = []
    # for i in range(row):
    #     for j in range(column):
    #         if labels[i, j] == background_label:
    #             bgps.append((i,j))
    # new_img = np.zeros(data.shape)
    # for p in bgps:
    #     x,y = p
    #     new_img[x,y]=255
    return data
# cv2.imshow('pic', data)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # plt.imshow(dst)
# # plt.show()
if __name__=="__main__":
    img = cv2.imread('../project pics/testroom.jpg', 1)
    data = removewalls(img)
    cv2.imshow('pic', data)
    print(data.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

