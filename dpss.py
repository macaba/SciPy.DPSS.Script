import sys
import json
import scipy.signal
import math

# Input file parameters:

# Samples: int
# Window length.

# SampleRate: int
# ADC sample rate.

# dF: float
# Minimum distance between frequency peaks you expect to resolve

from pathlib import Path
python_file_path = Path(__file__)
dir_path = python_file_path.parent
input_file_path = dir_path / 'dpss_input.json'
output_file_path = dir_path / 'dpss_output.bin'

with open( input_file_path ) as data_file:   
	input_args = json.loads( data_file.read() )

Samples, SampleRate = [ int(input_args.get( key )) for key in [ 'Samples', 'SampleRate' ] ]
dF = float(input_args.get( 'dF' ))	# Frequency resolution
N = Samples/SampleRate				# Size of the data window in seconds
NW = 4
Kmax = math.floor((N * dF) - 1)

# dpss parameters:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.dpss.html

# M: int
# Window length.

# NW: float
# 0.1 * 300000 * (1/30)
# Standardized half bandwidth corresponding to 2*NW = BW/f0 = BW*M*dt where dt is taken as 1.

# Kmax: int | None, optional
# Number of DPSS windows to return (orders 0 through Kmax-1). If None (default), return only a single window of shape (M,) instead of an array of windows of shape (Kmax, M).
# Kmax should be (M * dF) - 1

# sym: bool, optional
# When True (default), generates a symmetric window, for use in filter design. When False, generates a periodic window, for use in spectral analysis.

win_dpss = scipy.signal.windows.dpss(Samples, NW, Kmax, False, 'subsample')

output_file = open(output_file_path, 'wb')
for window in win_dpss:
	output_file.write(window)

print("Done")