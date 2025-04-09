from PIL import Image
import os
import numpy as np

paths = [
    'archive/test-20250112T065939Z-001/test/real',
    'archive/test-20250112T065939Z-001/test/fake',
    'archive/train-20250112T065955Z-001/train/real',
    'archive/train-20250112T065955Z-001/train/fake'
]

counts = np.zeros(len(paths))
avg_width = 0
avg_height = 0

for i, path in enumerate(paths):
    print(path)
    for dirpath, dnames, fnames in os.walk(path):
        for fname in fnames:
            img = Image.open("%s/%s" % (dirpath, fname))
            width, height = img.size
            avg_width += width
            avg_height += height
            counts[i] += 1

n = np.sum(counts)
print("\ncounts = %s, total = " % counts, n)
print("avg width = %s, avg height = %s" % (avg_width / n, avg_height / n))


