#!/bin/bash


### for [O/Fe]vs[Fe/H] 

awk '{ if ($1 >= -2.82 && $1 <= -1.82) print $0}' FeOvsOH_MP0.dat > a.dat
awk '{ if ($2 >= -0.425 && $2 <= 0.175) print $0}' a.dat > selection_area1.dat

rm a.dat

awk '{ if ($1 >= -1.82 && $1 <= -0.82) print $0}' FeOvsOH_MP0.dat > a.dat
awk '{ if ($2 >= 0.175 && $2 <= 1.175) print $0}' a.dat > selection_area2.dat

rm a.dat

awk '{ if ($1 >= -0.82 && $1 <= 0.68) print $0}' FeOvsOH_MP0.dat > a.dat
awk '{ if ($2 >= -0.425 && $2 <= 0.975) print $0}' a.dat > selection_area3.dat

rm a.dat

### for log(Fe/O) vs 12+log(O/H)

awk '{ if ($1 >= 6 && $1 <= 7) print $0}' FeOvsOH_MP.dat > a.dat
awk '{ if ($2 >= -1.4 && $2 <= -0.8) print $0}' a.dat > area1.dat

rm a.dat

awk '{ if ($1 >= 7 && $1 <= 8) print $0}' FeOvsOH_MP.dat > a.dat
awk '{ if ($2 >= -2.4 && $2 <= -1.4) print $0}' a.dat > area2.dat

rm a.dat

awk '{ if ($1 >= 8 && $1 <= 9.5) print $0}' FeOvsOH_MP.dat > a.dat
awk '{ if ($2 >= -2.2 && $2 <= -0.8) print $0}' a.dat > area3.dat

rm a.dat

