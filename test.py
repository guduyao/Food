import glob
import cv2
import os
from tqdm import tqdm
import numpy as np
from PIL import Image

# img_path = glob.glob("E:/PYCHARM/buy/CHANGE/photo/photo1/*.jpg")




# cv2.imshow('a',a)
# cv2.waitKey(0)



if __name__ == '__main__':
    list = []
    img_save = 'E:/pycharm/yolo3-keras/s'
    path = 'E:/pycharm/yolo3-keras/save'
    # top_size, bottom_size, left_size, right_size = (250, 250, 250, 250)
    img_path = os.listdir(path)
    for i in range(len(img_path)-2):
        save_path = os.path.join(img_save, img_path[i])
        img1 = cv2.imread(os.path.join(path, img_path[i]))
        img2 = cv2.imread(os.path.join(path, img_path[i+1]))
        img3 = cv2.imread(os.path.join(path, img_path[i+2]))
        img4 = cv2.imread(os.path.join(path, img_path[i+3]))
        # ====使用numpy的数组矩阵合并concatenate======

        # 横向连接
        image1 = np.concatenate([img1, img2], axis=1)
        image2 = np.concatenate([img3, img4], axis=1)
        # 纵向连接
        image = np.vstack((image1, image2))


        image = np.array(image)
        # img = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
        img = cv2.resize(image, (416, 416))
        cv2.imwrite(save_path, img)

