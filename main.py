from libxmp import XMPFiles, consts
import os
import cv2
import numpy as np
import glob
from tqdm import tqdm
directries=glob.glob("*_*")
for directry in tqdm(directries):
    os.chdir(directry)
    files=glob.glob("*.JPG")
    os.chdir('..')
    try:
        os.mkdir('normal/%s_normal ' % directry)
    except FileExistsError:
        pass
    
    for file in files:
        ##OpenCV処理
        image = cv2.imread('%s/%s' % (directry,file))
        img_normal = (image - np.mean(image))/np.std(image)*55+140
        cv2.imwrite('normal/%s_normal/%s' % (directry,file),img_normal)
        
        ##XMP処理
        xmpfile = XMPFiles( file_path="%s/%s" % (directry, file), open_forupdate=True )
        xmp = xmpfile.get_xmp()
        xmpfile.close_file()
        xmpfile_normal = XMPFiles( file_path="normal/%s_normal/%s" % (directry, file), open_forupdate=True )
        xmp_normal = xmpfile_normal.get_xmp()
        xmp_normal=xmp
        xmpfile_normal.put_xmp(xmp_normal)
        xmpfile_normal.close_file()
