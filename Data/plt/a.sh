#!/bin/bash

/opt/local/bin/gnuplot > load 'evol.plt'
sed 's/Si/C/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/N/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Al/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Mn/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Cr/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Co/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Ni/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 
sed 's/Si/Ti/g' evol.plt > a.plt
/opt/local/bin/gnuplot > load 'a.plt'
rm a.plt 


