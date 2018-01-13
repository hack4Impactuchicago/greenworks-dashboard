# Written by: Jersey Fonseca, Samuel Sagawa, James Liu

import csv

# This opens the csv file and grabs the first row from it #
with open('data.csv') as data:
    read_rows = csv.reader(data, delimiter=',', quotechar='|')
    rows = list(read_rows)

# This creates an HTML file and fills it with blocks of data
# from the inputted CSV file.
f = open('datasets.html', 'w')
f.write("datasets: [\n")
for labels in rows[0]:
    if (labels == 'Year'):
        continue
    else:
        dataset = """{{\nlabel: '%s',\ndata: '%s',\nbackgroundColor: 'rgba(168, 191, 18, 0.7)',\nborderColor: 'rgba(168, 191, 18, 1)',\nborderWidth: 0\n}},\n""" % labels, labels
        f.write(dataset)
f.close()
