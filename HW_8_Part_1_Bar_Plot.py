#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['EO', 'SAR', 'HSI', 'IR', 'AIS']
us_means = [10, 4, 2, 5, 3]
forg_means = [5, 12, 3, 2, 7]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, us_means, width, label='US')
rects2 = ax.bar(x + width/2, forg_means, width, label='Foregin')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Constellations')
ax.set_title('Number by owner and sensor')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


# In[ ]:




