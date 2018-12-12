import torch
import torch.nn as nn
from torch.autograd import Variable

cuda = False
if torch.cuda.is_available:
    cuda = True
    
N_FFT = 512
N_CHANNELS = round(1 + N_FFT/2)
OUT_CHANNELS = 64


class RandomCNN(nn.Module):
    def __init__(self):
        super(RandomCNN, self).__init__()

        # 2-D CNN
        self.conv1 = nn.Conv2d(1, 32, kernel_size=(3, 3), stride=1, padding=0)
        self.LeakyReLU = nn.LeakyReLU(0.2)

        # Set the random parameters to be constant.
        weight = torch.randn(self.conv1.weight.data.shape)
        self.conv1.weight = torch.nn.Parameter(weight, requires_grad=False)
        bias = torch.zeros(self.conv1.bias.data.shape)
        self.conv1.bias = torch.nn.Parameter(bias, requires_grad=False)
        
        
        # 2-D CNN
        self.conv2 = nn.Conv2d(32, 64, kernel_size=(3, 3), stride=1, padding=0)
        self.LeakyReLU = nn.LeakyReLU(0.25)

        # Set the random parameters to be constant.
        weight = torch.randn(self.conv2.weight.data.shape)
        self.conv2.weight = torch.nn.Parameter(weight, requires_grad=False)
        bias = torch.zeros(self.conv2.bias.data.shape)
        self.conv2.bias = torch.nn.Parameter(bias, requires_grad=False)

    def forward(self, x_delta):
        x_delta = self.LeakyReLU(self.conv1(x_delta))
        out = self.LeakyReLU(self.conv2(x_delta))
        return out
