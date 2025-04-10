from dqrobotics import *
from dqrobotics.robots import KukaLw4Robot
from dqrobotics.utils.DQ_Math import deg2rad

from dqrobotics_extensions.pyplot import plot

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
    x = r + 0.5 * E_ * (0.5 * j_ + 0.45 * k_) * r
    plot(x)

    # Draw a line
    l = k_
    m = cross(-0.3 * j_, l)
    l_dq = l + E_*m
    plot(l_dq, line=True, scale=1)

    # Draw a plane
    n_pi = i_
    d_pi = 0.1
    pi_dq = n_pi + E_*d_pi
    plot(pi_dq, plane=True, scale=1)

    # Draw a manipulator
    q = deg2rad([0, 45, 0, -90, 0, -45, 0])
    robot = KukaLw4Robot.kinematics()
    plot(robot, q=q)

    plt.show()