===========================
Pixel Concepts and Glossary
===========================

Full Well Capacity
------------------

The full well capacity (FWC) is the maximum number of electrons that a pixel can collect before saturation. Normally the usable full well is defined by the region over which the response of the pixel is linear, which can sometimes be called the *linear full well*. [#]_


Fill Factor
-----------

The fill factor (FF) refers to the ratio of the optically active area of a pixel, to the total area of a pixel. In front-side illuminated (FSI) sensors this is critical as there is a trade-off between the area dedicated to the photodiode, and the area available for the in-pixel transistors. Process improvements such as microlenses and light pipes helped increase the effective fill factor of FSI pixels by directing light away from the metal routing and transistors and towards the photodiode. In back-side illuminated (BSI) technologies the routing does not block the light and fill factors are much better, reaching 100% with microlenses.


Quantum Efficiency
------------------
The QE is the ratio of electrons measured by a sensor, to the photons received. It is wavelength dependent, and for typical sensors tends to peak in the green. A high QE means simply that images can taken at lower light levels.

.. math::
	QE = \frac{N_{electrons}}{N_{photons}}

Spectral Responsivity
---------------------
Spectral responsivity is a linked to quantum efficiency, but expressed in amperes generated per watt of light. 

.. math::
	SR (A/W) = QE \cdot \frac{q\lambda}{hc}

which can be simplified to 

.. math::
	SR (A/W) = \text{QE} \cdot \frac{\lambda (\text{nm})}{1239.8}


Conversion Gain
---------------

The conversion gain, also referred to as the charge to voltage factor (CVF) is the voltage change seen at the pixel sense node due to 1 electron.  The CVF depends on the capacitance at the sense node which is formed of the source-follower gate along with parasitics. Typical values can be around :math:`100\mu V / e^-`. 

.. math::
	CVF = \frac{q}{C_{SN}}

Some pixels implement additional transistors which increase the parasitic capacitance, which reduces the CVF of the pixel to handle larger signals. [#]_ These kinds of pixels can be said to have *dual conversion gain* (DCG).


Crosstalk
---------
Crosstalk generally referes to the signal from one pixel corupting the signal in a neghboring pixel. Two types of crosstalk that can be distinguished: optical and electrical. For example, optical crosstalk can occur when light passes through the colour filter of a pixel, and generates carriers in the neghboring pixel. 


Dynamic Range
-------------
The dynamic range (DR) of a sensor is the ratio between the highest signal level that can be converted and the lowest. The highest signal level is limited by the full well of the pixels, and the lowest is limited by the read noise of the signal chain. The ratio is most often expressed in decibels.

For example a pixel with a full well of 12,000e- and a read noise of 5e- will have a DR of nearly 68dB

.. math::
	\text{DR} = 20 \log_{10}\left(\frac{\text{FWC}}{\text{Read Noise}}\right)

	= 20 \log_{10}\left(\frac{12,000}{5}\right) = 67.6\text{dB}

An alternative unit of dynamic range used often in the context of conventional photography is *stops*. This uses a base-2 logarithm instead of base-10. To convert between the two use

.. math::
	\text{DR}[\text{stops}] \cdot 20 \log_{10}(2)= \text{DR}[\text{dB}]

Dark Current
------------
Dark current is the leakage current in the photodetector which occurs without illumination. 

Noise
-----
See the larger section on :ref:`noise <noise>`


.. [#] https://www.princetoninstruments.com/learn/camera-fundamentals/full-well-capacity-pixel-saturation

.. [#] https://www.pyxalis.com/wp-content/uploads/Publications/B3_Michelot.pdf