Overview
========

In this library, the user must call the function `plot()`. It will dispatch the setting defined by the user using
`kwargs` to the underlying methods that deal with each type of plot.

.. warning::
    Never use internal methods, e.g., with a trailing `_` directly. The API for those can change at any time.


Importing `dqrobotics-pyplot`
-----------------------------

.. warning::
    This import directive is to be used while `dqrobotics-pyplot` is not an integral part of the `dqrobotics` library.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 24-25

Setting up a plot with `plt`
----------------------------

.. note::
    If you don't create an `plt.axes` with `projection='3d'` the figure will be incompatible with `dqrobotics-pyplot`
    and an error will be raised.

A suitable figure must be created using `matplotlib.pyplot`, given that this library integrally rely on it.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 33-42
   :emphasize-lines: 3

Plot a pose
-----------

.. note::
    See its API :meth:`pyplot._pyplot._draw_pose`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 44-48
   :emphasize-lines: 5

Plot a line
-----------

.. note::
    See its API :meth:`pyplot._pyplot._draw_line`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 50-54
   :emphasize-lines: 5

Plot a plane
------------

.. note::
    See its API :meth:`pyplot._pyplot._draw_plane`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 56-60
   :emphasize-lines: 5

Plot a `DQ_SerialManipulator`
-----------------------------

.. note::
    See its API :meth:`pyplot._pyplot._draw_serial_manipulator`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 62-65
   :emphasize-lines: 4

Animating a `DQ_SerialManipulator`
++++++++++++++++++++++++++++++++++

.. note::

   This is fully reliant on https://matplotlib.org/stable/api/animation_api.html.

The important aspect of making animations is to properly use `matplotlib.animation` which is straightforward but does
not allow for "execution-time" plots. The idea is to store the desired motion aspects and then animate that afterwards.

We start importing the relevant libraries. We use `matplotlib.animation` and, to support more intricate animation
functions we use `functools.partial`.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example_animation.py
   :language: python
   :lines: 26-31
   :emphasize-lines: 5-6

One example animation function for the robot is

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example_animation.py
   :language: python
   :lines: 33-52
   :emphasize-lines: 20

where only the last line is related to `dqrobotics-pyplot`. Further reinforcing the need of a proper understanding of
how `matplotlib.animation` works.

Then, we have a `main` function that moves the robot as desired.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example_animation.py
   :language: python
   :lines: 54-95
   :emphasize-lines: 12-14,21-23,31-

Where we have some additional commands to store the control behavior, but, in general, only a few extra lines at the
end are needed to generate the animation.

