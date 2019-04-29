import tkinter as tki

def Button_Clicked():
    fPrinciple = float(txtPrinciple.get())
    fInterest = float(txtInterest.get())
    fCompMonth = float(txtCompMonth.get())
    fYear = float(txtYears.get())
    
    iYearToMonth = fYear * 12
    iTotalPeriod = iYearToMonth + fCompMonth
    
    fInterest = fInterest / 12
    fInterest = fInterest / 100 
    
    iCalc1 = fInterest * (1 + fInterest) ** iTotalPeriod
    iCalc2 = (1 + fInterest) ** iTotalPeriod - 1
    
    iTotal = fPrinciple * (iCalc1 / iCalc2)
    iTotal = round(iTotal, 2)
    iTotal = "$" + str(iTotal)
    
    lblCalculation = tki.Label(text = iTotal, fg = 'purple', bg = 'white', font = ('Comic Sans', 10))
    lblCalculation.place(x = 150, y = 150)
    
    def Exit_Process():
        window.destroy()
    
    btnExit = tki.Button(window, text = "Exit", command=Exit_Process)
    btnExit.place(x = 150, y = 250)

window = tki.Tk()
window.title('Amortization')
window.geometry('300x300')

txtPrinciple = tki.Entry(window, bd = 5)
txtPrinciple.place(x = 150, y = 12)
lblPrinciple = tki.Label(text = "principle", fg = 'maroon', bg = 'white', font = ('Comic Sans', 10))
lblPrinciple.place(x = 12, y = 12)

txtInterest = tki.Entry(window, bd = 5)
txtInterest.place(x = 150, y = 35)
lblInterest = tki.Label(text = "interest", fg = 'maroon', bg = 'white', font = ('Comic Sans', 10))
lblInterest.place(x = 12, y = 35)

txtCompMonth = tki.Entry(window, bd = 5)
txtCompMonth.place(x = 150, y = 58)
lblCompMonth = tki.Label(text = "compound period", fg = 'maroon', bg = 'white', font = ('Comic Sans', 10))
lblCompMonth.place(x = 12, y = 58)

txtYears = tki.Entry(window, bd = 5)
txtYears.place(x = 150, y = 81)
lblYears = tki.Label(text = "years", fg = 'maroon', bg = 'white', font = ('Comic Sans', 10))
lblYears.place(x = 12, y = 81)


btnCalculate = tki.Button(window, text = "Next", command=Button_Clicked)
btnCalculate.place(x = 75, y = 250)

tki.mainloop()
