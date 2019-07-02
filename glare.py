import numpy as np
import cv2
path='..../sample.jpg'  #original image path for which glare has to be removed 
img = cv2.imread(path)
img2 = cv2.imread(path,2)     # reading the same image for creation of mask with 2nd chanel as input
ret, bw_img = cv2.threshold(img2,170,255,cv2.THRESH_BINARY) 	    # setting a threshold for mask here 170 is the limit set		
cv2.imwrite('binary_mask1.jpg',bw_img)		# save the binary mask in a local path
maskpath='...../binary_mask1.jpg'
mask = cv2.imread(maskpath,0) 


#usinf inpaint function remove the mask from the original image 
dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
cv2.imwrite('final_image.jpg',dst)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
