from matplotlib import pyplot as plt
import numpy

gravity = 9.8
height = int(input("공 처음 높이 : "))
time = (10/49*height)**.5; velocity = 0; distance = 0
velocity_change = []; time_change = []; distance_change = []

i = 0
while(i <= time):
    time_change.append(i)
    velocity = gravity*i
    velocity_change.append(velocity)
    i += 0.00001

i = 0
while(i <= time):
    distance = 1/2*gravity*i**2
    distance_change.append(distance)
    i += 0.00001

print('공의 처음 높이 : %dm' % height)
print('땅에 떨어지는 시간 : %.15lfs' % time)
print('땅에 떨어질 시점 공의 속도 : %.15lfm/s' % velocity)

plt.subplot(2, 1, 1)
plt.plot(time_change, velocity_change)

plt.subplot(2, 1, 2)
plt.plot(time_change, distance_change)
plt.show()
