#
import sys
print(sys.version_info)
if(sys.version_info.major == 3 and sys.version_info.minor == 6):
    print('version is 3.6 OK')
else:
    print('version mismatch')

print(sys.version)
sys.version_info
import numpy as np
import matplotlib.pyplot as plt
import cv2



def main():
    img = cv2.imread( 'objects.jpg' )
    #print(img)
    iarray = np.array(img)
    r_ch= iarray[...,0]
    g_ch= iarray[...,1]
    b_ch= iarray[...,2]
    print( r_ch.max())
    iarray[...,1]=0
    iarray[...,2]=0
    image_print(iarray)

def image_print(data):    
    plt.imshow(data)
    plt.show()

if(__name__ == '__main__'):
    main()