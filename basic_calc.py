import tkinter

window = tkinter.Tk()
window.title("Calculator")
window.geometry('400x350')

txtBox = tkinter.Entry(window, fg='purple', justify='right', font=('Constantia', 20), width=19)
txtBox.place(x=86, y=15)

def Button_Clicked(whichClick):
    txtBox.insert("end", whichClick)
    
def Calc_Equation():
    try:
        sEquation = str(txtBox.get())
        txtBox.delete(0, "end")
        sEquation = eval(sEquation)
        txtBox.insert(0, sEquation)
    except ZeroDivisionError:
        txtBox.delete(0, "end")
        txtBox.insert(0, "Cannot Divide By Zero")
        
def Clear_Box():
    txtBox.delete(0, "end")        
    
btnOne = tkinter.Button(text='1', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(1))
btnOne.place(x=10, y=70)
btnTwo = tkinter.Button(text='2', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(2))
btnTwo.place(x=60, y=70)
btnThree = tkinter.Button(text='3', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(3))
btnThree.place(x=110, y=70)
btnFour = tkinter.Button(text='4', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(4))
btnFour.place(x=10, y=120)
btnFive = tkinter.Button(text='5', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(5))
btnFive.place(x=60, y=120)
btnSix = tkinter.Button(text='6', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(6))
btnSix.place(x=110, y=120)
btnSeven = tkinter.Button(text='7', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(7))
btnSeven.place(x=10, y=170)
btnEight = tkinter.Button(text='8', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(8))
btnEight.place(x=60, y=170)
btnNine = tkinter.Button(text='9', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(9))
btnNine.place(x=110, y=170)
btnZero = tkinter.Button(text='0', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked(0))
btnZero.place(x=60, y=220)
    
btnPlus = tkinter.Button(text='+', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked("+"))
btnPlus.place(x=280, y=70)
btnMinus = tkinter.Button(text='-', font=('Constantia',15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked("-"))
btnMinus.place(x=330, y=70)
btnMultiply = tkinter.Button(text='*', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked("*"))
btnMultiply.place(x=280, y=120)
btnDivide = tkinter.Button(text="/", font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Button_Clicked("/"))
btnDivide.place(x=330, y=120)
btnEqual = tkinter.Button(text="=", font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Calc_Equation())
btnEqual.place(x=280, y=170)
    
btnClear = tkinter.Button(text='c', font=('Constantia', 15, 'bold'), justify='center', fg='maroon', width=3, height=1, command=lambda:Clear_Box())
btnClear.place(x=330, y=170)
    
window.mainloop()
