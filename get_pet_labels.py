from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    filenames = listdir(image_dir)
    breed_corrections = {
        "lebrador": "labrador" 
    }
    
    for filename in filenames:
        if filename.startswith('.'):
            continue  
        
        
        name_without_ext = filename.split('.')[0].lower()  
        parts = name_without_ext.split('_')  
        
        if parts and parts[-1].isdigit():
            breed_parts = parts[:-1]  
        else:
            breed_parts = parts  
        
        breed = ' '.join(breed_parts)  
        
        
        breed = breed_corrections.get(breed, breed)
        
        results_dic[filename] = [breed]
    
    return results_dic