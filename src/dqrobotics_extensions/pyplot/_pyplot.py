"""
Copyright (C) 2025 Murilo Marques Marinho (www.murilomarinho.info)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Auhor: Murilo M. Marinho
"""
from dqrobotics import *
from dqrobotics.robot_modeling import DQ_SerialManipulator

from matplotlib import pyplot as plt

import numpy as np

from math import acos, sin, cos

def plot(obj, **kwargs):
    """
    An aggregator for all plot functions related to dqrobotics. Currently, supports
    - DQ
    - DQ_SerialManipulator

    Before this can be used, please remember to initialise the plt Axes. Example
        plt.figure()
        ax = plt.axes(projection='3d')
        plot(i_)
        plt.show()

    Plotting a unit dq "x":
        plot(x)
    Plotting a line dq "l_dq":
        plot(l_dq, line=True)
    Plotting a plane dq "pi_dq":
        plot(pi_dq, plane=True)
    Plotting a DQ_SerialManipulator "robot" at joint configurations q:
        plot(robot, q=q)

    :param obj: the input to be plotted.
    :param kwargs: arguments depending on type of plot you need, see the description above.
    :return: Nothing.
    """
    if isinstance(obj,DQ):
        if kwargs is None:
            _plotdq(dq=obj)
        else:
            _plotdq(obj, **kwargs)
    elif isinstance(obj,DQ_SerialManipulator):
        _draw_serial_manipulator(obj, **kwargs)
    else:
        raise RuntimeError(f"plot not implemented yet for {obj}")

def _plotdq(dq : DQ,
            scale: float = 0.1,
            name = None,
            line = None,
            plane = None,
            color = 'r',
            ax = None
            ):
    """
    Implementing the pyplot valid options of
    https://github.com/dqrobotics/matlab/blob/master/%40DQ/plot.m
    the particular plotting functions did not inherit from these implementations and are an informed attempt of using
    DQ operators to plot the objects.

    :param dq: the input DQ.
    :param scale: if not None, defines the size of the frame.
    :param name: if not None, defines the name of the frame.
    :param line: if not None, draw the input DQ as a line. Use a suitable 'linespec', that is, for instance 'r-' and.
    :param plane: if not None, draw the input DQ as a plane.
    :param color: Define color of the frame, line, or plane.
    :return: Nothing.
    """
    if line is not None:
        draw_line(l_dq=dq,
                  linespec=color,
                  length=scale,
                  ax=ax)
    elif plane is not None:
        _draw_plane(pi_dq=dq,
                    length_x=scale,
                    length_y=scale,
                    ax=ax)
    else:
        _draw_pose(x=dq,
                   length=scale,
                   ax=ax)


def _dq_ajoint_grid(x: DQ, x_grid, y_grid, z_grid):
    if x_grid.shape != y_grid.shape or x_grid.shape != z_grid.shape:
        raise RuntimeError("Shapes of arguments must be the same.")

    shape = x_grid.shape
    rows, cols = shape

    x_grid_ad = np.zeros(shape)
    y_grid_ad = np.zeros(shape)
    z_grid_ad = np.zeros(shape)

    for i in range(0, rows):
        for j in range(0, cols):
            x_element = x_grid[i, j]
            y_element = y_grid[i, j]
            z_element = z_grid[i, j]

            p = DQ([x_element, y_element, z_element])
            p_prime = _dq_adjoint(x, p)

            x_grid_ad[i, j] = p_prime.q[1]
            y_grid_ad[i, j] = p_prime.q[2]
            z_grid_ad[i, j] = p_prime.q[3]

    return x_grid_ad, y_grid_ad, z_grid_ad


