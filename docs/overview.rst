Overview
========

In this library, the user must call the function `plot()`. It will dispatch the setting defined by the user using
`kwargs` to the underlying methods that deal with each type of plot.

.. warning::
    Never use internal methods, e.g., with a trailing `_` directly. The API for those can change at any time.


Importing the `dqrobotics-pyplot`
---------------------------------

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

Draw a pose
-----------

.. note::
    See its API :meth:`pyplot._pyplot._draw_pose`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 44-48
   :emphasize-lines: 5

Draw a line
-----------

.. note::
    See its API :meth:`pyplot._pyplot._draw_line`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 50-54
   :emphasize-lines: 5

Draw a plane
------------

.. note::
    See its API :meth:`pyplot._pyplot._draw_plane`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 56-60
   :emphasize-lines: 5

Draw a `DQ_SerialManipulator`
-----------------------------

.. note::
    See its API :meth:`pyplot._pyplot._draw_serial_manipulator`.

The most basic version of the call is.

.. literalinclude:: ../src/dqrobotics_extensions/pyplot/example.py
   :language: python
   :lines: 62-65
   :emphasize-lines: 4