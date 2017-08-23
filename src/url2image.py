import numpy as np
import urllib
import cv2
 
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url1):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	req = urllib.request.Request(url=url1,method='GET',headers={'User-Agent':'Mozilla/5.0'})
	resp= urllib.request.urlopen(req)
##	print(resp.read())
	imag = np.asarray(bytearray(resp.read()), dtype="uint8")

	image = cv2.imdecode(imag, -1)
 
	# return the image
	return image
