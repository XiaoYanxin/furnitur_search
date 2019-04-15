import cv2
import numpy as np
import  remove_walls

def extract(apartment,deletewalls):#return candidate and its bounding box's coornidates (x,y,w,h)
  # img = cv2.imread('../project pics/testroom.jpg',1)
  # gray = cv2.imread('../project pics/deletewalls.jpg',0)
  # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  img = apartment
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  im_th = deletewalls
  # re,im_th = cv2.threshold(gray, 147, 255, cv2.THRESH_BINARY)
  res = []
  bounding_box=[]
  im_floodfill = im_th.copy()

  # Mask used to flood filling.
  # Notice the size needs to be 2 pixels than the image.
  h, w = im_th.shape[:2]
  mask = np.zeros((h + 2, w + 2), np.uint8)

  # Floodfill from point (0, 0)
  cv2.floodFill(im_floodfill, mask, (0, 0), 255)

  # Invert floodfilled image一种去除图像中不闭合曲线段的方法与流程
  im_floodfill_inv = cv2.bitwise_not(im_floodfill)

  # Combine the two images to get the foreground.
  im_out = im_th | im_floodfill_inv

  ##filtering to smooth edges
  im_out=cv2.GaussianBlur(im_out,(13,13),1.8)
  re1,im_out = cv2.threshold(im_out, 50, 255, cv2.THRESH_BINARY)
  ##the filter controls the precision of segmentation!

  im, cts, hi = cv2.findContours(im_out,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
  # cv2.drawContours(img,cts,-1,(0,0,255),3)
  for i in range(0,len(cts)):
    x, y, w, h = cv2.boundingRect(cts[i])
    cv2.rectangle(img, (x-2,y-2), (x+w+2,y+h+2), (0,255,0), 1)
    cropped = img_gray[y:y+h,x:x+w]
    res.append(cropped)
    bounding_box.append((x,y,w,h))
  cv2.namedWindow('image')
  cv2.imshow("Foreground", im_out)
  cv2.imshow('image', img)
  # cv2.imshow('image1', res[1])
  # cv2.imshow('image2', res[0])
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return res,bounding_box

if __name__=="__main__":
  img = cv2.imread('../project pics/testroom.jpg', 1)
  gray = cv2.imread('../project pics/deletewalls.jpg', 0)
  gray1 = remove_walls.removewalls(img)
  res,cor = extract(img,gray1)
  print(cor)
  print(len(res))
  cv2.namedWindow('image')
  # cv2.imshow("Foreground", im_out)
  cv2.imshow('image', img)
  # cv2.imshow('image1', res[1])
  # cv2.imshow('image2', res[0])
  cv2.waitKey(0)
  cv2.destroyAllWindows()