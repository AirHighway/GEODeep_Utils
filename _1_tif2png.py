# 以tiff转png为例，其他格式同理，
# 代码中路径更改为自己图像存放路径即可
from PIL import Image
import os
import cv2 as cv
import re
import numpy as np

files_path = r"D:\txt_files\ahu_2017\2017_512_images"
out_path = r"D:\txt_files\ahu_2017\2017_512_images_png\\"

imagesDirectory = files_path  # tiff图片所在文件夹路径

# length = len(imagesDirectory)

for imageName in os.listdir(imagesDirectory):
    imagePath = os.path.join(imagesDirectory, imageName)
    # image = Image.open(imagePath)  # 打开tiff图像

    # print(re.split("[\\\ ,.]", imagePath))

    img = cv.imread(imagePath, 1)

    # print(img.shape)
    # img = Image.fromarray(np.uint8(img))

    file_name = re.split("[\\\ ,.]", imagePath)
    # img.save(r'D:\_personSelf\_heao\Bi-SRNet-main\TEST_DIR\img1/' + file_name[-2] + ".png")

    cv.imwrite(out_path + file_name[-2] + ".png", img)
