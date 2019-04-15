#coding: utf-8
import build_library
import feature
import remove_walls as RW
import extract_candidates as EC
import match
import cv2
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def change_cv2_draw(image,strs,local,sizes=15,colour=(255,0,0)):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc',sizes, encoding="utf-8")
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
    return image


if __name__=='__main__':
    # address = input('input your floor plan\'address:')
    # address = '../project pics/testroom.jpg'
    # apartment = cv2.imread(address,1)
    apartment = cv2.imread('../project pics/testroom.jpg', 1)
    deletwalls = RW.removewalls(apartment)
    candidates,coornidates = EC.extract(apartment,deletwalls)
    Furnitures = build_library.FURNITURES
    print('Class or Kind?input one of them:')
    # k = input()
    k = 'Class'
    if k =='Class':
        print('input class name:one of bed,desk,fridge,sofa,chair,table,sink,washer,bathtub,shower,sprinkler,gas_cooker,TV_stand,washbasin,wardrobe,squatting_pan,stool')
        # for line in sys.stdin:
        #     if line == 'end':
        #         print('finished')
        #         break
        line = 'sink'
        found = 0
        for f in Furnitures.dict_class[line]:
            obj = f.img
            for i in range(len(candidates)):
                if match.match(candidates[i], obj):
                    x, y, w, h = coornidates[i]
                    cv2.rectangle(apartment, (x - 2, y - 2), (x + w + 2, y + h + 2), (0, 0, 255), 2)
                    # cv2.putText(apartment,line,(x-2,y-7),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                    ##cv2 cannot output Chinese
                    apartment = change_cv2_draw(apartment, line, (x, y - 25))
                    found += 1
                    print(f.name)
                    # print("found:", found)
                    # cv2.imshow('image', apartment)  # 展示图片
                    # cv2.waitKey(0)  # 等待按键按下img = cv2.imread('../project pics/testroom.jpg', 1)
                    # cv2.destroyAllWindows()  # 清除所有窗口

        print("found:", found)
        cv2.imshow('image', apartment)  # 展示图片
        cv2.waitKey(0)  # 等待按键按下img = cv2.imread('../project pics/testroom.jpg', 1)
        cv2.destroyAllWindows()  # 清除所有窗口

    if k == 'Kind':
        print('input class name:')
        # for line in sys.stdin:
        #     if line == 'end':
        #         print('finished')
        #         break
        #     else:
        # line = input()
        line = '03-圆餐桌'
        obj = Furnitures.dict_kind[line].img
        found = 0
        for i in range(len(candidates)):
            if match.match(candidates[i],obj):
                x,y,w,h = coornidates[i]
                cv2.rectangle(apartment, (x - 2, y - 2), (x + w + 2, y + h + 2), (0, 0, 255),2)
                #cv2.putText(apartment,line,(x-2,y-7),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                ##cv2 cannot output Chinese
                apartment = change_cv2_draw(apartment,line,(x,y-25))
                found+=1
                # print(i,'th in',len(candidates))
        print("found:",found)
        cv2.imshow('image', apartment)  # 展示图片
        cv2.waitKey(0)  # 等待按键按下img = cv2.imread('../project pics/testroom.jpg', 1)
        cv2.destroyAllWindows()  # 清除所有窗口
                #print('input new class name or end')



    else:
        print('input error')
