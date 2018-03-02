# Written by: Jersey Fonseca, Samuel Sagawa, James Liu

import csv
import os

# These are the colors that will be chosen from #
colors = ['rgba(168, 191, 18, 0.7)', 'rgba(168, 191, 18, 1)',
          'rgba(189, 187, 254, 0.7)', 'rgba(189, 187, 254, 1)',
          'rgba(254, 148, 144, 0.7)', 'rgba(254, 148, 144, 1)',
          'rgba(1, 188, 144, 0.7)', 'rgba(1, 188, 144, 1)',
          'rgba(249, 165, 3, 0.7)', 'rgba(249, 165, 3, 1)']

# This function chooses the color #
def ChooseColor (colors, choice):
    if choice == 1:
        values = "backgroundColor: '%s',\nborderColor: '%s'," % (colors[0], colors[1])
    elif choice == 2:
        values = "backgroundColor: '%s',\nborderColor: '%s'," % (colors[2], colors[3])
    elif choice == 3:
        values = "backgroundColor: '%s',\nborderColor: '%s'," % (colors[4], colors[5])
    elif choice == 4:
        values = "backgroundColor: '%s',\nborderColor: '%s'," % (colors[6], colors[7])
    elif choice == 5:
        values = "backgroundColor: '%s',\nborderColor: '%s'," % (colors[8], colors[9])
    else:
        return "Invalid choice number."

    return values

# This function extracts a specific column #
def ExtractColumn (file, index):
        with open(file) as csvfile:
            csvReader = csv.reader(csvfile)
            header = csvReader.next()

            coordList = []
            for row in csvReader:
                coordList.append(row[index])
            return(", ".join(coordList))

# This opens the csv file and grabs the first row from it #
with open('data.csv') as data:
    read_rows = csv.reader(data, delimiter=',', quotechar='|')
    rows = list(read_rows)

# This creates an HTML file and fills it with blocks of data
# from the inputted CSV file.
index = 1
f = open('datasets.html', 'w')
f.write("datasets: [\n")
for labels in rows[0]:
    if labels == 'Year' or labels == '' or labels == ' ':
        continue
    else:
        dataset = """{\nlabel: '%s',\ndata: [%s],\n%s\nborderWidth: 1\n},\n""" % (labels, ExtractColumn('data.csv', index), ChooseColor(colors, 1))
        index += 1
        f.write(dataset)

# This removes the final comma and closes the file #
f.seek(-2, os.SEEK_END)
f.truncate()
f.close()
