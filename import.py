import numpy as np
import time
import sys
import os
from PIL import Image

# Variable setup
current_milli_time = lambda: int(round(time.time() * 1000))
console_output_interval = 10
start_time = 0
image_limit = 100
training_split = 0.95

# Get command line arguments, if present
if len(sys.argv) == 2:
    image_limit = int(sys.argv[1])
elif len(sys.argv) == 3:
    image_limit = int(sys.argv[1])
    training_split = float(sys.argv[2])

# Start image generation
start_time = current_milli_time()
for file in os.listdir('./data'):
    # Process image name
    image_name = file.split('.')[0]
    if 'full%2Fnumpy_bitmap%2F' in image_name:
        image_name = image_name[22:].replace(' ', '_')
    print('Processing image: ', image_name)

    # Create output directories
    if not os.path.exists('output/training/' + image_name):
        os.makedirs('output/training/' + image_name)
    if not os.path.exists('output/validation/' + image_name):
        os.makedirs('output/validation/' + image_name)

    # Load data from file
    data = np.load('data/' + file)
    total_size = data.size

    if total_size < image_limit or image_limit == -1:
        image_limit = total_size

    # Loop over the array
    for i in range(image_limit):
        # Console output
        if i % console_output_interval == 0:
            progress = int(round((i / image_limit) * 100))
            elapsed_time = current_milli_time() - start_time
            print('Progress: ', i, ' (', progress, '%) time: ', elapsed_time, 'ms')

        # Create image
        image_data = data[i].reshape(28, 28)
        image = Image.fromarray(image_data)

        # Determine training or validation folder
        folder = ''
        if i >= image_limit * training_split:
            folder = 'validation/'
        else:
            folder = 'training/'

        # Save image
        image_output_path = 'output/' + folder + image_name + '/' + image_name + '-' + str(i) + '.png'
        image.save(image_output_path)

total_elapsed_time = current_milli_time() - start_time
print('Finished in ', total_elapsed_time, 'ms')
