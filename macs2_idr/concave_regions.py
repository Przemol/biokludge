#!/usr/bin/env python
"""
This is a generic "peak caller" for ATAC/DNase/MNase/ChIP genomic HTS data.
It finds regions of concave curvature as defined by the sign of the (heavily
smoothed) second derivative (a well-known classic approach from signal processing).

It works well in situations where peaks have a characteristic width, and was
written with the aim of "post-processing" peak calls from a statistical caller
(MACS2) in order to separate neighbouring peaks that are incorrectly
identified as a single peak by the statistical approach.

1. Call peaks using MACS2
2. Call concave regions using concave_peaks.py:
    bigWigToBedGraph ChIP_track.bw stdout | concave_peaks.py > ChIP_track.bed

3. Discard concave regions that do not overlap a MACS2 peak (e.g. bedtools subtract)
4. Filter peaks by the "curvature index" (column 5 in the output) to remove
visually non-compelling noise.

"""
import argparse
import datetime
import sys
import numpy as np

"""
Eight-order approximation centered at grid point derived from:
    Fornberg, Bengt (1988), "Generation of Finite Difference Formulas on Arbitrarily Spaced Grids",
        Mathematics of Computation 51 (184): 699-706, doi:10.1090/S0025-5718-1988-0935077-0
"""
def D2_kernel(): return [-1.0/560, 8.0/315, -1.0/5, 8.0/5, -205.0/72, 8.0/5, -1.0/5, 8.0/315, -1.0/560]

def rolling_mean_kernel(width): return np.ones(width) / float(width)

def call_peaks_on_chrom(l_iv):
    # Build signal array from interval list
    signal = np.zeros(l_iv[-1][2])
    for (chrom, start, end, val) in l_iv:
        signal[start:end] = val

    # Convolve signal (kernel is multiplied by an adhoc large number for numerical stability)
    width = 250
    kernel = 1E6 * np.convolve(np.convolve(np.convolve(D2_kernel(),
                                                       rolling_mean_kernel(width)),
                                                       rolling_mean_kernel(width)),
                                                       rolling_mean_kernel(width))
    signal_convolve = np.convolve(signal, kernel[::-1], mode='same')
    start = signal_convolve.shape[0] + 1
    score = float('inf')
    for i in range(signal_convolve.shape[0]):
        if signal_convolve[i] < 0:
            start = min(start, i)
            score = min(score, signal_convolve[i])

        elif np.isfinite(score):
            print '%(chrom)s\t%(start)d\t%(i)d\t.\t%(score)f' % locals()
            score = float('inf')
            start = signal_convolve.shape[0] + 1

if __name__ == "__main__":
    l_iv = []
    for line in sys.stdin:
        tokens = line.rstrip().split("\t")
        try:
            chrom = tokens[0]
            start = int(tokens[1])
            end = int(tokens[2])
            val = float(tokens[3])
            if len(l_iv) > 0 and chrom != l_iv[0][0]:
                print >>sys.stderr, '%s\tCalling peaks on: %s' % (datetime.datetime.now(), l_iv[0][0])
                call_peaks_on_chrom(l_iv)
                l_iv = []
            l_iv.append((chrom, start, end, val))
        except:
            print >>sys.stderr, 'Skipping line: %(line)s' % locals(),

    print >>sys.stderr, '%s\tCalling peaks on: %s' % (datetime.datetime.now(), l_iv[0][0])
    call_peaks_on_chrom(l_iv)
