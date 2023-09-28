from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0") 
        self.root.title("Billing Software")

        #variable
        self.c_name=StringVar ()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories list
        self.Category=["Select Option", "Laptop", "CPU","RAM","Storage Device","GPU","Motherboard"]

        #laptop
        self.SubCatLaptop=["Apple", "Dell", "Lenovo"]
        self.Apple=["Macbook AIR", "Macbook Pro"]
        self.price_MacbookAIR=92990
        self.price_MacbookPro=122000

        self.Dell=["Dell XPS 13","Dell XPS 15"]
        self.price_DellXPS13=106489
        self.price_DellXPS15=202989

        self.Lenovo=["ThinkPad","IdeaPad"]
        self.price_ThinkPad=45990
        self.price_IdeaPad=43690

        #CPU
        self.SubCatCPU=['Gaming', 'Office']
        self.Gaming=["ryzen7","ryzen9"]
        self.price_ryzen7=35750
        self.price_ryzen9=53900

        self.office=["i5","i7"]
        self.price_i5=22900
        self.price_i7=39900

        #RAM
        self.SubCatRAM=['Dual 4GB','Dual 8GB','Dual 16GB']
        self.Dual_4GB=["2200mghz","4000mghz"]
        self.price_2200mghz4=3000
        self.price_4000mghz4=6000

        self.Dual_8GB=["2200mghz","4000mghz"]
        self.price_2200mghz8=6000
        self.price_4000mghz8=12000

        self.Dual_16GB=["2200mghz","4000mghz"]
        self.price_2200mghz16=10000
        self.price_4000mghz16=22000

        #StorageDevice
        self.SubCatStorageDevice=['512GB','1TB']
        self.pachso=["SSD","HDD"]
        self.price_SSD5=5000
        self.price_HDD5=3000

        self.hazar=["SSD","HDD"]
        self.price_SSD10=10000
        self.price_HDD10=8000

        #GPU
        self.SubCatGPU=['Nvidia','GigaByte']
        self.Nvidia=['3080 Ti','3060 Ti']
        self.price_3080Ti=107000
        self.price_3060Ti=35900

        self.Gigabyte=["GeForce RTX 3090","GeForce RTX 3080"]
        self.price_RTX3090=152000
        self.price_RTX3080=100000

        #motherboard
        self.SubCaMotherboard=['Gigabyte','Zebronics']
        self.Gigabyte1=["GIGABYTE H410M","GIGABYTE X570"]
        self.price_H410M=6100
        self.price_X570=20500

        self.Zebronics=["H61","Zeb G41"]
        self.price_H61=3710
        self.price_G41=2600


        #photo1
        img=Image.open("image/P1.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #photo2
        img_1=Image.open("image/P2.jpeg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        #photo3
        img_2=Image.open("image/P3.jpeg")
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=500,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="white")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue') 
        lbl.place(x=0,y=0,width=120,height=50)
        time()   
        
        #customer labelframe
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Customer Name",bd=4,fg="black")
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4,fg="black")
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #product lable frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=615,height=140)

        #category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4,fg="black")
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #sub category
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="SubCategories",bd=4,fg="black")
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1 ,column=1,stick=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.product_add)

        #product name
        self.lblProduct=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name",bd=4,fg="black")
        self.lblProduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Combo_Product=ttk.Combobox(Product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Product.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.Combo_Product.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price",bd=4,fg="black")
        self.lblPrice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame,font=('arial',10,'bold'),textvariable=self.prices,width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4,fg="black")
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.entry_Qty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=24)
        self.entry_Qty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        #middle frame
        MiddleFrame=Frame(self.root,bd=10)
        MiddleFrame.place(x=12,y=325,width=978,height=280)

        #photo1-
        img13=Image.open("image/P4.png")
        img13=img13.resize((489,280),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=0,y=0,width=489,height=280)

        #photo2-
        img_12=Image.open("image/P5.jpg")
        img_12=img_12.resize((489,280),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)
        
        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=489,y=0,width=500,height=280)

        #search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1000,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg="red",text="Graph-->",fg="White")
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)



        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="OPEN",font=('arial',10,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        #bill Area
        RightLabelFrame=LabelFrame( Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440) 

        Scroll_y= Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=420,width=1520,height=100)

        

        #button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=75,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenetrate_Bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnGenetrate_Bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnSave.grid(row=0,column=2 )

        self.BtnPrint=Button(Btn_Frame,height=2,command=self.iprint,text="Print",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="black",width=20,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    #==Function==
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add any Product to Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ==============================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ==============================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want ot save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill no{self.bill_no.get()}saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        root = Tk()
        root.title('Select Graph')
        root.geometry ("200x450")

        def Jan():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['4','15','6','12','28','20']
            plt.bar(name,it1)
            plt.show()

        def Feb():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['2','16','4','15','15','18']
            plt.bar(name,it1)
            plt.show()

        def Mar():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['3','13','3','14','22','19']
            plt.bar(name,it1)
            plt.show()   

        def Apr():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['2','16','7','12','21','11']
            plt.bar(name,it1)
            plt.show()

        def May():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['3','19','12','11','23','21']
            plt.bar(name,it1)
            plt.show()

            
        def Jun():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['5','16','5','11','27','21']
            plt.bar(name,it1)
            plt.show()   

        def Jul():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['4','15','4','10','26','19']
            plt.bar(name,it1)
            plt.show()

        def Aug():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['5','16','5','11','27','21']
            plt.bar(name,it1)
            plt.show()    

        def Sept():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['4','15','4','10','26','19']
            plt.bar(name,it1)
            plt.show()

        def Oct():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['2','16','4','15','15','18']
            plt.bar(name,it1)
            plt.show()

        def Nov():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['3','13','3','14','22','19']
            plt.bar(name,it1)
            plt.show()   

        def Dec():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['2','16','7','12','21','11']
            plt.bar(name,it1)
            plt.show()   

        def Y1():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['24','193','48','120','128','216']
            plt.bar(name,it1)
            plt.show()

        def Y2():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['42','156','36','168','264','228']
            plt.bar(name,it1)
            plt.show()   

        def Y3():
            name= ['cabinate','processor','storage','ram','laptop','GraphicCard']
            it1=['24','192','84','144','252','212']
            plt.bar(name,it1)
            plt.show()       



        my_button1 = Button(root, text="January",command=Jan)
        my_button1.pack()

        my_button2 = Button(root, text="February",command=Feb)
        my_button2.pack()

        my_button3 = Button(root, text="March",command=Mar)
        my_button3.pack()

        my_button4 = Button(root, text="April",command=Apr)
        my_button4.pack()

        my_button5 = Button(root, text="May",command=May)
        my_button5.pack()

        my_button6 = Button(root, text="June",command=Jun)
        my_button6.pack()

        my_button7 = Button(root, text="July",command=Jul)
        my_button7.pack()

        my_button8 = Button(root, text="August",command=Aug)
        my_button8.pack()

        my_button9 = Button(root, text="September",command=Sept)
        my_button9.pack()

        my_button10 = Button(root, text="October",command=Oct)
        my_button10.pack()

        my_button11= Button(root, text="November",command=Nov)
        my_button11.pack()

        my_button12= Button(root, text="December",command=Dec)
        my_button12.pack()

        my_button13 = Button(root, text="2020",command=Y1)
        my_button13.pack()

        my_button14 = Button(root, text="2019",command=Y2)
        my_button14.pack()

        my_button15= Button(root, text="2018",command=Y3)
        my_button15.pack()

        root.mainloop()

              

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("") 
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()
            

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f"\t Welcome To Computer store")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n============================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\tPrice")
        self.textarea.insert(END,"\n============================================\n")


    def Categories(self,event=""):
        if self.Combo_Category.get()=='Laptop':
            self.Combo_SubCategory.config(value=self.SubCatLaptop)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=='CPU':
            self.Combo_SubCategory.config(value=self.SubCatCPU)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=='RAM':
            self.Combo_SubCategory.config(value=self.SubCatRAM)
            self.Combo_SubCategory.current(0)   

        if self.Combo_Category.get()=='Storage Device':
            self.Combo_SubCategory.config(value=self.SubCatStorageDevice)
            self.Combo_SubCategory.current(0)    

        if self.Combo_Category.get()=='GPU':
            self.Combo_SubCategory.config(value=self.SubCatGPU)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get()=='Motherboard':
            self.Combo_SubCategory.config(value=self.SubCaMotherboard)
            self.Combo_SubCategory.current(0)    
    def product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Apple":
            self.Combo_Product.config(value=self.Apple)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Dell":
            self.Combo_Product.config(value=self.Dell)
            self.Combo_Product.current(0) 

        if self.Combo_SubCategory.get()=="Lenovo":
            self.Combo_Product.config(value=self.Lenovo)
            self.Combo_Product.current(0)      

        if self.Combo_SubCategory.get()=="Gaming":
            self.Combo_Product.config(value=self.Gaming)
            self.Combo_Product.current(0)     

        if self.Combo_SubCategory.get()=="Office":
            self.Combo_Product.config(value=self.office)
            self.Combo_Product.current(0)    

        if self.Combo_SubCategory.get()=="Dual 4GB":
            self.Combo_Product.config(value=self.Dual_4GB)
            self.Combo_Product.current(0)   

        if self.Combo_SubCategory.get()=="Dual 8GB":
            self.Combo_Product.config(value=self.Dual_8GB)
            self.Combo_Product.current(0)    

        if self.Combo_SubCategory.get()=="Dual 16GB":
            self.Combo_Product.config(value=self.Dual_16GB)
            self.Combo_Product.current(0)   

        if self.Combo_SubCategory.get()=="512GB":
            self.Combo_Product.config(value=self.pachso)
            self.Combo_Product.current(0)  

        if self.Combo_SubCategory.get()=="1TB":
            self.Combo_Product.config(value=self.hazar)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Nvidia":
            self.Combo_Product.config(value=self.Nvidia)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="GigaByte":
            self.Combo_Product.config(value=self.Gigabyte)
            self.Combo_Product.current(0)

        if self.Combo_SubCategory.get()=="Gigabyte":
            self.Combo_Product.config(value=self.Gigabyte1)
            self.Combo_Product.current(0)  

        if self.Combo_SubCategory.get()=="Zebronics":
            self.Combo_Product.config(value=self.Zebronics)
            self.Combo_Product.current(0) 

    def price(self,event=""):

         if self.Combo_Product.get()=="Macbook AIR":
             self.Combo_Price.config(value=self.price_MacbookAIR)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="Macbook Pro":
             self.Combo_Price.config(value=self.price_MacbookPro)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="Dell XPS 13":
             self.Combo_Price.config(value=self.price_DellXPS13)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="Dell XPS 15":
             self.Combo_Price.config(value=self.price_DellXPS15)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="ThinkPad":
             self.Combo_Price.config(value=self.price_ThinkPad)
             self.Combo_Price.current(0)
             self.qty.set(1)   

         if self.Combo_Product.get()=="ryzen7":
             self.Combo_Price.config(value=self.price_ryzen7)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="i5":
             self.Combo_Price.config(value=self.price_i5)
             self.Combo_Price.current(0)
             self.qty.set(1)                    

         if self.Combo_Product.get()=="i7":
             self.Combo_Price.config(value=self.price_i7)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="2200mghz":
             self.Combo_Price.config(value=self.price_2200mghz4)
             self.Combo_Price.current(0)
             self.qty.set(1)    

         if self.Combo_Product.get()=="4000mghz":
             self.Combo_Price.config(value=self.price_4000mghz4)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="2200mghz":
             self.Combo_Price.config(value=self.price_2200mghz8)
             self.Combo_Price.current(0)
             self.qty.set(1)    

         if self.Combo_Product.get()=="4000mghz":
             self.Combo_Price.config(value=self.price_4000mghz8)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="2200mghz":
             self.Combo_Price.config(value=self.price_2200mghz16)
             self.Combo_Price.current(0)
             self.qty.set(1)    

         if self.Combo_Product.get()=="4000mghz":
             self.Combo_Price.config(value=self.price_4000mghz16)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="SSd":
             self.Combo_Price.config(value=self.price_SSD5)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="HDD":
             self.Combo_Price.config(value=self.price_HDD5)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="SSD":
             self.Combo_Price.config(value=self.price_SSD10)
             self.Combo_Price.current(0)
             self.qty.set(1)
         if self.Combo_Product.get()=="HDD":
             self.Combo_Price.config(value=self.price_HDD10)
             self.Combo_Price.current(0)
             self.qty.set(1)  

         if self.Combo_Product.get()=="3080 Ti":
             self.Combo_Price.config(value=self.price_3080Ti)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="3060 Ti":
             self.Combo_Price.config(value=self.price_3060Ti)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="GeForce RTX 3090":
             self.Combo_Price.config(value=self.price_RTX3090)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="GeForce RTX 3080":
             self.Combo_Price.config(value=self.price_RTX3080)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="GIGABYTE H410M":
             self.Combo_Price.config(value=self.price_H410M)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="H61":
             self.Combo_Price.config(value=self.price_H61)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="Zeb G41":
             self.Combo_Price.config(value=self.price_G41)
             self.Combo_Price.current(0)
             self.qty.set(1)

         if self.Combo_Product.get()=="GIGABYTE X570":
             self.Combo_Price.config(value=self.price_X570)
             self.Combo_Price.current(0)
             self.qty.set(1)   

         if self.Combo_Product.get()=="IdeaPad":
             self.Combo_Price.config(value=self.price_IdeaPad)
             self.Combo_Price.current(0)
             self.qty.set(1) 

         if self.Combo_Product.get()=="ryzen9":
             self.Combo_Price.config(value=self.price_ryzen9)
             self.Combo_Price.current(0)
             self.qty.set(1)                                                        
             
                       


if __name__ == '__main__':
    root=Tk()
    obj =Bill_App(root)
    root.mainloop()