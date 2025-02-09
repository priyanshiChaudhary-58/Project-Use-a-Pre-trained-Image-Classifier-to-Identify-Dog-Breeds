def check_classifying_images(results_dic):
    """
    Prints Pet Image Label and Classifier Label for matches and mismatches,
    and ensures the results dictionary has the correct structure.

    Parameters:
        results_dic - Dictionary with the results of classification. 
                      Key is the filename, and value is a list containing:
                      [0] Pet image label (string)
                      [1] Classifier label (string)
                      [2] Match indicator (int, 1 for match, 0 for mismatch)

    Returns:
        None - Prints the details of matches and mismatches.
    """
    if results_dic is None:
        print("* Results Dictionary not checked because 'classify_images' isn't defined.")
        return

    n_match = 0
    n_notmatch = 0

    print("\nMATCHES:")
    for key, value in results_dic.items():
        if len(value) < 3:
            print(f"Error: {key} does not have the expected structure. Current value: {value}")
            while len(value) < 3:
                value.append(None)

       
        if value[2] == 1:
            n_match += 1
            print(f"{key}: Real: {value[0]}  Classifier: {value[1]}")

    print("\nNOT MATCHES:")
    for key, value in results_dic.items():
        if value[2] == 0:
            n_notmatch += 1
            print(f"{key}: Real: {value[0]}  Classifier: {value[1]}")

    
    print(f"\nTotal Images: {n_match + n_notmatch}, Matches: {n_match}, Not Matches: {n_notmatch}")


def check_creating_pet_image_labels(results_dic):
    """
    Verifies the correctness of pet image labels by checking the structure
    of the results dictionary and printing its contents.

    Parameters:
        results_dic - Dictionary with the pet image labels. 
                      Key is the filename, and value is a list containing:
                      [0] Pet image label (string)

    Returns:
        None - Prints the filenames and their corresponding pet image labels.
    """
    if results_dic is None:
        print("* Results Dictionary not checked because 'get_pet_labels' isn't defined.")
        return

    print("\nChecking Pet Image Labels:")
    for key, value in results_dic.items():
        if len(value) != 1:
            print(f"Error: {key} does not have the expected label structure. Current value: {value}")
        else:
            print(f"Filename: {key} -> Label: {value[0]}")

    # Print total number of images checked
    print(f"\nTotal Images: {len(results_dic)}")
