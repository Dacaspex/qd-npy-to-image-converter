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

# Start image generation
start_time = current_milli_time()
for file in os.listdir('./data'):
    image_name = file.split('.')[0]
    print('Processing image: ', image_name)

    # Create output directory
    if not os.path.exists('output/' + image_name):
        os.makedirs('output/' + image_name)

    # Load data from file
    data = np.load('data/' + file)
    total_size = data.size

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
        image_output_path = 'output/' + image_name + '/' + image_name + '-' + str(i) + '.png'
        image.save(image_output_path)

total_elapsed_time = current_milli_time() - start_time
print('Finished in ', total_elapsed_time, 'ms')
