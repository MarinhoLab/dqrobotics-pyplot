MISC
====

Saving an animation video
-------------------------

In a macos environment, this needs

.. code-block:: console

    brew install ffmpeg

then, before doing `plt.show()`, add the code below to save an animation called `anim`.

.. code-block:: python

   anim.save("test.mp4")
