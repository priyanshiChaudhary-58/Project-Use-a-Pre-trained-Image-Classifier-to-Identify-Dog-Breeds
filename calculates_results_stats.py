def calculates_results_stats(results_dic):
    """
    Calculates statistics of the classification results and organizes them into a 
    dictionary for easy analysis.

    Parameters:
        results_dic - Dictionary where:
                      Key: Image filename (string)
                      Value: List containing:
                        [0]: Pet image label (string)
                        [1]: Classifier label (string)
                        [2]: Match indicator (1 if labels match, 0 otherwise)
                        [3]: Dog indicator (1 if pet image is a dog, 0 otherwise)
                        [4]: Classifier dog indicator (1 if classifier predicts a dog, 0 otherwise)

    Returns:
        results_stats_dic - Dictionary containing computed statistics:
                            Count keys start with 'n', percentages with 'pct'.
    """
    # Initialize the stats dictionary with counts
    results_stats_dic = {
        'n_dogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }

    # Process each image's results in the dictionary
    for key in results_dic:
        # Count label matches
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Count dog images and related stats
        if results_dic[key][3] == 1:  # Pet image is a dog
            results_stats_dic['n_dogs_img'] += 1

            # Count correctly classified breeds
            if results_dic[key][2] == 1:  # Labels match
                results_stats_dic['n_correct_breed'] += 1

            # Count correctly classified dogs
            if results_dic[key][4] == 1:  # Classifier predicts dog
                results_stats_dic['n_correct_dogs'] += 1

        # Count correctly classified non-dogs
        else:  # Pet image is NOT a dog
            if results_dic[key][4] == 0:  # Classifier predicts NOT a dog
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate overall image counts
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (
        (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0 
        if results_stats_dic['n_dogs_img'] > 0 else 0.0
    )
    results_stats_dic['pct_correct_breed'] = (
        (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0 
        if results_stats_dic['n_dogs_img'] > 0 else 0.0
    )
    results_stats_dic['pct_correct_notdogs'] = (
        (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0 
        if results_stats_dic['n_notdogs_img'] > 0 else 0.0
    )

    return results_stats_dic
