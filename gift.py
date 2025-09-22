import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

filenames = ['image1.jpeg', 'image2.jpeg']

desktop_path = os.path.expanduser("~/Desktop")

images = []
base_size = None

for fn in filenames:
    img_path = os.path.join(desktop_path, fn)
    img = Image.open(img_path)

    if base_size is None:
        base_size = (800, int(800 * img.height / img.width))

    img = img.resize(base_size)
    images.append(np.array(img))

output_file = os.path.join(desktop_path, "movie.gif")
iio.imwrite(output_file, images, loop=0, duration=2.5)
print(f"Saved GIF as {output_file}")
