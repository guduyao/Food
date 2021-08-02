import os


path1 = r'C:\Users\106\Desktop\bigwork\yolo3-keras\VOCdevkit\VOC2007\test'

def file_name(file_dir):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
            elif os.path.splitext(file)[1] == '.xml':
                xml_list.append(os.path.splitext(file)[0])

    diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print(len(diff))
    for name in diff:
        print("no jpg", name + ".xml")

    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))
    for name in diff2:
        print("no xml", name + ".jpg")
    return jpg_list,xml_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名

if __name__ == '__main__':

    file_name(path1)