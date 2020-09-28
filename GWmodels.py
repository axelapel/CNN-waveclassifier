import numpy as np
import pycbc.waveform as waveform

# Creation of a set of waveforms with m_1 varying from 1.4 to 1.7 Mo.
sz_sample = 10
m1_prior = np.linspace(1.4, 1.7, sz_sample)

approximants = {"phenom": "IMRPhenomPv2_NRTidal", "taylor": "TaylorF2"}

for i, m1 in enumerate(m1_prior):
    hp, hc = waveform.get_td_waveform(approximant=approximants["phenom"],
                                      mass1=m1_prior[i], mass2=1.5,
                                      delta_t=1.0/4096, f_lower=40)
    hp.save("waveforms/phenom/phenomPNRT_M1={:.2f}M0.npy".format(m1))
