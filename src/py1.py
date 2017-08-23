#
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread( 'objects.jpg' )
#print(img)   #print the contents
plt.imshow(img)  #show image

plt.show()
