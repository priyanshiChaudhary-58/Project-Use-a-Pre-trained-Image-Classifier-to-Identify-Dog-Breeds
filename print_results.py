def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results of the classification and, optionally, incorrectly 
    classified dogs and breeds.

    Parameters:
        results_dic - Dictionary with key as image filename and value as a list:
                      [0]: Pet image label (string)
                      [1]: Classifier label (string)
                      [2]: Match indicator (int, 1 if labels match, 0 otherwise)
                      [3]: Dog indicator (int, 1 if pet image is a dog, 0 otherwise)
                      [4]: Classifier dog indicator (int, 1 if classifier label is a dog, 0 otherwise)
        results_stats_dic - Dictionary containing classification statistics:
                            Keys start with 'n' for counts or 'pct' for percentages.
        model - CNN model architecture used for classification (string).
        print_incorrect_dogs - Boolean, if True, prints misclassified dogs and non-dogs.
        print_incorrect_breed - Boolean, if True, prints misclassified dog breeds.

    Returns:
        None - Prints the results.
    """
    # summary of the classification results
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    
    # Print percentage statistics
    print("\nPercentage Statistics:")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:.2f}%".format(key, results_stats_dic[key]))

    # Print misclassified dog and non-dog cases if enabled
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']:
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            # Dog mislabeled as non-dog or vice versa
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:  # Dog -> Non-Dog
                print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")
            elif results_dic[key][3] == 0 and results_dic[key][4] == 1:  # Non-Dog -> Dog
                print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")

    # Print misclassified breeds if enabled
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            # Correctly identified as dog but wrong breed
            if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0:
                print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")
