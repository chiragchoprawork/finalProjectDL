import os
import scipy.misc

# Set the root directory where your current images are stored
root = r'C:/Users/apoor/Desktop/p7images/images/images'

# Set the destination PATH where you want the resized images to be stored
PATH = r'D:/images64'

for subdir, dirs, files in os.walk(root):
    # Extract the relative path from the root to maintain the folder structure
    relative_path = os.path.relpath(subdir, root)
    # Use the relative path to construct the output directory path
    destination_subdir = os.path.join(PATH, relative_path)
    
    # Check if the destination subdirectory exists, if not, create it
    if not os.path.exists(destination_subdir):
        os.makedirs(destination_subdir)
    
    for i, f in enumerate(files):
        # Construct the full source file path
        source = os.path.join(subdir, f)
        # Print the processing file
        print(f"{i}: {source}")
        try:
            # Read the image using scipy.misc.imread
            image = scipy.misc.imread(source)
            # Resize the image using scipy.misc.imresize
            image_resized = scipy.misc.imresize(image, (64, 64))
            # Construct the full destination file path
            destination_file = os.path.join(destination_subdir, f"{i}.png")
            # Save the resized image using scipy.misc.imsave
            scipy.misc.imsave(destination_file, image_resized)
        except Exception as e:
            print(f"Failed to process {source}: {e}")
