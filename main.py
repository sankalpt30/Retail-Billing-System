from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#Functionality Part

def clear():
    HondaCityEntry.delete(0, END)
    HondaAmazeEntry.delete(0, END)
    HondaCivicEntry.delete(0, END)
    HondaElevateEntry.delete(0, END)
    HondaAccordEntry.delete(0, END)

    MarutiSuzukiEntry.delete(0, END)
    MarutiBrezzaEntry.delete(0, END)
    MarutiSwiftEntry.delete(0, END)
    MarutiWagonEntry.delete(0, END)
    MarutiBalenoEntry.delete(0, END)

    MahindraTharEntry.delete(0, END)
    MahindraXUVEntry.delete(0, END)
    MahindraBoleroEntry.delete(0, END)
    MahindraScorpioEntry.delete(0, END)
    MahindraMarazzoEntry.delete(0, END)

    HondaCityEntry.insert(0, 0)
    HondaAmazeEntry.insert(0, 0)
    HondaCivicEntry.insert(0, 0)
    HondaElevateEntry.insert(0, 0)
    HondaAccordEntry.insert(0, 0)

    MarutiSuzukiEntry.insert(0,0)
    MarutiBrezzaEntry.insert(0,0)
    MarutiSwiftEntry.insert(0,0)
    MarutiWagonEntry.insert(0,0)
    MarutiBalenoEntry.insert(0,0)

    MahindraTharEntry.insert(0,0)
    MahindraXUVEntry.insert(0,0)
    MahindraBoleroEntry.insert(0,0)
    MahindraScorpioEntry.insert(0,0)
    MahindraMarazzoEntry.insert(0,0)

    HondapriceEntry.delete(0,END)
    MarutipriceEntry.delete(0,END)
    MahindrapriceEntry.delete(0,END)

    HondataxEntry.delete(0, END)
    MarutitaxEntry.delete(0, END)
    MahindrataxEntry.delete(0, END)

    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    BillEntry.delete(0,END)

    textarea.delete(1.0,END)



#For email password we have to create Application specific Password:
  #open your gmail,click on accounts,thn on security,thn on 2 step verification


def print_bill():
    if textarea.get(1.0,END)=='\n':                     #Textarea is empty
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')                                #Using tempfile for creating a temporary file
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)                            #smtplib is used for gmail purpose
            ob.starttls()                                                              #starttls() is used for establishing a secure connection
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recipientEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()                                                      #breaks the root1 windows screen
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)


    if textarea.get(1.0,END)=='\n':                     #Textarea is empty
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()                                      #You can only access this root1 window
        root1.title('Send Gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)                           #Can't maximize this windows


        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)


        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recipientLabel = Label(recipientFrame, text="Recipient's Email", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recipientLabel.grid(row=0, column=0, padx=10, pady=8)
        recipientEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recipientEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20',
                               fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)


        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','')
                              .replace('\t\t\t','\t\t'))



        sendButton=Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)


        root1.mainloop()


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==BillEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):                             #used for creating bill named folder
    os.mkdir('bills')                                       #mkdir means make folder



