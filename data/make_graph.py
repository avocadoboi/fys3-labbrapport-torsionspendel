import csv
import matplotlib.pyplot as pyplot
import os
import numpy

file_name = input("Enter file name: ")

with open(file_name, newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    axes = list(map(
        lambda x: 
            numpy.array(list(map(lambda x: float(x) if x else numpy.nan, x)))
        , zip(*reader)
    ))

x = axes[0]

pyplot.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 14.0
})

pyplot.figure(figsize=(12, 5))
pyplot.hlines(0, x[0], x[-1], colors="#ccc", linestyles="dashed")
for i, y in enumerate(axes[1:]):
    display_name = input(f"Enter plot name {i}: ")
    mask = numpy.isfinite(y)
    pyplot.plot(x[mask], y[mask], label = display_name)
    
# x1 = numpy.linspace(x[0], x[-1], 200)
# pyplot.plot(x1, 0.173949187928*x1**1.35224384357+0.0316287217477, label="$y=0.1739x^{1.352}+0.03163$")
# pyplot.plot(x, x*0.398323692005+0.0316287217477, label="$y=0.3983x+0.03163$")

pyplot.legend()
# pyplot.xlabel("Spänning [V]")
# pyplot.ylabel("$\\frac{\lambda}{I}$ [rad$^{-1}$s$^{-1}$]")
pyplot.xlabel("Tid [s]")
pyplot.ylabel("Avvikelse [m]")
pyplot.autoscale(tight=True)
pyplot.savefig(f"../images/graf_{os.path.splitext(file_name)[0]}.png", bbox_inches="tight")
