#t_f = True or False
def arithmetic_arranger(problems, t_f):
    f1 = ''
    f2 = ''
    f3 = ''
    f4 = ''
    fl = ''

#Checking the amount of problems, making sure it's less than 5
    if len(problems) > 5 :
        print('Error, too many problems')
#Loop trough the problems
    for x in problems :
    #Split and put into seperate variebles
        fs = x.split()
        f = fs[0] #First Num
        s = fs[2] #Second Num
        o = fs[1] #Operator
    #Extra variebles to verify if numbers are only number and length of said numbers
        nm_f = f.isnumeric()
        nm_s = s.isnumeric()
        l1 = len(f)
        l2 = len(s)
    #Verify operator
        if o != '+' and o != '-':
            print('Error: Operator must be + or -') 
    #Verify that they are all digits    
        if nm_f is False or nm_s is False :
            print('Error: Numbers must only contain digits.')
    #Verify length is not greater then 4    
        elif max(l1,l2) > 4 :
            print('Error: Numbers cannot be more than four digits.')
    #Verify which number is bigger to determine width
        mn = max(l1,l2) + 2
    #Looks like we need a varieble to determine the whitespace
        w1 = None
        w2 = None
        if l1 >= l2 :
            w1 = mn - int(l1)
            w2 = int(l1) - int(l2)
        elif l1 < l2 :
            w1 = mn - int(l1)
            w2 = 0
    #Make the seperate lines
        space = (' ' * 4)
        l1 = (' ' * w1) + f + space
        l2 = o + ' ' + (' ' * w2) + s + space
        l3 = ("-" * mn) + space
        solved = None
        if o == '+':
            solved = str(int(f) + int(s)) + space
        else: 
            solved = str(int(f) - int(s)) + space
    #Bring everything together
        f1 += l1
        f2 += l2
        f3 += l3
        f4 += (' ' * 2) + solved
    #Check for state of t_f
    if t_f is True:
        fl = f1 + '\n'+ f2 +'\n' + f3 + '\n' + f4
    else:
        fl = f1 + '\n'+ f2 +'\n' + f3 + '\n'
    print(fl)
    return fl

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)