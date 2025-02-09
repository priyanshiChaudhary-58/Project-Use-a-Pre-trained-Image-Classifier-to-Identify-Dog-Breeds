# Project-Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds
This project uses pre-trained Convolutional Neural Networks (CNNs) to classify dog breeds and distinguish dogs from non-dog images. Built with Python and PyTorch, it evaluates three CNN architectures (VGG, ResNet, AlexNet) for accuracy and runtime efficiency

# Pre-trained-Image-Classifier-to-Identify-Dog-Breeds
This project uses pre-trained Convolutional Neural Networks (CNNs) to classify dog breeds and distinguish dogs from non-dog images. Built with Python and PyTorch, it evaluates three CNN architectures (VGG, ResNet, AlexNet) for accuracy and runtime efficiency

# Dog Breed Classifier with CNN Models 🐕🖼️

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A Python-based project that uses pre-trained CNN models (VGG, ResNet, AlexNet) to classify dog breeds and distinguish dogs from non-dog images. Developed as part of Udacity's AI Programming with Python Nanodegree.

## Key Features
- **Dog Detection**: Accurately identifies dog vs. non-dog images.
- **Breed Classification**: Predicts 120+ dog breeds using transfer learning.
- **Model Comparison**: Benchmarks VGG, ResNet, and AlexNet for accuracy/runtime trade-offs.
- **Performance Metrics**: Generates % correct dogs, breeds, and non-dogs.

## Tech Stack
- **Languages**: Python
- **Frameworks**: PyTorch, argparse, PIL, Matplotlib
- **Pre-trained Models**: VGG16, ResNet18, AlexNet

## Repository Structure
.
- ├── check_images.py # Main script for classification
- ├── classifier.py # Pre-trained model loader
- ├── dognames.txt # Valid dog breeds list
- ├── pet_images/ # Sample dataset (dogs + non-dogs)
- ├── requirements.txt # Dependencies
- └── README.md


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshiChaudhary-58/Pre-trained-Image-Classifier-to-Identify-Dog-Breeds.git
   cd Pre-trained-Image-Classifier-to-Identify-Dog-Breeds

## Usage
**Note**: Unzip `pet_images.zip` before running the code.
- python check_images.py \
  --arch vgg \                  # Model: vgg/resnet/alexnet
  --dir pet_images/ \           # Input image directory
  --dogfile dognames.txt        # Dog breed list

## Example Results
**Results for VGG Model**
- N Images: 41 | Dog Images: 23 | Non-Dog Images: 18
- %-Correct Dogs: 78.26% | %-Correct Breed: 26.09% | Runtime: 0:0:4


## Acknowledgements
- Dataset: Udacity Pet Images & ImageNet
- Models: Pre-trained CNNs from PyTorch's Model Zoo

## Let’s connect!
📧 Email: priyanshichy2513@gmail.com | 💼 LinkedIn: www.linkedin.com/in/priyanshi-kumari
