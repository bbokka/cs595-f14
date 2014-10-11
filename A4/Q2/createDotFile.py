#!/usr/bin/env python

import os
import sys
import glob


#Main Function
def main():

    path       = "/home/bbokka/cs594/A4/Q1/links/*.link"
    md5_Url    = open('md5Links.txt','r')
    mapping    = open('mapping.dot','w')
    mapping.write('digraph A4_question3 { size = "6,6"; node [color = lightblue2 ,style = filled]; ')
    for line in md5_Url.readlines():
        line = line.split(" ")
        md5  = line[0] 
        url  = line[1]

        first_spit          = url.split("://")
        store_first_split   = first_spit[1]
        second_split        = store_first_split.split("/")
        store_second_split  = second_split[0]
        url_label_string        = store_second_split
        #print label_string

        md5_file = glob.glob(path)
        for each_md5_file in md5_file:
            #print each_md5_file
            filename      = each_md5_file.split("/links/")
            md5_file_name = filename[1]
            md5_code      = md5_file_name.split(".link")
            md5_code_file = md5_code[0]
            #print md5_code_file 
            if (md5 == md5_code_file):          
                open_md5 = open(each_md5_file,'r')
                for link in open_md5.readlines():
                    first_spit_1        = link.strip().split("://")
                    store_first_split_1  = first_spit_1[1]
                    second_split_1       = store_first_split_1.split("/")
                    store_second_split_1  = second_split_1[0]
                    link_label_string        = store_second_split_1      
                    link = link.strip()
                    url  = url.strip()              
                    #string       = ' "'+url.strip()+'"' +'->' +'" ' +links.strip()+'"[' + 'label =' +'"'+ label_string + '"' +'];'
                    string         = '"'+ url.strip() + '"'+' '+'->'+' '+'"'+ link.strip() + '"'+ ' \n '+'"'+ url.strip()   + '"'+' '+ '[label =' + '"'+ url_label_string  + '"' +'];'+' \n ' +'"'+ links + '"'+' '+ '[label =' + '"'+ link_label_string + '"' +']' +';'
                    mapping.write(string)
                    mapping.write('\n')
    mapping.write ('}')



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)