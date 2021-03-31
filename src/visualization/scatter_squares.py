import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.scatter(x_value, y_value, s=200)
plt.title("我的散点图", fontsize=24)
plt.xlabel("VALUE", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()
