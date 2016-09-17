## IDR:

Example run on cluster:

```{.sh}
cd /mnt/jadb/DBfile/DBfiles/temp
export PATH=~/software/bin:$PATH
~/anaconda/bin/ipython ~/TEST/macs2_idr.ipy -- \
  ../LET418/N2/AA569_aa82_Q3861/LET418^Q3861_aa82^E^N2^YA_aligned^NA^NA_AA569^F1033833.bam \
  ../LET418/N2/AA568_aa80_Q3861/LET418^Q3861_aa80^E^N2^YA_aligned^NA^NA_AA568^F5e33833.bam \
  -c ../Input/SummedInputs/EGS_HiSeq_input.bam
```

## Concave

ChIP-seq peak calls were refined using an adhoc post-processing step,
as visually distinct peaks close to each other were sometimes
identified as a single peak by MACS2. We identified concave regions
within MACS2 peaks using the smoothed second derivative of the
mapq0 pileup coverage signal with 250bp kernel. We empirically found the minimum of
the second derivative within a concave region to be a good indicator
of a visually compelling peak, and used concave regions (within MACS2
peaks) with a threshold of -500 curvature index as our final peak calls.


```{.sh}
cd /mnt/jadb/DBfile/DBfiles/temp
export PATH=~/software/bin:$PATH
~/anaconda/bin/ipython ~/TEST/macs2_idr.ipy -- \
  ../LET418/N2/AA569_aa82_Q3861/LET418^Q3861_aa82^E^N2^YA_aligned^NA^NA_AA569^F1033833.bam \
  ../LET418/N2/AA568_aa80_Q3861/LET418^Q3861_aa80^E^N2^YA_aligned^NA^NA_AA568^F5e33833.bam \
  -c ../Input/SummedInputs/EGS_HiSeq_input.bam
```
