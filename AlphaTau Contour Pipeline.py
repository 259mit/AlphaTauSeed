#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isolate_contours(image, n, l, value):
    r = image[n][:,:,l]
    # Find contours at a constant value of 0.8
    contours = measure.find_contours(r, value)
    # Select the largest contiguous contour
    contour = sorted(contours, key=lambda x: len(x))
    return contour

