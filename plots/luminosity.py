import wnutils.xml as wx
import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as pc
from astropy import units as u

xml = wx.Xml('out_rp.xml')

props = xml.get_properties_as_floats(['time', 't9', 'radius'])

lum = 4 * np.pi * (props['radius'] ** 2) * pc.sigma_sb.cgs * (props['t9'] ** 4)
print(lum)

u_lum = lum  * u.K**4 * u.s**3 / u.g

print(u_lum)

plt.plot(props['time'], u_lum)

plt.xlabel('time (s)')
plt.ylabel('$Luminosity\ (ergs\ s^{-1})$')

plt.xscale('log')
plt.yscale('log')

plt.show()

