import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors

font = {'fontname':'Courier'}

with np.load('spec_rad.npz') as data:
    spec_rad_si      = data['spec_rad_si']
    spec_rad_oci     = data['spec_rad_oci']
    mfp              = data['mfp']
    ratio            = data['ratio']
    spec_rad_ratio   = data['spec_rad_ratio']
    N_ratio          = data['N_ratio']

# none of the information i
spec_rad_si[np.isnan(spec_rad_si)] = 0

# values fixing as spec rad function cant copmute on si when the reqired number
# of itterations are so low
# extrpolating from the previous two (assuming a linear relationship)
# base off of known behavior of source itterations
for i in range(spec_rad_si.shape[0]):
    exterp = spec_rad_si[i,2] + (0-2)*((spec_rad_si[i,1]-spec_rad_si[i,2])/(1-2))
    spec_rad_si[i,0] = exterp

spec_rad_ratio = spec_rad_si/spec_rad_oci
spec_rad_ratio[np.isnan(spec_rad_ratio)] = 1

x = ratio
y = mfp

xs = x.size
ys = y.size
[Xx, Yy] = np.meshgrid(y,x)

cmap = 'viridis'


#fig, ax = plt.subplots(nrows=1, ncols=3, subplot_kw={"projection": "3d"})
fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True, layout='constrained')



#ax[0].plot_surface(Xx,Yy,spec_rad_oci, cmap='viridis') contourf
ax[0].contourf(Xx, Yy, spec_rad_oci, cmap='viridis')
#ax[0].set_title('OCI SCB Spectral Radius Plot')
ax[0].set_xlabel(r'mfp [$\Sigma * \Delta x$]', **font)
ax[0].set_ylabel('Scattering Ratio [$Σ_s$/Σ]', **font)
ax[0].text(13, 0.05, 'OCI', color='w', fontsize=18, **font)

#ax[0].set_zlabel('Spectrial Radius OCI [ρ]')


pcm = ax[1].contourf(Xx,Yy,spec_rad_si, cmap='viridis')
#ax[1].set_title('SI SCB Spectral Radius Plot')
ax[1].set_xlabel(r'mfp [$\Sigma * \Delta x$]')
ax[1].text(15, 0.05, 'SI', color='w', fontsize=18)
#ax[1].set_ylabel('Scattering Ratio [$Σ_s$/Σ]')
#ax[1].set_zlabel('Spectrial Radius SI [ρ]')

norm = mpl.colors.Normalize(vmin=0, vmax=1)

cbar = plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax[0:2], location='bottom')
cbar.ax.set_xlabel('ρ')

#norm = mpl.colors.Normalize(vmin=0, vmax=1)
#fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), location='bottom')


CS = ax[2].contourf(Xx,Yy,spec_rad_ratio, cmap='viridis')
C1 = ax[2].contour(Xx,Yy,spec_rad_ratio, levels=[0,1.0],  colors='w', linewidths=(5,))
plt.clabel(C1, fmt='%2.1f', colors='w', fontsize=14)
#plt.title('ρ_si/ρ_oci')
#ax[2].set_ylabel(r'Scattering Ratio [$\Sigma_s/\Sigma$]')
ax[2].set_xlabel(r'mfp [$\Sigma * \Delta x$]')
cbar = plt.colorbar(CS, location='bottom')
cbar.ax.set_xlabel(r'$ρ_{si}/ρ_{oci}$')



#fig.colorbar(pcm)

#plt.tight_layout()
#ax[2].set_zlabel(r'Ratio of spectral radii $ρ_{SI}/ρ_{OCI}$')


#plt.tight_layout()

plt.show()
#plt.savefig('specrad_oci',dpi=600)
