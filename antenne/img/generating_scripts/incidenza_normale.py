#!/usr/bin/python3
# %matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'

h = 0.5
l = 0.6

# figura dell'incidenza normale
fig_normale = plt.figure(frameon=False, figsize=(3, 2))
ax = fig_normale.gca()
ax.set_axis_off()

ax.add_patch(
	patches.Rectangle(
		xy=(0, 0),
		width=l,
		height=h,
		color='black',
		alpha=0.25,
		edgecolor=None) )

ax.add_patch(
	patches.Rectangle(
		xy=(0, h),
		width=l,
		height=h,
		color='black',
		alpha=0.1,
		edgecolor=None) )

ax.plot([0, l], [h, h], linestyle='--', color='black', linewidth=1)

ax.plot([0, l], [h, h],
	linestyle='-',
	color='green',
	linewidth=2,
	alpha=0.5)

num1 = 3
lambda1 = h / num1
for i in range(1, num1):
	ax.plot([0, l], [i * lambda1, i * lambda1],
		linestyle='-',
		color='green',
		linewidth=2,
		alpha=0.4)

num2 = 4
lambda2 = h / num2
for i in range(1, num2):
	ax.plot([0, l], [h + i * lambda2, h + i * lambda2],
		linestyle='-',
		color='green',
		linewidth=2,
		alpha=0.4)

# draw k1 vector
ax.arrow(l/3, 1/2 * lambda1, 0, (num1 - 1) * lambda1 - 0.05,
	head_width=0.01,
	head_length=0.05,
	facecolor='black',
	edgecolor='black')
plt.text(l/3 + 0.01, lambda1 + 0.05, r'$\vec{k_1}$', fontdict={'size': 14})

# draw lambda1 sign
plt.annotate(
    '', (3/5*l, lambda1), (3/5*l, 2*lambda1),
    arrowprops={'arrowstyle': '<->'})

plt.text(3/5*l + 0.01, lambda1*1.25, r'$\lambda_1$', fontdict={'size': 14})

# draw k2 vector
ax.arrow(l/3, h + 1/2 * lambda2, 0, (num2 - 1) * lambda2 - 0.05,
	head_width=0.01,
	head_length=0.05,
	facecolor='black',
	edgecolor='black')
plt.text(l/3 + 0.01, h + lambda2 + 0.02, r'$\vec{k_2}$',
	fontdict={'size': 14})

plt.text(l - 0.15, h + 0.03, 'Mezzo 1',
	fontdict={'size': 12})

plt.text(l - 0.15, h - 0.1, 'Mezzo 2',
	fontdict={'size': 12})

# draw lambda2
plt.annotate(
    '', (3/5*l, h + lambda2), (3/5*l, h + 2*lambda2),
    arrowprops={'arrowstyle': '<->'})

plt.text(3/5*l + 0.01, h + lambda2*1.25, r'$\lambda_2$', fontdict={'size': 14})

ax.set_xlim([0, l])
ax.set_ylim([0, 2*h])

plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
plt.savefig('../incidenza_normale.pgf',
	format='pgf',
	bbox_inches='tight',
	pad_inches=0)
plt.show()
