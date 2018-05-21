from tkinter import *
from random import randint
from openpyxl import *

def callback(myanswer):
    def wrapper(answer=myanswer):
        global score, qvar
        print(answer[1], qvar[1])
        if answer[1]==qvar[1]:
            score.set(score.get()+1)
            configValues()

        else:
            score.set(0)
                        
    return wrapper

def configValues():
        global qvar, a1var, a2var, a3var, a4var, a5var, a6var, a7var, a8var, score, wb, sheet
        
        rand = str(randint(1,26432))
        while sheet['F'+rand].value == None:
            rand = str(randint(1,26432))  
        qvar[0].set(sheet['G'+ rand].value)
        qvar[1] = rand

        arr = [a1var, a2var, a3var, a4var, a5var, a6var, a7var, a8var]
        
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+rand].value)
        arr[index][1] = rand
        arr.pop(index)

        val = str(randint(1,26432))
        while sheet['F'+val].value == None:
            val = str(randint(1,26432))

        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val].value)
        arr[index][1] = val
        arr.pop(index)
        
        val2 = str(randint(1,26432))
        while val==val2 or sheet['F'+val2].value == None:
            val2 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val2].value)
        arr[index][1] = val2
        arr.pop(index)

        val3 = str(randint(1,26432))
        while val==val2 or val==val3 or val2==val3  or sheet['F'+val3].value == None:
            val3 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val3].value)
        arr[index][1] = val3
        arr.pop(index)

        val4 = str(randint(1,26432))
        while val==val2 or val==val3 or val==val4 or val2==val3 or val2==val4 or val3==val4 or sheet['F'+val4].value == None:
            val4 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val4].value)
        arr[index][1] = val4
        arr.pop(index)

        val5 = str(randint(1,26432))
        while val==val2 or val==val3 or val==val4 or val2==val3 or val2==val4 or val3==val4 or val==val5 or val2==val5 or val3==val5 or val4 == val5 or sheet['F'+val5].value == None:
            val5 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val5].value)
        arr[index][1] = val5
        arr.pop(index)

        val6 = str(randint(1,26432))
        while val==val2 or val==val3 or val==val4 or val2==val3 or val2==val4 or val3==val4 or val==val5 or val2==val5 or val3==val5 or val4 == val5 or val==val6 or val2==val6 or val3==val6 or val4==val6 or val5==val6 or sheet['F'+val6].value == None:
            val6 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val6].value)
        arr[index][1] = val6
        arr.pop(index)

        val7 = str(randint(1,26432))
        while val==val2 or val==val3 or val==val4 or val2==val3 or val2==val4 or val3==val4 or val==val5 or val2==val5 or val3==val5 or val4 == val5 or val==val6 or val2==val6 or val3==val6 or val4==val6 or val5==val6 or val==val7 or val2==val7 or val3==val7 or val4==val7 or val5==val7 or val6==val7 or sheet['F'+val7].value == None:
            val7 = str(randint(1,26432))
            
        index = randint(0,len(arr)-1)
        arr[index][0].set(sheet['F'+val7].value)
        arr[index][1] = val7
        arr.pop(index)
        
if __name__ == '__main__':
    root = Tk()
    qvar = [StringVar(),IntVar()]
    a1var = [StringVar(),IntVar()]
    a2var = [StringVar(),IntVar()]
    a3var = [StringVar(),IntVar()]
    a4var = [StringVar(),IntVar()]
    a5var = [StringVar(),IntVar()]
    a6var = [StringVar(),IntVar()]
    a7var = [StringVar(),IntVar()]
    a8var = [StringVar(),IntVar()]
    score = IntVar()
    score.set(0)
    wb = load_workbook('verbs.xlsx')
    sheet = wb.get_sheet_by_name('german verbs backup 9800')
    configValues()
                                             
    question = Label(root, textvariable=qvar[0], width = 90, wraplength=660, font=25).grid(row=0, column=1, columnspan=2)
    tlbutton = Button(root, textvariable=a1var[0], width = 45, wraplength=330, font=25, command=callback(a1var)).grid(row =1, column=1)
    trbutton = Button(root, textvariable=a2var[0], width = 45, wraplength=330, font=25, command=callback(a2var)).grid(row =1, column=2)
    blbutton = Button(root, textvariable=a3var[0], width = 45, wraplength=330, font=25, command=callback(a3var)).grid(row =2, column=1)
    brbutton = Button(root, textvariable=a4var[0], width = 45, wraplength=330, font=25, command=callback(a4var)).grid(row =2, column=2)
    bl1button = Button(root, textvariable=a5var[0], width = 45, wraplength=330, font=25, command=callback(a5var)).grid(row =3, column=1)
    br1button = Button(root, textvariable=a6var[0], width = 45, wraplength=330, font=25, command=callback(a6var)).grid(row =3, column=2)
    bl2button = Button(root, textvariable=a7var[0], width = 45, wraplength=330, font=25, command=callback(a7var)).grid(row =4, column=1)
    br2button = Button(root, textvariable=a8var[0], width = 45, wraplength=330, font=25, command=callback(a8var)).grid(row =4, column=2)
    gamescore = Button(root, textvariable=score, width = 90, wraplength=660, font=25).grid(row=5, column=1, columnspan=2)

    root.mainloop()
