import torch
import torchvision
import sys
print(sys.executable)

# How to check if pytorch is using the GPU? #

print('\ntest cuda avalaible: ' + str(torch.cuda.is_available()))
#>>> True

print('torch device: ' + str(torch.cuda.current_device()))
#>>> 0

print('device 0 emplacement: ' + str(torch.cuda.device(0)))
#>>> <torch.cuda.device at 0x7efce0b03be0>

print('nombre de device: ' + str(torch.cuda.device_count()))
#>>> 1

print('device 0 name: ' + str(torch.cuda.get_device_name(0)))

#If you get an error message that reads
'''
Found GPU0 XXXXX which is of cuda capability #.#.
PyTorch no longer supports this GPU because it is too old.
'''
print('test PyTorch and CUDA: ' + str(torch.zeros(1).cuda()) + '\n\n')
###



# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
    
    
'''
Using device: cuda

Tesla K80
Memory Usage:
Allocated: 0.3 GB
Cached:    0.6 GB
'''

x = torch.rand(5, 3)
print('\nTest PyTorch')
print(x)