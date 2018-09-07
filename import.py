import numpy as np
import time
from PIL import Image

# Variable setup
current_milli_time = lambda: int(round(time.time() * 1000))
console_output_interval = 4
start_time = 0
image_limit = 10000

# Load data from file
data = np.load('data/alarm_clock.npy')
total_size = data.size

# Start image generation
start_time = current_milli_time()
for i in range(image_limit):
    if i % console_output_interval == 0:
        progress = int(round((i / image_limit) * 100))
        elapsed_time = current_milli_time() - start_time
        print('Processing image: ', i, ' (', progress, '%) time: ', elapsed_time, 'ms')
    image_data = data[i].reshape(28, 28)
    image = Image.fromarray(image_data)
    image_output_path = 'output/alarm-clock-' + str(i) + '.png'
    image.save(image_output_path)

total_elapsed_time = current_milli_time() - start_time
print('Finished in ', total_elapsed_time, 'ms')
