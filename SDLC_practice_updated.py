#program to search file and find the total keywords and their occurrance

import string
import sys
import os
import string

def main():

    n = len(sys.argv)
    args=len(sys.argv[1:])
    #print(args)
    if args==0:
        print("input the file path")
        dict_check={'errors':-3}
    else:
#check the file is present or not
        if file_search():
            print("file present")
#check the extension of file is text
            if find_file_extension() == '.txt':
                print("given text file")
#check the size is greater than 10kb
                if find_file_size()/1000 > 10:
                    dict_check = {'error': -1}
                    print("over size")
                else:
                    dict_check = keyword_set()
            else :
                dict_check={'error':-2}
                print("not a text file")
        else:
            dict_check={"error":-3}
            print("file not present in the path ")
            #print(dict)
    print(dict_check)
    return dict_check

#function to check the file presence
def file_search():
    print("File path:", sys.argv[1])
    if os.path.isfile(sys.argv[1]) :
        return True
    else:
        return False
 #print(os.path.isfile(sys.argv[1]))

# function to find the extension of file
def find_file_extension():
    head, tail = os.path.split(sys.argv[1])
    split_tup = os.path.splitext(tail)
    print("File name :", tail)
# extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
    return file_extension

#function to find the file size
def find_file_size():
    filesize = os.path.getsize(sys.argv[1])
    print('File size:', '{}'.format(filesize / 1000) + 'kb')
    return filesize

#function to extract keywords from file
def keyword_set():
    d = dict()
    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip()
            line = line.translate(line.maketrans(" ", " ", string.punctuation))
            word = line.split(" ")
            #print(word)

            for words in word:
                if words in d:
                    d[words] = d[words] + 1
                else:
                    d[words] = 1
    word_list=dict()
    dict_check = {'error':0}
    for key in list(d.keys()):
        word_list[key]=d[key]
        #print(word_list)

    dict_check['words']=word_list
    #print(dict_check)
    return dict_check



if __name__ == "__main__":
    main()