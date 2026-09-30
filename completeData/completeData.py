import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# ---------- 1. 采样参数 ----------
dt = 0.05              # 时间间隔 0.05s
duration = 100          # 信号时长（秒）
t = np.arange(0, duration, dt)

# ---------- 2. 三个频率成分叠加 ----------
f1, f2, f3 = 0.1, 0.15, 0.21
A1, A2, A3 = 1.0, 0.8, 0.5

signal = (A1 * np.sin(2 * np.pi * f1 * t)
          + A2 * np.sin(2 * np.pi * f2 * t)
          + A3 * np.sin(2 * np.pi * f3 * t))

# 构造 pandas 对象，时间作为索引
s = pd.Series(signal, index=pd.Index(t, name="time"), name="signal")
s_original = s.copy()          # 备份原始信号，用于绘图对比

# plt.plot(s['time'],s['signal'])

# ---------- 3. 随机删除 100 行 ----------
n_drop = 100
rng = np.random.default_rng(seed=42)   # 固定种子，结果可复现

# 用位置索引随机抽取要删除的行，避免浮点时间索引匹配问题
drop_pos = rng.choice(len(s), size=n_drop, replace=False)
drop_idx = s.index[drop_pos]

s_drop = s.drop(drop_idx)      # 删除后得到新对象，原 s 不变

print("原始数据点数:", len(s))
print("删除数据点数:", n_drop)
print("剩余数据点数:", len(s_drop))


print("===============================")

print("删除的时间点:")
del_list = []
for i in t:
    if i in drop_idx:
        del_list.append(i)
print(np.reshape(del_list, (-1, 10)))  # 每行显示 10 个时间点
print(f"删除的时间点总数: {len(del_list)}")

# 以NAN填充删除的时间点
s_drop.dropna(inplace=True)  # 删除缺失值
for t in del_list:
    s_drop.loc[t] = np.nan
s_index_complete = s_drop.sort_index()  # 按时间索引排序

# 方法一：线性插值补全
print("===============================")
print("补全数据 - 方法一：线性插值补全")
s_complete_1 = s_index_complete.interpolate(method='linear')

# 方法二：索引插值补全
print("===============================")
print("补全数据 - 方法二：索引插值补全")
s_complete_2 = s_index_complete.interpolate(method='index')

# 绘图对比
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
group = [s_original, s_drop, s_complete_1, s_complete_2]
title = ["Original Signal", "s_drop", "Method 1: linear interpolation", "Method 2: index interpolation"]
axes_flat = axes.flatten()
# 连线图
plt.figure()
for i, (series, ttl) in enumerate(zip(group, title)):
    series.plot(ax=axes_flat[i], title=ttl)
    axes_flat[i].scatter(series.index, series.values, color='red', s=5)  # 绘制散点
plt.tight_layout()

plt.show()