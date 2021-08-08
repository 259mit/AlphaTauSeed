#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def displayImgAndMask(idx):
    #train_data_path = os.path.join(data_path,'train')
    imageid = os.listdir(data_path)
    train_path = os.path.join(data_path,imageid[idx])
    img_path_main = os.path.join(train_path,'images')
    img_path = os.path.join(img_path_main,str(imageid[idx])+'.npy')
    masks_path_main = os.path.join(train_path,'masks')
    mask_path = os.path.join(masks_path_main,'mask.npy')
    seedcsv = os.path.join(train_path,'seeds.csv')
    seednpy = os.path.join(train_path,'seeds.npy')
    return img_path, mask_path, seednpy, seedcsv

def load_train_data(n):
    impath = displayImgAndMask(n)[0]
    maskpath = displayImgAndMask(n)[0]
    snp = displayImgAndMask(n)[0]
    imgs_train = np.load(impath)
    imgs_train_mask = np.load(maskpath)
    seed_train = np.load(snp)
    return imgs_train,imgs_train_mask, seed_train

def resize_volume(img):
    depth = img.shape[-1] / 41
    width = img.shape[0] / 512
    height = img.shape[1] / 512
    depth_factor = 1 / depth
    width_factor = 1 / width
    height_factor = 1 / height
    img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=1)
    return img

def getinshape(img, mask):
    newarray = resize_volume(img)
    newmask = resize_volume(mask)
    return newarray, newmask

def normalize(image, MIN_BOUND, MAX_BOUND):
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image>1] = 1.
    image[image<0] = 0.
    return image

def preproceesing(path):
    k = len(os.listdir(path))
    imgs_train = []
    imgs_train_mask = []
    seed_train = []
    newimg = []
    newimg2 = []
    newmasklist = []
    for i in range(0,k):
        imgs_train1 ,imgs_train_mask1 , seed_train1 = load_train_data(i)
        imgs_train.append(imgs_train1)
        imgs_train_mask.append(imgs_train_mask1)
        seed_train.append(seed_train1)
    for j in range(0,k):
        newarray, newmask = getinshape(imgs_train[j], imgs_train_mask[j])
        newimg.append(newarray)
        newmasklist.append(newmask)
    for m in range(0, k):
        newimg2.append(normalize(newimg[m], -500, 500))
    return newimg2, newmasklist

