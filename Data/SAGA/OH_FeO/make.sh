#!/bin/bash

awk '{print $1-3.180+12.0"  "$2*(-1)-1.225}' FeOvsOH_MP0.dat > FeOvsOH_MP.dat
awk '{print $1-3.180+12.0" "$2*(-1)-1.225}' FeOvsOH_EMP_MS0.dat > FeOvsOH_EMP_MS.dat
awk '{print $1-3.180+12.0" "$2*(-1)-1.225}' FeOvsOH_EMP_RGB0.dat > FeOvsOH_EMP_RGB.dat

