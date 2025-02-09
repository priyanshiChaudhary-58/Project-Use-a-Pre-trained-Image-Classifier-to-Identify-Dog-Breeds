from time import time
from os.path import join
from print_functions_for_lab_checks import *  # For debugging and validation functions
from get_input_args import get_input_args  #  to parse command-line arguments
from get_pet_labels import get_pet_labels  # to create pet image labels
from classify_images import classify_images  # for image classification
from adjust_results4_isadog import adjust_results4_isadog  #  to adjust results
from calculates_results_stats import calculates_results_stats  #  to calculate statistics
from print_results import print_results  #  to display results
from classifier import classifier  # Import the classifier function

def main():
    start_time = time()

    
    in_arg = get_input_args()

    
    results = get_pet_labels(in_arg.dir)

    
    classify_images(in_arg.dir, results, in_arg.arch)

   
    adjust_results4_isadog(results, in_arg.dogfile)

    
    results_stats = calculates_results_stats(results)

    
    print_results(results, results_stats, in_arg.arch, True, True)

    
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600)}:{int((tot_time % 3600) // 60)}:{int(tot_time % 60)}")


if __name__ == "__main__":
    main()
