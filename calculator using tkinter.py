from array import *
import tkinter
window = tkinter.Tk()

window.title("CALCULATOR")

e = tkinter.Entry(window,width = 45,borderwidth = 5)
expression = ""




def button_click(number):
    ScreenContent = e.get()
    Entry_Len = len(ScreenContent)
    if (ScreenContent == ""):
        e.insert(Entry_Len,str(number))
    elif (ScreenContent == "0"):
        e.delete(0,Entry_Len)
        NewContent = str(ScreenContent[0:0])+str(number)
        e.insert(Entry_Len,str(number))
    else:
        e.insert(Entry_Len,str(number))



def pressZero(number):
    ScreenContent = e.get()
    Entry_Len = len(ScreenContent)
   # e.insert(Entry_Len,str(number))
    if (ScreenContent == ""):
        e.insert(0,str(number))
    elif (ScreenContent[0] == "0"):
        NewContent = str(ScreenContent[0:0]) + str(number)
        Entry_Len = len(ScreenContent)
        e.delete(0,Entry_Len)
        e.insert(0,NewContent)
    elif (ScreenContent[-1] != 0):
        Entry_Len = len(ScreenContent)
        e.insert(Entry_Len,str(number))

def Decimal():
    ScreenContent = e.get()
    Entry_Len = len(ScreenContent)
    if (ScreenContent == ""):
        e.insert(Entry_Len,"0.")
    elif (ScreenContent == "0"):
        e.insert(Entry_Len,".")
    else:
        i = -1
        Found = 0
        while(abs(i) <= Entry_Len and ScreenContent[i] != "+" and ScreenContent[i] != "-" and ScreenContent[i] != "*" and ScreenContent[i] != "/"):
            if (ScreenContent[i] == "."):
                Found = 1
                break
            i = i - 1
        if(Found == 0):
            e.insert(Entry_Len,".")
            return

            


'''
def Decimal1(number):
    ScreenContent = e.get()
    Entry_Len = len(ScreenContent)
    
    if (ScreenContent == ""):
        e.insert(Entry_Len,str(number))
    elif (ScreenContent[0] == "0"):
        e.delete(0,Entry_Len)
        NewContent = str(ScreenContent[0:0])+str(number)
        e.insert(0,NewContent)
    elif ((ScreenContent[0:Entry_Len]) != 0):
        Entry_Len = len(e.get())
        e.insert(Entry_Len,str("."))
    else :
        if (ScreenContent[0] != "0"):
            i = -1
            while(ScreenContent[i] != "+" or ScreenContent[i] != "-" or ScreenContent[i] != "*" or ScreenContent[i] != "/"):
                if (ScreenContent[i] == "."):
                    break
                i = i - 1
            e.insert(Entry_Len,".")
'''
def symbol(number):
    
    ScreenContent = e.get()
    if(ScreenContent[-1] == "+" or ScreenContent[-1] == "-" or ScreenContent[-1] == "*" or ScreenContent[-1] == "/"):
        NewContent = str(ScreenContent[0:-1]) + str(number)
        Entry_Len = len(e.get())
        e.delete(0,Entry_Len)
        e.insert(0,NewContent)
    else:
        Entry_Len = len(ScreenContent)
        e.insert(Entry_Len,str(number))




def clear():
    Entry_Len = len(e.get())
    e.delete(0,Entry_Len)





def Calculate():
    try:
        ScreenContent = e.get()
        Entry_Len = len(e.get())
        answer = eval(e.get())
        e.delete(0,Entry_Len)
        e.insert(0,str(answer))
    except ZeroDivisionError:
        e.delete(0,Entry_Len)
        e.insert(0,"Can't divide by Zero")
    except:
        e.delete(0,Entry_Len)
        e.insert(0,"Can't calculate.")





add = tkinter.Button(window,text = '+',fg = 'white',bg = 'red',width = 10,height = '2',command = lambda: symbol("+"))#.pack()
substract = tkinter.Button(window,text = '-',fg = 'white',bg = 'red',width = 10,height = '2',command = lambda: symbol("-"))#.pack()
multiply = tkinter.Button(window,text = '*',fg = 'white',bg = 'red',width = 10,height = '2',command = lambda: symbol("*"))#.pack()
divide = tkinter.Button(window,text = '/',fg = 'white',bg = 'red',width = 10,height = '2',command = lambda: symbol("/"))#.pack()

calculate = tkinter.Button(window,text = '=',fg = 'white',bg = 'red',width = 10,height = '2',command = Calculate)#.pack()

one = tkinter.Button(window,text = '1',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(1))#.pack()
two = tkinter.Button(window,text = '2',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(2))#.pack()
three = tkinter.Button(window,text = '3',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(3))#.pack()
four = tkinter.Button(window,text = '4',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(4))#.pack()
five = tkinter.Button(window,text = '5',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(5))#.pack()
six = tkinter.Button(window,text = '6',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(6))#.pack()
seven = tkinter.Button(window,text = '7',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(7))#.pack()
eight = tkinter.Button(window,text = '8',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(8))#.pack()
nine = tkinter.Button(window,text = '9',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: button_click(9))#.pack()
zero = tkinter.Button(window,text = '0',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: pressZero(0))#.pack()

decimal = tkinter.Button(window,text = '.',fg = 'black',bg = 'red',width = 10,height = '2',command = lambda: Decimal())#.pack()

clear = tkinter.Button(window,text = 'clear',fg = 'black',bg = 'red',width = 10,height = '2',command = clear)#.pack()

e.grid(row= 0,column = 0,columnspan=4)

add.grid(row=1 , column = 3)
substract.grid(row=2 , column = 3)
multiply.grid(row=3 , column = 3)
divide.grid(row=4 , column = 3)
calculate.grid(row=4 , column = 2)

one.grid(row=1 , column = 0)
two.grid(row=1 , column = 1)
three.grid(row=1 , column = 2)
four.grid(row=2, column = 0)
five.grid(row=2 , column = 1)
six.grid(row=2 , column = 2)
seven.grid(row=3 , column = 0)
eight.grid(row=3 , column = 1)
nine.grid(row=3 , column = 2)
zero.grid(row=4 , column = 1)
decimal.grid(row=4,column = 0)

clear.grid(row=5,column=0)

window.mainloop()
