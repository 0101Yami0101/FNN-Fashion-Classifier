from data import get_data_loaders

if __name__ == "__main__":
	train_loader, val_loader = get_data_loaders()
	print(f"Train batches: {len(train_loader)}")
	print(f"Validation batches: {len(val_loader)}")
