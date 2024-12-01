import os
import torch
from torchvision import models, transforms
from PIL import Image

def classify_images(images_dir, results, model):
    """
    Uses a CNN model to classify pet images and adds the classifier label
    to the results dictionary.
    
    Parameters:
      images_dir - Path to the folder of pet images (string)
      results - Dictionary with key as image filename and value as a list. 
                The list contains:
                    [0] Pet image label (string)
                    [1] Classifier label (string, to be added by this function)
                    [2] Match indicator (int, to be added: 1 if match, 0 otherwise)
      model - Pre-trained CNN model architecture to use for classification (string)
              Supported models: 'resnet', 'alexnet', 'vgg'
    
    Returns:
      None - Updates the results dictionary in-place.
    """

    # Load the specified model based on the 'model' parameter
    if model == "resnet":
        cnn_model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    elif model == "alexnet":
        cnn_model = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
    elif model == "vgg":
        cnn_model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
    else:
        # Raise an error if an unsupported model is specified
        raise ValueError(f"Model {model} not supported. Use 'resnet', 'alexnet', or 'vgg'.")

    # Set the model to evaluation mode to avoid training behavior during inference
    cnn_model.eval()

    # Define the preprocessing pipeline to transform images into the format expected by the model
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize image to 224x224 pixels
        transforms.ToTensor(),  # Convert image to a tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Normalize using pre-defined mean
                             std=[0.229, 0.224, 0.225])   # Normalize using pre-defined std deviation
    ])

    # Iterate over all image filenames in the results dictionary
    for filename in results:
        # Ensure that each entry in the dictionary has the required structure
        if len(results[filename]) < 3:
            # Add placeholders if elements are missing
            results[filename] = ["Unknown", "Not Classified", 0]

        # Construct the full path to the image
        image_path = os.path.join(images_dir, filename)

        # Check if the file exists, otherwise handle the error
        if not os.path.exists(image_path):
            print(f"Error: File {image_path} does not exist.")
            results[filename][1] = "File not found"
            results[filename][2] = 0  # Set match indicator to 0 since the file is missing
            continue

        try:
            # Load the image and ensure it has an RGB color format
            image = Image.open(image_path).convert("RGB")

            # Preprocess the image for model input
            input_tensor = preprocess(image).unsqueeze(0)  # Add a batch dimension

            # Perform inference without calculating gradients to improve efficiency
            with torch.no_grad():
                outputs = cnn_model(input_tensor)

            # Determine the predicted class index
            _, predicted_class = outputs.max(1)
            classifier_label = str(predicted_class.item())  # Convert prediction to string

            # Update the results dictionary with the classifier label
            results[filename][1] = classifier_label

            # Compare the pet label and the classifier label (case-insensitive)
            pet_label = results[filename][0].lower().strip()
            classifier_label = classifier_label.lower().strip()
            results[filename][2] = 1 if pet_label in classifier_label else 0

        except Exception as e:
            # Handle any errors that occur during processing
            print(f"Error processing {filename}: {e}")
            results[filename][1] = "Error during classification"
            results[filename][2] = 0  # Set match indicator to 0 for errors
