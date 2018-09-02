import csv
import os
#import parse as parser

colorOpts1 = ['rgba(63, 131, 171, 0.6)','rgba(134, 195, 180, 0.6)','rgba(200, 220, 195, 0.6)','rgba(134, 209, 209, 0.6)','rgba(244, 227, 209, 0.6)']
colorOpts2 = ['#A020F099','#FF883399','#FFEB0099','#3AA65599','#02A4D399']
colorOpts3 = ['#4E3A5E99','#56887D99','#7A89B899','#9E5E6F99','#8BA8B799']
colorOpts4 = ['#FF993399','#FD5B7899','#FFFF6699','#CCFF0099','#AAF0D199']
colorOptsDefault = ['rgba(255, 239, 162, .6)', 'rgba(254, 208, 208, .6)','rgba(185, 242, 177, .6)','rgba(218, 237, 254, .6)','rgba(150, 201, 255, .6)']

colorsGraphText = ['#2176d2','#49A596','#FD0E35','#A17A74','#FF6EFF']

# These are the colors that will be chosen from #
colorsBBC = ['rgba(168, 191, 18, 0.7)', 'rgba(168, 191, 18, 1)',
          'rgba(189, 187, 254, 0.7)', 'rgba(189, 187, 254, 1)',
          'rgba(254, 148, 144, 0.7)', 'rgba(254, 148, 144, 1)',
          'rgba(1, 188, 144, 0.7)', 'rgba(1, 188, 144, 1)',
          'rgba(249, 165, 3, 0.7)', 'rgba(249, 165, 3, 1)']

# This function chooses the color #
def GraphColorChoices(colors, choice):
    choice = choice % 5
    if colors == "1":
        return colorOpts1[choice]
    elif colors == "2":
        return colorOpts2[choice]
    elif colors == "3":
        return colorOpts3[choice]
    elif colors == "4":
        return colorOpts4[choice]
    else:
        return colorOptsDefault[choice]

def TextColorChoices(colors):
    colors2 = int(colors)
    if colors2 >= 0 and colors2 <= 4:
        return colorsGraphText[colors2]
    else:
        return "Invalid choice number."

def csvToDict(csvfile,dict_of_otherinfo,p):
    #Checking to see if graphtype given
    if 'graphtypes_' in dict_of_otherinfo:
        gt = dict_of_otherinfo['graphtypes_']
    else:
        gt = 'bar'

    #Checking to see if Title is given
    if 'title' in dict_of_otherinfo:
        tt = dict_of_otherinfo['title']
    else:
        tt = '[No Title]'

    #checking to see BBCcolors
    if dict_of_otherinfo.get('selectBBC') is None:
        bbc = 0
    else:
        bbc = dict_of_otherinfo['selectBBC']

    #checking to see Actual Colors
    if dict_of_otherinfo.get('selectR') is None:
        colorN = 0
    else:
        colorN = dict_of_otherinfo['selectR']

    if 'stacked' in dict_of_otherinfo:
        stack = True
    else:
        stack = False

    if 'log' in dict_of_otherinfo:
        log = "logarithmic"
    else:
        log = "linear"

    if 'min' in dict_of_otherinfo:
        min1 = dict_of_otherinfo['min']
    else:
        min1 = ""

    if 'max' in dict_of_otherinfo:
        max1 = dict_of_otherinfo['max']
    else:
        max1 = ""

    ##nowww opening the file
    csvname = os.path.normpath(os.path.join(p, csvfile.filename))
    print(csvname)
    with open(csvname) as infile:
        #Reading the CSV file
        reader = csv.reader(infile)
        cols = zip(*reader)
        data=[]
        counter=0
        for c in cols:
            if counter == 2:
                if 'graphtypes_2' in dict_of_otherinfo:
                    data.append(
                    {'label':c[0],
                     'data':c[1:],
                     'backgroundColor': GraphColorChoices(colorN,counter),
                     'borderColor': GraphColorChoices(colorN,counter),
                     'borderWidth': 3,
                     'type': dict_of_otherinfo['graphtypes_2']})
                else:
                    data.append(
                    {'label':c[0],
                        'data':c[1:],
                        'backgroundColor': GraphColorChoices(colorN,counter),
                        'borderColor': GraphColorChoices(colorN,counter),
                        'borderWidth': 3})
            else:
                print(GraphColorChoices(colorN, counter))
                data.append(
                {'label':c[0],
                    'data':c[1:],
                    'backgroundColor': GraphColorChoices(colorN,counter),
                    'borderColor': GraphColorChoices(colorN,counter),
                    'borderWidth': 3})
            counter += 1
    #and finally creating the data for chart.js
#    if gt == 'bar':
    opts = {
    'type':gt,
    'data':
    {
        'labels': data[0]['data'],
        'datasets': data[1:]
    },
    'options':
    {
        'spanGaps': True,
        'scales':
        {
        'yAxes':
        [{
            'type': log,
            'ticks': {
                'suggestedMin': min1,
                'suggestedMax': max1,
            },
            'scaleLabel': {
            'display': True,
            'labelString': dict_of_otherinfo.get('title-x'),
            'fontColor': TextColorChoices(colorN)
            },
            'stacked': stack,
        }],
        'xAxes':
        [{
            'scaleLabel' : {
                'display': True,
                'labelString': dict_of_otherinfo.get('title-y'),
                'fontColor': TextColorChoices(colorN)
            },
            'stacked': stack,
        }]
        },
        'title':
        {
        'display':True,
        'text':tt,
        'position':'top',
        'fontColor': TextColorChoices(colorN)
        }
    }
    }
    return opts
    #print(opts)

#options=csvToDict('planted_trees.csv')
#print(options)

#MISSING PARTS OF VAR OPTS:

#in datasets: borderColor
#in options: all of scales
