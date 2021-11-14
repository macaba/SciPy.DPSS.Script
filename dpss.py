import sys
import json
import scipy.signal

from pathlib import Path
python_file_path = Path(__file__)
dir_path = python_file_path.parent
input_file_path = dir_path / 'dpss_input.json'

with open( input_file_path ) as data_file:   
	input_args = json.loads( data_file.read() )

# M: int
# Window length.

# NW: float
# 0.1 * 300000 * (1/30)
# Standardized half bandwidth corresponding to 2*NW = BW/f0 = BW*M*dt where dt is taken as 1.

# Kmax: int | None, optional
# Number of DPSS windows to return (orders 0 through Kmax-1). If None (default), return only a single window of shape (M,) instead of an array of windows of shape (Kmax, M).

# sym: bool, optional
# When True (default), generates a symmetric window, for use in filter design. When False, generates a periodic window, for use in spectral analysis.

M, Kmax = [ int(input_args.get( key )) for key in [ 'M', 'Kmax' ] ]
NW = [ float(input_args.get( key )) for key in [ 'NW' ] ]

win_dpss = scipy.signal.windows.dpss(M, NW, Kmax, False)

