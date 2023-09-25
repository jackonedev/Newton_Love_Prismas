import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())
print ("device: ", torch.cuda.get_device_name(0))