def _draw_cylinder(x,
                   height_z: float,
                   radius: float,
                   param_dict: dict,
                   ax=None):
    """
    Internal method to draw a cylinder. x is a unit dual quaternion that defines the centre of the cilinder. The cylinder
    will span from -height_z/2 to +height_z/2. Use param_dict to define anything to be passed on to plot_surface.
    :param x: a unit dual quaternion representing the pose of the centre of the cylinder.
    :param height_z: the height of the cylinder.
    :param radius: the radius of the cylinder.
    :param param_dict: the parameter dictionary to be passed on to plot_surface.
    :param ax: Figure Axes or plt.gca() if None.
    :return: nothing
    """
    if not is_unit(x):
        raise RuntimeError("The argument x must be a unit dual quaternion.")
    # https://stackoverflow.com/questions/26989131/add-cylinder-to-plot
    # I modified the code above to use dual quaternion algebra.
    if ax is None:
        ax = plt.gca()

    # Cylindrical points start at zero
    z = np.linspace(-height_z / 2.0, height_z / 2.0, 20)  # Draw half the cylinder
    theta = np.linspace(0, 2 * np.pi, 20)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)

    x_grid_ad, y_grid_ad, z_grid_ad = _dq_ajoint_grid(x, x_grid, y_grid, z_grid)

    ax.plot_surface(x_grid_ad,
                    y_grid_ad,
                    z_grid_ad,
                    **param_dict)

def _draw_plane(pi_dq,
                length_x: float,
                length_y: float,
                ax=None):

    if not is_plane(pi_dq):
        raise RuntimeError(f"The input pi_dq = {pi_dq} is not a line.")
    # https://stackoverflow.com/questions/26989131/add-cylinder-to-plot
    # I modified the code above to use dual quaternion algebra.
    if ax is None:
        ax = plt.gca()

    # For the purposes of plotting, we need to align the z-axis of the plot to the normal of the plane.
    n = P(pi_dq)
    d = D(pi_dq)
    if n != k_:
        phi: float = acos(dot(n, k_).q[0])
        v: DQ = cross(n, k_) * (1.0 / sin(phi))
        r: DQ = cos(phi / 2.0) + v * sin(phi / 2.0)
    else:
        r: DQ = DQ([1])

    # The translation about z is after the normal is applied.
    x_dq: DQ = r * (1 + 0.5*E_*d*k_)
    _draw_pose(x_dq)

    # Cylindrical points start at zero
    x = np.linspace(-length_x / 2.0, length_x / 2.0, 2)
    y = np.linspace(-length_y / 2.0, length_y / 2.0, 2)

    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.zeros(x_grid.shape)

    x_grid_ad, y_grid_ad, z_grid_ad = _dq_ajoint_grid(x_dq, x_grid, y_grid, z_grid)

    ax.plot_surface(x_grid_ad,
                    y_grid_ad,
                    z_grid_ad,
                    alpha=0.8)


def _draw_revolute_joint(x,
                         height_z=0.07,
                         radius=0.02,
                         ax=None):
    param_dict = {
        "alpha": 0.8,
        "linewidth": 0,
        "color": 'r'
    }
    _draw_cylinder(x,
                   height_z=height_z,
                   radius=radius,
                   param_dict=param_dict,
                   ax=ax)


def _dq_adjoint(x: DQ, t: DQ):
    """
    This currently does not seem to exist in the implementation of dqrobotics.
    I'm basing this on (25) of https://faculty.sites.iastate.edu/jia/files/inline-files/dual-quaternion.pdf
    until I find another authoritative source.

    :param x: A unit dual quaternion.
    :param t: A pure quaternion representing the point to be transformed.
    :return: A pure quaternion of representing the transformed point.
    """
    if not is_unit(x):
        raise RuntimeError("The argument x must be a unit dual quaternion.")
    if not (is_pure(t) and is_quaternion(t)):
        raise RuntimeError("The argument t must be a pure quaternion.")

    t_dq = 1 + E_ * t
    return translation(x * t_dq * conj(x.sharp())) * 0.5


