import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fromm", type=str)
parser.add_argument("to", type=str)
parser.add_argument("--operation", choices=["s"], default="s")

args = parser.parse_args()


a = str(input("Please enter a text: "))

#type casting the string into a list
a = list(a)


#split arguments incase of a range of characters (i.e., A-Z)
if (len(args.fromm), len(args.to)) == (3,3):

    #Get the range of characters 
    fromm = args.fromm.split('-')
    to = args.to.split('-')
    
    #Creates a list of the characters in both ranges
    range_1 = [chr(i) for i in range(ord(fromm[0]), ord(fromm[1])+1)]
    range_2 = [chr(i) for i in range(ord(to[0]), ord(to[1])+1)]

    for i in range(len(a)):

        #See if the current element is in the first range. For example, if the (from) range is [A-Z], then the 'x' in "Axe" should not be translated.
        if a[i] in range_1:

            #Find the position of the current character in the range. For example, the 'b' in Bob lies in index 1 of [a-z]
            position = range_1.index(a[i])

            #Edge case where the second set is smaller than the first, prevents index error
            #Implement try
            
            # if temp >= len(range_2):
            #     a[i] = range_2[len(range_2)-1]
            # else:
            #     a[i] = range_2[temp]

            try:
                a[i] = range_2[position]
            except IndexError:
                a[i] = range_2[len(range_2)-1]


    a = "".join(a)
    print (a)    

if args.operation == "s":
    for i in range(len(a)):
        if a[i] == args.fromm:
            a[i] = args.to

    a = ''.join(a)
    print(a)

    
