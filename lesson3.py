import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
#  question5
a=5
b=3
fig, ax = plt.subplots(1, 1)
# Generate samples
r = beta.rvs(a, b, size=10000)
r_mean=np.average(r)
odds=r_mean/(1-r_mean)
print('odds: %.1f' % odds)
ax.hist(r, density=True, histtype='stepfilled',bins=100, alpha=0.6)
ax.legend(loc='best', frameon=False)
x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
ax.plot(x, beta.pdf(x, a, b),
        lw=5, alpha=0.6, label='beta pdf')
plt.show()