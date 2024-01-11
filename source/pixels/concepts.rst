===========================
Pixel Concepts and Glossary
===========================

Full Well Capacity
------------------

The full well capacity (FWC) is the maximum number of electrons that a pixel can collect before saturation. Normally the usable full well is defined by the region over which the response of the pixel is linear, which can sometimes be called the *linear full well*. [#]_


Fill Factor
-----------

The fill factor (FF) refers to the ratio of the optically active area of a pixel, to the total area of a pixel. In front-side illuminated (FSI) sensors this is critical as there is a trade-off between the area dedicated to the photodiode, and the area available for the in-pixel transistors. Process improvements such as microlenses and light pipes helped increase the effective fill factor of FSI pixels by directing light away from the metal routing and transistors and towards the photodiode. In back-side illuminated (BSI) technologies the routing does not block the light and fill factors are much better, reaching 100% with microlenses.

Responsivity
------------

Quantum Efficiency
------------------

Sensitivity
-----------

Conversion Factor
-----------------

The conversion factor (CVF), sometimes also referred to as the conversion gain, is the voltage change seen at the pixel sense node due to 1 electron. Typical values can be around :math:`100\mu V / e^-`. 

The CVF depends on the capacitance at the sense node which is formed of the source-follower gate along with parasitics. 

Some pixels implement additional transistors which increase the parasitic capacitance, which reduces the CVF of the pixel to handle larger signals. [#]_ These kinds of pixels can be said to have *dual conversion gain* (DCG).

Crosstalk
---------

Optical and electrical 

Dynamic Range
-------------

The dynamic range (DR) of a sensor is the ratio between the highest signal level that can be converted and the lowest. The highest signal level is limited by the full well of the pixels, and the lowest is limited by the read noise of the signal chain. The ratio is most often expressed in decibels.

For example a pixel with a full well of 12,000e- and a read noise of 5e- will have a DR of nearly 68dB

.. math::
	DR = 20 \cdot \text{log}_{10}\left(\frac{12,000}{5}\right) = 67.6\text{dB}

Dark Current
------------

.. [#] https://www.princetoninstruments.com/learn/camera-fundamentals/full-well-capacity-pixel-saturation

.. [#] https://www.pyxalis.com/wp-content/uploads/Publications/B3_Michelot.pdf