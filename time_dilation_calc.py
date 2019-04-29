import tkinter
import math

window = tkinter.Tk()
window.title("Time Dilation")
window.geometry('500x300')

def Time_Funct():
    fTime = float(txtTime.get())
    fVelocity = float(txtVelocity.get())
    
    iCalc1 = (fVelocity ** 2) / (186000 ** 2)
    iCalc2 = math.sqrt(iCalc1) - 1
    iCalc3 = fTime / iCalc2
    
    lblResult = tkinter.Label(window, font=('Constantia', 15, 'bold'), fg='purple', text=iCalc3)
    lblResult.place(x=180, y=190)

txtTime = tkinter.Entry(window, font=('Constantia', 15, 'bold'))
txtTime.place(x=200, y=10)
txtVelocity = tkinter.Entry(window, font=('Constantia', 15, 'bold'))
txtVelocity.place(x=200, y=60)

lblTime = tkinter.Label(text="Time", fg='steelblue', font=('Constantia', 15, 'bold'))
lblTime.place(x=100, y=10)
lblVelocity = tkinter.Label(text="Velocity", fg='steelblue', font=('Constantia', 15, 'bold'))
lblVelocity.place(x=100, y=60)

btnCalc = tkinter.Button(window, text="Calculate",  fg='purple', font=('Constantia', 20, 'bold'), command= Time_Funct)
btnCalc.place(x=200, y=120)

window.mainloop()
