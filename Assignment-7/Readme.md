*************************************************************************************

S7_Final_Solution.ipynb --> This is the main solution file.


S7_functions.ipynb --> This is the file having all the defined functions.


**************************************************************************************




***************************************************************************************

Logs

**************************************************************************************



  0%|          | 0/391 [00:00<?, ?it/s]----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 32, 32]             864
              ReLU-2           [-1, 32, 32, 32]               0
       BatchNorm2d-3           [-1, 32, 32, 32]              64
            Conv2d-4           [-1, 64, 32, 32]          18,432
              ReLU-5           [-1, 64, 32, 32]               0
       BatchNorm2d-6           [-1, 64, 32, 32]             128
         MaxPool2d-7           [-1, 64, 16, 16]               0
            Conv2d-8          [-1, 128, 16, 16]          73,728
              ReLU-9          [-1, 128, 16, 16]               0
      BatchNorm2d-10          [-1, 128, 16, 16]             256
           Conv2d-11          [-1, 128, 16, 16]           1,152
           Conv2d-12          [-1, 256, 18, 18]          32,768
             ReLU-13          [-1, 256, 18, 18]               0
      BatchNorm2d-14          [-1, 256, 18, 18]             512
        MaxPool2d-15            [-1, 256, 9, 9]               0
           Conv2d-16            [-1, 256, 9, 9]         589,824
             ReLU-17            [-1, 256, 9, 9]               0
      BatchNorm2d-18            [-1, 256, 9, 9]             512
        MaxPool2d-19            [-1, 256, 4, 4]               0
        AvgPool2d-20            [-1, 256, 1, 1]               0
           Conv2d-21             [-1, 10, 1, 1]           2,560
================================================================
Total params: 720,800
Trainable params: 720,800
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 5.94
Params size (MB): 2.75
Estimated Total Size (MB): 8.70
----------------------------------------------------------------
EPOCH: 0
Loss=0.8590723872184753 Batch_id=390 Accuracy=53.21: 100%|██████████| 391/391 [00:51<00:00,  7.53it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 1.0647, Accuracy: 6190/10000 (61.90%)

EPOCH: 1
Loss=0.6949154138565063 Batch_id=390 Accuracy=68.78: 100%|██████████| 391/391 [00:53<00:00,  7.26it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.9096, Accuracy: 6730/10000 (67.30%)

EPOCH: 2
Loss=0.4679679870605469 Batch_id=390 Accuracy=75.49: 100%|██████████| 391/391 [00:53<00:00,  7.28it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7593, Accuracy: 7382/10000 (73.82%)

EPOCH: 3
Loss=0.5299914479255676 Batch_id=390 Accuracy=80.32: 100%|██████████| 391/391 [00:53<00:00,  7.32it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7224, Accuracy: 7502/10000 (75.02%)

EPOCH: 4
Loss=0.5057204961776733 Batch_id=390 Accuracy=84.19: 100%|██████████| 391/391 [00:52<00:00,  7.48it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7057, Accuracy: 7596/10000 (75.96%)

EPOCH: 5
Loss=0.3865779936313629 Batch_id=390 Accuracy=87.05: 100%|██████████| 391/391 [00:53<00:00,  7.30it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7292, Accuracy: 7607/10000 (76.07%)

EPOCH: 6
Loss=0.3638181686401367 Batch_id=390 Accuracy=90.17: 100%|██████████| 391/391 [00:53<00:00,  7.33it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7058, Accuracy: 7689/10000 (76.89%)

EPOCH: 7
Loss=0.3507469594478607 Batch_id=390 Accuracy=92.89: 100%|██████████| 391/391 [00:53<00:00,  7.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7093, Accuracy: 7829/10000 (78.29%)

EPOCH: 8
Loss=0.22068016231060028 Batch_id=390 Accuracy=94.93: 100%|██████████| 391/391 [00:52<00:00,  7.50it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7412, Accuracy: 7771/10000 (77.71%)

EPOCH: 9
Loss=0.0976063460111618 Batch_id=390 Accuracy=97.07: 100%|██████████| 391/391 [00:53<00:00,  7.32it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7294, Accuracy: 7787/10000 (77.87%)

EPOCH: 10
Loss=0.026559878140687943 Batch_id=390 Accuracy=98.76: 100%|██████████| 391/391 [00:53<00:00,  7.29it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.7170, Accuracy: 7950/10000 (79.50%)

EPOCH: 11
Loss=0.027880018576979637 Batch_id=390 Accuracy=99.64: 100%|██████████| 391/391 [00:53<00:00,  7.37it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.6987, Accuracy: 8060/10000 (80.60%)

EPOCH: 12
Loss=0.008585411123931408 Batch_id=390 Accuracy=99.96: 100%|██████████| 391/391 [00:52<00:00,  7.50it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.6831, Accuracy: 8183/10000 (81.83%)

EPOCH: 13
Loss=0.005089324899017811 Batch_id=390 Accuracy=99.98: 100%|██████████| 391/391 [00:53<00:00,  7.35it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.6712, Accuracy: 8208/10000 (82.08%)

EPOCH: 14
Loss=0.004492932464927435 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [00:53<00:00,  7.33it/s]

Test set: Average loss: 0.6812, Accuracy: 8203/10000 (82.03%)

