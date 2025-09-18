import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def get_data_loaders(batch_size=64, root='./data'):
	"""
	Loads Fashion-MNIST dataset and returns train and validation DataLoaders.
	"""
	transform = transforms.Compose([
		transforms.ToTensor(),
		transforms.Normalize((0.5,), (0.5,))
	])

	train_dataset = datasets.FashionMNIST(
		root=root, train=True, download=True, transform=transform
	)
	val_dataset = datasets.FashionMNIST(
		root=root, train=False, download=True, transform=transform
	)

	train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
	val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

	return train_loader, val_loader




