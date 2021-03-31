import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]

plt.scatter(x_value, y_value, c=(0, 0, 0.5), edgecolors='none', s=40)
plt.title("我的散点图", fontsize=24)
plt.xlabel("VALUE", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
