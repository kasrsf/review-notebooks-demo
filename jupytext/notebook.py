# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np

# # Heading
#
# Some random text. Some random text. Some random text. Some random text. Some random text. Some random text. Some random text.Some random text. Some random text. Some random text. Some random text. Some random text. Some random text. Some random text. Some random text. Some random text.Some random text. Some random text. 

# +
# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
# -


print("i now print new stuff")
