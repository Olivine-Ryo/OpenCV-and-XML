import os
import cv2
import numpy as np
import glob
from tqdm import tqdm
directries=glob.glob("*_*")
#for directry in directries:
#    os.mkdir('%s_normal' % directry)

for directry in tqdm(directries):
    os.chdir(directry)
    files=glob.glob("*.JPG")
    os.chdir('..')
    for file in files:
        image = cv2.imread('%s/%s' % (directry,file))
        img_normal = (image - np.mean(image))/np.std(image)*55+140
        cv2.imwrite('normal/%s_normal/%s' % (directry,file),img_normal)
