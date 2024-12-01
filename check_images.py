from time import time
from os.path import join
from print_functions_for_lab_checks import *  # For debugging and validation functions
from get_input_args import get_input_args  # Import function to parse command-line arguments
from get_pet_labels import get_pet_labels  # Import function to create pet image labels
from classify_images import classify_images  # Import function for image classification
from adjust_results4_isadog import adjust_results4_isadog  # Import function to adjust results
from calculates_results_stats import calculates_results_stats  # Import function to calculate statistics
from print_results import print_results  # Import function to display results
from classifier import classifier  # Import the classifier function

def main():
    """
    Main function to orchestrate the image classification workflow.
    It handles the following:
    1. Parses command-line arguments.
    2. Processes pet images to create labels.
    3. Classifies images and adjusts results for dog identification.
    4. Calculates performance statistics and prints results.
    """

    # Record the start time for runtime calculation
    start_time = time()

    # Step 1: Retrieve command-line arguments
    in_arg = get_input_args()

    # Debugging Step: Print the retrieved arguments for verification
    print("\n** Command-line Arguments:")
    print(f"Image Folder: {in_arg.dir}")
    print(f"Model Architecture: {in_arg.arch}")
    print(f"Dognames File: {in_arg.dogfile}")

    # Step 2: Generate pet image labels and store in a dictionary
    results = get_pet_labels(in_arg.dir)

    # Debugging Step: Verify the results dictionary structure
    print("\n** Results after creating pet image labels:")
    check_creating_pet_image_labels(results)

    # Step 3: Classify the images using the specified model architecture
    classify_images(in_arg.dir, results, in_arg.arch)

    # Debugging Step: Check results after image classification
    print("\n** Results after image classification:")
    check_classifying_images(results)

    # Step 4: Adjust results to determine if images represent dogs or not
    adjust_results4_isadog(results, in_arg.dogfile)

    # Debugging Step: Check results after adjusting for 'is-a-dog' labels
    print("\n** Results after adjusting for is-a-dog labels:")
    check_classifying_labels_as_dogs(results)

    # Step 5: Calculate performance statistics for the classifier
    results_stats = calculates_results_stats(results)

    # Debugging Step: Verify the calculated statistics
    print("\n** Results statistics:")
    check_calculating_results(results, results_stats)

    # Step 6: Print final classification results and statistics
    print_results(results, results_stats, in_arg.arch, True, True)

    # Record the end time for runtime calculation
    end_time = time()

    # Calculate total runtime of the program in seconds
    tot_time = end_time - start_time

    # Convert runtime into hh:mm:ss format and display it
    print("\n** Total Elapsed Runtime: ",
          str(int(tot_time // 3600)) + ":" + 
          str(int((tot_time % 3600) // 60)) + ":" + 
          str(int(tot_time % 60)))

# Ensures the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
