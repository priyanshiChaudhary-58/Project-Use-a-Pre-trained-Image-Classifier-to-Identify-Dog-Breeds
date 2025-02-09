def adjust_results4_isadog(results_dic, dogfile):
    dognames = set()
    with open(dogfile, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 
            
         
            parts = line.split(',')
            if len(parts) < 2:
                continue 
                
            breed = parts[1].strip().lower()
            dognames.add(breed)
    
    
    for key in results_dic:
        
        pet_label = results_dic[key][0].lower().strip()
        classifier_label = results_dic[key][1].lower().strip()
        
        
        classifier_labels = [label.strip() for label in classifier_label.split(',')]
        
        
        classifier_is_dog = 1 if any(label in dognames for label in classifier_labels) else 0
        
        
        pet_is_dog = 1 if pet_label in dognames else 0
        
        
        results_dic[key] += [pet_is_dog, classifier_is_dog]
    
    return results_dic