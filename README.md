# FNN Fashion Classifier

This project implements a Feedforward Neural Network (FNN) to classify images from the Fashion-MNIST dataset.

## Features
- Loads and preprocesses Fashion-MNIST data
- Implements a fully connected neural network
- Training loop with loss, optimizer, scheduler, and early stopping
- Regularization with dropout and L2
- Visualizes training curves, confusion matrix, and first-layer weights
- Compares training and validation metrics

## Getting Started
1. Clone the repository and navigate to the project folder.
2. (Optional) Create and activate a Python virtual environment.
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Run the main script:
	```bash
	python main.py
	```

## Project Structure
- `main.py` - Entry point
- `data.py` - Data loading utilities
- `model.py` - Model definition
- `train.py` - Training loop
- `evaluate.py` - Evaluation and metrics
- `visualize.py` - Visualization tools
- `utils.py` - Helper functions
- `models/` - Saved models
- `outputs/` - Plots and results

## Goals
- Understand how an FNN learns on images
- Practice training, regularization, and optimizer effects
- Visualize and interpret model behavior

## License
MIT
