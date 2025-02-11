from time import time, sleep
from print_functions_for_lab_checks import *  # For debugging and validation functions
from get_input_args import get_input_args  # To parse command-line arguments
from get_pet_labels import get_pet_labels  # To create pet image labels
from classify_images import classify_images  # For image classification
from adjust_results4_isadog import adjust_results4_isadog  # To adjust results
from calculates_results_stats import calculates_results_stats  # To calculate statistics
from print_results import print_results  # To display results

def main():
    start_time = time()

    # Parse command-line arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Create pet image labels
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Classify images
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # Adjust results for dog classification
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Calculate and check results statistics
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # Print final results
    print_results(results, results_stats, in_arg.arch, True, True)

    # Calculate and print total runtime
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600)}:{int((tot_time % 3600) // 60)}:{int(tot_time % 60)}")

if __name__ == "__main__":
    main()