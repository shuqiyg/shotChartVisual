import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_json('shotChartDetail22-23/1610612737/1627749.json')
right = df[df.SHOT_ZONE_AREA == "Right Side(R)"]
print(df)

sns.set_style("white")
sns.set_color_codes()
plt.figure(figsize=(15, 14))
plt.scatter(df.LOC_X, df.LOC_Y)
plt.scatter(right.LOC_X, right.LOC_Y)
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()
