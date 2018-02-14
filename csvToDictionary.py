import csv

colorOpts = ['rgba(150, 201, 255, 1)',
             'rgba(168, 191, 18, 1)',
             'rgba(249, 147, 0, 1)',
             'rgba(0, 170, 181, 1)',
             'rgba(242, 226, 5, 1)',
             'rgba(239, 36, 119, 1)',
             'rgba(231, 73, 75, 1)',
             'rgba(54, 162, 235, 1)']
        
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
 #               'backgroundColor': 'rgba(150, 201, 255, 0.8)',
 #               'borderColor': 'rgba(150, 201, 255, 1)',
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
