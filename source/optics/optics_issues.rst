=============
Optics Issues
=============

Veiling Glare
-------------
Veiling glare is an optical effect which arises from stray light, that is any light which takes a path that is not part of the normal image forming path, entering the camera and making it to the sensor. It has the effect of fogging the image, reducing contrast [#]_

.. [#] https://www.imatest.com/docs/veilingglare/

Lens Flare
----------
https://www.imatest.com/docs/stray-light-flare/
https://library.imaging.org/ei/articles/35/16/AVM-127

.. youtube:: z_WRaTsGbVE
	:width: 100%


Chromatic Aberration
--------------------
Chromatic aberrations are artifacts visibile in the final image caused by the fact that different wavelengths (colours) have slightly different indices of refraction through the lens elements and therefore focus at different locations on the sensor.

This can be corrected with an extra lens element.

https://www.imatest.com/docs/sfr_chromatic/

Vignetting
----------
Vignetting, or *illumination falloff*, is the reduction of the image brightness towards the edges and corners of the image. Natural vignetting can be described by 

.. math::
	cos^4(\theta)

where :math:`\theta` is the angle between the central, optical axis of the lens, and the angle at which the light hits the pixel. At the centre of the image the angle is 0 and so there is no falloff.

The effect originates from the fact that the lens has a specific length and objects that are off-axis see a reduced aperture. Natural vignetting can be reduced by stepping the lens aperture down. [#]_ 

Vignetting can be compensated by taking a photo of a uniform white object to determine the per-pixel attenuation, and later dividing it out during post-processing.

.. [#] https://www.cs.cmu.edu/~sensing-sensors/readings/vignetting.pdf

Distortion
----------
The two main types of lens distortion are called after the way they change the shape of the imaged objects. These are *barrel distortion* and *pincushion distortion*.

