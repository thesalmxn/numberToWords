#2
di11 = {
    '10':"ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "ninteen"
}
di = {
    '0': "",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}
di2 = {
    '0': "",
    '2': "twenty",
    '3': "thirty",
    '4': "forty",
    '5': "fifty",
    '6': "sixty",
    '7': "seventy",
    '8': "eighty",
    '9': "ninety"
}
n = int(input())
l = len(str(n))
print(l)


def sallu(n,l):
    res = []
    if(l == 1):
        res.append(di[str(n)[::-1][0]])
        
        
    elif(l == 2):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])
            
            
    elif(l == 3):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        
    elif(l == 4):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")
        res.append(di[str(n)[::-1][3]])
        
        
    elif(l == 5):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        
        
    elif(l == 6):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        res.append("hundred")
        res.append(di[str(n)[::-1][5]])
        
        
    elif(l == 7):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        res.append("hundred")
        res.append(di[str(n)[::-1][5]])
        
        #millions
        res.append("million")
        res.append(di[str(n)[::-1][6]])
    
    
    elif(l == 8):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        res.append("hundred")
        res.append(di[str(n)[::-1][5]])
        
        #millions
        res.append("million")
        
        if(str(n)[::-1][7]== '1'):
            res.append(di11[str(n)[::-1][6:8][::-1]])
        else:
            res.append(di[str(n)[::-1][6]])
            res.append(di2[str(n)[::-1][7]])
    
    
    elif(l == 9):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        res.append("hundred")
        res.append(di[str(n)[::-1][5]])
        
        #millions
        res.append("million")
        
        if(str(n)[::-1][7]== '1'):
            res.append(di11[str(n)[::-1][6:8][::-1]])
        else:
            res.append(di[str(n)[::-1][6]])
            res.append(di2[str(n)[::-1][7]])
        res.append("hundred")
        res.append(di[str(n)[::-1][8]])
    
    
    elif(l == 10):
        if(str(n)[::-1][1]== '1'):
            res.append(di11[str(n)[::-1][0:2][::-1]])
        else:
            res.append(di[str(n)[::-1][0]])
            res.append(di2[str(n)[::-1][1]])

        #hundreds
        res.append("hundred")
        res.append(di[str(n)[::-1][2]])
        
        #thousands
        res.append("thousand")

        if(str(n)[::-1][4]== '1'):
            res.append(di11[str(n)[::-1][3:5][::-1]])
        else:
            res.append(di[str(n)[::-1][3]])
            res.append(di2[str(n)[::-1][4]])
        res.append("hundred")
        res.append(di[str(n)[::-1][5]])
        
        #millions
        res.append("million")
        
        if(str(n)[::-1][7]== '1'):
            res.append(di11[str(n)[::-1][6:8][::-1]])
        else:
            res.append(di[str(n)[::-1][6]])
            res.append(di2[str(n)[::-1][7]])
        res.append("hundred")
        res.append(di[str(n)[::-1][8]])
    
        #billions
        res.append("billion")

        res.append(di[str(n)[::-1][9]])
    return res
    
    
    
    
    
    
    
    
    
# if(str(n)[::-1][1]== '1'):
#     res.append(di11[str(n)[::-1][0:2][::-1]])
# else:
#     res.append(di[str(n)[::-1][0]])
#     res.append(di2[str(n)[::-1][1]])

# #hundreds
# res.append("hundred")
# res.append(di[str(n)[::-1][2]])

# #thousands
# res.append("thousand")

# if(str(n)[::-1][4]== '1'):
#     res.append(di11[str(n)[::-1][3:5][::-1]])
# else:
#     res.append(di[str(n)[::-1][3]])
#     res.append(di2[str(n)[::-1][4]])
# res.append("hundred")
# res.append(di[str(n)[::-1][5]])

# #millions
# res.append("million")

# if(str(n)[::-1][7]== '1'):
#     res.append(di11[str(n)[::-1][6:8][::-1]])
# else:
#     res.append(di[str(n)[::-1][6]])
#     res.append(di2[str(n)[::-1][7]])
# res.append("hundred")
# res.append(di[str(n)[::-1][8]])
    
# #billions
# res.append("billion")

# res.append(di[str(n)[::-1][9]])

li_res = sallu(n,l)
# print(li_res)

for i in li_res[::-1]:
    print(i,end=" ")
