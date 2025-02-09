from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    filenames = listdir(image_dir)
    breed_corrections = {
        "lebrador": "labrador"  # Add other corrections as needed
    }
    for filename in filenames:
        if filename.startswith('.'): continue
        
        # Extract breed name and correct typos
        name_without_ext = filename.split('.')[0].lower()
        breed = ' '.join(name_without_ext.split('_'))
        breed = breed_corrections.get(breed, breed)  # Apply corrections
        
        results_dic[filename] = [breed]
    return results_dic
