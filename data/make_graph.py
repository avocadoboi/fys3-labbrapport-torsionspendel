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
    # axes = list(map(list, zip(*map(
    #     lambda x: map(float, x), 
    #     filter(lambda x: any(x), reader)
    # ))))

x = axes[0]

pyplot.figure(figsize=(12, 5))
pyplot.hlines(0, x[0], x[-1], colors="#ccc", linestyles="dashed")
for i, y in enumerate(axes[1:]):
    display_name = input(f"Enter plot name {i}: ")
    mask = numpy.isfinite(y)
    pyplot.plot(x[mask], y[mask], label = display_name)
pyplot.legend()
pyplot.xlabel("tid [sekunder]")
pyplot.ylabel("avvikelse [meter]")
pyplot.autoscale(tight=True)
pyplot.savefig(f"../images/graf_{os.path.splitext(file_name)[0]}.png", bbox_inches="tight")
