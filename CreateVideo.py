import os
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext in ['.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        
        print(len(images))
        count = len(images)
        
        frame = cv2.imread(image[0])
        height, width, layers = frame.shape
        size = (width,height)
        
        out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
        for i in range(0,count):
            print(images[i])
            frame = cv2.imread(images[i])
            out.write(frame)
            
            out.release() 
            print("done")
            