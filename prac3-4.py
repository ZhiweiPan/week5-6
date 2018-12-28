import tkinter
import math
import tkinter.messagebox

class Calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(280,450)
        self.root.maxsize(280,480)
        self.root.title("Simplified Calculator")
        self.result = tkinter.StringVar()
        self.result.set(0)
        self.lists =[]
        self.ispressign = False
        self.layout()
        self.root.mainloop()

    def layout(self):
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd = 3, bg = "white" , font = ('宋体',30), anchor = "e", textvariable =self.result)
        show_label.place(x = 5,y =20 ,width = 270,height = 80)

        button_mc =tkinter.Button(self.root, text = "MC", command = self.wait)
        button_mc.place(x=5,y=100,width = 50,height = 50)

        button_mr = tkinter.Button(self.root, text="MR", command=self.wait)
        button_mr.place(x=60, y=100, width=50, height=50)

        button_ms = tkinter.Button(self.root, text="MS", command=self.wait)
        button_ms.place(x=115, y=100, width=50, height=50)

        button_mplus = tkinter.Button(self.root, text="M+", command=self.wait)
        button_mplus.place(x=170, y=100, width=50, height=50)

        button_mminus = tkinter.Button(self.root, text="M-", command=self.wait)
        button_mminus.place(x=225, y=100, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=5, y=155, width=50, height=50)

        button_ce = tkinter.Button(self.root, text="CE", command=lambda:self.result.set(0) )
        button_ce.place(x=5, y=155, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=60, y=155, width=50, height=50)

        button_C = tkinter.Button(self.root, text="C", command=self.sweepress)
        button_C.place(x=115, y=155, width=50, height=50)

        button_pm = tkinter.Button(self.root, text="±", command=self.pm)
        button_pm.place(x=170, y=155, width=50, height=50)

        button_sqr = tkinter.Button(self.root, text="√", command=self.sqr)
        button_sqr.place(x=225, y=155, width=50, height=50)

        button_del = tkinter.Button(self.root, text="←", command=self.dele_one)
        button_del.place(x=5, y=155, width=50, height=50)

        button_seven = tkinter.Button(self.root, text="7", command=lambda: self.pressnum("7"))
        button_seven.place(x=5, y=210, width=50, height=50)

        button_eight = tkinter.Button(self.root, text="8", command=lambda: self.pressnum("8"))
        button_eight.place(x=60, y=210, width=50, height=50)

        button_nine = tkinter.Button(self.root, text="9", command=lambda: self.pressnum("9"))
        button_nine.place(x=115, y=210, width=50, height=50)

        button_division = tkinter.Button(self.root, text="÷", command=lambda :self.presscalculate("/"))
        button_division.place(x=170, y=210, width=50, height=50)

        button_remainder = tkinter.Button(self.root, text="//", command=lambda :self.presscalculate("//"))
        button_remainder.place(x=225, y=210, width=50, height=50)

        button_four = tkinter.Button(self.root, text="4", command=lambda: self.pressnum("4"))
        button_four.place(x=5, y=265, width=50, height=50)


        button_five = tkinter.Button(self.root, text="5", command=lambda: self.pressnum("5"))
        button_five.place(x=60, y=265, width=50, height=50)

        button_six = tkinter.Button(self.root, text="6", command=lambda: self.pressnum("6"))
        button_six.place(x=115, y=265, width=50, height=50)

        button_mutip = tkinter.Button(self.root, text="×", command=lambda :self.presscalculate("×"))
        button_mutip.place(x = 170, y=265, width=50, height=50)

        button_recip = tkinter.Button(self.root, text="1/x", command=lambda: self.ds)
        button_recip.place(x=225, y=265, width=50, height=50)

        button_one = tkinter.Button(self.root, text="1", command=lambda: self.pressnum("1"))
        button_one.place(x=5, y=320, width=50, height=50)

        button_two = tkinter.Button(self.root, text="2", command=lambda: self.pressnum("2"))
        button_two.place(x=60, y=320, width=50, height=50)

        button_three = tkinter.Button(self.root, text="3", command=lambda: self.pressnum("3"))
        button_three.place(x=115, y=320, width=50, height=50)

        button_minus = tkinter.Button(self.root, text="-", command=lambda: self.presscalculate("-"))
        button_minus.place(x=170, y=320, width=50, height=50)

        button_eq = tkinter.Button(self.root, text="=", command=lambda: self.pressequal())
        button_eq.place(x=225, y=320, width=50, height=105)

        button_zero = tkinter.Button(self.root, text="0", command=lambda :self.pressnum("0"))
        button_zero.place(x=5, y=375, width=105, height=50)

        button_point= tkinter.Button(self.root, text=".", command=lambda: self.pressnum("."))
        button_point.place(x=115, y=375, width=50, height=50)

        button_plus = tkinter.Button(self.root, text="+", command=lambda: self.presscalculate())
        button_plus.place(x=170, y=375, width=50, height=50)


    def pressnum(self,num):
        if self.ispressign == False:
            pass
        else:
            self.result.set(0)
            self.ispressign = False
        if num == ".":
            num = "0."
        oldnum = self.result.get()
        if oldnum == "0":
            self.result.set(num)
        else:
            newnum = oldnum + num
            self.result.set(newnum)

    def presscalculate(self,sign):
        num = self.result.get()
        self.lists.append(num)
        self.lists.append(sign)
        self.ispressign = True

    def pressequal(self):
        curnum = self.result.get()
        self.lists.append(curnum)
        calculatestr = ''. join(self.lists)
        endnum = eval(calculatestr)
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispressign = True
        self.lists.clear()

    def wait(self):
        tkinter.messagebox.showinfo('','Sorry, This function is still tried to implement. Please wait!')

    def dele_one(self):
        if self.result.get() == '' or self.result.get() == "0":
            self.result.set('0')
            return
        else :
            num = len(self.result.get())
            if num >1 :
                strnum = self.result.get()
                strnum = strnum[0:num-1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def pm(self):
        strnum = self.result.get()
        if strnum[0] == "-":
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != "0":
            self.result.set('-' + strnum)


    def ds(self):
        dsnum = 1/int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispressign = True
        self.lists.clear()


    def sweepress(self):
        self.lists.clear( )
        self.result.set(0)

    def sqr(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == "0":
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispressign = True
            self.lists.clear()

mycalculator = Calculator()