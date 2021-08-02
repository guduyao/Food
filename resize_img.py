from PIL import Image
import os
import glob

'''
os.path.join()函数：连接两个或更多的路径名组件
1.如果各组件名首字母不包含’/’，则函数会自动加上
2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾

os.path.basename(jpgfile)
返回path最后的文件名。如果path以／或\结尾，那么就会返回空值

Image.NEAREST ：低质量
Image.BILINEAR：双线性
Image.BICUBIC ：三次样条插值
Image.ANTIALIAS：高质量

os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，包括当前文件名
root 所指的是当前正在遍历的这个文件夹的本身的地址
dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)

glob.glob返回所有匹配的文件路径列表
'''

#读取图片，修改图片，另存图片
def convertjpg(jpgfile,outdir,width=224,height=224,img_sum=0):
    img=Image.open(jpgfile)#提取目录下所有图片
    try:
        new_img=img.resize((width,height),Image.BILINEAR)#更改尺寸
        img_sum=str('%08d'%img_sum)#图片保存成00000001格式
        new_img.save(os.path.join(outdir)+img_sum+'.jpg')#保存到另一目录
    except Exception as e:
        print(e)

#读取文件名
def file_name(file_dir):
    L=[]#保存文件名
    img_num=0#计算图片总数
    for root, dirs, files in os.walk(file_dir):
        img_num=img_num+len(files)
        one=os.path.basename(str(root))#获取路径最后的/或者\后的文件名
        L.append(one)
    num=len(L)-1  #获取路径下文件个数
    print('%s路径下有%d个文件,一共%d张图片'%(L[0],num,img_num))
    return L ,num ,img_num


filepath='/root/pycharm/yolo3-keras/VOCdevkit/VOC2007'
files,files_num,imgs_num=file_name(filepath)

img_name=0
for i in range(files_num):#遍历文件
    filename=files[i+1]#文件索引从1开始
    for jpgfile in glob.glob(filepath+"/"+filename+"/*.jpg"):#返回所有匹配的图片路径列表
        print(jpgfile)
        img_name=img_name+1
        convertjpg(jpgfile,"/root/pycharm/yolo3-keras/img/",img_sum=img_name)