def _draw_serial_manipulator(robot: DQ_SerialManipulator,
                             q: np.ndarray,
                             linespec: str = "k-",
                             linewidth=3,
                             ax=None):
    """
    Draw a serial manipulator at a given joint configuration q. Each joint transformation will be connected by a line
    with spec linespec and width linewidth.
    :param robot: A concrete subclass of DQ_SerialManipulator.
    :param q: the joint configurations.
    :param linespec: a matplotlib linespec. Has a default value.
    :param linewidth: the width compatible with matplotlib. Has a default value.
    :param ax: Figure Axes or plt.gca() if None.
    :return: Nothing.
    """
    if ax is None:
        ax = plt.gca()

    x_plot = []
    y_plot = []
    z_plot = []

    for dof in range(0, robot.get_dim_configuration_space()):
        pose = robot.fkm(q, dof)
        t = translation(pose)
        x_plot.append(t.q[1])
        y_plot.append(t.q[2])
        z_plot.append(t.q[3])

        _draw_revolute_joint(pose, ax=ax)
        _draw_pose(pose, ax=ax)

    # Draw reference frame
    x_ref = robot.get_reference_frame()
    t_ref = translation(x_ref)
    ax.plot3D((t_ref.q[1], x_plot[0]),
              (t_ref.q[2], y_plot[0]),
              (t_ref.q[3], z_plot[0]),
              linespec,
              linewidth=linewidth)
    _draw_pose(x_ref, ax=ax)

    for i in range(0, len(x_plot) - 1):
        ax.plot3D((x_plot[i], x_plot[i + 1]),
                  (y_plot[i], y_plot[i + 1]),
                  (z_plot[i], z_plot[i + 1]),
                  linespec,
                  linewidth=linewidth)

    # Draw end effector frame
    x_eff = robot.fkm(q)
    t_eff = translation(x_eff)
    ax.plot3D((t_eff.q[1], x_plot[-1]),
              (t_eff.q[2], y_plot[-1]),
              (t_eff.q[3], z_plot[-1]),
              linespec,
              linewidth=linewidth)
    _draw_pose(x_eff, ax=ax)


def _draw_pose(x: DQ, length: float = 0.1, ax=None):
    """
    Draw a reference frame at a given pose x.
    :param x: the pose as a unit DQ.
    :param length: the length of each axis' line. Has a default value.
    :param ax: Figure Axes or plt.gca() if None.
    :return: nothing.
    """
    if not is_unit(x):
        raise RuntimeError(f"The input x = {x} is not a unit dual quaternion.")
    if ax is None:
        ax = plt.gca()

    t = translation(x)

    i_prime = Ad(x, i_)
    j_prime = Ad(x, j_)
    k_prime = Ad(x, k_)

    # Centre of the reference frame
    ax.plot3D(t.q[1],
              t.q[2],
              t.q[3],
              "kx")

    # x-axis arrow
    ax.quiver(t.q[1], t.q[2], t.q[3],
              i_prime.q[1], i_prime.q[2], i_prime.q[3],
              length=length,
              color="r",
              normalize=True)

    # y-axis arrow
    ax.quiver(t.q[1], t.q[2], t.q[3],
              j_prime.q[1], j_prime.q[2], j_prime.q[3],
              length=length,
              color="g",
              normalize=True)

    # z-axis arrow
    ax.quiver(t.q[1], t.q[2], t.q[3],
              k_prime.q[1], k_prime.q[2], k_prime.q[3],
              length=length,
              color="b",
              normalize=True)



def draw_line(l_dq: DQ, linespec: str = "r", length: float = 10.0, ax=None):
    """
    Draw a line representing the DQ l_dq. This expects a figure to be currently active.

    :param l_dq: the DQ representation of the line.
    :param linespec: the desired linespec. Has a default value.
    :param length: the length. Has a default value.
    :param ax: Figure Axes or plt.gca() if None.
    :return: nothing.
    """
    if not is_line(l_dq):
        raise RuntimeError(f"The input l_dq = {l_dq} is not a line.")
    if ax is None:
        ax = plt.gca()

    # Decompose line
    l = P(l_dq)
    m = D(l_dq)

    # This is always a point in the line. More specifically, the projection of 0i_ + 0j_ + 0k_ onto the line.
    pl = cross(l, m)

    pl_positive = pl + length * l
    pl_negative = pl - length * l

    ax.plot3D((pl_negative.q[1], pl_positive.q[1]),
              (pl_negative.q[2], pl_positive.q[2]),
              (pl_negative.q[3], pl_positive.q[3]), linespec)
