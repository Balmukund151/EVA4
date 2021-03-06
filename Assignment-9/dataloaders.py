# -*- coding: utf-8 -*-
"""Dataloaders.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GjdhRCuFpj7WXwXyZ-_R7lGxpz6sPtki
"""

from torchvision import datasets,transforms
import torch
import albumentations
from albumentations import torch as AT
import numpy as np
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
from PIL import Image

def train_test_dataloaders(seed, batch_size, workers,train_transforms,test_transforms):
  
  SEED = seed

  # CUDA?
  cuda = torch.cuda.is_available()
  print("CUDA Available?", cuda)

  # For reproducibility
  torch.manual_seed(SEED)

  if cuda:
      torch.cuda.manual_seed(SEED)

  # dataloader arguments - something you'll fetch these from cmdprmt
  dataloader_args = dict(shuffle=True, batch_size=batch_size, num_workers=workers, pin_memory=True) if cuda else dict(shuffle=True, batch_size=batch_size)
  testdataloader_args = dict(shuffle=False, batch_size=batch_size, num_workers=workers, pin_memory=True) if cuda else dict(shuffle=True, batch_size=batch_size)

  trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transforms)
  trainloader = torch.utils.data.DataLoader(trainset, **dataloader_args)

  testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transforms)
  testloader = torch.utils.data.DataLoader(testset, **testdataloader_args)
  classes = ('plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck')
  return trainloader, testloader

def transformations():
  # Train Phase transformations
  train_transforms = transforms.Compose([
                                       #transforms.RandomRotation((-12.0, 12.0), fill=(1,)),
                                       transforms.RandomCrop(32, padding=4),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                       ])

  # Test Phase transformations
  test_transforms = transforms.Compose([
                                       transforms.ToTensor(),
                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                                       ])
  return train_transforms , test_transforms

  
def get_training_augmentation(img):
    #print(type(img))
    train_transform = [
        albumentations.Resize(32 , 32),
		AT.ToTensor()
    ]
    transforms =  albumentations.Compose(train_transform)
    return lambda img:transforms(image=np.array(img))['image']
	
class AlbumentationWrapper(object):
    def __init__(self,split):
        self.split=split
        self.aug=albumentations.Compose([
    albumentations.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    AT.ToTensor()
    ])
	
        if self.split=='train':
            self.aug=albumentations.Compose([
    albumentations.HorizontalFlip(),
    albumentations.RandomBrightness(),
    #albumentations.ShiftScaleRotate(rotate_limit=15, scale_limit=0.10),
    #albumentations.HueSaturationValue(),
    albumentations.Cutout(1,4,4,0.5),
    #albumentations.GaussNoise(),
    #albumentations.ElasticTransform(),
    albumentations.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    AT.ToTensor()
    ])
    
    
    def __call__(self,img):
        img = np.array(img)
        img = self.aug(image=img)['image']
        #img = Cutout(1,8,img).applyCutOut()
        #self.n_holes=1 
        #self.length=8
        
        return img
       
       
class Cutout(object):
    """Randomly mask out one or more patches from an image.
    Args:
        n_holes (int): Number of patches to cut out of each image.
        length (int): The length (in pixels) of each square patch.
    """
    """
        Args:
            img (Tensor): Tensor image of size (C, H, W).
        Returns:
            Tensor: Image with n_holes of dimension length x length cut out of it.
        """
    def __init__(self, n_holes, length, img):
        self.n_holes = n_holes
        self.length = length
        self.img = img
    
    def applyCutOut(self):
        
        h = self.img.size(1)
        w = self.img.size(2)

        mask = np.ones((h, w), np.float32)

        for n in range(self.n_holes):
            y = np.random.randint(h)
            x = np.random.randint(w)

            y1 = np.clip(y - self.length // 2, 0, h)
            y2 = np.clip(y + self.length // 2, 0, h)
            x1 = np.clip(x - self.length // 2, 0, w)
            x2 = np.clip(x + self.length // 2, 0, w)

            mask[y1: y2, x1: x2] = 0.

        mask = torch.from_numpy(mask)
        mask = mask.expand_as(self.img)
        self.img = self.img * mask

        return self.img