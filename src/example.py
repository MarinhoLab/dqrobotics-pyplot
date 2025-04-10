from dqrobotics import *
from dqrobotics.robots import KukaLw4Robot
from dqrobotics.utils.DQ_Math import deg2rad

from dqrobotics_extensions.pyplot import *

from matplotlib import pyplot as plt

from math import sin, cos, pi

if __name__ == "__main__":
    plt.figure()
    plot_size = 1
    ax = plt.axes(projection='3d')
    ax.set_xlabel('$x$')
    ax.set_xlim((-plot_size, plot_size))
    ax.set_ylabel('$y$')
    ax.set_ylim((-plot_size, plot_size))
    ax.set_zlabel('$z$')
    ax.set_zlim((-plot_size, plot_size))

    # Draw a pose
    x_phi = pi/3
    r = cos(x_phi) + i_*sin(x_phi)
    x = r + 0.5*E_*(0.5*j_ + 0.45*k_)*r
    draw_pose(x, ax=ax)

    # Draw a line
    l = k_
    m = cross(0.5*i_ - 0.3*j_, l)
    l_dq = l + E_*m
    draw_line(l_dq, ax=ax, length=1.0)

    # Draw a manipulator
    q = deg2rad([0, 45, 0, -90, 0, -45, 0])
    robot = KukaLw4Robot.kinematics()
    draw_serial_manipulator(robot, q, ax=ax)

    plt.show()