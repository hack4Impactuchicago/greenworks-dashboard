import csv

def csvToDict(filename):
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)

        cols = zip(*reader)
        data=[]
        for c in cols:
            data.append(
              {
                'label':c[0],'data':c[1:],'borderWidth':0, 
                'backgroundColor': 'rgba(150, 201, 255, 0.8)',
                'borderColor': 'rgba(150, 201, 255, 1)'})

            
        opts={
          'type':'bar',
          'labels':data[0],
          'datasets': data[1:],
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
            
# options=csvToDict('planted_trees.csv')
# print(options)

#MISSING PARTS OF VAR OPTS:

#in datasets: borderColor
#in options: all of scales
