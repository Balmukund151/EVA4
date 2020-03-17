# -*- coding: utf-8 -*-
"""Models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rIKmM5gHvYWvwVevkfR3RXx6nUWjp5-8
"""

import torch.nn as nn
from torchsummary import summary
import torch.nn.functional as F

dropout_value = 0.1
class QuizModel(nn.Module):
    def __init__(self, dropout):
        super(QuizModel, self).__init__()
        dropout_value = dropout
        # Input Block
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(32)
        )

        self.intermediate1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(1, 1), padding=0 , bias=False),
        )
        
        self.intermediate2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 1), padding=0 , bias=False),
        )
        
        self.pool = nn.MaxPool2d(2, 2)

        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=2, dilation=2, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            # nn.Dropout(dropout_value)            
        )

        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(64)
        )
        
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            nn.BatchNorm2d(64)
        )

        self.intermediate3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(1, 1), padding=0 , bias=False),
        )
        
        self.intermediate4 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 1), padding=0 , bias=False),
        )        

        

        
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=8)
        ) # output_size =1  RF=209
        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=10, kernel_size=(1, 1), padding=0, bias=False)
        ) # output_size =1  RF=209

    def forward(self, x1):
        x2 = self.convblock1(x1)
        x1 = self.intermediate1(x1)
        x3 = self.convblock2(x1+x2)
        x4 = self.pool(self.intermediate2(x1)+self.intermediate2(x2)+x3)
        x5 = self.convblock3(x4)        
        x6 = self.convblock3(x4+x5)
        x7 = self.convblock3(x4+x5+x6)
        x8 = self.pool(x5+x6+x7)
        x9 = self.convblock4(x8)
        #x8 = self.intermediate3(x8)  
        x10 = self.convblock4(x8+x9)
        x11 = self.convblock4(x8+x9+x10)        
        x = self.gap(x11)
        x = self.convblock7(x)
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)

def model_params(model, input_size,device):
  model = model.to(device)
  summary(model, input_size)