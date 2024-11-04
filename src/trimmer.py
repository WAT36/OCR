from PIL import Image
from PIL import ImageDraw
import sys
import os

#####################
## 英文法用の設定値 ###
#####################
LEFT_TOP_MARGIN = 95
LEFT_BOTTOM_MARGIN = 220
LEFT_LEFT_MARGIN = 180
LEFT_RIGHT_MARGIN = 0

RIGHT_TOP_MARGIN = 110
RIGHT_BOTTOM_MARGIN = 140
RIGHT_LEFT_MARGIN = 130
RIGHT_RIGHT_MARGIN = 90
######################

args = sys.argv

if len(args) != 2:
    print("Error: Usage: {0} (Input img file)".format(args[0]))
    sys.exit(1)

img_file = args[1]

if(not os.path.isfile(img_file)):
    print("Error: {0} is not found.".format(img_file))
    sys.exit(1)

im = Image.open(img_file)

# 左半分を切り出す
def crop_left(pil_img):
    img_width, img_height = pil_img.size
    return pil_img.crop((LEFT_LEFT_MARGIN,LEFT_TOP_MARGIN,(img_width // 2)-LEFT_RIGHT_MARGIN,img_height-LEFT_BOTTOM_MARGIN))

# 右半分を切り出す
def crop_right(pil_img):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width // 2)+RIGHT_LEFT_MARGIN,RIGHT_TOP_MARGIN,img_width-RIGHT_RIGHT_MARGIN,img_height-RIGHT_BOTTOM_MARGIN))


img_left = crop_left(im)
img_left.save(img_file[:-4]+'-left'+img_file[-4:])

img_right = crop_right(im)

########################
### ここは英文法用の処理 ##
########################
draw = ImageDraw.Draw(img_right) 
# 伏せる用の長方形
rectcolor = (255, 255, 255) # 矩形の色(RGB)。
linewidth = 1 # 線の太さ
# 問題番号の部分を全て塗りつぶす
# draw.rectangle([(10, 20), (120, 45)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(10, 280), (120, 310)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(10, 600), (120, 625)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(10, 890), (120, 920)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(10, 1125), (120, 1150)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# # 「正解( )」の部分を全て塗りつぶす
# draw.rectangle([(755, 20), (826, 45)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(755, 280), (826, 310)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(755, 600), (826, 625)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(755, 890), (826, 920)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(755, 1125), (826, 1150)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(842, 20), (850, 45)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(842, 280), (850, 310)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(842, 600), (850, 625)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(842, 890), (850, 920)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(842, 1125), (850, 1150)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# # 語句訳の部分を全て塗りつぶす
# img_right_width, img_right_height = img_right.size
# draw.rectangle([(0, 200), (img_right_width, 250)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(0, 495), (img_right_width, 580)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(0, 810), (img_right_width, 880)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(0, 1045), (img_right_width, 1120)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
# draw.rectangle([(0, 1280), (img_right_width, img_right_height)],fill=(255, 255, 255),outline=rectcolor, width=linewidth)
#########################

img_right.save(img_file[:-4]+'-right'+img_file[-4:])
