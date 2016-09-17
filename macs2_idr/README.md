Example run on cluster:

```{.sh}
cd /mnt/jadb/DBfile/DBfiles/temp
export PATH=/home/ps562/software/bin:$PATH
~/anaconda/bin/ipython ~/TEST/macs2_idr.ipy -- \
  ../LET418/N2/AA569_aa82_Q3861/LET418^Q3861_aa82^E^N2^YA_aligned^NA^NA_AA569^F1033833.bam \
  ../LET418/N2/AA568_aa80_Q3861/LET418^Q3861_aa80^E^N2^YA_aligned^NA^NA_AA568^F5e33833.bam \
  -c ../Input/SummedInputs/EGS_HiSeq_input.bam
```
