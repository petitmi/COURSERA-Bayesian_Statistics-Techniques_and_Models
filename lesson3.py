import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd
a, b = 5, 3
# draw dist and pdf
fig, ax = plt.subplots(1, 1)
x = np.linspace(stats.beta.ppf(0.01, a, b),
                stats.beta.ppf(0.99, a, b), 100)
ax.plot(x, stats.beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')
rv = stats.beta(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
r = stats.beta.rvs(a, b, size=10000)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.8)
ax.legend(loc='best', frameon=False)
plt.show()
#question5
A_q5=np.average(r/(1-r))
print(A_q5)
#question6
r_pd=pd.DataFrame(r)
A_q6=r_pd[r_pd>0.5].count()/r_pd.count()
print(A_q6)
#question7
A_q7=stats.norm().ppf(0.3)
print(A_q7)
