# glare_removal

In this repo I show how to remove a glare from an image using opencv and python

Here you have to load the image in which glare has to be removed and set a threshold which matches your requirement of glare. In my code I set a threshold of 170 actual range is from (0-255).

Using inpaint function from opencv you can remove the binary mask of the glare which has been created from the above threshold from the original image.

Here sample.jpg is the original image where glare has to be removed, binary_mask1.jpg is the mask created from the threshold function and binary_mask3.jpg is the final image without glare.
 

