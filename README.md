# Project-Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds
This project uses pre-trained deep learning models (ResNet, AlexNet, and VGG16) to classify images and identify dog breeds. It applies transfer learning with models trained on the ImageNet dataset, adjusting results to determine whether an image contains a dog and, if so, which breed it is. 
# Dog Breed Classifier

## Project Overview

This project utilizes a pre-trained deep learning model to identify and classify dog breeds from images. The model uses popular architectures such as ResNet18, AlexNet, and VGG16, pretrained on the ImageNet dataset. It takes an image as input and predicts the breed of the dog in the image.

## Key Features
- **Pre-trained Models**: The classifier uses ResNet18, AlexNet, and VGG16 models, which are pretrained on ImageNet.
- **Image Processing**: The input image is resized, cropped, and normalized to match the format expected by the pre-trained models.
- **Breed Prediction**: The classifier returns the breed of the dog present in the image.
- **Accuracy Evaluation**: The model is evaluated on its ability to correctly classify whether the image contains a dog and the specific breed.

## Setup

### Requirements

- Python 3.x
- PyTorch (1.7.0 or higher)
- torchvision
- PIL
- Other dependencies (listed in `requirements.txt`)

