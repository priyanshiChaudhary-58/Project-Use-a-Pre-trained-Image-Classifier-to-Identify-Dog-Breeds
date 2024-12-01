from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary with filenames as keys and pet image labels as values.
    Parameters:
      image_dir (str): Directory containing the pet images.
    Returns:
      dict: Dictionary with 'key' as image filename and 'value' as a list containing the pet image label.
    """
    # Retrieve the filenames from the directory
    filename_list = listdir(image_dir)
    
    # Initialize an empty dictionary
    results_dic = {}

    # Process each file in the directory
    for filename in filename_list:
        # Skip hidden files (e.g., .DS_Store)
        if filename.startswith('.'):
            continue
        
        # Convert filename to lowercase and split by underscores
        pet_name = ""
        word_list = filename.lower().split("_")

        # Process each word to create the pet label
        for word in word_list:
            if word.isalpha():  # Add only alphabetic words
                pet_name += word + " "
        
        # Strip leading and trailing whitespace from pet_name
        pet_name = pet_name.strip()

        # Add to results dictionary (warn if duplicate key is found)
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print(f"** Warning: Duplicate filename found: {filename}")

    return results_dic
