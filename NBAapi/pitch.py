# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors

# # color-map
# cmap = ["#222222", "#3A2527", "#52282B", "#6A2B30", "#762C32", "#822D34",
#         "#8E2F37", "#9A3039", "#B2323D", "#BE3440", "#CA3542", "#E13746"]
# cmap = matplotlib.colors.ListedColormap(cmap)

# # prepare data
# np.random.seed(10)
# shotsX = np.random.randn(1000)*20+10
# shotsY = np.random.randn(1000)*15+50

# # original plot
# cfg = dict(x=shotsX, y=shotsY, cmap=cmap, gridsize=22, extent=[0, 100, 0, 100])
# h = plt.hexbin(ec="#222222", lw=2, zorder=-3, **cfg)
# plt.axis('off')

# # draw thick white contours + overlay previous style
# cfg = {**cfg, 'vmin': h.get_clim()[0], 'vmax': h.get_clim()[1]}
# plt.hexbin(ec="white", lw=5, zorder=-2, mincnt=10, **cfg)
# plt.hexbin(ec="#222222", lw=2, zorder=-1, mincnt=10, **cfg)
# plt.xlim(-3, 103)  # required as second call of plt.hexbin()
# plt.ylim(-3, 103)  # strangely affects the limits ...

# plt.show()
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Fetch the image from a URL
url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/1628389.png'
response = requests.get(url)

# Read the image data using PIL
image_data = Image.open(BytesIO(response.content))

# Create a figure and axes
fig, ax = plt.subplots()

# Display the image using imshow()
ax.imshow(image_data)

# Show the plot
plt.show()
