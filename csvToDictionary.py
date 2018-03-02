import csv
import parse as parser

colorOpts = ['rgba(150, 201, 255, 1)',
             'rgba(168, 191, 18, 1)',
             'rgba(249, 147, 0, 1)',
             'rgba(0, 170, 181, 1)',
             'rgba(242, 226, 5, 1)',
             'rgba(239, 36, 119, 1)',
             'rgba(231, 73, 75, 1)',
             'rgba(54, 162, 235, 1)']

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


def colorPicker(counter):
    if(counter < len(colorOpts)):
        return colorOpts[counter]
    else:
        return colorOpts[counter-len(colorOpts)]


def csvToDict(filename):
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        cols = zip(*reader)

        data=[]
        counter=0;
        for c in cols:
            data.append(
              {
                'label':c[0],'data':c[1:],
                'backgroundColor': colorPicker(counter),
                'borderColor': colorPicker(counter),
                'borderWidth':0})
            counter+=1


        opts={
          'type':'bar',
          'data':{'labels':data[0]['data'],
          'datasets': data[1:]},
          'options':{
            'scales': {
              'yAxes': [{
                'stacked': True,
                'scaleLabel': {
                  'display': True,
                  'labelString': 'Trees Planted'
                }
              }],
              'xAxes': [{
                'stacked': True
              }]
            },
            'title':{
              'display':True,'text':filename,'position':'top'}}}

    return opts
    #print(opts)

#options=csvToDict('planted_trees.csv')
#print(options)

#MISSING PARTS OF VAR OPTS:

#in datasets: borderColor
#in options: all of scales
