from PIL import Image
import sys
import os

# 英文法用
LEFT_TOP_MARGIN = 160
LEFT_BOTTOM_MARGIN = 220
LEFT_LEFT_MARGIN = 180
LEFT_RIGHT_MARGIN = 0

RIGHT_TOP_MARGIN = 110
RIGHT_BOTTOM_MARGIN = 160
RIGHT_LEFT_MARGIN = 130
RIGHT_RIGHT_MARGIN = 90

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
img_right.save(img_file[:-4]+'-right'+img_file[-4:])
