import cv2
import extract_candidates
import feature as ft
from matplotlib import pyplot as plt

def match(candidate,obj):#input gray or binary pic
    # apartment = extract_candidates.res
    # rectable2 = apartment[1]
    # rectable2 = cv2.cvtColor(rectable2,cv2.COLOR_BGR2GRAY)
    # obj = cv2.imread('..//project pics/平面图块/02-茶几.jpg',0)
    re,candidate = cv2.threshold(candidate, 147, 255, cv2.THRESH_BINARY)
    re1,obj = cv2.threshold(obj, 147, 255, cv2.THRESH_BINARY)
    h1 = ft.EDH(candidate)
    h2 = ft.EDH(obj)
    t = cv2.compareHist(h1,h2,method = cv2.HISTCMP_CHISQR)#0.04 or cv2.HISTCMP_BHATTACHARYYA 0.075
    if t<0.03:
        return True
    else:
        return False