import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("bug.jpg")   #loads the image from file
print(type(img))
print(img.shape)    # image dimensions
print(img[0,0])     # shows pixel 0,0 R,G,B colors [43 84 52]

output = img.copy()     # The original image is read-only!
output[:, :, :2] = 0    # color RGB - removes R,G -> blue image
output[:, 600:610] = [255,0,0] #pixel between coluns 600 and 610 set to red

mpimg.imsave("bug-blue.jpg", output)    #saves the image in a file

plt.figure(1)
#plt.imshow(output)  # shows the image

# a) - Create an image 8 times smaller and transposed 90º
output[::8, ::8,]
plt.imshow(output)
#np.transpose (axis0,axis1,axis2)


# b) - Create a gray iamge wich has only 2D. the pixel value is the average of R,G, B  
#       imsave(....., cmap='gray') - to specific gray color map


plt.show()

sum(x/2 for x in range(7) if x%2==0)