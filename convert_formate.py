import os
from PIL import Image

# Set the path to the folder containing the images
folder_path = 'static\images'

# Iterate over all files in the directory
for filename in os.listdir(folder_path):
    # Build the full path to the image
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is an image (based on extension or some other method)
    if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.gif', '.bmp', '.tiff', '.jpeg', '.webp')):
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Create a new filename with the .jpg extension
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Convert the image to RGB (necessary for saving as JPG)
                img = img.convert('RGB')
                
                # Save the image as JPEG
                img.save(new_file_path, 'JPEG')

                # Optionally, you can remove the original file if needed
                # os.remove(file_path)
                
                print(f"Converted '{filename}' to '{new_filename}'")
        
        except Exception as e:
            print(f"Failed to convert '{filename}': {e}")
