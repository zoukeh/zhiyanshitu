# """
# 用于批量处理某一文件夹下的图像文件，由raw格式转为tif/png/jpg
# """
#
import os
import cv2
import numpy as np
import rawpy
# 在这里修改存放raw文件的文件夹路径
path = 'C:/Users/ZouKeh/Desktop/imgae/'
files = os.listdir(path)

# 首先确定原始图片的基本信息：数据格式，行数列数，通道数
rows = 512  # 图像的行数
cols = 512 # 图像的列数
channels = 3  # 图像的通道数，灰度图为1

print('--批量转换开始--')

for file in files:

    # 将文件名和后缀分成两部分
    portion = os.path.splitext(file)
    # 只处理.raw文件
    if portion[1] == '.NEF':
        realPath = path + file
        # 利用numpy的fromfile函数读取raw文件，并指定数据格式
        raw = rawpy.imread(realPath)
        image_rawpy = raw.postprocess()
        # 利用numpy中array的reshape函数将读取到的数据进行重新排列。
        # img = img.reshape(rows, cols, channels)
        # Convert RGB to BGR
        image_rawpy = image_rawpy[:, :, ::-1].copy()
        image_rawpy = cv2.resize(image_rawpy, (682, 512))
        # 将图像保存为tif格式
        fileName = portion[0] + '.jpg'
        tif_fileName = os.path.join(path, fileName)
        print(tif_fileName)
        cv2.imwrite(tif_fileName,image_rawpy)  # 1为tif无损压缩；修改这里的参数可以转为其他格式，具体参考上面两篇文章
        print(file + ' 转换完成')
    else:
        print(file + ' 不是.raw文件')

print('--批量转换结束--')

# Reading a Nikon RAW (NEF) image
# This uses rawpy library
# filename='C:/Users/ZouKeh/Desktop/imgae/DSC_7789.NEF'
#
# print("reading RAW file using rawpy.")
# raw = rawpy.imread(filename)
# image_rawpy = raw.postprocess()
# print("Size of image read:" + str(image_rawpy.shape))

# Optional
# Convert RGB to BGR
# image_rawpy = image_rawpy[:, :, ::-1].copy()

####################
# Show using matplotlib
# fig = plt.figure("image_rawpy read file: " + filename)

# image_rawpy.save('C:/Users/ZouKeh/Desktop/imgae/DSC_7789', 'PNG')
# image_rawpy = cv2.resize(image_rawpy,(682,512))
# cv2.imwrite('C:/Users/ZouKeh/Desktop/imgae/DSC_7789.png', image_rawpy)
# imgplot = plt.imshow(plt_image)
# plt.show(block=False)
# Show using OpenCV
# cv2.imshow("image_rawpy read file: " + filename, image_rawpy)

# ####################
# # This uses imageio
# print("reading RAW file using rawio.")
# image_imageio=imageio.imread(filename)
# print("Size of image read:" + str(image_imageio.shape))
# fig2 = plt.figure("image_imageio read file: " + filename)
# plt_image2 = image_imageio
# imgplot2 = plt.imshow(plt_image2)
# plt.show(block=False)
# # Show using OpenCV
# cv2.imshow("image_imageio read file: " + filename, image_imageio)
#
#
# cv2.waitKey()
# cv2.destroyAllWindows()