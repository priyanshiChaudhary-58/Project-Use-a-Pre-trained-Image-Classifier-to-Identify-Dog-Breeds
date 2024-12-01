import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command-line arguments provided by the user.
    Command-line arguments:
      --dir: Path to the folder of pet images (default: 'pet_images/')
      --arch: CNN model architecture to use (default: 'resnet')
      --dogfile: Text file containing dognames (default: 'dognames.txt')
    
    Returns:
      argparse.Namespace: Parsed arguments
    """
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Process command-line arguments for the pet classifier.")

    # Add arguments
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to the folder of pet images (default: pet_images/)')
    parser.add_argument('--arch', type=str, default='resnet', 
                        help="CNN model architecture to use (default: 'resnet')")
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help="Text file containing dognames (default: 'dognames.txt')")

    # Parse and return arguments
    return parser.parse_args()
