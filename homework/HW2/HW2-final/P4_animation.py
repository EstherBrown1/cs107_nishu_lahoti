import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

# Closure definition

def clock_hand(r):

  def angle(t):
    t *= (np.pi / 180)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return (x, y)
  
  return angle

fig = plt.figure(figsize=(6,6))

# Setting while loop
i = 0
while i < 100:
    
    plt.cla()

    # Current date and time
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second

    # Calculate theta in degrees for each hand

    t_h = 90 - (30*hour) - (minute / 2)
    t_m = 90 - (6*minute)
    t_s = 90 - (6*second)

    # Specify the length of hour, minute, and second hands

    h_length = 1
    m_length = 2
    s_length = 3

    # hour_hand = name_of_closure(length_of_hour_hand)

    hour_hand = clock_hand(h_length)
    minute_hand = clock_hand(m_length)
    second_hand = clock_hand(s_length)

    # x_hour, y_hour = hour_hand(theta_hour)

    x_hour, y_hour = hour_hand(t_h)
    x_minute, y_minute = minute_hand(t_m)
    x_second, y_second = second_hand(t_s)

    # Plot the clock

    pts = [[x_hour, y_hour], 
        [x_minute, y_minute],
        [x_second, y_second]]

    arr = np.array(pts)
    plt.plot([np.zeros(3), arr[:, 0]], [np.zeros(3), arr[:, 1]])
    plt.axis([-4, 4, -4, 4])

    fig.canvas.draw()
    plt.pause(0.1)

    i +=1