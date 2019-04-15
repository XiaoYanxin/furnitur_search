import cv2
import os
import feature

class Furniture(object):
    def __init__(self,name,path):
        self.name = name
        self.gray = cv2.imread(path, 0)
        re, img = cv2.threshold(self.gray, 147, 255, cv2.THRESH_BINARY)
        self.img = img
        #self.feature = feature.EDH(self.img)
        #self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        #self.kp = get_kp(self.img)
        #self.des = getFeatures(self.img, self.kp)

class FSET(object):
    def __init__(self):
        self.classlist = ['bed', 'desk', 'fridge', 'sofa', 'chair', 'table', 'sink', 'washer', 'bathtub', 'shower',
                     'sprinkler','gas_cooker', 'TV_stand', 'washbasin', 'wardrobe', 'squatting_pan', 'stool']
        self.dict_class = {}
        self.dict_kind = {}
        for name in self.classlist:
            self.dict_class[name] = []
    def add(self,classname,furniture):
        self.dict_class[classname].append(furniture)
        self.dict_kind[furniture.name] = furniture

FURNITURES = FSET()
list_fur = os.listdir('../project pics/平面图块')
for furniture in list_fur:
    if '01-1200床' in furniture:
        bed011200 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed011200)
    elif '01-1500床' in furniture:
        bed011500 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed011500)
    elif '01-1800床' in furniture:
        bed011800 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed011800)
    elif '01-三人沙发' in furniture:
        mult_sofa01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',mult_sofa01)
    elif '01-书桌书椅' in furniture:
        desk01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('desk',desk01)
    elif '01-冰箱' in furniture:
        fridge01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('fridge',fridge01)
    elif '01-单人沙发' in furniture:
        single_sofa01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',single_sofa01)
    elif '01-单椅' in furniture:
        chair01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('chair',chair01)
    elif '01-双人沙发' in furniture:
        doub_sofa01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',doub_sofa01)
    elif '01-圆餐桌' in furniture:
        circle_table01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',circle_table01)
    elif '01-方餐桌' in furniture:
        rect_table01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',rect_table01)
    elif '01-水槽' in furniture:
        sink01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sink',sink01)
    elif '01-洗衣机' in furniture:
        washer01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washer',washer01)
    elif '01-浴缸' in furniture:
        bathtub01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bathtub',bathtub01)
    elif '01-淋浴房' in furniture:
        shower01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('shower',shower01)
    elif '01-淋浴花洒' in furniture:
        sprinkler01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sprinkler',sprinkler01)
    elif '01-燃气灶' in furniture:
        gas_cooker01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('gas_cooker',gas_cooker01)
    elif '01-电视柜' in furniture:
        TV_stand01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('TV_stand',TV_stand01)
    elif '01-盥洗台' in furniture:
        washbasin01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washbasin',washbasin01)
    elif '01-茶几' in furniture:
        teapoy01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',teapoy01)
    elif '01-衣柜' in furniture:
        wardrobe01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('wardrobe',wardrobe01)
    elif '01-蹲便器' in furniture:
        squatting_pan01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('squatting_pan',squatting_pan01)
    elif '01-边几' in furniture:
        side_table01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',side_table01)
    elif '01-马桶' in furniture:
        stool01= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('stool',stool01)
    elif '02-1200床' in furniture:
        bed021200 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed021200)
    elif '02-1500床' in furniture:
        bed021500 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed021500)
    elif '02-1800床' in furniture:
        bed021800 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed021800)
    elif '02-三人沙发' in furniture:
        mult_sofa02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',mult_sofa02)
    elif '02-书桌书椅' in furniture:
        desk02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('desk',desk02)
    elif '02-冰箱' in furniture:
        fridge02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('fridge',fridge02)
    elif '02-单人沙发' in furniture:
        single_sofa02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',single_sofa02)
    elif '02-单椅' in furniture:
        chair02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('chair',chair02)
    elif '02-双人沙发' in furniture:
        doub_sofa02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',doub_sofa02)
    elif '02-圆餐桌' in furniture:
        circle_table02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',circle_table02)
    elif '02-方餐桌' in furniture:
        rect_table02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',rect_table02)
    elif '02-水槽' in furniture:
        sink02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sink',sink02)
    elif '02-洗衣机' in furniture:
        washer02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washer',washer02)
    elif '02-浴缸' in furniture:
        bathtub02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bathtub',bathtub02)
    elif '02-淋浴房' in furniture:
        shower02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('shower',shower02)
    elif '02-淋浴花洒' in furniture:
        sprinkler02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sprinkler',sprinkler02)
    elif '02-燃气灶' in furniture:
        gas_cooker02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('gas_cooker',gas_cooker02)
    elif '02-电视柜' in furniture:
        TV_stand02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('TV_stand',TV_stand02)
    elif '02-盥洗台' in furniture:
        washbasin02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washbasin',washbasin02)
    elif '02-茶几' in furniture:
        teapoy02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',teapoy02)
    elif '02-衣柜' in furniture:
        wardrobe02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('wardrobe',wardrobe02)
    elif '02-蹲便器' in furniture:
        squatting_pan02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('squatting_pan',squatting_pan02)
    elif '02-边几' in furniture:
        side_table02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',side_table02)
    elif '02-马桶' in furniture:
        stool02= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('stool',stool02)
    elif '03-1200床' in furniture:
        bed031200 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed031200)
    elif '03-1500床' in furniture:
        bed031500 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed031500)
    elif '03-1800床' in furniture:
        bed031800 = Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bed',bed031800)
    elif '03-三人沙发' in furniture:
        mult_sofa03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',mult_sofa03)
    elif '03-书桌书椅' in furniture:
        desk03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('desk',desk03)
    elif '03-冰箱' in furniture:
        fridge03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('fridge',fridge03)
    elif '03-单人沙发' in furniture:
        single_sofa03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',single_sofa03)
    elif '03-单椅' in furniture:
        chair03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('chair',chair03)
    elif '03-双人沙发' in furniture:
        doub_sofa03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sofa',doub_sofa03)
    elif '03-圆餐桌' in furniture:
        circle_table03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',circle_table03)
    elif '03-方餐桌' in furniture:
        rect_table03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',rect_table03)
    elif '03-水槽' in furniture:
        sink03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sink',sink03)
    elif '03-洗衣机' in furniture:
        washer03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washer',washer03)
    elif '03-浴缸' in furniture:
        bathtub03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('bathtub',bathtub03)
    elif '03-淋浴房' in furniture:
        shower03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('shower',shower03)
    elif '03-淋浴花洒' in furniture:
        sprinkler03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('sprinkler',sprinkler03)
    elif '03-燃气灶' in furniture:
        gas_cooker03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('gas_cooker',gas_cooker03)
    elif '03-电视柜' in furniture:
        TV_stand03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('TV_stand',TV_stand03)
    elif '03-盥洗台' in furniture:
        washbasin03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('washbasin',washbasin03)
    elif '03-茶几' in furniture:
        teapoy03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',teapoy03)
    elif '03-衣柜' in furniture:
        wardrobe03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('wardrobe',wardrobe03)
    elif '03-蹲便器' in furniture:
        squatting_pan03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('squatting_pan',squatting_pan03)
    elif '03-边几' in furniture:
        side_table03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('table',side_table03)
    elif '03-马桶' in furniture:
        stool03= Furniture(furniture[:-4], '../project pics/平面图块/' + furniture)
        FURNITURES.add('stool',stool03)
    else :pass

#print(FSET.classlist)