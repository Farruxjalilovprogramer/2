from tkinter import *
from PIL import Image, ImageTk

a=Tk()
a.geometry("1370x800")
a.resizable(0,0)
a.title("start")
rasm = Image.open('unnamed.jpg').resize((1370,800))
ssss = ImageTk.PhotoImage(rasm)
label = Label(a, image=ssss)
label.place(x=0, y=0)


def g2():
    a.destroy()
    g()
def g3():
    
    g()

d=Label(a,text='''Bizning kompyuter do'konimizga
xush kelibsiz ''',font=("Times",40,"bold"),bg="dark blue",fg="#34eb9b",cursor="dotbox")
d.place(x=300,y=80)
y12=""
infa=""
sos=""
sos1=""

infa2=""
sos2=""

infa3=""
sos3=""

infa4=""
sos4=""

infa5=""
sos5=""

def g():
    
  

    
        
   
            

            
    


    
    
    h=Tk()
    h.title("sotuv")
    h.geometry("1370x800")
    h.resizable(0,0)
    rasm23 = Image.open('de183cbc10.png').resize((1370,800))
    ssss= ImageTk.PhotoImage(rasm23)
    label1=Label(h,image=ssss)
    label1.place(x=0, y=0)
    


    
    



    s2=Label(h,bg="black",width="200",height="2")
    s2.pack()

    def f3():
        

        h.destroy()
        h1=Tk()
        h1.title("protsessor")
        h1.geometry("1370x800")
        h1.resizable(0,0)
        rasm12 = Image.open('Biznes-plan-po-remontu-kompyuterov-960x960.png').resize((1370,800))
        sss = ImageTk.PhotoImage(rasm12)
        label12 = Label(h1, image=sss)
        label12.place(x=0, y=0)

        dd=Label(h1,text="Markaziy protsessor",bg="white",fg="dark blue",font=("Times",40,"bold"),width=45,cursor="dotbox")
        dd.place(x=0,y=0)
        def de1():
            global sos1,y12,infa
            sos1=""
            
            sos1+="Без названия.jpg"
            y12=""
            y12+="6480000"
           
            infa=""
            
            
            infa+='''Core i9-10900F 
    с TDP 65 Вт'''
            h1.destroy()
            
            g3()
        p123 = Image.open('Без названия.jpg').resize((200,200))
        u123= ImageTk.PhotoImage(p123)
        ff=Button(h1,image=u123,bg="black",command=de1)
        ff.place(x=0,y=70)
        s123=Label(h1,text='''Core i9-10900F 
    с TDP 65 Вт''')
        s123.place(x=205,y=70)
        e123=Label(h1,text="6 480 000 so'm",fg="black",bg="white",cursor="tcross")
        e123.place(x=205,y=120)
        def de2():
            global sos1,y12,infa
            sos1=""
            
            sos1+="orig.webp"
            y12=""
            y12+="2860000 "
           
            infa=""
            
            infa+='''Intel Core i5-12400F 
    # LGA1700, 6 x 2500 МГц'''
            h1.destroy()
            
            g3()
        p124 = Image.open('orig.webp').resize((200,200))
        u124= ImageTk.PhotoImage(p124)
        ff1=Button(h1,image=u124,bg="black",command=de2)
        ff1.place(x=300,y=70)
        ss=Label(h1,text='''Intel Core i5-12400F 
    # LGA1700, 6 x 2500 МГц''')
        ss.place(x=505,y=70)
        ee=Label(h1,text="2 860 000 so'm",fg="black",bg="white",cursor="tcross")
        ee.place(x=505,y=120)
        def de3():
            global sos1,y12,infa
            sos1=""
            
            sos1+="_DSF9361.jpg"
            y12=""
            y12+="6120000"
           
            infa=""
            
            infa+='''Intel Core
         i9-10850K'''
            h1.destroy()
            
            g3()
        p125 = Image.open('_DSF9361.jpg').resize((200,200))
        u125= ImageTk.PhotoImage(p125)
        ff2=Button(h1,image=u125,bg="black",command=de3)
        ff2.place(x=620,y=70)
        ss1=Label(h1,text='''Intel Core
         i9-10850K''')
        ss1.place(x=825,y=70)
        ee1=Label(h1,text="6,120,000 so'm",fg="black",bg="white",cursor="tcross")
        ee1.place(x=825,y=120)
        def de4():
            global sos1,y12,infa
            sos1=""
            
            sos1+="_DSF7436.jpg"
            y12=""
            y12+="4672000 "
           
            infa=""
            
            infa+='''Intel Core i7-9700K
        :Ryzen'''
            h1.destroy()
            
            g3()
        p126 = Image.open('_DSF7436.jpg').resize((200,200))
        u126= ImageTk.PhotoImage(p126)
        ff3=Button(h1,image=u126,bg="black",command=de4)
        ff3.place(x=910,y=70)
        ss2=Label(h1,text='''Intel Core i7-9700K
        :Ryzen''')
        ss2.place(x=1115,y=70)
        ee2=Label(h1,text="4 672 000 so'm",fg="black",bg="white",cursor="tcross")
        ee2.place(x=1115,y=120)



        def de5():
            global sos1,y12,infa
            sos1=""
            
            sos1+="273799.jpg"
            y12=""
            y12+="2403000"
           
            infa=""
            
            infa+=''' Intel Core i5 - 
        12400F OEM'''
            h1.destroy()
            
            g3()

        p127 = Image.open('273799.jpg').resize((200,200))
        u127= ImageTk.PhotoImage(p127)
        ff4=Button(h1,image=u127,bg="black",command=de5)
        ff4.place(x=0,y=300)
        s127=Label(h1,text=''' Intel Core i5 - 
        12400F OEM''')
        s127.place(x=205,y=300)
        e127=Label(h1,text="2 403 000 so'm",fg="black",bg="white",cursor="tcross")
        e127.place(x=205,y=330)
        def de6():
            global sos1,y12,infa
            sos1=""
            
            sos1+="imag.jpg"
            y12=""
            y12+="457600 "
           
            infa=""
            
            infa+='''Intel Core i7-4770K'''
            h1.destroy()
            
            g3()
        p128 = Image.open('imag.jpg').resize((200,200))
        u128= ImageTk.PhotoImage(p128)
        ff5=Button(h1,image=u128,bg="black",command=de6)
        ff5.place(x=300,y=300)
        ss4=Label(h1,text='''Intel Core i7-4770K''')
        ss4.place(x=505,y=300)
        ee4=Label(h1,text="457 600 so'm",fg="black",bg="white",cursor="tcross")
        ee4.place(x=505,y=330)
        def de7():
            global sos1,y12,infa
            sos1=""
            
            sos1+="intel-core-i9-x-series-skylake.jpg"
            y12=""
            y12+="13519000 "
           
            infa=""
            
            infa+='''INTEL CORE 
        i9-9980XE
         EXTREME 
         EDITION'''
            h1.destroy()
            
            g3()
        p129 = Image.open('intel-core-i9-x-series-skylake.jpg').resize((200,200))
        u129= ImageTk.PhotoImage(p129)
        ff6=Button(h1,image=u129,bg="black",command=de7)
        ff6.place(x=620,y=300)
        ss5=Label(h1,text='''INTEL CORE 
        i9-9980XE
         EXTREME 
         EDITION''')
        ss5.place(x=825,y=300)
        ee5=Label(h1,text="13 519 000 so'm",fg="black",bg="white",cursor="tcross")
        ee5.place(x=825,y=330)
        def de8():
            global sos1,y12,infa
            sos1=""
            
            sos1+="intel.jpg"
                        
            y12=""
            y12+="8569000"
           
            infa=""
            
            infa+='''INTEL CORE I9-12900K'''
            h1.destroy()
            
            g3()
        p1210 = Image.open('intel.jpg').resize((200,200))
        u1210= ImageTk.PhotoImage(p1210)
        ff7=Button(h1,image=u1210,bg="black",command=de8)
        ff7.place(x=910,y=300)
        ss6=Label(h1,text='''INTEL CORE I9-12900K''')
        ss6.place(x=1115,y=300)
        ee6=Label(h1,text="8 569 000 so'm",fg="black",bg="white",cursor="tcross")
        ee6.place(x=1115,y=330)





        def de9():
            global sos1,y12,infa
            sos1=""
            
            sos1+="q93_b70ea229d99d1991cc07917663ccb812b5347bffffa850b15e682823c07469d8.jpg"
            y12=""
            y12+="49271000 "
           
            infa=""
            
            infa+=''' Ryzen 9'''
            h1.destroy()
            
            g3()
        p1211 = Image.open('q93_b70ea229d99d1991cc07917663ccb812b5347bffffa850b15e682823c07469d8.jpg').resize((200,200))
        u1211= ImageTk.PhotoImage(p1211)
        ff8=Button(h1,image=u1211,bg="black",command=de9)
        ff8.place(x=0,y=530)
        s1211=Label(h1,text=''' Ryzen 9''')
        s1211.place(x=205,y=530)
        e1211=Label(h1,text="49 271 000 so'm",fg="black",bg="white",cursor="tcross")
        e1211.place(x=205,y=560)
        def de10():
            global sos1,y12,infa
            sos1=""
            
            sos1+="image.jpg"
            y12=""
            y12+="145906 "
           
            infa=""
            
            infa+='''Intel Core i7-4770K'''
            h1.destroy()
            
            g3()
        p1212 = Image.open('image.jpg').resize((200,200))
        u1212= ImageTk.PhotoImage(p1212)
        ff9=Button(h1,image=u1212,bg="black",command=de10)
        ff9.place(x=300,y=530)
        ss8=Label(h1,text='''Intel Core i7-4770K''')
        ss8.place(x=505,y=530)
        ee8=Label(h1,text="145 906 so'm",fg="black",bg="white",cursor="tcross")
        ee8.place(x=505,y=560)
        def de11():
            global sos1,y12,infa
            
            sos1=""
            
            sos1+="9feb30c3bbca3b4a3f66b6b55639be68.jpg"
            y12=""
            y12+="5642000 "
           
            infa=""
            
            infa+='''Intel-Core i9 - 9900К,  
        3.6 GHz, 64M,
         oem, 
         LGA1151'''
            h1.destroy()
            
            g3()
        p1213 = Image.open('9feb30c3bbca3b4a3f66b6b55639be68.jpg').resize((200,200))
        u1213= ImageTk.PhotoImage(p1213)
        ff10=Button(h1,image=u1213,bg="black",command=de11)
        ff10.place(x=620,y=530)
        ss9=Label(h1,text='''Intel-Core i9 - 9900К,  
        3.6 GHz, 64M,
         oem, 
         LGA1151''')
        ss9.place(x=825,y=530)
        ee9=Label(h1,text="5 642 000  so'm",fg="black",bg="white",cursor="tcross")
        ee9.place(x=825,y=560)
        def de12():
            global sos1,y12,infa
            
            sos1=""
            sos1+="1.jpg"
            y12=""
            y12+="3134404"
           
            
            infa+="AMD Ryzen 7 5700G AM4 "

            
            h1.destroy()
            
            g3()


        p1214 = Image.open('1.jpg').resize((200,200))
        u1214= ImageTk.PhotoImage(p1214)
        ff11=Button(h1,image=u1214,bg="black",command=de12)
        ff11.place(x=910,y=530)
        ss10=Label(h1,text='''AMD Ryzen 7 5700G AM4 ''')
        ss10.place(x=1115,y=530)
        ee10=Label(h1,text="3 134 404 so'm",fg="black",bg="white",cursor="tcross")
        ee10.place(x=1115,y=560)  



        h1.mainloop()
    s=Button(h,text=" Markaziy protsessor",bg="black",fg="white",command=f3)
    s.place(x=100,y=2)
    t123=eval(y12)       
    aaa=Label(h,text=f"{t123} so'm",fg="green",font=("Times",40,"bold"))    
    aaa.place(x=600,y=660)

    p1215 = Image.open(sos1).resize((200,200))
    u1215= ImageTk.PhotoImage(p1215)
    s12=Label(h,image=u1215)
    s12.place(x=100,y=35)

    s1212=Label(h,text=infa)
    s1212.place(x=100,y=235)
    


    def karta():
        

        h.destroy()
        h2=Tk()
        h2.title("video karta")
        h2.geometry("1370x800")
        h2.resizable(0,0)
        rasmxa = Image.open('Biznes-plan-po-remontu-kompyuterov-960x960.png').resize((1370,800))
        sssxa = ImageTk.PhotoImage(rasmxa)
        labelxa = Label(h2, image=sssxa)
        labelxa.place(x=0, y=0)

        ddxa=Label(h2,text="video karta",bg="white",fg="dark blue",font=("Times",40,"bold"),width=45,cursor="dotbox")
        ddxa.place(x=0,y=0)
        def de1():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="316524_1.jpg"
            y12+="+"
            y12+="2768500"
            
            infa2=""
            
            
            infa2+=''' Radeon RX 
    # 580 8 ГБ'''
            h2.destroy()
            
            g()
        p123 = Image.open('316524_1.jpg').resize((200,200))
        u123= ImageTk.PhotoImage(p123)
        ff=Button(h2,image=u123,bg="black",command=de1)
        ff.place(x=0,y=70)
        s123=Label(h2,text=''' Radeon RX 
    # 580 8 ГБ''')
        s123.place(x=205,y=70)
        e123=Label(h2,text="2 768 500 so'm",fg="black",bg="white",cursor="tcross")
        e123.place(x=205,y=120)
        def de2():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="images.jpg"
            y12+="+"
            y12+="5536000 "
            
            infa2=""
            
            infa2+=''' Radeon RX 
    # 580 8 ГБ'''
            h2.destroy()
            
            g()
        p124 = Image.open('images.jpg').resize((200,200))
        u124= ImageTk.PhotoImage(p124)
        ff1=Button(h2,image=u124,bg="black",command=de2)
        ff1.place(x=300,y=70)
        ss=Label(h2,text=''' Radeon RX 
    # 580 8 ГБ''')
        ss.place(x=505,y=70)
        ee=Label(h2,text="5 536 000 so'm",fg="black",bg="white",cursor="tcross")
        ee.place(x=505,y=120)
        def de3():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="ASUS-TUF-RTX-3080-mv1.webp"
            y12+="+"
            y12+="20645000"
            
            infa2=""
            
            infa2+='''  ASUS TUF Gaming GeForce 
     RTX 3080'''
            h2.destroy()
            
            g()
        p125 = Image.open('ASUS-TUF-RTX-3080-mv1.webp').resize((200,200))
        u125= ImageTk.PhotoImage(p125)
        ff2=Button(h2,image=u125,bg="black",command=de3)
        ff2.place(x=620,y=70)
        ss1=Label(h2,text='''  ASUS TUF
        Gaming GeForce 
        RTX 3080''')
        ss1.place(x=825,y=70)
        ee1=Label(h2,text="20 645 000 so'm",fg="black",bg="white",cursor="tcross")
        ee1.place(x=825,y=120)
        def de4():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="226836.jpg"
            y12+="+"
            y12+="979000"
            
            infa2=""
            
            infa2+='''Gigabyte GeForce GT 
     730 902Mhz PCI-E 2.0 2048Mb 1800Mhz
     64 bit DVI HDMI HDCP'''
            h2.destroy()
            
            g()
        p126 = Image.open('226836.jpg').resize((200,200))
        u126= ImageTk.PhotoImage(p126)
        ff3=Button(h2,image=u126,bg="black",command=de4)
        ff3.place(x=910,y=70)
        ss2=Label(h2,text='''Gigabyte GeForce GT 
     730 902Mhz PCI-E 2.0 2048Mb 1800Mhz
      64 bit DVI HDMI HDCP''')
        ss2.place(x=1115,y=70)
        ee2=Label(h2,text="979 000 so'm",fg="black",bg="white",cursor="tcross")
        ee2.place(x=1115,y=120)



        def de5():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="SU0434742-0.jpg"
            y12+="+"
            y12+="2429000"
            
            infa2=""
            
            infa2+=''' GIGABYTE GeForce
         GTX1650 4096Mb 
         D6 OC'''
            h2.destroy()
            
            g()

        p127 = Image.open('SU0434742-0.jpg').resize((200,200))
        u127= ImageTk.PhotoImage(p127)
        ff4=Button(h2,image=u127,bg="black",command=de5)
        ff4.place(x=0,y=300)
        s127=Label(h2,text=''' GIGABYTE GeForce
         GTX1650 4096Mb 
         D6 OC''')
        s127.place(x=205,y=300)
        e127=Label(h2,text="2 429 000 so'm",fg="black",bg="white",cursor="tcross")
        e127.place(x=205,y=330)
        def de6():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="SU0523404-0.jpg"
            y12+="+"
            y12+="6188000"
            
            infa2=""
            
            infa2+='''GIGABYTE Radeon
        RX 6700 
        XT 12Gb EAGLE'''
            h2.destroy()
            
            g()
        p128 = Image.open('SU0523404-0.jpg').resize((200,200))
        u128= ImageTk.PhotoImage(p128)
        ff5=Button(h2,image=u128,bg="black",command=de6)
        ff5.place(x=300,y=300)
        ss4=Label(h2,text='''GIGABYTE Radeon
        RX 6700 
        XT 12Gb EAGLE''')
        ss4.place(x=505,y=300)
        ee4=Label(h2,text="6 188 000 so'm",fg="black",bg="white",cursor="tcross")
        ee4.place(x=505,y=330)
        def de7():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="ima.jpg"
            y12+="+"
            y12+="8014000"
            
            infa2=""
            
            infa2+='''GIGABYTE GeForce 
        RTX 3070 
        GAMING OC'''
            h2.destroy()
            
            g()
        p129 = Image.open('ima.jpg').resize((200,200))
        u129= ImageTk.PhotoImage(p129)
        ff6=Button(h2,image=u129,bg="black",command=de7)
        ff6.place(x=620,y=300)
        ss5=Label(h2,text='''GIGABYTE GeForce 
        RTX 3070 
        GAMING OC''')
        ss5.place(x=825,y=300)
        ee5=Label(h2,text="8 014 000 so'm",fg="black",bg="white",cursor="tcross")
        ee5.place(x=825,y=330)
        def de8():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="im.jpg"
                        
            y12+="+"
            y12+="8569000"
            
            infa2=""
            
            infa2+='''GPU Geforce 
        GTX 1660 Ti'''
            h2.destroy()
            
            g()
        p1210 = Image.open('im.jpg').resize((200,200))
        u1210= ImageTk.PhotoImage(p1210)
        ff7=Button(h2,image=u1210,bg="black",command=de8)
        ff7.place(x=910,y=300)
        ss6=Label(h2,text='''GPU Geforce 
        GTX 1660 Ti''')
        ss6.place(x=1115,y=300)
        ee6=Label(h2,text="8 569 000 so'm",fg="black",bg="white",cursor="tcross")
        ee6.place(x=1115,y=330)





        def de9():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="i.jpg"
            y12+="+"
            y12+="2138000"
            
            infa2=""
            
            infa2+=''' GTX 1070 8Gb
             Founders 
             Edition 8G''' 
            h2.destroy()
            
            g()
        p1211 = Image.open('i.jpg').resize((200,200))
        u1211= ImageTk.PhotoImage(p1211)
        ff8=Button(h2,image=u1211,bg="black",command=de9)
        ff8.place(x=0,y=530)
        s1211=Label(h2,text=''' GTX 1070 8Gb
             Founders 
             Edition 8G''' )
        s1211.place(x=205,y=530)
        e1211=Label(h2,text="2 138 000 so'm",fg="black",bg="white",cursor="tcross")
        e1211.place(x=205,y=560)
        def de10():
            global sos2,y12,infa2
            sos2=""
            
            sos2+="MSIRadeonRX6800XT16GBDDR6GAMINGXTrio.jpg"
            y12+="+"
            y12+="145906 "
            
            infa2=""
            
            infa2+='''MSI Radeon 
            RX 6800 XT 16GB'''
            h2.destroy()
            
            g()
        p1212 = Image.open('MSIRadeonRX6800XT16GBDDR6GAMINGXTrio.jpg').resize((200,200))
        u1212= ImageTk.PhotoImage(p1212)
        ff9=Button(h2,image=u1212,bg="black",command=de10)
        ff9.place(x=300,y=530)
        ss8=Label(h2,text='''MSI Radeon 
            RX 6800 XT 16GB''')
        ss8.place(x=505,y=530)
        ee8=Label(h2,text="145 906 so'm",fg="black",bg="white",cursor="tcross")
        ee8.place(x=505,y=560)
        def de11():
            global sos2,y12,infa2
            
            sos2=""
            
            sos2+="4042905826_w200_h200_videokarta-msi-geforce.webp"
            y12+="+"
            y12+="5208000"
            
            infa2=""
            
            infa2+=''' Zotac GeForce 
            RTX2060 D6 
            6GB'''
            h2.destroy()
            
            g()
        p1213 = Image.open('4042905826_w200_h200_videokarta-msi-geforce.webp').resize((200,200))
        u1213= ImageTk.PhotoImage(p1213)
        ff10=Button(h2,image=u1213,bg="black",command=de11)
        ff10.place(x=620,y=530)
        ss9=Label(h2,text=''' Zotac GeForce 
            RTX2060 D6 
            6GB''')
        ss9.place(x=825,y=530)
        ee9=Label(h2,text="5 208 000 so'm",fg="black",bg="white",cursor="tcross")
        ee9.place(x=825,y=560)
        def de12():
            global sos2,y12,infa2
            
            sos2=""
            sos2+="3032953788_w220_h220_3032953788.webp"
            y12+="+"
            y12+="2358000"
            infa2=""
            
            infa2+="Sapphire Pulse RX 5700 XT 8GB"

            
            h2.destroy()
            
            g()


        p1214 = Image.open('3032953788_w220_h220_3032953788.webp').resize((200,200))
        u1214= ImageTk.PhotoImage(p1214)
        ff11=Button(h2,image=u1214,bg="black",command=de12)
        ff11.place(x=910,y=530)
        ss10=Label(h2,text='''Sapphire Pulse RX 5700 XT 8GB''')
        ss10.place(x=1115,y=530)
        ee10=Label(h2,text="2 358 000 so'm",fg="black",bg="white",cursor="tcross")
        ee10.place(x=1115,y=560)  



        h2.mainloop()
    video=Button(h,text="video karta",bg="black",fg="white",command=karta)
    video.place(x=350,y=2) 
    p1215xa = Image.open(sos2).resize((200,200))
    u1215xa= ImageTk.PhotoImage(p1215xa)
    s12xa=Label(h,image=u1215xa)
    s12xa.place(x=350,y=35)

    s1212xa=Label(h,text=infa2)
    s1212xa.place(x=350,y=235)    
    def Operativ():
        

        h.destroy()
        h3=Tk()
        h3.title("Operativ xotira")
        h3.geometry("1370x800")
        h3.resizable(0,0)
        rasmxa1 = Image.open('Biznes-plan-po-remontu-kompyuterov-960x960.png').resize((1370,800))
        sssxa1 = ImageTk.PhotoImage(rasmxa1)
        labelxa1 = Label(h3, image=sssxa1)
        labelxa1.place(x=0, y=0)

        ddxa1=Label(h3,text="Operativ xotira",bg="white",fg="dark blue",font=("Times",40,"bold"),width=45,cursor="dotbox")
        ddxa1.place(x=0,y=0)
        def de1():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="images (2).jpg"
            y12+="+"
            y12+="1373000"
            
            infa3=""
            
            
            infa3+=''' Corsair 
    Vengeance 
    RGB Pro 
    16 Gb 
    (2x8gb) 
    3200Mhz'''
            h3.destroy()
            
            g()
        p123 = Image.open('images (2).jpg').resize((200,200))
        u123= ImageTk.PhotoImage(p123)
        ff=Button(h3,image=u123,bg="black",command=de1)
        ff.place(x=0,y=70)
        s123=Label(h3,text=''' Corsair 
    Vengeance 
    RGB Pro 
    16 Gb 
    (2x8gb) 
    3200Mhz''')
        s123.place(x=205,y=70)
        e123=Label(h3,text="1 373 000 so'm",fg="black",bg="white",cursor="tcross")
        e123.place(x=205,y=250)
        def de2():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="hyperx-predator-rgb-32gb-kit-2x16gb-ddr43200.jpg"
            y12+="+"
            y12+="2970000"
            
            infa3=""
            
            infa3+=''' HyperX 
    Predator 
    RGB 32GB 
    Kit (2x16GB)
     DDR4/3200'''
            h3.destroy()
            
            g()
        p124 = Image.open('hyperx-predator-rgb-32gb-kit-2x16gb-ddr43200.jpg').resize((200,200))
        u124= ImageTk.PhotoImage(p124)
        ff1=Button(h3,image=u124,bg="black",command=de2)
        ff1.place(x=300,y=70)
        ss=Label(h3,text=''' HyperX 
    Predator 
    RGB 32GB 
    Kit (2x16GB)
     DDR4/3200''')
        ss.place(x=505,y=70)
        ee=Label(h3,text="2 970 000 so'm so'm",fg="black",bg="white",cursor="tcross")
        ee.place(x=505,y=250)
        def de3():
            global sos3,y12,infa3
            sos3=""
            
            sos3+='mWSxOBJUlm9r56PptOSYTJV6j0HMDkfCuOaw38TuA0UAphsAhbNrXGLdbW3Y.jpeg'
            y12+="+"
            y12+="20645000"
            
            infa3=""
            
            infa3+=''' Kingston DDR4
      64GB Fury 
      Beast RGB
      (32GBx2) 
      3200MHz '''
            h3.destroy()
            
            g()
        p125 = Image.open('mWSxOBJUlm9r56PptOSYTJV6j0HMDkfCuOaw38TuA0UAphsAhbNrXGLdbW3Y.jpeg').resize((200,200))
        u125= ImageTk.PhotoImage(p125)
        ff2=Button(h3,image=u125,bg="black",command=de3)
        ff2.place(x=620,y=70)
        ss1=Label(h3,text=''' Kingston DDR4
      64GB Fury 
      Beast RGB
      (32GBx2) 
      3200MHz ''')
        ss1.place(x=825,y=70)
        ee1=Label(h3,text="3 333 500 so'm",fg="black",bg="white",cursor="tcross")
        ee1.place(x=825,y=250)
        def de4():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="o_1_5e6b16a1bf1b5.jpg"
            y12+="+"
            y12+="767000 "
            
            infa3=""
            
            infa3+='''  Apacer 
     DDR4 16GB 
     3000MHz (8GBx2)'''
            h3.destroy()
            
            g()
        p126 = Image.open('o_1_5e6b16a1bf1b5.jpg').resize((200,200))
        u126= ImageTk.PhotoImage(p126)
        ff3=Button(h3,image=u126,bg="black",command=de4)
        ff3.place(x=910,y=70)
        ss2=Label(h3,text='''  Apacer 
     DDR4 16GB 
     3000MHz (8GBx2)''')
        ss2.place(x=1115,y=70)
        ee2=Label(h3,text="767 000 so'm",fg="black",bg="white",cursor="tcross")
        ee2.place(x=1115,y=250)





        def de5():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="KaKYwHKU61Kz2q3HnaBZF6VNwRtwXAaFuL4ji9CA.png"
            y12+="+"
            y12+="684000"
            
            infa3=""
            
            infa3+=''' eamGroup DDR4
         16GB 3200Mhz'''
            h3.destroy()
            
            g()

        p127 = Image.open('KaKYwHKU61Kz2q3HnaBZF6VNwRtwXAaFuL4ji9CA.png').resize((200,200))
        u127= ImageTk.PhotoImage(p127)
        ff4=Button(h3,image=u127,bg="black",command=de5)
        ff4.place(x=0,y=300)
        s127=Label(h3,text=''' eamGroup DDR4
         16GB 3200Mhz''')
        s127.place(x=205,y=300)
        e127=Label(h3,text="684 000 so'm",fg="black",bg="white",cursor="tcross")
        e127.place(x=205,y=460)
        def de6():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="2021-01-12-11-24-18-981952-40233166091f6d8a08a523c141c3b153.jpg"
            y12+="+"
            y12+="943000"
            
            infa3=""
            
            infa3+='''SilliconPower 16GB 
            DDR4 3200Mhz'''
            h3.destroy()
            
            g()
        p128 = Image.open('2021-01-12-11-24-18-981952-40233166091f6d8a08a523c141c3b153.jpg').resize((200,200))
        u128= ImageTk.PhotoImage(p128)
        ff5=Button(h3,image=u128,bg="black",command=de6)
        ff5.place(x=300,y=300)
        ss4=Label(h3,text='''SilliconPower 16GB 
            DDR4 3200Mhz''')
        ss4.place(x=505,y=300)
        ee4=Label(h3,text="943 000 so'm",fg="black",bg="white",cursor="tcross")
        ee4.place(x=505,y=460)
        def de7():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="operativ.jpg"
            y12+="+"
            y12+="1516000 "
            
            infa3=""
            
            infa3+='''Corsair 
            Dominator 
            platinum 
            RGB DDR4 
            16Gb (2x8GB)
            3200Mhz'''
            h3.destroy()
            
            g()
        p129 = Image.open('operativ.jpg').resize((200,200))
        u129= ImageTk.PhotoImage(p129)
        ff6=Button(h3,image=u129,bg="black",command=de7)
        ff6.place(x=620,y=300)
        ss5=Label(h3,text='''Corsair 
            Dominator 
            platinum 
            RGB DDR4 
            16Gb (2x8GB)
            3200Mhz''')
        ss5.place(x=825,y=300)
        ee5=Label(h3,text="1 516 000  so'm",fg="black",bg="white",cursor="tcross")
        ee5.place(x=825,y=460)
        def de8():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="pdIHdsdFm7p7XzcybIAslsPSZ7K4ZO0HHFieDl5c.jpeg"
                        
            y12+="+"
            y12+="684000"
            
            infa3=""
            
            infa3+='''TeamGroup DDR4 
            16GB 3200Mhz'''
            h3.destroy()
            
            g()
        p1210 = Image.open('pdIHdsdFm7p7XzcybIAslsPSZ7K4ZO0HHFieDl5c.jpeg').resize((200,200))
        u1210= ImageTk.PhotoImage(p1210)
        ff7=Button(h3,image=u1210,bg="black",command=de8)
        ff7.place(x=910,y=300)
        ss6=Label(h3,text='''TeamGroup DDR4 
            16GB 3200Mhz''')
        ss6.place(x=1115,y=300)
        ee6=Label(h3,text="684 000 so'm",fg="black",bg="white",cursor="tcross")
        ee6.place(x=1115,y=460)





        def de9():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="bd27ef7f7c08c95f480363e1bd7c8ee42020121918272540072r8lE1alL1a.jpg.webp"
            y12+="+"
            y12+="2138000"
            
            infa3=""
            
            infa3+=''' Team Group 
            T-Force Night
             Hawk RGB DDR4
              32GB (2x16GB) 
              3200Mhz''' 
            h3.destroy()
            
            g()
        p1211 = Image.open('bd27ef7f7c08c95f480363e1bd7c8ee42020121918272540072r8lE1alL1a.jpg.webp').resize((200,200))
        u1211= ImageTk.PhotoImage(p1211)
        ff8=Button(h3,image=u1211,bg="black",command=de9)
        ff8.place(x=0,y=530)
        s1211=Label(h3,text=''' Team Group 
            T-Force Night
             Hawk RGB DDR4
              32GB (2x16GB) 
              3200Mhz'''  )
        s1211.place(x=205,y=530)
        e1211=Label(h3,text="2 138 000 so'm",fg="black",bg="white",cursor="tcross")
        e1211.place(x=205,y=690)
        def de10():
            global sos3,y12,infa3
            sos3=""
            
            sos3+="jpeg___1__w1rf-rk.jpg"
            y12+="+"
            y12+="873000"
            
            infa3=""
            
            infa3+='''CRUCIAL 16ГБ 
            DDR4 BALLISTIX 
            SPORT'''
            h3.destroy()
            
            g()
        p1212 = Image.open('jpeg___1__w1rf-rk.jpg').resize((200,200))
        u1212= ImageTk.PhotoImage(p1212)
        ff9=Button(h3,image=u1212,bg="black",command=de10)
        ff9.place(x=300,y=530)
        ss8=Label(h3,text='''CRUCIAL 16ГБ 
            DDR4 BALLISTIX 
            SPORT''')
        ss8.place(x=505,y=530)
        ee8=Label(h3,text="873 000 so'm",fg="black",bg="white",cursor="tcross")
        ee8.place(x=505,y=690)
        def de11():
            global sos3,y12,infa3
            
            sos3=""
            
            sos3+="6NSaoSLVyBrMvcfiptMODG60jeeLtz30hIphpcpT.jpeg"
            y12+="+"
            y12+="2172000"
            
            infa3=""
            
            infa3+='''Lexar DDR5 
            32GB 
            (16GB*2) 
            5200Mhz'''
            h3.destroy()
            
            g()
        p1213 = Image.open('6NSaoSLVyBrMvcfiptMODG60jeeLtz30hIphpcpT.jpeg').resize((200,200))
        u1213= ImageTk.PhotoImage(p1213)
        ff10=Button(h3,image=u1213,bg="black",command=de11)
        ff10.place(x=620,y=530)
        ss9=Label(h3,text='''Lexar DDR5 
            32GB 
            (16GB*2) 
            5200Mhz''')
        ss9.place(x=825,y=530)
        ee9=Label(h3,text="2 172 000 so'm",fg="black",bg="white",cursor="tcross")
        ee9.place(x=825,y=690)
        def de12():
            global sos3,y12,infa3
            
            sos3=""
            sos3+="3ec5b6df-6c67-4c79-9094-7889b1e20f04.png"
            y12+="+"
            y12+="1513000"
            infa3=""
            
            infa3+=''' HIKVISION RAM 
            DDR4 RGB 16GB 
            3200 МГц'''
            h3.destroy()
            g()

        p1214 = Image.open('3ec5b6df-6c67-4c79-9094-7889b1e20f04.png').resize((200,200))
        u1214= ImageTk.PhotoImage(p1214)
        ff11=Button(h3,image=u1214,bg="black",command=de12)
        ff11.place(x=910,y=530)
        ss10=Label(h3,text=''' HIKVISION RAM 
            DDR4 RGB 16GB 
            3200 МГц''')
        ss10.place(x=1115,y=530)
        ee10=Label(h3,text="1 513 000  so'm",fg="black",bg="white",cursor="tcross")
        ee10.place(x=1115,y=560)  
        
        h3.mainloop()
        
    xa=Button(h,text="Operativ xotira",bg="black",fg="white",command=Operativ)
    xa.place(x=600,y=2) 

    p1215xa1 = Image.open(sos3).resize((200,200))
    u1215xa1= ImageTk.PhotoImage(p1215xa1)
    s12xa1=Label(h,image=u1215xa1)
    s12xa1.place(x=600,y=35)

    s1212xa1=Label(h,text=infa3)
    s1212xa1.place(x=600,y=235)

    def qattiq ():
        

        h.destroy()
        h4=Tk()
        h4.title("qattiq disk")
        h4.geometry("1370x800")
        h4.resizable(0,0)
        rasmxa2 = Image.open('Biznes-plan-po-remontu-kompyuterov-960x960.png').resize((1370,800))
        sssxa2 = ImageTk.PhotoImage(rasmxa2)
        labelxa2 = Label(h4, image=sssxa2)
        labelxa2.place(x=0, y=0)

        ddxa2=Label(h4,text="qattiq disk",bg="white",fg="dark blue",font=("Times",40,"bold"),width=45,cursor="dotbox")
        ddxa2.place(x=0,y=0)
        def de1():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="SeagateHDD6TB.jpg"
            y12+="+"
            y12+="1710000"
            
            infa4=""
            
            
            infa4+='''Seagate HDD 
     6TB'''
            h4.destroy()
            
            g()
        p123 = Image.open('SeagateHDD6TB.jpg').resize((200,200))
        u123= ImageTk.PhotoImage(p123)
        ff=Button(h4,image=u123,bg="black",command=de1)
        ff.place(x=0,y=70)
        s123=Label(h4,text='''Seagate HDD 
     6TB''')
        s123.place(x=205,y=70)
        e123=Label(h4,text="1 710 000 so'm",fg="black",bg="white",cursor="tcross")
        e123.place(x=205,y=250)
        def de2():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="babdd21d-98c8-4e7f-8344-0b38e48f68eb.webp"
            y12+="+"
            y12+="217000"
            
            infa4=""
            
            infa4+='''HDD 500GB Seagate 
     7200 Ref'''
            h4.destroy()
            
            g()
        p124 = Image.open('babdd21d-98c8-4e7f-8344-0b38e48f68eb.webp').resize((200,200))
        u124= ImageTk.PhotoImage(p124)
        ff1=Button(h4,image=u124,bg="black",command=de2)
        ff1.place(x=300,y=70)
        ss=Label(h4,text='''HDD 500GB Seagate 
     7200 Ref''')
        ss.place(x=505,y=70)
        ee=Label(h4,text="217 000 so'm so'm",fg="black",bg="white",cursor="tcross")
        ee.place(x=505,y=250)
        def de3():
            global sos4,y12,infa4
            sos4=""
            
            sos4+='150233.jpg'
            y12+="+"
            y12+="548000 "
            
            infa4=""
            
            infa4+='''TOSHIBA HDD 
     500GB'''
            h4.destroy()
            
            g()
        p125 = Image.open('150233.jpg').resize((200,200))
        u125= ImageTk.PhotoImage(p125)
        ff2=Button(h4,image=u125,bg="black",command=de3)
        ff2.place(x=620,y=70)
        ss1=Label(h4,text='''TOSHIBA HDD 
     500GB''')
        ss1.place(x=825,y=70)
        ee1=Label(h4,text="548 000  so'm",fg="black",bg="white",cursor="tcross")
        ee1.place(x=825,y=250)
        def de4():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="JtFoFvplRKDVqWLSYunN8ts3IvSjHRCnGUExNi8a.jpeg"
            y12+="+"
            y12+="1220400"
            
            infa4=""
            
            infa4+='''HDD Seagate Barracuda 4 TB'''
            h4.destroy()
            
            g()
        p126 = Image.open('JtFoFvplRKDVqWLSYunN8ts3IvSjHRCnGUExNi8a.jpeg').resize((200,200))
        u126= ImageTk.PhotoImage(p126)
        ff3=Button(h4,image=u126,bg="black",command=de4)
        ff3.place(x=910,y=70)
        ss2=Label(h4,text='''HDD Seagate Barracuda 4 TB''')
        ss2.place(x=1115,y=70)
        ee2=Label(h4,text="1 220 400 so'm",fg="black",bg="white",cursor="tcross")
        ee2.place(x=1115,y=250)





        def de5():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="11.jpg"
            y12+="+"
            y12+="684000"
            
            infa4=""
            
            infa4+=''' HDD 1000 Gb Toshiba 
        (HDWD110UZSVA)'''
            h4.destroy()
            
            g()

        p127 = Image.open('11.jpg').resize((200,200))
        u127= ImageTk.PhotoImage(p127)
        ff4=Button(h4,image=u127,bg="black",command=de5)
        ff4.place(x=0,y=300)
        s127=Label(h4,text=''' HDD 1000 Gb Toshiba 
        (HDWD110UZSVA)''')
        s127.place(x=205,y=300)
        e127=Label(h4,text="684 000 so'm",fg="black",bg="white",cursor="tcross")
        e127.place(x=205,y=460)
        def de6():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="G5FlS4Jh7o8IouGDlaf2e9DJYmdsuWM7TcHaHHXa.png"
            y12+="+"
            y12+="3240000 "
            
            infa4=""
            
            infa4+=''' Seagate Barracuda
         HDD 8tb'''
            h4.destroy()
            
            g()
        p128 = Image.open('G5FlS4Jh7o8IouGDlaf2e9DJYmdsuWM7TcHaHHXa.png').resize((200,200))
        u128= ImageTk.PhotoImage(p128)
        ff5=Button(h4,image=u128,bg="black",command=de6)
        ff5.place(x=300,y=300)
        ss4=Label(h4,text=''' Seagate Barracuda
         HDD 8tb''')
        ss4.place(x=505,y=300)
        ee4=Label(h4,text="3 240 000  so'm",fg="black",bg="white",cursor="tcross")
        ee4.place(x=505,y=460)
        def de7():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="638715bb1d1ba.jpg"
            y12+="+"
            y12+="5175000"
            
            infa4=""
            
            infa4+='''WD Purple pro 10 tb'''
            h4.destroy()
            
            g()
        p129 = Image.open('638715bb1d1ba.jpg').resize((200,200))
        u129= ImageTk.PhotoImage(p129)
        ff6=Button(h4,image=u129,bg="black",command=de7)
        ff6.place(x=620,y=300)
        ss5=Label(h4,text='''WD Purple pro 10 tb''')
        ss5.place(x=825,y=300)
        ee5=Label(h4,text="5 175 000  so'm",fg="black",bg="white",cursor="tcross")
        ee5.place(x=825,y=460)
        def de8():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="475848_v03_b.jpg"
                        
            y12+="+"
            y12+="684000"
            
            infa4=""
            
            infa4+='''WD Purple 3Tb'''
            h4.destroy()
            
            g()
        p1210 = Image.open('475848_v03_b.jpg').resize((200,200))
        u1210= ImageTk.PhotoImage(p1210)
        ff7=Button(h4,image=u1210,bg="black",command=de8)
        ff7.place(x=910,y=300)
        ss6=Label(h4,text='''TeamGroup DDR4 
            16GB 3200Mhz''')
        ss6.place(x=1115,y=300)
        ee6=Label(h4,text="684 000 so'm",fg="black",bg="white",cursor="tcross")
        ee6.place(x=1115,y=460)





        def de9():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="7f100b7b36092fb9b06dfb4fac3609312021050512460398803sgLbonqtYw.jpg.webp"
            y12+="+"
            y12+="3450000"
            
            infa4=""
            
            infa4+=''' Western Digital 
        Purple 8 Тб'''
            h4.destroy()
            
            g()
        p1211 = Image.open('7f100b7b36092fb9b06dfb4fac3609312021050512460398803sgLbonqtYw.jpg.webp').resize((200,200))
        u1211= ImageTk.PhotoImage(p1211)
        ff8=Button(h4,image=u1211,bg="black",command=de9)
        ff8.place(x=0,y=530)
        s1211=Label(h4,text=''' Western Digital 
        Purple 8 Тб'''  )
        s1211.place(x=205,y=530)
        e1211=Label(h4,text="3 450 000 so'm",fg="black",bg="white",cursor="tcross")
        e1211.place(x=205,y=690)
        def de10():
            global sos4,y12,infa4
            sos4=""
            
            sos4+="3tb.jpg"
            y12+="+"
            y12+="940000 "
            
            infa4=""
            
            infa4+='''Purple — 3_TB 
            WD30PURX-78'''
            h4.destroy()
            
            g()
        p1212 = Image.open('3tb.jpg').resize((200,200))
        u1212= ImageTk.PhotoImage(p1212)
        ff9=Button(h4,image=u1212,bg="black",command=de10)
        ff9.place(x=300,y=530)
        ss8=Label(h4,text='''Purple — 3_TB 
        WD30PURX-78''')
        ss8.place(x=505,y=530)
        ee8=Label(h4,text="940 000  so'm",fg="black",bg="white",cursor="tcross")
        ee8.place(x=505,y=690)
        def de11():
            global sos4,y12,infa4
            
            sos4=""
            
            sos4+="14q8bw1uax9zuirg8yyfuh5mo0xxsrz2.png"
            y12+="+"
            y12+="2172000"
            
            infa4=""
            
            infa4+='''WD20PURZ Purple 
            2000GB 64MB'''
            h4.destroy()
            
            g()
        p1213 = Image.open('14q8bw1uax9zuirg8yyfuh5mo0xxsrz2.png').resize((200,200))
        u1213= ImageTk.PhotoImage(p1213)
        ff10=Button(h4,image=u1213,bg="black",command=de11)
        ff10.place(x=620,y=530)
        ss9=Label(h4,text='''WD20PURZ Purple 
            2000GB 64MB''')
        ss9.place(x=825,y=530)
        ee9=Label(h4,text="2 172 000 so'm",fg="black",bg="white",cursor="tcross")
        ee9.place(x=825,y=690)
        def de12():
            global sos4,y12,infa4
            
            sos4=""
            sos4+="u_s7H-XwEI2B3xyXBr8GsQJpaDn2sOrm.jpg"
            y12+="+"
            y12+="558600 "
            infa4=""
            
            infa4+=''' Hikvision SSD 512GB
             SATA III'''
            h4.destroy()
            g()

        p1214 = Image.open('u_s7H-XwEI2B3xyXBr8GsQJpaDn2sOrm.jpg').resize((200,200))
        u1214= ImageTk.PhotoImage(p1214)
        ff11=Button(h4,image=u1214,bg="black",command=de12)
        ff11.place(x=910,y=530)
        ss10=Label(h4,text='''Hikvision SSD 512GB
         SATA III''')
        ss10.place(x=1115,y=530)
        ee10=Label(h4,text="558 600 so'm",fg="black",bg="white",cursor="tcross")
        ee10.place(x=1115,y=560)  
        
        h4.mainloop()




    xa2=Button(h,text="qattiq disk",bg="black",fg="white",command=qattiq )
    xa2.place(x=850,y=2) 

    p1215xa2 = Image.open(sos4).resize((200,200))
    u1215xa2= ImageTk.PhotoImage(p1215xa2)
    s12xa2=Label(h,image=u1215xa2)
    s12xa2.place(x=850,y=35)

    s1212xa2=Label(h,text=infa4)
    s1212xa2.place(x=850,y=235)





    def korpus():
        

        h.destroy()
        h5=Tk()
        h5.title("ko'rpus")
        h5.geometry("1370x800")
        h5.resizable(0,0)
        rasmxa3 = Image.open('Biznes-plan-po-remontu-kompyuterov-960x960.png').resize((1370,800))
        sssxa3 = ImageTk.PhotoImage(rasmxa3)
        labelxa3 = Label(h5, image=sssxa3)
        labelxa3.place(x=0, y=0)

        ddxa3=Label(h5,text="ko'rpus",bg="white",fg="dark blue",font=("Times",40,"bold"),width=45,cursor="dotbox")
        ddxa3.place(x=0,y=0)
        def de1():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="te92e30a1d.jpg"
            y12+="+"
            y12+="11429000 "
            
            
            
            
         
            h5.destroy()
            
            g()
        p123 = Image.open('te92e30a1d.jpg').resize((200,200))
        u123= ImageTk.PhotoImage(p123)
        ff=Button(h5,image=u123,bg="black",command=de1)
        ff.place(x=0,y=70)
      
        e123=Label(h5,text="11 429 000 so'm",fg="black",bg="white",cursor="tcross")
        e123.place(x=205,y=250)
        def de2():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="[table_image] _2022.png"
            y12+="+"
            y12+="217000"
            
            
            
            
            h5.destroy()
            
            g()
        p124 = Image.open('[table_image] _2022.png').resize((200,200))
        u124= ImageTk.PhotoImage(p124)
        ff1=Button(h5,image=u124,bg="black",command=de2)
        ff1.place(x=300,y=70)
        
        ee=Label(h5,text="5 450 000 so'm",fg="black",bg="white",cursor="tcross")
        ee.place(x=505,y=250)
        def de3():
            global sos5,y12,infa5
            sos5=""
            
            sos5+='CorsairVengeanceRGBPro(2x16gb)3200Mhz2-500x500.jpg'
            y12+="+"
            y12+="638000"
            
            
       
            h5.destroy()
            
            g()
        p125 = Image.open('CorsairVengeanceRGBPro(2x16gb)3200Mhz2-500x500.jpg').resize((200,200))
        u125= ImageTk.PhotoImage(p125)
        ff2=Button(h5,image=u125,bg="black",command=de3)
        ff2.place(x=620,y=70)
       
        ee1=Label(h5,text="638 000 so'm",fg="black",bg="white",cursor="tcross")
        ee1.place(x=825,y=250)
        def de4():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="Без названия (1).jpg"
            y12+="+"
            y12+="1648000 "
            
            
            
            h5.destroy()
            
            g()
        p126 = Image.open('Без названия (1).jpg').resize((200,200))
        u126= ImageTk.PhotoImage(p126)
        ff3=Button(h5,image=u126,bg="black",command=de4)
        ff3.place(x=910,y=70)
       
        ee2=Label(h5,text="1 648 000  so'm",fg="black",bg="white",cursor="tcross")
        ee2.place(x=1115,y=250)





        def de5():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="30058924bb.webp"
            y12+="+"
            y12+="5000000 "
            
            
            
            
            h5.destroy()
            
            g()

        p127 = Image.open('30058924bb.webp').resize((200,200))
        u127= ImageTk.PhotoImage(p127)
        ff4=Button(h5,image=u127,bg="black",command=de5)
        ff4.place(x=0,y=300)
       
        e127=Label(h5,text="5 000 000  so'm",fg="black",bg="white",cursor="tcross")
        e127.place(x=205,y=460)
        def de6():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="img_20211124141354.jpeg"
            y12+="+"
            y12+="2450000"
            
            
            
            
            h5.destroy()
            
            g()
        p128 = Image.open('img_20211124141354.jpeg').resize((200,200))
        u128= ImageTk.PhotoImage(p128)
        ff5=Button(h5,image=u128,bg="black",command=de6)
        ff5.place(x=300,y=300)
    
        ee4=Label(h5,text="2 450 000 so'm",fg="black",bg="white",cursor="tcross")
        ee4.place(x=505,y=460)
        def de7():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="images (3).jpg"
            y12+="+"
            y12+="450000"
            
            
           
            h5.destroy()
            
            g()
        p129 = Image.open('images (3).jpg').resize((200,200))
        u129= ImageTk.PhotoImage(p129)
        ff6=Button(h5,image=u129,bg="black",command=de7)
        ff6.place(x=620,y=300)
        
        ee5=Label(h5,text="450 000so'm",fg="black",bg="white",cursor="tcross")
        ee5.place(x=825,y=460)
        def de8():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="images (4).jpg"
                        
            y12+="+"
            y12+="2450000"
            
            
            
            
            h5.destroy()
            
            g()
        p1210 = Image.open('images (4).jpg').resize((200,200))
        u1210= ImageTk.PhotoImage(p1210)
        ff7=Button(h5,image=u1210,bg="black",command=de8)
        ff7.place(x=910,y=300)
    
        ee6=Label(h5,text="2 450 000 so'm",fg="black",bg="white",cursor="tcross")
        ee6.place(x=1115,y=460)





        def de9():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="ccnb283b3ho5lmupnu0g.jpg"
            y12+="+"
            y12+="459000"
            
            
            
            
            h5.destroy()
            
            g()
        p1211 = Image.open('ccnb283b3ho5lmupnu0g.jpg').resize((200,200))
        u1211= ImageTk.PhotoImage(p1211)
        ff8=Button(h5,image=u1211,bg="black",command=de9)
        ff8.place(x=0,y=530)
     
        e1211=Label(h5,text="459 000 so'm",fg="black",bg="white",cursor="tcross")
        e1211.place(x=205,y=690)
        def de10():
            global sos5,y12,infa5
            sos5=""
            
            sos5+="Без названия (2).jpg"
            y12+="+"
            y12+="480000"
            
            
            
            
            h5.destroy()
            
            g()
        p1212 = Image.open('Без названия (2).jpg').resize((200,200))
        u1212= ImageTk.PhotoImage(p1212)
        ff9=Button(h5,image=u1212,bg="black",command=de10)
        ff9.place(x=300,y=530)
      
        ee8=Label(h5,text="480 000 so'm",fg="black",bg="white",cursor="tcross")
        ee8.place(x=505,y=690)
        def de11():
            global sos5,y12,infa5
            
            sos5=""
            
            sos5+="cougar-conquer-_-5lmr-_10.png"
            y12+="+"
            y12+="3670000"
            
            
            
            h5.destroy()
            
            g()
        p1213 = Image.open('cougar-conquer-_-5lmr-_10.png').resize((200,200))
        u1213= ImageTk.PhotoImage(p1213)
        ff10=Button(h5,image=u1213,bg="black",command=de11)
        ff10.place(x=620,y=530)
        
        ee9=Label(h5,text="3 670 000 so'm",fg="black",bg="white",cursor="tcross")
        ee9.place(x=825,y=690)
        def de12():
            global sos5,y12,infa5
            
            sos5=""
            sos5+="Без названия (3).jpg"
            y12+="+"
            y12+="600450"
            
            
            
            h5.destroy()
            g()

        p1214 = Image.open('Без названия (3).jpg').resize((200,200))
        u1214= ImageTk.PhotoImage(p1214)
        ff11=Button(h5,image=u1214,bg="black",command=de12)
        ff11.place(x=910,y=530)

        ee10=Label(h5,text="600 450 so'm",fg="black",bg="white",cursor="tcross")
        ee10.place(x=1115,y=560)  
        
        h5.mainloop()

    xa3=Button(h,text="ko'rpus",bg="black",fg="white",command=korpus )
    xa3.place(x=1100,y=2) 

    p1215xa3 = Image.open(sos5).resize((200,200))
    u1215xa3= ImageTk.PhotoImage(p1215xa3)
    s12xa3=Label(h,image=u1215xa3)
    s12xa3.place(x=1100,y=35)
    



    def tegatish():
        h.destroy()
        ura=Tk()
        ura.geometry("1370x800")
        ura.resizable(0,0)
        rasmxa = Image.open('999021186.jpg').resize((1370,860))
        ssssxa = ImageTk.PhotoImage(rasmxa)
        labelxaxaxa = Label(ura, image=ssssxa)
        labelxaxaxa.place(x=0, y=-60)

        

        rasmxa1 = Image.open(sos5).resize((200,200))
        ssssxa1 = ImageTk.PhotoImage(rasmxa1)
        ass=Label(ura,image=ssssxa1,bg="black")
        ass.place(x=550,y=400)
        ass2=Label(ura,text='''<-  Mana sizning  
        kompyuteringiz''',font=("Times",40,"bold"),bg="black",fg="blue")
        ass2.place(x=800,y=400)
        ass3=Label(ura,text=f"{t123} so'm",fg="green",font=("Times",40,"bold"))
        ass3.place(x=550,y=600)
        ass1=Label(ura,text='''Tabriklaymiz siz kompyuter sotib oldingiz 
        siz bizning servisimiz bilan 
        ishlaganingiz uchun rahmat 
        va yana qaytasiz deb umit qilamiz''',font=("Times",40,"bold"),bg="black",fg="blue")
        ass1.place(x=150,y=100)


        ura.mainloop()
    


    
    xaxa1=Label(h,text=''' sotib olishdan oldin o'ylab korgin 
    agar siz hozir talagan 
    narsalaringizni bilmasdan 
    tanlagan bilsangiz 
    keyin ozgartira ololmaysiz ''',bg="black",fg="red")
    xaxa1.place(x=350,y=400)
    xaxa=Button(h,text="Sotib olish",font=("Times",40,"bold"),command=tegatish)
    xaxa.place(x=550,y=400)




        












    








   





 
        
        


        
    # print(t123)
        






    h.mainloop()
f=Button(a,text="Start",font=("Times",40,"bold"),bg="dark blue",cursor="hand2",highlightthickness=0,
bd=0,fg="#34eb9b",activebackground="#34eb9b",activeforeground="dark blue",command=g2)
f.place(x=620,y=480)

a.mainloop()
