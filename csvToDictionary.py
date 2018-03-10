import csv
import os
#import parse as parser

colorOpts1 = ['#3f83ab','#86C3B4','#C8DCC3','#86d1d1','#F4E3D1']
colorOpts2 = ['#A020F0','#FF8833','#FFEB00','#3AA655','#02A4D3']
colorOpts3 = ['#4E3A5E','#56887D','#7A89B8','#9E5E6F','#8BA8B7']
colorOpts4 = ['#FF9933','#FD5B78','#FFFF66','#CCFF00','#AAF0D1']
colorOptsDefault = ['#ffefa2','#fed0d0','#b9f2b1','#DAEDFE','#96c9ff']

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
    if colors == 1:
        return colorOpts1[choice]
    elif colors == 2:
        return colorOpts2[choice]
    elif colors == 3:
        return colorOpts3[choice]
    elif colors == 4:
        return colorOpts4[choice]
    elif choice == 0:
        return colorOptsDefault[choice]
    else:
        return "Invalid choice number."

def TextColorChoices(colors):
    if colors >= 0 or colors <= 4:
        return colorsGraphText[colors]
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
    if 'BBCcheck' in dict_of_otherinfo:
        bbc = 0
    else:
        bbc = dict_of_otherinfo['selectBBC']

    #checking to see Actual Colors
    if 'Radiocheck' in dict_of_otherinfo:
        colorN = 0
    else:
        colorN = dict_of_otherinfo['selectR']

    ##nowww opening the file
    csvname = os.path.join(p, csvfile.filename)
    with open(csvname, mode='r') as infile:
        #Reading the CSV file
        reader = csv.reader(infile)
        cols = zip(*reader)
        data=[]
        counter=0;
        for c in cols:
            data.append(
              {'label':c[0],
                'data':c[1:],
                'backgroundColor': GraphColorChoices(colorN,counter),
                'borderColor': GraphColorChoices(colorN,counter),
                'borderWidth':0})
            counter+=1

    #and finally creating the data for chart.js
    if gt == 'bar':
        opts={
          'type':gt,
          'data':
          {
            'labels': data[0]['data'],
            'datasets': data[1:]
          },
          'options':
          {
            'scales':
            {
              'yAxes':
              [{
                'stacked': True,
                'scaleLabel': {
                  'display': True,
                  'labelString': dict_of_otherinfo['title-x']
                  #'fontColor': TextColorChoices(colorN)
                }
              }],
              'xAxes':
              [{
                'stacked': True
                #'display': True,
                #'labelString': dict_of_otherinfo['title-y']
                #'fontColor': TextColorChoices(colorN)
              }]
            },
            'title':
            {
              'display':True,
              'text':tt,
              'position':'top'
              #'fontColor': TextColorChoices(colorN)
            }
        }
        }
    else:
        opts = {}


    return opts
    #print(opts)

#options=csvToDict('planted_trees.csv')
#print(options)

#MISSING PARTS OF VAR OPTS:

#in datasets: borderColor
#in options: all of scales
