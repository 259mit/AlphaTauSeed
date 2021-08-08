#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plotmaster(n, l, fh=5, fw=5):
    #imgs_train,imgs_train_mask, seed_train = newarray, newmask, 0
    image = newimg[n]
    mask = newmasklist[n]
    fig, ax = plt.subplots(figsize = (fh,fw))
    plt.imshow(image[:,:,l], cmap = 'gray')
    plt.imshow(mask[:,:,l]>0, cmap='jet', alpha=0.3)

def plotmasternorm(n, l, fh=5, fw=5):
    #imgs_train,imgs_train_mask, seed_train = newarray, newmask, 0
    image = newimg[n]
    mask = newmasklist[n]
    fig, ax = plt.subplots(figsize = (fh,fw))
    plt.imshow(image[:,:,l], cmap = 'gray')
    plt.imshow(mask[:,:,l]>500, cmap='jet', alpha=0.3)

