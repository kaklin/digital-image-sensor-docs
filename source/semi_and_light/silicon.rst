=======
Silicon
=======

Data from [#]_. Tabulated data available at `PV Education <https://www.pveducation.org/pvcdrom/materials/optical-properties-of-silicon>`_.  

Optical Absorption
------------------

.. math::
	I(d) = I_0 e^{-\alpha d}

.. plot:: semi_and_light/silicon_optical_properties.py plot_silicon_absorption

	Optical absorption coefficient as a function of wavelength (left) and the optical absorption depth (right) in silicon at 300K. 



Refractive Index
----------------

.. math::
	n^* = n + i \kappa

.. plot:: semi_and_light/silicon_optical_properties.py plot_refractive_index


Reflectivity
------------

.. math::
	R_{0}=\left\|{\frac{n_1-n_2}{n_1+n_2}}\right\|^{2}

.. plot:: semi_and_light/silicon_optical_properties.py plot_reflectivity
	
	Reflectivity of silicon at an interface with air, :math:`n_1=1`.


.. https://www.ioffe.ru/SVA/NSM/Semicond/Si/optic.html
.. https://www.ioffe.ru/SVA/NSM/Semicond/Si/
.. https://www.tf.uni-kiel.de/matwis/amat/admat_en/kap_5/backbone/r5_2_3.html

.. [#] Green, M.A. and Keevers, M. "Optical properties of intrinsic silicon at 300 K ", Progress in Photovoltaics, p.189-92, vol.3, no.3; (1995)
