=======
Filters
=======

Anti-Aliasing Filter
--------------------
Since an image sensor is composed of an array individual pixels, it samples the image produced by the lens at discrete locations. Because of this spatial sampling it's possible that high spatial frequencies in the scene will alias and appear as low spatial frequencies in the generated image [#]_. This can be prevented by adding an anti-aliasing filter which will blur the image slightly. While this prevents aliasing, the tradeoff with blurring has to be considered.

Physically, an AA filter can be composed of two layers of a birefringent material. This will spread the light passing through it.

IR Filter
---------
Most systems make a decision about what to do with infrared light. Cameras for general photography applications are generally only interested in the visible portion of the spectrum and will an IR blocking filter to prevent infrared light from generating a signal.

In different applications, such as hand tracking, depth sensing, or face identification the scene is actively illuminated with an infrared light and the system will have an IR bandpas filter to capture only the IR reflections.

Polarisation Filter
-------------------


.. [#] S.B. Campana and D.F. Barbe, "Tradeoffs Between Aliasing and MTF" in *Technology and Applications of CCDs*, 1974. `(link) <https://www.imagesensors.org/Past%20Workshops/Dick%20Bredthauer%20Collection/1974%20Scotland%20Conference/1974%2021%20Campana.pdf>`_ 