def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number:{billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber=random.randint(500,1000)



def total():
    global HondaCityPrice, HondaAmazePrice, HondaCivicPrice, HondaElevatePrice, HondaAccordPrice
    global MarutiSuzukiPrice, MarutiBrezzaPrice, MarutiSwiftPrice, MarutiWagonPrice, MarutiBalenoPrice
    global MahindraTharPrice, MahindraXUVPrice, MahindraBoleroPrice, MahindraScorpioPrice, MahindraMarazzoPrice
    global totalbill
    #Honda Calculation
    HondaCityPrice=int(HondaCityEntry.get())*35000
    HondaAmazePrice=int(HondaAmazeEntry.get())*40000
    HondaCivicPrice=int(HondaCivicEntry.get())*43000
    HondaElevatePrice=int(HondaElevateEntry.get())*33000
    HondaAccordPrice=int(HondaAccordEntry.get())*45000

    totalhondaprice=HondaCityPrice+HondaAmazePrice+HondaCivicPrice+HondaElevatePrice+HondaAccordPrice
    HondapriceEntry.delete(0,END)
    HondapriceEntry.insert(0,f'{totalhondaprice} Rs')
    HondaTax=totalhondaprice*0.12
    HondataxEntry.delete(0,END)
    HondataxEntry.insert(0,f'{HondaTax} Rs')


    #Maruti Calculation
    MarutiSuzukiPrice=int(MarutiSuzukiEntry.get())*34000
    MarutiBrezzaPrice=int(MarutiBrezzaEntry.get())*42000
    MarutiSwiftPrice = int(MarutiSwiftEntry.get()) * 37000
    MarutiWagonPrice=int(MarutiWagonEntry.get())*30000
    MarutiBalenoPrice = int(MarutiBalenoEntry.get()) * 40000

    totalmarutiprice=MarutiSuzukiPrice+MarutiBrezzaPrice+MarutiBalenoPrice+MarutiWagonPrice+MarutiSwiftPrice
    MarutipriceEntry.delete(0,END)
    MarutipriceEntry.insert(0,f'{totalmarutiprice} Rs')
    MarutiTax=totalmarutiprice*0.05
    MarutitaxEntry.delete(0,END)
    MarutitaxEntry.insert(0,f'{MarutiTax} Rs')



    #Mahindra Calculation
    MahindraTharPrice=int(MahindraTharEntry.get())*45000
    MahindraXUVPrice=int(MahindraXUVEntry.get())*35000
    MahindraBoleroPrice=int(MahindraBoleroEntry.get())*44000
    MahindraScorpioPrice=int(MahindraScorpioEntry.get())*50000
    MahindraMarazzoPrice=int(MahindraMarazzoEntry.get())*37000

    totalmahindraprice=MahindraTharPrice+MahindraXUVPrice+MahindraBoleroPrice+MahindraScorpioPrice+MahindraMarazzoPrice
    MahindrapriceEntry.delete(0,END)
    MahindrapriceEntry.insert(0,f'{totalmahindraprice} Rs')
    MahindraTax=totalmahindraprice*0.08
    MahindrataxEntry.delete(0,END)
    MahindrataxEntry.insert(0,f'{MahindraTax} Rs')



    totalbill=totalhondaprice+totalmarutiprice+totalmahindraprice+HondaTax+MarutiTax+MahindraTax




#GUI Part(Design of Page)
root = Tk()  # using tkinter class Tk() for creating windows
root.title('CHROME CARS')
root.geometry('1270x685')  # geometry function is used for screen size (width x height)
root.iconbitmap('icon.ico')  # iconbitmap is used for updating icon of window
headingLabel = Label(root, text='Retail Billing System', font=('Berlin Sans FB', 30, 'bold')
                     , bg='cadetblue', fg='black', bd=12,
                     relief=GROOVE)  # Label is used for adding the text, fg = foreground
headingLabel.pack(fill=X)  # pack() is used to print the text at top, fill is used to cover whole text

# Creating Frame(Customer details)
customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold')
                                    , bg='Wheat2', fg='black', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 11, 'bold')
                  , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
nameLabel.grid(row=0, column=0, padx=20, pady=2)
# grid is used to add things on windows in form of rows and columns
# padx,pady is used for giving horizontal spacing and vertical spacing

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)  # Entry is used for creating entry fields
nameEntry.grid(row=0, column=1, padx=8)

PhoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 11, 'bold')
                   , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
PhoneLabel.grid(row=0, column=2, padx=20, pady=2)

PhoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7,
                   width=18)  # Entry is used for creating entry fields
PhoneEntry.grid(row=0, column=3, padx=8)

BillLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 11, 'bold')
                  , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
BillLabel.grid(row=0, column=4, padx=20, pady=2)

BillEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)  # Entry is used for creating entry fields
BillEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='SEARCH', font=('arial', 12, 'bold')
                      ,bd=7, width=10,command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

Honda_frame = LabelFrame(productsFrame, text='HONDA CARS', font=('times new roman', 15, 'bold')
                         , bg='Wheat2', fg='black', bd=8, relief=GROOVE)
Honda_frame.grid(row=0, column=0, padx=5)
# Honda_frame.pack()

HondaCityLabel = Label(Honda_frame, text='Honda City', font=('times new roman', 11, 'bold')
                       , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondaCityLabel.grid(row=1, column=0, padx=20, pady=5, sticky='w')

HondaCityEntry = Entry(Honda_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
HondaCityEntry.grid(row=1, column=1, padx=8, pady=5)
HondaCityEntry.insert(0,0)

HondaAmazeLabel = Label(Honda_frame, text='Honda Amaze', font=('times new roman', 11, 'bold')
                        , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondaAmazeLabel.grid(row=2, column=0, padx=20, pady=5, sticky='w')

HondaAmazeEntry = Entry(Honda_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
HondaAmazeEntry.grid(row=2, column=1, padx=8, pady=5)
HondaAmazeEntry.insert(0,0)

HondaCivicLabel = Label(Honda_frame, text='Honda Civic', font=('times new roman', 11, 'bold')
                        , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondaCivicLabel.grid(row=3, column=0, padx=20, pady=5, sticky='w')

HondaCivicEntry = Entry(Honda_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
HondaCivicEntry.grid(row=3, column=1, padx=8, pady=5)
HondaCivicEntry.insert(0,0)

HondaElevateLabel = Label(Honda_frame, text='Honda Elevate', font=('times new roman', 11, 'bold')
                          , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondaElevateLabel.grid(row=4, column=0, padx=20, pady=5, sticky='w')

HondaElevateEntry = Entry(Honda_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
HondaElevateEntry.grid(row=4, column=1, padx=8, pady=5)
HondaElevateEntry.insert(0,0)

HondaAccordLabel = Label(Honda_frame, text='Honda Accord', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondaAccordLabel.grid(row=5, column=0, padx=20, pady=5, sticky='w')

HondaAccordEntry = Entry(Honda_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
HondaAccordEntry.grid(row=5, column=1, padx=8, pady=5)
HondaAccordEntry.insert(0,0)

Maruti_frame = LabelFrame(productsFrame, text='MARUTI CARS', font=('times new roman', 15, 'bold')
                          , bg='Wheat2', fg='black', bd=8, relief=GROOVE)

Maruti_frame.grid(row=0, column=1, padx=5)
# Maruti_frame.pack()


MarutiSuzukiLabel = Label(Maruti_frame, text='MarutiSuzuki', font=('times new roman', 11, 'bold')
                          , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutiSuzukiLabel.grid(row=1, column=0, padx=20, pady=5, sticky='w')

MarutiSuzukiEntry = Entry(Maruti_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MarutiSuzukiEntry.grid(row=1, column=1, padx=8, pady=5)  # sticky is used for alignment
MarutiSuzukiEntry.insert(0,0)

MarutiBrezzaLabel = Label(Maruti_frame, text='MarutiBrezza', font=('times new roman', 11, 'bold')
                          , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutiBrezzaLabel.grid(row=2, column=0, padx=20, pady=5, sticky='w')

MarutiBrezzaEntry = Entry(Maruti_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MarutiBrezzaEntry.grid(row=2, column=1, padx=8, pady=5)  # sticky is used for alignment
MarutiBrezzaEntry.insert(0,0)

MarutiSwiftLabel = Label(Maruti_frame, text='MarutiSwift', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutiSwiftLabel.grid(row=3, column=0, padx=20, pady=5, sticky='w')

MarutiSwiftEntry = Entry(Maruti_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MarutiSwiftEntry.grid(row=3, column=1, padx=8, pady=5)  # sticky is used for alignment
MarutiSwiftEntry.insert(0,0)

MarutiWagonLabel = Label(Maruti_frame, text='MarutiWagon', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutiWagonLabel.grid(row=4, column=0, padx=20, pady=5, sticky='w')

MarutiWagonEntry = Entry(Maruti_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MarutiWagonEntry.grid(row=4, column=1, padx=8, pady=5)  # sticky is used for alignment
MarutiWagonEntry.insert(0,0)

MarutiBalenoLabel = Label(Maruti_frame, text='MarutiBaleno', font=('times new roman', 11, 'bold')
                          , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutiBalenoLabel.grid(row=5, column=0, padx=20, pady=5, sticky='w')

MarutiBalenoEntry = Entry(Maruti_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MarutiBalenoEntry.grid(row=5, column=1, padx=8, pady=5)  # sticky is used for alignment
MarutiBalenoEntry.insert(0,0)

Mahindra_frame = LabelFrame(productsFrame, text='MAHINDRA CARS', font=('times new roman', 15, 'bold')
                            , bg='Wheat2', fg='black', bd=8, relief=GROOVE)

Mahindra_frame.grid(row=0, column=2, padx=5)

MahindraTharLabel = Label(Mahindra_frame, text='MahindraThar', font=('times new roman', 11, 'bold')
                          , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindraTharLabel.grid(row=1, column=0, padx=20, pady=5, sticky='w')

MahindraTharEntry = Entry(Mahindra_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MahindraTharEntry.grid(row=1, column=1, padx=8, pady=5)  # sticky is used for alignment
MahindraTharEntry.insert(0,0)

MahindraXUVLabel = Label(Mahindra_frame, text='MahindraXUV', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindraXUVLabel.grid(row=2, column=0, padx=20, pady=5, sticky='w')

MahindraXUVEntry = Entry(Mahindra_frame, font=('arial', 15), bd=7, width=7)  # Entry is used for creating entry fields
MahindraXUVEntry.grid(row=2, column=1, padx=8, pady=5)  # sticky is used for alignment
MahindraXUVEntry.insert(0,0)

MahindraBoleroLabel = Label(Mahindra_frame, text='MahindraBolero', font=('times new roman', 11, 'bold')
                            , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindraBoleroLabel.grid(row=3, column=0, padx=20, pady=5, sticky='w')

MahindraBoleroEntry = Entry(Mahindra_frame, font=('arial', 15), bd=7,
                            width=7)  # Entry is used for creating entry fields
MahindraBoleroEntry.grid(row=3, column=1, padx=8, pady=5)  # sticky is used for alignment
MahindraBoleroEntry.insert(0,0)

MahindraScorpioLabel = Label(Mahindra_frame, text='MahindraScorpio', font=('times new roman', 11, 'bold')
                             , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindraScorpioLabel.grid(row=4, column=0, padx=20, pady=5, sticky='w')

MahindraScorpioEntry = Entry(Mahindra_frame, font=('arial', 15), bd=7,
                             width=7)  # Entry is used for creating entry fields
MahindraScorpioEntry.grid(row=4, column=1, padx=8, pady=5)  # sticky is used for alignment
MahindraScorpioEntry.insert(0,0)

MahindraMarazzoLabel = Label(Mahindra_frame, text='MahindraMarazzo', font=('times new roman', 11, 'bold')
                             , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindraMarazzoLabel.grid(row=5, column=0, padx=20, pady=5, sticky='w')

MahindraMarazzoEntry = Entry(Mahindra_frame, font=('arial', 15), bd=7,
                             width=7)  # Entry is used for creating entry fields
MahindraMarazzoEntry.grid(row=5, column=1, padx=8, pady=5)  # sticky is used for alignment
MahindraMarazzoEntry.insert(0,0)

Billframe = Frame(productsFrame, bd=8, relief=GROOVE)
Billframe.grid(row=0, column=3, padx=10)

BillAreaLabel = Label(Billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
BillAreaLabel.pack(fill=X)

scrollbar = Scrollbar(Billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(Billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

Bill_Menu_frame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold')
                             , bg='Wheat2', fg='black', bd=8, relief=GROOVE)
Bill_Menu_frame.pack(fill=X)

HondapriceLabel = Label(Bill_Menu_frame, text='Honda Price', font=('times new roman', 11, 'bold')
                        , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondapriceLabel.grid(row=0, column=0, padx=20, pady=6, sticky='w')

HondapriceEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7, width=10)  # Entry is used for creating entry fields
HondapriceEntry.grid(row=0, column=1, padx=8, pady=6)

MarutipriceLabel = Label(Bill_Menu_frame, text='Maruti Price', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutipriceLabel.grid(row=1, column=0, padx=20, pady=6, sticky='w')

MarutipriceEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7, width=10)  # Entry is used for creating entry fields
MarutipriceEntry.grid(row=1, column=1, padx=8, pady=6)

MahindrapriceLabel = Label(Bill_Menu_frame, text='Mahindra Price', font=('times new roman', 11, 'bold')
                           , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindrapriceLabel.grid(row=2, column=0, padx=10, pady=6, sticky='w')

MahindrapriceEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7,
                           width=10)  # Entry is used for creating entry fields
MahindrapriceEntry.grid(row=2, column=1, padx=8, pady=6)

HondataxLabel = Label(Bill_Menu_frame, text='Honda Tax', font=('times new roman', 11, 'bold')
                      , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
HondataxLabel.grid(row=0, column=2, padx=20, pady=6, sticky='w')

HondataxEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7, width=10)  # Entry is used for creating entry fields
HondataxEntry.grid(row=0, column=3, padx=8, pady=6)

MarutitaxLabel = Label(Bill_Menu_frame, text='Maruti Tax', font=('times new roman', 11, 'bold')
                       , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MarutitaxLabel.grid(row=1, column=2, padx=20, pady=6, sticky='w')

MarutitaxEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7, width=10)  # Entry is used for creating entry fields
MarutitaxEntry.grid(row=1, column=3, padx=8, pady=6)

MahindrataxLabel = Label(Bill_Menu_frame, text='Mahindra Tax', font=('times new roman', 11, 'bold')
                         , bg='Wheat2', fg='black', bd=6, relief=GROOVE)
MahindrataxLabel.grid(row=2, column=2, padx=10, pady=6, sticky='w')

MahindrataxEntry = Entry(Bill_Menu_frame, font=('arial', 15), bd=7, width=10)  # Entry is used for creating entry fields
MahindrataxEntry.grid(row=2, column=3, padx=8, pady=6)

buttonFrame = Frame(Bill_Menu_frame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

TotalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='Wheat2', fg='black'
                     , bd=5, width=8, pady=10,command=total)
TotalButton.grid(row=0, column=0, pady=20, padx=5)

BillButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='Wheat2', fg='black'
                    , bd=5, width=8, pady=10,command=bill_area)
BillButton.grid(row=0, column=1, pady=20, padx=5)

EmailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='Wheat2', fg='black'
                     , bd=5, width=8, pady=10,command=send_email)
EmailButton.grid(row=0, column=2, pady=20, padx=5)

PrintButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='Wheat2', fg='black'
                     , bd=5, width=8, pady=10,command=print_bill)
PrintButton.grid(row=0, column=3, pady=20, padx=5)

ClearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='Wheat2', fg='black'
                     , bd=5, width=8, pady=10,command=clear)
ClearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()  # used for holding output screen





def bill_area():
    if nameEntry.get()=='' or PhoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif HondapriceEntry.get()=='' and MarutipriceEntry.get()=='' and MahindrapriceEntry.get()=='':
        messagebox.showerror('Error','No Products Are Selected')
    elif HondapriceEntry.get()=='0 Rs' and MarutipriceEntry.get()=='0 Rs' and MahindrapriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products Are Selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nPhone Number: {PhoneEntry.get()}')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if HondaCityEntry.get()!='0':
            textarea.insert(END,f'\nHONDA CITY\t\t\t{HondaCityEntry.get()}\t\t{HondaCityPrice} Rs')
        if HondaAmazeEntry.get()!='0':
            textarea.insert(END,f'\nHONDA AMAZE\t\t\t{HondaAmazeEntry.get()}\t\t{HondaAmazePrice} Rs')
        if HondaCivicEntry.get()!='0':
            textarea.insert(END,f'\nHONDA CIVIC\t\t\t{HondaCivicEntry.get()}\t\t{HondaCivicPrice} Rs')
        if HondaElevateEntry.get()!='0':
            textarea.insert(END,f'\nHONDA ELEVATE\t\t\t{HondaElevateEntry.get()}\t\t{HondaElevatePrice} Rs')
        if HondaAccordEntry.get()!='0':
            textarea.insert(END,f'\nHONDA ACCORD\t\t\t{HondaAccordEntry.get()}\t\t{HondaAccordPrice} Rs')


        if MarutiSuzukiEntry.get()!='0':
            textarea.insert(END,f'\nMARUTI SUZUKI\t\t\t{MarutiSuzukiEntry.get()}\t\t{MarutiSuzukiPrice} Rs')
        if MarutiBrezzaEntry.get()!='0':
            textarea.insert(END,f'\nMARUTI BREZZA\t\t\t{MarutiBrezzaEntry.get()}\t\t{MarutiBrezzaPrice} Rs')
        if MarutiSwiftEntry.get()!='0':
            textarea.insert(END,f'\nMARUTI SWIFT\t\t\t{MarutiSwiftEntry.get()}\t\t{MarutiSwiftPrice} Rs')
        if MarutiWagonEntry.get()!='0':
            textarea.insert(END,f'\nMARUTI WAGON\t\t\t{MarutiWagonEntry.get()}\t\t{MarutiWagonPrice} Rs')
        if MarutiBalenoEntry.get()!='0':
            textarea.insert(END,f'\nMARUTI BALENO\t\t\t{MarutiBalenoEntry.get()}\t\t{MarutiBalenoPrice} Rs')


        if MahindraTharEntry.get()!='0':
            textarea.insert(END,f'\nMAHINDRA THAR\t\t\t{MahindraTharEntry.get()}\t\t{MahindraTharPrice} Rs')
        if MahindraXUVEntry.get()!='0':
            textarea.insert(END,f'\nMAHINDRA XUV\t\t\t{MahindraXUVEntry.get()}\t\t{MahindraXUVPrice} Rs')
        if MahindraBoleroEntry.get()!='0':
            textarea.insert(END,f'\nMAHINDRA BOLERO\t\t\t{MahindraBoleroEntry.get()}\t\t{MahindraBoleroPrice} Rs')
        if MahindraScorpioEntry.get()!='0':
            textarea.insert(END,f'\nMAHINDRA SCORPIO\t\t\t{MahindraScorpioEntry.get()}\t\t{MahindraScorpioPrice} Rs')
        if MahindraMarazzoEntry.get()!='0':
            textarea.insert(END,f'\nMAHINDRA MARAZZO\t\t\t{MahindraMarazzoEntry.get()}\t\t{MahindraMarazzoPrice} Rs')
        textarea.insert(END, '\n-------------------------------------------------------')


        if HondataxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nHONDA TAX\t\t\t\t\t{HondataxEntry.get()}')
        if MarutitaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nMARUTI TAX\t\t\t\t\t{MarutitaxEntry.get()}')
        if MahindrataxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nMAHINDRA TAX\t\t\t\t\t{MahindrataxEntry.get()}')

        textarea.insert(END, '\n-------------------------------------------------------')

        textarea.insert(END,f'\nTotal Bill\t\t\t\t\t{totalbill} Rs')


        save_bill()

