from tkinter import *
import random      #os
from math import sqrt
from tkinter import messagebox
class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(background='black')
        self.root.title("Billing System")
        title = Label(self.root, text="BILLING SYSTEM", bd=12,bg='turquoise', fg='white',relief=GROOVE, font=("times new roman", 30, "bold"),
                      pady=5, padx=10).pack(fill=X)
        self.totalCosmatic = 0.0
        self.totalGrocceries = 0.0
        self.totalOthers = 0.0
        self.list_Cos = []
        self.list_Grocery = []
        self.List_Others = []
        # customer details
        F1 = LabelFrame(self.root, text="customer details", bd=12, relief=GROOVE,bg='turquoise')
        F1.place(x=0, y=80, width=990)
        self.Cust_N = StringVar()
        self.Cust_PN = StringVar()
        self.Bill_N = StringVar()
        cnameL = Label(F1, text="Customer Name", bg='turquoise', font=18).grid(row=0, column=0)
        cnameT = Entry(F1, width=15, bd=7, textvariable=self.Cust_N,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)
        cphnL = Label(F1, text="Phone NO.",  bg='turquoise', font=18).grid(row=0, column=2)
        cphnT = Entry(F1, width=15, bd=7, textvariable=self.Cust_PN, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)
        Bill_no = Label(F1, text="Bill number",  bg='turquoise', font=18).grid(row=0, column=4)
        Bill_noT = Entry(F1, width=15, bd=7, textvariable=self.Bill_N,relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)
        search = Button(F1, text="SEARCH", font=18, bd=7,  bg='turquoise',relief=GROOVE).grid(row=0, column=6, padx=10, pady=5)

        # Cosmetics
        F2 = LabelFrame(self.root, text="Cosmetics", bd=12,  bg='turquoise', fg='white', relief=GROOVE)
        F2.place(x=0, y=170, height=380, width=330)
        QUANTITY = Label(F2, text="Quantity", bg='turquoise').grid(row=0, column=1, padx=0, pady=5)
        self.B_soapQ = IntVar()
        self.B_soapP = IntVar()
        PRICE = Label(F2, text="Price",  bg='turquoise',font=15).grid(row=0, column=2, padx=10, pady=5)
        BathSL = Label(F2, text="Bath Soap",  bg='turquoise', font=18).grid(row=1, column=0, padx=10, pady=5)
        BathSQ = Entry(F2, width=5, bd=7, textvariable= self.B_soapQ, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)
        BathSP = Entry(F2, width=15, bd=7, textvariable= self.B_soapP, relief=SUNKEN).grid(row=1, column=2, padx=5, pady=5)
        self.F_cream = IntVar()
        self.F_creamP=IntVar()
        FaceL = Label(F2, text="Face Cream",  bg='turquoise',font=18).grid(row=2, column=0, padx=10, pady=5)
        FaceQ = Entry(F2, width=5, bd=7, textvariable= self.F_cream,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=5)
        FaceP = Entry(F2, width=15, bd=7,textvariable= self.F_creamP, relief=SUNKEN).grid(row=2, column=2, padx=5, pady=5)
        self.H_shampoo=IntVar()
        self.H_shmampooP = IntVar()
        Hair_SL = Label(F2, text="Hair Shampoo",  bg='turquoise', font=18).grid(row=3, column=0, padx=10, pady=5)
        Hair_STQ= Entry(F2, width=5, bd=7, textvariable= self.H_shampoo, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=5)
        Hair_STP = Entry(F2, width=15, bd=7, textvariable= self.H_shmampooP, relief=SUNKEN).grid(row=3, column=2, padx=5, pady=5)
        self.HGEl = IntVar()
        self.HGELP = IntVar()
        Hair_GL = Label(F2, text="Hair GEL/Wex",  bg='turquoise',font=18).grid(row=4, column=0, padx=10, pady=5)
        Hair_GTQ = Entry(F2, width=5, bd=7,textvariable= self.HGEl, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=5)
        Hair_GTP = Entry(F2, width=15, bd=7, textvariable= self.HGELP,relief=SUNKEN).grid(row=4, column=2, padx=5, pady=5)
        self.Fwwash = IntVar()
        self.FwwashP = IntVar()
        FaceWL = Label(F2, text="Face wash",  bg='turquoise',font=18).grid(row=5, column=0, padx=10, pady=5)
        FaceWQ = Entry(F2, width=5, bd=7, textvariable= self.Fwwash, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=5)
        FaceWP = Entry(F2, width=15, bd=7, textvariable= self.FwwashP,relief=SUNKEN).grid(row=5, column=2, padx=5, pady=5)
        self.B_losh = IntVar()
        self.B_loshP = IntVar()
        BodyLL = Label(F2, text="Body Loshan",  bg='turquoise',font=18).grid(row=6, column=0, padx=10, pady=5)
        BodyLQ = Entry(F2, width=5, bd=7, textvariable= self.B_losh,relief=SUNKEN).grid(row=6, column=1, padx=10, pady=5)
        BodyLP = Entry(F2, width=15, bd=7, textvariable= self.B_loshP, relief=SUNKEN).grid(row=6, column=2, padx=5, pady=5)

        # Grocceries
        # Cosmetics
        F3 = LabelFrame(self.root, text="Grocerries",  bg='turquoise',bd=12, relief=GROOVE)
        F3.place(x=330, y=170, height=380, width=330)
        self.Rice = IntVar()
        G1 = Label(F3, text="Rice", font=18, bg='turquoise', fg='black',).grid(row=0, column=0, padx=10, pady=5)
        rice = Entry(F3, width=20, bd=7, textvariable= self.Rice, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)
        self.Sugar = IntVar()
        G2 = Label(F3, text="Sugar", bg='turquoise', font=18).grid(row=1, column=0, padx=10, pady=5)
        Sugar = Entry(F3, width=20, bd=7, textvariable= self.Sugar, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)
        self.Food_oil = IntVar()
        G3 = Label(F3, text="Food oil", bg='turquoise', font=18).grid(row=2, column=0, padx=10, pady=5)
        Food_oil = Entry(F3, width=20, bd=7, textvariable= self.Food_oil, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=5)
        self.Wheat=IntVar()
        G4 = Label(F3, text="Wheat", bg='turquoise', font=18).grid(row=3, column=0, padx=10, pady=5)
        Wheat = Entry(F3, width=20, bd=7, textvariable= self.Wheat, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=5)
        self.Daal = IntVar()
        G5 = Label(F3, text="Daal", bg='turquoise', font=18).grid(row=4, column=0, padx=10, pady=5)
        DAAL = Entry(F3, width=20, bd=7, textvariable= self.Daal, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=5)
        self.Tea = IntVar()
        G6 = Label(F3, text="Tea/Coffee", bg='turquoise', font=18).grid(row=5, column=0, padx=10, pady=5)
        Tea = Entry(F3, width=20, bd=7, textvariable= self.Tea, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=5)

        # +_______________________ oTHERS_________
        F4 = LabelFrame(self.root, text="OTHERS",bg='turquoise', bd=12, relief=GROOVE)
        F4.place(x=660, y=170, height=380, width=330)
        self.ColdD = IntVar()
        O1 = Label(F4, text="Cold Drinks", bg='turquoise', font=18).grid(row=0, column=0, padx=10, pady=5)
        coldD = Entry(F4, width=20, bd=7, textvariable= self.ColdD, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)
        self.Noodle = IntVar()
        o2 = Label(F4, text="Noodles", bg='turquoise', font=18).grid(row=1, column=0, padx=10, pady=5)
        Noodles = Entry(F4, width=20, bd=7, textvariable= self.Noodle, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)
        self.snack = IntVar()
        o3 = Label(F4, text="SNACKS", bg='turquoise', font=18).grid(row=2, column=0, padx=10, pady=5)
        snacks = Entry(F4, width=20, bd=7, textvariable= self.snack, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=5)
        self.Sauces = IntVar()
        o4 = Label(F4, text="Sauces", bg='turquoise', font=18).grid(row=3, column=0, padx=10, pady=5)
        sauces = Entry(F4, width=20, bd=7, textvariable= self.Sauces, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=5)
        self.Namkeen = IntVar()
        o5 = Label(F4, text="Namkeen", bg='turquoise', font=18).grid(row=4, column=0, padx=10, pady=5)
        namkeen = Entry(F4, width=20, bd=7, textvariable= self.Namkeen, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=5)
        self.Other = IntVar()
        o6 = Label(F4, text="Other", bg='turquoise', font=18).grid(row=5, column=0, padx=10, pady=5)
        other = Entry(F4, width=20, bd=7, textvariable= self.Other, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=5)

        # _____________bill area_________________

        F5 = Frame(self.root, bd=10, relief=GROOVE, bg='white')
        F5.place(x=995, y=320, width=350, height=380)  # 80
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bg='white', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH)

        #        Total area

        F6 = Frame(self.root, bd=10, relief=GROOVE)
        F6.place(x=0, y=550, width=660, height=150)
        self.cosmaticT = StringVar()
        total_c = Label(F6, text='Cosamtic Total', font=18,).grid(row=0, column=0, padx=5, pady=6)
        Total_C = Entry(F6, width=18, bd=7, textvariable=self.cosmaticT, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=6)
        self.groccerT = StringVar()
        total_g = Label(F6, text='Groccery Total', font=18,).grid(row=1, column=0, padx=5, pady=6)
        Total_G = Entry(F6, width=18, bd=7, textvariable=self.groccerT, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=6)
        self.OtherTotal = StringVar()
        total_o = Label(F6, text='OTHERS Total', font=18,).grid(row=2, column=0, padx=5, pady=6)
        Total_O = Entry(F6, width=18, bd=7, textvariable=self.OtherTotal, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=6)

        total_cT = Label(F6, text='Cosamtic Total TAX', font=18, ).grid(row=0, column=3, padx=5, pady=6)
        Total_CT = Entry(F6, width=18, bd=7, relief=SUNKEN).grid(row=0, column=4, padx=10, pady=6)
        total_gT = Label(F6, text='Groccery Total TAX', font=18, ).grid(row=1, column=3, padx=5, pady=6)
        Total_GT = Entry(F6, width=18, bd=7, relief=SUNKEN).grid(row=1, column=4, padx=10, pady=6)
        total_oT = Label(F6, text='OTHERS Total TAX', font=18, ).grid(row=2, column=3, padx=5, pady=6)
        Total_OT = Entry(F6, width=18, bd=7, relief=SUNKEN).grid(row=2, column=4, padx=10, pady=6)

        btn_f = LabelFrame(self.root,bd=10,relief=GROOVE)
        btn_f.place(x=660,y=550,height=150,width=330)
        total = Button(btn_f, text='TOTAL', command=self.Total, font=18,bd=12,height=1,width=9,bg='light blue').grid(row=0,column=0,padx=10,pady=7)
        Genrate = Button(btn_f, text='Genrate Bill', font=18, command=self.Bill_Area, bd=12, height=1, width=9, bg='light blue').grid(row=0,column=1, padx=10,pady=7)
        clear = Button(btn_f, text='CLEAR', font=18, command=self.clear_bill, bd=12, height=1, width=9, bg='light blue').grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=7)
        exit = Button(btn_f, text='EXIT', command=self.EXIT,font=18, bd=12,height=1, width=9, bg='light blue').grid(row=1,
                                                                                                               column=1,
                                                                                                               padx=10,
                                                                                                               pady=7)
        self.Welcome_bill()
        self.Calculator()
    def Total(self):
        self.list_Cos = [self.B_soapQ.get()*self.B_soapP.get(),
                                    self.F_cream.get()*self.F_creamP.get(),
                                    self.H_shampoo.get()*self.H_shmampooP.get(),
                                    self.HGEl.get()*self.HGELP.get(),
                                    self.Fwwash.get() * self.FwwashP.get(),
                                    self.B_losh.get()*self.B_loshP.get()]
        self.totalCosmatic = float(sum(self.list_Cos))
        self.cosmaticT.set(str(self.totalCosmatic))

        self.list_Grocery = [(self.Rice.get() * 32),
                                   (self.Sugar.get() * 40),
                                   (self.Food_oil.get() * 35),
                                   (self.Wheat.get() * 15),
                                    (self.Daal.get() * 80),
                                   (self.Tea.get() * 30)]
        self.totalGrocceries = float(sum(self.list_Grocery))
        self.groccerT.set(str(self.totalGrocceries))
        #_____________OTHERS
        self.List_Others = [self.ColdD.get() * 30,
                                     self.Noodle.get() * 40,
                                     self.snack.get() * 32,self.Sauces.get() * 15,
                                     self.Namkeen.get() * 80,
                                     self.Other.get() * 35]
        self.totalOthers = float(sum(self.List_Others))
        self.OtherTotal.set(str(self.totalOthers))
    def Welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome XYZ Retail Shop")
        self.textarea.insert(END,f"\n Bill Number : {self.Bill_N.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.Cust_N.get()}")
        self.textarea.insert(END, f"\n Customer Phone NO. : {self.Cust_PN.get()}")
        self.textarea.insert(END, f"\n--------------------------------------")
        self.textarea.insert(END, f"\n Produsts\t\tQty\t\tPrice")
        self.textarea.insert(END, f"\n--------------------------------------")
    def Bill_Area(self):
        self.Bill_N.set(random.randint(1000,100000))
        if self.Cust_N.get() =="":
            messagebox.showerror("Error","customer name is must")
        else:
            self.Welcome_bill()
            if (self.B_soapQ.get() != 0 and self.B_soapP.get() !=0):
                self.textarea.insert(END, f"\n Bath Soap\t\t{self.B_soapQ.get()}\t\t{self.list_Cos[0]}")
            if (self.F_cream.get() != 0 and self.F_creamP.get() !=0):
                self.textarea.insert(END, f"\n Face cream\t\t{self.F_cream.get()}\t\t{self.list_Cos[1]}")
            if (self.H_shampoo.get() != 0 and self.H_shmampooP.get() !=0):
                self.textarea.insert(END, f"\n Hair shampoo\t\t{self.H_shampoo.get()}\t\t{self.list_Cos[2]}")
            if (self.HGEl.get() != 0 and self.HGELP.get() !=0):
                self.textarea.insert(END, f"\n Hair GEL/WAX\t\t{self.HGEl.get()}\t\t{self.list_Cos[3]}")
            if (self.Fwwash.get() != 0 and self.FwwashP.get() !=0):
                self.textarea.insert(END, f"\n Face Wash\t\t{self.Fwwash.get()}\t\t{self.list_Cos[4]}")
            if (self.B_losh.get() != 0 and self.B_loshP.get() !=0):
                self.textarea.insert(END, f"\n Body Loshan\t\t{self.B_losh.get()}\t\t{self.list_Cos[5]}")

            # Groccery
            if (self.Rice.get() != 0):
                self.textarea.insert(END, f"\n Rice\t\t{self.Rice.get()}\t\t{self.list_Grocery[0]}")
            if (self.Sugar.get() != 0):
                self.textarea.insert(END, f"\n Sugar\t\t{self.Sugar.get()}\t\t{self.list_Grocery[1]}")
            if (self.Food_oil.get() != 0 ):
                self.textarea.insert(END, f"\n Food Oil\t\t{self.Food_oil.get()}\t\t{self.list_Grocery[2]}")
            if (self.Wheat.get() != 0):
                self.textarea.insert(END, f"\n Wheat\t\t{self.Wheat.get()}\t\t{self.list_Grocery[3]}")
            if (self.Daal.get() != 0):
                self.textarea.insert(END, f"\n Daal\t\t{self.Daal.get()}\t\t{self.list_Grocery[4]}")
            if (self.Tea.get() != 0):
                self.textarea.insert(END, f"\n Tea/cofee\t\t{self.Tea.get()}\t\t{self.list_Grocery[5]}")
            #OTHERS
            if (self.ColdD.get() != 0):
                self.textarea.insert(END, f"\n Cold drink\t\t{self.ColdD.get()}\t\t{self.List_Others[0]}")
            if (self.Noodle.get() != 0):
                self.textarea.insert(END, f"\n Noodle\t\t{self.Noodle.get()}\t\t{self.List_Others[1]}")
            if (self.snack.get() != 0 ):
                self.textarea.insert(END, f"\n Snack\t\t{self.snack.get()}\t\t{self.List_Others[2]}")
            if (self.Sauces.get() != 0):
                self.textarea.insert(END, f"\n Sauces\t\t{self.Sauces.get()}\t\t{self.List_Others[3]}")
            if (self.Namkeen.get() != 0):
                self.textarea.insert(END, f"\n Namkeen\t\t{self.Namkeen.get()}\t\t{self.List_Others[4]}")
            if (self.Other.get() != 0):
                self.textarea.insert(END, f"\n Other\t\t{self.Other.get()}\t\t{self.List_Others[5]}")

            self.textarea.insert(END, f"\n--------------------------------------")
            self.textarea.insert(END, f"\n TOTAl = \t\t\t{self.totalCosmatic + self.totalGrocceries + self.totalOthers}")
            self.textarea.insert(END, f"\n--------------------------------------")

            self.Save_bill()
    def Save_bill(self):
        op = messagebox.askyesno("save bill","do you want to save the bill")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("BillS"+str(self.Bill_N.get())+".txt","W")
            f1.write(self.bill_data)
            messagebox.showinfo("saved","your bill is saved")
        else:
            return
    '''def find_bill(self):
        for i in os.lisdir("BillS/"):
            if i.split('.')[0]==self.Bill_N.get():
                f1=open( )'''
    def clear_bill(self):
        self.Cust_N.set("")
        self.Cust_PN.set("")
        self.Bill_N.set("")
        self.groccerT.set("")
        self.cosmaticT.set("")
        self.OtherTotal.set("")
        self.Other.set(0)
        self.Namkeen.set(0)
        self.Sauces.set(0)
        self.snack.set(0)
        self.Noodle.set(0)
        self.ColdD.set(0)
        self.Tea.set(0)
        self.Daal.set(0)
        self.Wheat.set(0)
        self.Food_oil.set(0)
        self.Sugar.set(0)
        self.Rice.set(0)
        self.B_losh.set(0)
        self.B_loshP.set(0)
        self.Fwwash.set(0)
        self.FwwashP.set(0)
        self.HGEl.set(0)
        self.HGELP.set(0)
        self.H_shampoo.set(0)
        self.H_shmampooP.set(0)
        self.F_cream.set(0)
        self.F_creamP.set(0)
        self.Namkeen.set(0)
        self.B_soapP.set(0)
        self.B_soapQ.set(0)
        self.Welcome_bill()

    def EXIT(self):
        op = messagebox.askyesno('Exit',"do you really want to exit")
        if op>0:
            self.root.destroy()

    def Calculator(self):
        self.expression = ""

        def press(num):
            #self.expression

            self.expression = self.expression + str(num)

            equation.set(self.expression)

        def equalpress():

            try:

                #self.expression

                total = str(eval(self.expression))

                equation.set(total)

            except:

                equation.set("Error..")
                self.expression = ""

        def SquareRoot():
            #self.expression
            SQ = str(sqrt(eval(self.expression)))
            equation.set(SQ)

        def Remove():
            #self.expression
            self.expression = self.expression[:-1]
            equation.set(self.expression)

        def clear():
            #self.expression
            self.expression = ""
            equation.set("")

        gui = LabelFrame(self.root,text="Calculator",bd=7,relief=GROOVE,bg='blue')
        gui.place(x=995,y=80,width=230,height=200)
        #gui.configure(background='black')

        #gui.title("simple calculator")

        #gui.geometry("200x150")

        equation = StringVar()

        expression_field = Entry(gui, textvariable=equation, relief=SUNKEN,bd=7)
        expression_field.grid(columnspan=4, ipadx=40,pady=10)

        equation.set('enter your expression')

        b1 = Button(gui, text='1', fg='white', bg='black', command=lambda: press(1), height=1, width=6)
        b1.grid(row=2, column=0)

        b2 = Button(gui, text='2', fg='white', bg='black', command=lambda: press(2), height=1, width=6)
        b2.grid(row=2, column=1)

        b3 = Button(gui, text=' 3 ', fg='white', bg='black', command=lambda: press(3), height=1, width=6)
        b3.grid(row=2, column=2)

        b4 = Button(gui, text=' 4 ', fg='white', bg='black', command=lambda: press(4), height=1, width=6)
        b4.grid(row=3, column=0)

        b5 = Button(gui, text=' 5 ', fg='white', bg='black', command=lambda: press(5), height=1, width=6)
        b5.grid(row=3, column=1)

        b6 = Button(gui, text=' 6 ', fg='white', bg='black', command=lambda: press(6), height=1, width=6)
        b6.grid(row=3, column=2)

        b6 = Button(gui, text=' 7 ', fg='white', bg='black', command=lambda: press(6), height=1, width=6)
        b6.grid(row=4, column=0)

        b8 = Button(gui, text=' 8 ', fg='white', bg='black', command=lambda: press(8), height=1, width=6)
        b8.grid(row=4, column=1)

        b9 = Button(gui, text=' 9 ', fg='white', bg='black', command=lambda: press(9), height=1, width=6)
        b9.grid(row=4, column=2)

        b0 = Button(gui, text=' 0 ', fg='white', bg='black', command=lambda: press(0), height=1, width=6)
        b0.grid(row=5, column=0)

        plus = Button(gui, text=' + ', fg='white', bg='black',
                      command=lambda: press("+"), height=1, width=6)
        plus.grid(row=2, column=3)

        minus = Button(gui, text=' - ', fg='white', bg='black',
                       command=lambda: press("-"), height=1, width=6)
        minus.grid(row=3, column=3)

        multiply = Button(gui, text=' * ', fg='white', bg='black',
                          command=lambda: press("*"), height=1, width=6)
        multiply.grid(row=4, column=3)

        divide = Button(gui, text=' / ', fg='white', bg='black', command=lambda: press("/"), height=1, width=6)
        divide.grid(row=5, column=3)

        per = Button(gui, text=' % ', fg='white', bg='black', command=lambda: press("%"), height=1, width=6)
        per.grid(row=6, column=3)

        EP = Button(gui, text=' = ', fg='white', bg='black', command=equalpress, height=1, width=6)
        EP.grid(row=5, column=2)

        clear = Button(gui, text='Clear', fg='white', bg='black', command=clear, height=1, width=6)
        clear.grid(row=6, column=0)

        Decimal = Button(gui, text='.', fg='white', bg='black',
                         command=lambda: press('.'), height=1, width=6)
        Decimal.grid(row=5, column=1)

        SQRT = Button(gui, text='sqrt', fg='white', bg='black', command=SquareRoot, height=1, width=6)
        SQRT.grid(row=6, column=1)

        RL = Button(gui, text='<x', fg='white', bg='black', command=Remove, height=1, width=6)
        RL.grid(row=6, column=2)
        # start
        #gui.mainloop()


root = Tk()
bill = Bill_app(root)
root.mainloop()
