import os
import shutil

dir="D:\VoxelNet-tensorflow\data_object_velodyne\\training\\velodyne"
#dir="D:\VoxelNet-tensorflow\data_object_label_2\\training\label_2"
#dir="D:\VoxelNet-tensorflow\data_object_image_2\\training\image_2"
val_find="D:\\val.txt"
dest="D:\VoxelNet-tensorflow\data_object_velodyne\\validation\\velodyne"
#dest="D:\VoxelNet-tensorflow\data_object_label_2\\validation\label_2"
#dest="D:\VoxelNet-tensorflow\data_object_image_2\\validation\image_2"

#dest="D:\VoxelNet-tensorflow\data_object_velodyne\\train\\velodyne"
#dest="D:\VoxelNet-tensorflow\data_object_label_2\\train\label_2"
#dest="D:\VoxelNet-tensorflow\data_object_image_2\\train\image_2"

num=[]
with open(val_find) as vf:
    for i in vf:
        i=i.split()
        num.append(i[0]+'.bin')
        #num.append(i[0]+'.txt')
        #num.append(i[0]+'.png')
print(dest)

os.makedirs(dest)
for i in num:
    shutil.move(os.path.join(dir,i),dest)
#shutil.move('D:\\000000.bin',dest)
