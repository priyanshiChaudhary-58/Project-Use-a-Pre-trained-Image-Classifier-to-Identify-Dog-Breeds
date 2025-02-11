from classifier import classifier
import os

def classify_images(images_dir, results, model):
    for filename in results:
        image_path = os.path.join(images_dir, filename)
        classifier_label = classifier(image_path, model).lower().strip()
        pet_label = results[filename][0].lower()                                                                      
        print(f"Image: {filename}")
        print(f"Pet Label: {pet_label} → Classifier Label: {classifier_label}\n")
        match = 1 if pet_label in classifier_label else 0
        results[filename] += [classifier_label, match]
        
    return results