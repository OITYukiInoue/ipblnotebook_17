import url2image
from matplotlib import pyplot as plt
img = url2image.url_to_image('http://www.oit.ac.jp/rd/img/index/pc/logo.png')
print(img)
plt.imshow(img)
plt.show()

