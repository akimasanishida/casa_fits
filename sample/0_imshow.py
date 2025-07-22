import sys

sys.path.append(".")
from casa_fits import load_image, imshow
import matplotlib.pyplot as plt


img = load_image("./example.image.pbcor", width=128, height=128)
fig, ax = plt.subplots(figsize=(6, 4))
imshow(ax, img, title="TWHya Continuum")
fig.tight_layout()
fig.savefig("0_imshow.png", dpi=300)
plt.show()