def add_time(x,y,z=None):
    days = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
    second_half = {12:'12',13:'1',14:'2',15:'3',16:'4',17:'5',18:'6',19:'7',20:'8',21:'9',22:'10',23:'11',0:'12'}

    split = x.split(' ')
    t = split[0]
    m_e = split[1]
    s_split = t.split(':')
    hour = s_split[0]
    mns = s_split[1]
    if m_e == 'PM':
        hour = list(second_half.keys())[list(second_half.values()).index(hour)]
    s_plit2 = y.split(':')
    a_hour = s_plit2[0]
    a_mns = s_plit2[1]
    new_hour = int(hour) + int(a_hour)
    new_num = int(mns) + int(a_mns)
    #print(new_hour) #Test to check the current time
    day_count = 0

    if new_num > 60:
        while new_num > 60:
            new_hour += 1
            new_num = new_num - 60
    if new_hour > 24:
        while new_hour >= 24:
            new_hour -= 24
            day_count += 1
    
    if len(str(new_num)) == 1:
        new_num = '0' + str(new_num)
    #print(new_hour,new_num, ':',day_count)

    if new_hour in second_half:
        if new_hour == 0:
            f_time = (f'{second_half[new_hour]}:{new_num} AM')
        else:
            f_time = (f'{second_half[new_hour]}:{new_num} PM')
        
    else:
        f_time = (f'{new_hour}:{new_num} AM')
        
    if z != None:
        new_z = z.lower()
        final_st = new_z.replace(new_z[0], new_z[0].upper())
        final_st = list(days.keys())[list(days.values()).index(final_st)] + day_count
        if final_st > 7:
            while final_st > 7:
                final_st -= 7
        f_time += f', {days[final_st]}'
        #print(f_time)


    if day_count > 0:
        if day_count == 1:
            f_time += ' (next day)'
       #     print(f_time)
        else:    
            f_time += f' ({day_count} days later)'
       #     print(f_time)
    print(f_time)
    
    
    

# Use add_Time('3:00 PM', '3:30')
add_time('2:59 AM', '24:00', 'saturDay')