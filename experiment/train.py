import torch
import torch.nn as nn
from model.lenet import LeNet
from torchsummary import summary

# print(torch.__version__)
print(torch.cuda.is_available())

net = LeNet(classes=2)
# net = net.cuda()
net = net.to("cuda")
net.initialize_weights()

summary(net, input_size=(3, 32, 32)) 