import collections

import cv2
import numpy as np
import requests
from PIL import Image

BACKEND_URL = "http://127.0.0.1:8000"

THRESHOLD = 0.3

img = Image.open("test.jpg")
# Resize or crop to 300 x 300
img = img.resize((300, 300), Image.ANTIALIAS)
img.save("img2.jpg")

input_img = cv2.imread("img2.jpg")
mean = np.array([104, 117, 124], dtype='float32')[:, np.newaxis, np.newaxis]
# Switch axis to [channel, height, width]
img = np.swapaxes(img, 1, 2)
img = np.swapaxes(img, 1, 0)
# Minus mean
img = (img - mean).flatten()
req = {"image": img.tolist()}

# Request to restful server
req = requests.request("POST", url=BACKEND_URL, json=req)
result = np.array(req.json()['data'], dtype='float32')

# Only keep result which confidence > THRESHOLD
keep_inds = np.where(result[:, 2] >= THRESHOLD)[0]
results = []

# Only keep one result for each label
results = collections.defaultdict(list)
for idx in keep_inds:
    results[result[idx][1] + 1].append((result[idx][2],
                                        result[idx][3], result[idx][4],
                                        result[idx][5],
                                        result[idx][6]))

for label in results:
    result = results[label]
    result.sort(reverse=True)
    # Print result in command line
    print label, result[0]
    result = result[0]

    xmin = int(result[1] * 300)
    ymin = int(result[2] * 300)
    xmax = int(result[3] * 300)
    ymax = int(result[4] * 300)

    cv2.rectangle(input_img, (xmin, ymin), (xmax, ymax),
                  (0, (1 - xmin) * 255, xmin * 255), 2)

# Print to image
cv2.imwrite('result.jpg', input_img)
