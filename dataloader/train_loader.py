# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:36:14 2021

@author: hudew
"""

import sys
sys.path.insert(0,"E:\\tools\\")

import util
import HessianField as hf
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
import torch 
from torch.utils.data import DataLoader, Dataset

def plot_quiver(im, flow):
    h,w = im.shape
    x,y = np.meshgrid(np.linspace(0,h-1,h),np.linspace(0,w-1,w))
    
    plt.figure(figsize=(12,12))
    plt.imshow(im,cmap='gray')
    plt.quiver(x.reshape(h*w),y.reshape(h*w),
               flow[0,:,:].reshape(h*w),
               flow[1,:,:].reshape(h*w),color='r')
    plt.show()

rose_root = "E:\\ROSE\\"
OCTA_root = "E:\\OCTA500\\GT\\OCTA-500\\OCTA_6M\\"
DRIVE_root = "E:\\DRIVE\\"

#%%
gt = []
data = []

for folder in os.listdir(OCTA_root):
    if folder == "GroundTruth":
        gt_root = OCTA_root + folder + "\\"
        for file in os.listdir(gt_root):
            im = np.uint8(imageio.imread(gt_root + file)>200)
            gt.append(im)
    elif folder == "Projection Maps":
        data_root = OCTA_root + folder + "\\OCTA(ILM_OPL)\\"
        for file in os.listdir(data_root):
            data.append(imageio.imread(data_root + file))
    else:
        pass

class GetTrainDataset(Dataset):
    
    def __init__(self, im_size, num_sample, data_list, gt_list):
        super().__init__()
        self.im_size = im_size
        self.num_sample = num_sample
        self.data_list = data_list
        self.gt_list = gt_list
        self.data = ()
        
        for i in range(len(self.data_list)):
            im = self.
        
        
        
        
        
