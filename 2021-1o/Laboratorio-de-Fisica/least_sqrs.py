import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([9.2, 10.5, 14.8, 15.6, 19.6, 20.2])

# y = A . p
# y = (x, 1)(m, c)
A = np.vstack([x, np.ones(len(x))]).T

a, b = np.linalg.lstsq(A, y, rcond=None)[0]

print(f"a: {a} |b: {b}")

_ = plt.plot(x, a*x + b, 'r', label="Line")
_ = plt.plot(x, y, 'o', label="Original data", markersize=10)
_ = plt.legend()
plt.show()

