from mpl_toolkits.mplot3d import Axes3D  # 3D 그래프
import matplotlib.pyplot as plt  # 그래프
import numpy
import math

# 값 입력 및 물리량 계산
G = 9.8  # 중력 가속도
M = float(input('공의 질량(kg) : '))  # 공 질량 입력
H = float(input('공이 떨어지는 높이(M) : '))  # 낙하하는 높이 입력
P = float(input('공에 처음 가하는 충격량의 크기(kgm/s) : '))  # 공에 가하는 알짜힘 입력
Th = float(input('수직선과 이루는 각의 크기(0~180) : '))  # 각의 크기 입력
if(Th > 90):  # 만약 각도가 90도 보다 크면
    F_vertical = P*math.cos(math.radians(Th))  # 수직방향 힘 계산
    F_horizon = -P*math.sin(math.radians(Th))  # 수평방향 힘 계산
else:
    F_vertical = P*math.cos(math.radians(Th))  # 수직방향 힘 계산
    F_horizon = P*math.sin(math.radians(Th))  # 수평방향 힘 계산
v0_vertical = F_vertical/M  # 수직방향 처음 속도
v0_horizon = F_horizon/M  # 수평방향 처음 속도
T = (-v0_vertical+(2*G*H+v0_vertical**2)**.5)/G  # 낙하하는데 걸리는 시간 계산
v1_vertical = v0_vertical+G*T  # 최종 수직방향 속도 계산
v1_horizon = v0_horizon
speed0 = F/M  # 공의 처음 속력
speed1 = (v1_horizon**2+v1_vertical**2)**.5  # 최종 속력 계산

# 결과 출력
print('----------결과----------')
print('공의 질량 : %lf kg' % M)
print('공의 처음 높이 : %lf m' % H)
print('공에 처음 가한 충격량 : %lf N' % P)
print('힘을 가한 방향과 수직선이 이루는 각도 : %lf°' % Th)
print('수직 방향으로 가해진 힘 : %lf N' % F_vertical)
print('수평 방향으로 가해진 힘 : %lf N' % F_horizon)

print('공의 수평방향 이동거리 : %lf m' % (v0_horizon*T))
print('공의 최종 변위 : 시초선 기준 %.1lf°로 %lf m' %
      (270+Th, (H**2+(v0_horizon*T)**2)**.5))
print('땅에 떨어지는 시간 : %lf s' % T)
print('처음 공의 속력 : %lf m/s' % speed0)
print('최종 공의 속력 : %lf m/s' % speed1)
print('처음 수직방향 공의 속도 : %lf m/s' % v0_vertical)
print('처음 수평방향 공의 속도 : %lf m/s' % v0_horizon)
print('땅에 떨어질 시점 수직방향 공의 속도 : %lf m/s' % v1_vertical)
print('땅에 떨어질 시점 수평방향 공의 속도 : %lf m/s' % v1_horizon)
print('공이 땅에 닿을 시점의 운동량 : %lf kgm/s' % (M*speed1))

# 그래프 그리기
height_set = []
horizon_set = []
time_set = []
# 높이
H_ori = H
for time in numpy.arange(0, T, 0.01):
    H = H_ori-(v0_vertical*time+1/2*G*time**2)
    height_set.append(H)
# 시간
for time in numpy.arange(0, T, 0.01):
    time_set.append(time)
# 수평방향
horizon = v0_horizon
for time in numpy.arange(0, T, 0.01):
    horizon_set.append(v0_horizon*time)

fig = plt.figure(figsize=(7, 7))

ax0 = fig.add_subplot(221, projection='3d')
ax0.set_xlabel("X-horizon")
ax0.set_ylabel("Y-time")
ax0.set_zlabel("Z-vertical")
ax0.view_init(elev=30, azim=120)
ax0.plot(horizon_set, time_set, height_set)

ax1 = fig.add_subplot(222, projection='3d')
ax1.set_xlabel("X-horizon")
ax1.set_zlabel("Z-vertical")
ax1.view_init(elev=0, azim=270)
ax1.plot(horizon_set, time_set, height_set)

ax2 = fig.add_subplot(223, projection='3d')
ax2.set_xlabel("X-horizon")
ax2.set_ylabel("Y-time")
ax2.view_init(elev=90, azim=270)
ax2.plot(horizon_set, time_set, height_set)

ax3 = fig.add_subplot(224, projection='3d')
ax3.set_ylabel("Y-time")
ax3.set_zlabel("Z-vertical")
ax3.view_init(elev=0, azim=0)
ax3.plot(horizon_set, time_set, height_set)

plt.show()
