import cv2
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def change_cv2_draw(image,strs,local,sizes=40,colour=(0,0,255)):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc',sizes, encoding="utf-8")
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image

apartment = cv2.imread('../project pics/testroom.jpg', 1)
img = change_cv2_draw(apartment,'中国',(100,100))
cv2.imshow('image', img)  # 展示图片
cv2.waitKey(0)  # 等待按键按下img = cv2.imread('../project pics/testroom.jpg', 1)
cv2.destroyAllWindows()  # 清除所有窗口