import csv
import os
import numpy

file_name = input("Enter file name: ")

with open(file_name, newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    rows = list(reader)
    name, extension = os.path.splitext(file_name)
    writer = csv.writer(open(f"{name}_centered{extension}", 'w', newline=''), delimiter='\t')
    for row in rows:
        writer.writerow(map(
            lambda x: 
                x[1] if x[0] == 0 else 
                    (str(float(x[1]) - float(rows[-1][x[0]])) if x[1] else x[1])
            , enumerate(row)
        ))

