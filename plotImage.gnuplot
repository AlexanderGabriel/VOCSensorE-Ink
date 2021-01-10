#set title "VOC/Flüchtige organische Verbindungen"
unset multiplot
set xdata time
set style data lines  
set term png size 296,128
set timefmt "%Y-%m-%d %H:%M:%S"
set format x ""
#set format x "%H:%M"
#set xlabel "Time"
#set ylabel "VOC" 
set datafile separator ","
set autoscale y
set xrange [time(0) - 60*60:]
set output "airsensorimage.png"
set tics font ",10"
plot "airsensordata.txt" using 1:($2 == 0 ? NaN : $2) w lines notitle
