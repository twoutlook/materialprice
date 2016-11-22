# http://blog.mariokuschel.info/?p=364

import re
import sys

def main():

        file = open(r"maillog","r")
        text = file.read()
        file.close()
        tuples = re.findall(r"to=<(\w+@\w+.\w+)>",text)
        tuples = list(tuples)

        unique_EMail = []
        for i in range (0,len(tuples)):
                if tuples[i] not in unique_EMail:
                        unique_EMail.append(tuples[i])

        outputfile = open("p2output.txt","w")
        for i in range (0,len(unique_EMail)):
                outputfile.write(unique_EMail[i] + '\n')
        outputfile.close()
"""
        for sorted_tuples in tuples:
                (username,domain,tld) = sorted_tuples
                sorted_tuples = list(sorted_tuples)
                lstEMail = []
                lstEMail.append(sorted_tuples[0]+"@"+sorted_tuples[1]+"."+sorted_tuples[2])
                print lstEMail

"""
if __name__ == '__main__':
  main()
