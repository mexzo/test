#-------------------------------------------------------------------------------
# Name:        Test
# Purpose:
#
# Author:      Horatio
#
# Created:     28/05/2019

#-------------------------------------------------------------------------------

import operator
filepath='C:/a/lorem.txt'


def read_file(file_path):
    content={}
    f=open(file_path, "r")
    data=f.read()
    print(data)
    data_len=len(data)

    ## This is for words
    data1=data.lower()
    words=data1.split()

    e={}

    for item in words:
        j=e.keys()
        if item in j:
            e[item] +=1   # Miss Out the   += that why i had 1 as my result
        else:
            e[item]=1

    my_result=sorted(e.items(), key=operator.itemgetter(1), reverse=True)
    print (my_result)




    return my_result












    #content.append(data)






    return

if __name__ == '__main__':
    read_file(filepath)


