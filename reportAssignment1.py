import matplotlib.pyplot as plt
import numpy as np

pythonResults = [1.430511474609375e-06, 7.152557373046875e-07, 3.814697265625e-06, 2.384185791015625e-07,
                 3.5762786865234375e-06, 5.9604644775390625e-06, 4.291534423828125e-06, 0.0006015300750732422,
                 0.002644777297973633, 0.002644777297973633, 2.6702880859375e-05, 0.0005764961242675781,
                 0.002252340316772461, 2.384185791015625e-07, 2.384185791015625e-07]

numpyResults = [7.3909759521484375e-06, 4.267692565917969e-05, 5.650520324707031e-05, 6.604194641113281e-05,
                0.0003719329833984375, 0.000518798828125, 0.0006313323974609375, 0.0015146732330322266,
                0.004233837127685547, 0.004888772964477539, 0.0050160884857177734, 0.00595402717590332,
                0.00827932357788086, 0.009897708892822266, 0.010218620300292969]

barWidth = 0.2
opacity = 0.4

index = np.arange(15) + 1

plt.bar(index - 0.1, pythonResults, barWidth, alpha=opacity, color='r', label='python')
plt.bar(index + 0.1, numpyResults, barWidth, alpha=opacity, color='g', label='numpy')

plt.yscale('symlog')

# ax.yaxis.set_ticks(np.arange(min(npy), max(npy)*0.02, 0.02))


plt.ylabel('Running time in seconds')

plt.title("Running time comparison between python and numpy")
plt.legend()

plt.show()
