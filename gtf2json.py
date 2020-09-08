#!/usr/bin/python

import sys
import re
import json

def gtf2json():
    
    #create an empty json list
    jsonList = []
    #Read gtf file
    with open(sys.argv[1], 'r') as gtf_file:
        #for loop each line
        for line in gtf_file:
            #find third column is gene
            m = re.findall(".*?\sgene\s.*", line)
            #if match, the m will not empty
            if m != []:
                #find out the gene_name, chr, startPos, endPos
                match = re.match(r'(\d).*?(\d{1,}).*?(\d{1,}).*?\s*.\s*[-+]?\s*.\s*\w*\s\"\w*\";\s\w*\s\"(\w*-?\w*.?\w).*', line)
                #make a dictionary of this line
                dict = {}
                if match:
                    dict["geneName"] = match.group(4)
                    dict["chr"] = match.group(1)
                    dict["startPos"] = match.group(2)
                    dict["endPos"] = match.group(3)
                else:
                    print(m[0])
                    print("No match!!!")
                print(dict)
                jsonList.append(dict)
    #write json list to data.json file
    with open('data.json','w') as json_file:
        json.dump(jsonList, json_file)



gtf2json()
