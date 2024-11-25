import numpy as np
import matplotlib.pyplot as plt

# 定义智能体的初始位置和速度
# 领航者初始位置和速度
leader_position = np.array([0, 0], dtype=float)
leader_velocity = np.array([1, 0.5], dtype=float)

# 跟随者初始位置和速度
follower1_position = np.array([-1, -1], dtype=float)
follower1_velocity = np.array([0, 0], dtype=float)
follower2_position = np.array([-2, -2], dtype=float)
follower2_velocity = np.array([0, 0], dtype=float)

# 控制参数
k1 = 1.0  # 领航者影响力
k2 = 0.5  # 跟随者之间的影响力
k3 = 0.1  # 速度衰减系数

# 仿真时间和步长
time = 20  # 仿真总时间为20秒
dt = 0.1  # 时间步长为0.1秒
steps = int(time / dt)  # 总的仿真步数

# 记录位置变化
leader_positions = [leader_position.copy()]
follower1_positions = [follower1_position.copy()]
follower2_positions = [follower2_position.copy()]

# 仿真过程
for step in range(steps):
    # 更新领航者位置
    leader_position += leader_velocity * dt
    
    # 计算跟随者的控制输入
    # u_f1和u_f2是跟随者1和跟随者2的控制输入
    u_f1 = k1 * (leader_position - follower1_position) + k2 * (follower2_position - follower1_position) - k3 * follower1_velocity
    u_f2 = k1 * (leader_position - follower2_position) + k2 * (follower1_position - follower2_position) - k3 * follower2_velocity
    
    # 更新跟随者速度和位置
    follower1_velocity += u_f1 * dt
    follower1_position += follower1_velocity * dt
    follower2_velocity += u_f2 * dt
    follower2_position += follower2_velocity * dt
    
    # 记录位置
    leader_positions.append(leader_position.copy())
    follower1_positions.append(follower1_position.copy())
    follower2_positions.append(follower2_position.copy())

# 将位置记录转换为numpy数组，方便绘图
leader_positions = np.array(leader_positions)
follower1_positions = np.array(follower1_positions)
follower2_positions = np.array(follower2_positions)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(leader_positions[:, 0], leader_positions[:, 1], 'r-', label='Leader')
plt.plot(follower1_positions[:, 0], follower1_positions[:, 1], 'b--', label='Follower 1')
plt.plot(follower2_positions[:, 0], follower2_positions[:, 1], 'g-.', label='Follower 2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.title('Leader-Follower Formation')
plt.grid(True)
plt.show()
