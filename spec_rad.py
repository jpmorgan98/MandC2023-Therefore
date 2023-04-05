import numpy as np
import matplotlib.pyplot as plt

with np.load('spec_rad.npz') as data:
    spec_rad_si      = data['spec_rad_si']
    spec_rad_oci     = data['spec_rad_oci']
    mfp              = data['mfp']
    ratio            = data['ratio']
    spec_rad_ratio   = data['spec_rad_ratio']
    N_ratio          = data['N_ratio']

x = ratio
y = mfp

xs = x.size
ys = y.size
[Xx, Yy] = np.meshgrid(y,x)

fig,ax = plt.subplots(nrows=1, ncols=3, subplot_kw={"projection": "3d"})

#ax[0].plot_surface(Xx,Yy,spec_rad_oci, cmap='viridis')
ax[0].imshow(spec_rad_oci, cmap='viridis', interpolation='nearest')

ax[0].set_title('OCI SCB Spectral Radius Plot')
ax[0].set_xlabel(r'mfp [$\Sigma * \Delta x$]')
ax[0].set_ylabel('Scattering Ratio [$Σ_s$/Σ]')
ax[0].set_zlabel('Spectrial Radius [ρ]')


ax[1].plot_surface(Xx,Yy,spec_rad_si, cmap='viridis')
ax[1].set_title('SI SCB Spectral Radius Plot')
ax[1].set_xlabel(r'mfp [$\Sigma * \Delta x$]')
ax[1].set_ylabel('Scattering Ratio [$Σ_s$/Σ]')
ax[1].set_zlabel('Spectrial Radius [ρ]')

ax[2].plot_surface(Xx,Yy,spec_rad_ratio, cmap='viridis')
ax[2].set_title('ρ_si/ρ_oci')
ax[2].set_xlabel(r'mfp [$\Sigma * \Delta x$]')
ax[2].set_ylabel(r'Scattering Ratio [$\sigma_s/\sigma$]')
ax[2].set_zlabel(r'$\frac{N_{SI}}{N_{OCI}}$')


plt.show()
#plt.savefig('specrad_oci',dpi=600)
