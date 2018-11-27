from tkinter import *
from tkinter import ttk
from tkinter import messagebox as box
import mysql.connector
from PIL import Image
from PIL import ImageTk
import smtplib
from datetime import date

# LightSteelBlue1-4,DarkSeaGreen1-4,khaki1-4,paleGreen1-4


class MainPanel:

    def __init__(self, master):
        self.master = master
        width = 80
        height = 80
        self.master.img = Image.open('admin.png')
        self.master.img = self.master.img.resize((width, height), Image.ANTIALIAS)
        self.master.photoImg = ImageTk.PhotoImage(self.master.img)
        lab = Label(self.master, image=self.master.photoImg)
        lab.place(x=127, y=145)

        width_h = 420
        height_h = 150
        self.master.img_h = Image.open('paying-guest-head.png')
        self.master.img_h = self.master.img_h.resize((width_h, height_h), Image.ANTIALIAS)
        self.master.photoImg_h = ImageTk.PhotoImage(self.master.img_h)
        lab_h = Label(self.master, image=self.master.photoImg_h)
        lab_h.place(x=300, y=15)

        width_i = 150
        height_i = 150
        self.master.img_i = Image.open('paying-guest.png')
        self.master.img_i = self.master.img_i.resize((width_i, height_i), Image.ANTIALIAS)
        self.master.photoImg_i = ImageTk.PhotoImage(self.master.img_i)
        lab_i = Label(self.master, image=self.master.photoImg_i)
        lab_i.place(x=434, y=225)

        width_c = 170
        height_c = 85
        self.master.img_c = Image.open('Feedback-Complaints.png')
        self.master.img_c = self.master.img_c.resize((width_c, height_c), Image.ANTIALIAS)
        self.master.photoImg_c = ImageTk.PhotoImage(self.master.img_c)
        but_c = Button(self.master, image=self.master.photoImg_c, border=0, command =self.feedback)
        but_c.place(x=750, y=140)

        width_d = 100
        height_d = 90
        self.master.img_d = Image.open('user.png')
        self.master.img_d = self.master.img_d.resize((width_d, height_d), Image.ANTIALIAS)
        self.master.photoImg_d = ImageTk.PhotoImage(self.master.img_d)
        but_d = Button(self.master, image=self.master.photoImg_d, border=0, command=self.showcase)
        but_d.place(x=790, y=250)

        width_f = 200
        height_f = 40
        self.master.img_f = Image.open('view-food-menu.png')
        self.master.img_f = self.master.img_f.resize((width_f, height_f), Image.ANTIALIAS)
        self.master.photoImg_f = ImageTk.PhotoImage(self.master.img_f)
        but_f = Button(self.master, image=self.master.photoImg_f, border=0)
        but_f.place(x=735, y=385)

        """width_w = 22
        height_w = 22
        self.master.img_w = Image.open('whatsapp.png')
        self.master.img_w = self.master.img_w.resize((width_w, height_w), Image.ANTIALIAS)
        self.master.photoImg_w = ImageTk.PhotoImage(self.master.img_w)
        lab_w = Label(self.master, image=self.master.photoImg_w)
        lab_w.place(x=690, y=350)
        lab_no = Label(master, text='9944994400', font=('bold', 12))
        lab_no.place(x=720, y=350)

        width_pt = 22
        height_pt = 22
        self.master.img_pt = Image.open('contact.png')
        self.master.img_pt = self.master.img_pt.resize((width_pt, height_pt), Image.ANTIALIAS)
        self.master.photoImg_pt = ImageTk.PhotoImage(self.master.img_pt)
        lab_pt = Label(self.master, image=self.master.photoImg_pt)
        lab_pt.place(x=840, y=350)
        lab_pt = Label(master, text='9944994400', font=('bold', 12))
        lab_pt.place(x=880, y=350)"""

        label_heading = Label(self.master, text='Admin Login', font=('bold', 20), width=20)
        label_heading.place(x=6, y=230)

        label_username = Label(self.master, text='User Name', font=('bold', 10), width=20)
        label_username.place(x=2, y=290)
        label_password = Label(self.master, text='Password', font=('bold', 10), width=20)
        label_password.place(x=2, y=340)

        master.entry_username = ttk.Entry(self.master)
        master.entry_username.place(x=150, y=290)
        master.entry_username.focus()
        master.entry_password = ttk.Entry(self.master, show='*')
        master.entry_password.place(x=150, y=340)

        master.top = Menu(master)
        master.config(menu=master.top)
        master.setup = Menu(master.top, tearoff=0)
        master.setup.add_command(label='New...', command=self.info, underline=0)
        master.setup.add_separator()
        master.top.add_cascade(label='Setup', menu=master.setup, underline=0)

        master.submenu = Menu(master.setup, tearoff=0)
        master.submenu.add_command(label='Room', command=self.up_room, underline=0)
        #master.submenu.add_command(label='Facilities', underline=0)
        master.setup.add_cascade(label='Update', menu=master.submenu, underline=0)

        #lab_status = Label(self.master, text='Login...', bd=1, relief='sunken', anchor='w')
        #lab_status.pack(fill=X, side=BOTTOM)

        """width_li = 40
        height_li = 40
        self.master.img_li = Image.open('login-icon.png')
        self.master.img_li = self.master.img_li.resize((width_li, height_li), Image.ANTIALIAS)
        self.master.photoImg_li = ImageTk.PhotoImage(self.master.img_li)
        lab_li = Label(self.master, image=self.master.photoImg_li)
        lab_li.place(x=40, y=400)

        width_l = 190
        height_l = 55
        self.master.img_l = Image.open('login.png')
        self.master.img_l = self.master.img_l.resize((width_l, height_l), Image.ANTIALIAS)
        self.master.photoImg_l = ImageTk.PhotoImage(self.master.img_l)
        but_l = Button(self.master, image=self.master.photoImg_l, border=0)
        but_l.place(x=70, y=400)"""
        but_l = Button(self.master, text='LOGIN', bg='gray', fg='white', width=20, border=5)
        but_l.place(x=80, y=400)

        but_l.bind("<Return>", self.login)
        but_l.bind("<Button-1>", self.login)

    def feedback(self):
        feed = Toplevel(self.master)
        feed.resizable(0, 0)
        window_height = 350
        window_width = 450
        screen_width = feed.winfo_screenwidth()
        screen_height = feed.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        feed.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        feed.title('PG[Feedback & Complaint...]')
        feedback = FeedBack(feed)
        feed.transient(self.master)
        feed.grab_set()
        feed.wait_window(self.master)
        feed.mainloop()

    def up_room(self):
        up = Toplevel(self.master)
        up.resizable(0, 0)
        window_height = 200
        window_width = 380
        screen_width = up.winfo_screenwidth()
        screen_height = up.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        up.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        up.title('PG[Update Room No...]')
        uproom = Uproom(up)
        up.transient(self.master)
        up.grab_set()
        up.wait_window(self.master)
        up.mainloop()

    def info(self):
        root3 = Toplevel(self.master)
        root3.resizable(0, 0)
        window_height = 580
        window_width = 700
        screen_width = root3.winfo_screenwidth()
        screen_height = root3.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root3.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root3.title('Paying Guest[Basic Info]')
        root3.iconbitmap(r'pg.ico')
        info = Information(root3)
        root3.transient(self.master)
        root3.grab_set()
        root3.wait_window(self.master)
        root3.mainloop()

    def login(self, k_enter):

        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='admin_info')
            mycursor = db.cursor()
            mycursor.execute('select * from admin_data ')
            rows = mycursor.fetchall()
            u = ' '
            p = ' '
            username = self.master.entry_username.get()
            password = self.master.entry_password.get()
            for line in rows:
                #if username == line[1] and password == line[2]:
                if u == ' ' and p == ' ':
                    #box.showinfo('Login Successful', 'Login Success')
                    db.commit()
                    self.master.destroy()
                    root1 = Tk()
                    root1.state('zoomed')
                    root1.title('Paying Guest[Dash Board]')
                    root1.iconbitmap(r'pg.ico')
                    dashboard = DashBoard(root1)

                else:
                    box.showerror('Invalid', 'Try Again')
                    #self.master.entry_username.delete(0, 'end')
                    self.master.entry_password.delete(0, 'end')
                    self.master.entry_username.focus()

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.close()

    def showcase(self):
        showc = Toplevel(self.master)
        showc.title('Show[Courier Info]')
        window_width = 540
        window_height = 300
        screen_width = showc.winfo_screenwidth()
        screen_height = showc.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        showc.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        showc.resizable(0, 0)
        showc.iconbitmap(r'pg.ico')
        new_obj = ShowCase(showc)
        showc.transient(self.master)
        showc.grab_set()
        showc.wait_window(self.master)


class FeedBack:
    def __init__(self, master):
        self.master = master
        lab_head = Label(master, text='Complaint Section', font=('bold', 20))
        lab_head.place(x=130, y=15)

        """master.var1 = StringVar()
        master.ch_but = Checkbutton(master, text='Maintanance', variable=master.var1, font=('bold', 15))
        master.ch_but.place(x=40, y=70)

        master.var2 = StringVar()
        ch_but2 = Checkbutton(master, text='amenities', variable=master.var2, font=('bold', 15))
        ch_but2.place(x=200, y=70)

        master.var3 = StringVar()
        ch_but3 = Checkbutton(master, text='Geyser', variable=master.var3, font=('bold', 15))
        ch_but3.place(x=335, y=70)

        master.var4 = StringVar()
        ch_but4 = Checkbutton(master, text='Washing Machine', variable=master.var4, font=('bold', 15))
        ch_but4.place(x=40, y=120)

        master.var5 = StringVar()
        ch_but5 = Checkbutton(master, text='Parking', variable=master.var5, font=('bold', 15))
        ch_but5.place(x=245, y=120)"""

        labframeQ = ttk.LabelFrame(master, text=' General Queries... ')
        labframeQ.place(x=24, y=140)

        master.entQ = Text(labframeQ, width=50, height=3)
        master.entQ.pack()

        labframe = ttk.LabelFrame(master, text=' Individual Room... ')
        labframe.place(x=24, y=240)

        master.entI = Text(labframe, width=50, height=2)
        master.entI.pack()

        name_lab = Label(master, text='Name', font=('bold', 12))
        name_lab.place(x=45, y=90)

        master.ent = ttk.Entry(master, width=20)
        master.ent.place(x=110, y=90)

        room_lab = Label(master, text='Room No.', font=('bold', 12))
        room_lab.place(x=250, y=90)

        #star_lab = Label(master, text='*', font=('bold', 12), fg='red')
        #star_lab.place(x=310, y=216)

        master.room_ent = ttk.Entry(master, width=5)
        master.room_ent.place(x=340, y=90)

        master.button_ok = Button(master, text='Ok', bg='LightSteelBlue4', fg='white', width=30, height=2,
                                  command=self.comp_reg)
        master.button_ok.pack(fill=X, side=BOTTOM)
        master.button_ok.focus()

    def comp_reg(self):
        fname = self.master.ent.get()
        froom = self.master.room_ent.get()
        gen_query = self.master.entQ.get("1.0", END)
        ind_query = self.master.entI.get("1.0", END)
        """maintain = self.master.var1.get()
        food = self.master.var2.get()
        geyser = self.master.var3.get()
        w_machine = self.master.var4.get()
        parking = self.master.var5.get()"""
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='feedback')
            mycursor = db.cursor()
            mycursor.execute('INSERT INTO feed_data (name, room, gen_query, ind_query)'
                             'VALUES(%s, %s, %s, %s)', (fname, froom, gen_query, ind_query))

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        box.showinfo('Done', 'Complaint Registered')
        self.master.destroy()

        #print(fname, froom, gen_query, ind_query, maintain, food, geyser, w_machine, parking)


class ShowCase:
    def __init__(self, master):
        self.master = master

        lab_head = Label(master, text='Courier Information', font=('bold', 20))
        lab_head.place(x=150, y=15)

        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Complete Courier Info... ')
        labelsFrame.place(x=12, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='courier_info')
            mycursor = db.cursor()
            mycursor.execute('select * from courier_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[0], line[1], line[2], line[3]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2, 3, 4), height=6, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="E-Mail")
        tree.heading(3, text="Agency")
        tree.heading(4, text="Room No")

        tree.column(1, width=150)
        tree.column(2, width=180)
        tree.column(3, width=100)
        tree.column(4, width=70)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3]))

        master.button_ok = Button(master, text='Ok', bg='LightSteelBlue4', fg='white', width=30, height=2,
                                  command=self.ok)
        master.button_ok.pack(fill=X, side=BOTTOM)
        master.button_ok.focus()

    def ok(self):
        self.master.destroy()


class Uproom:
    def __init__(self, master):
        self.master = master

        master.label_head1 = Label(master, text='Update Room Number', fg='Black', font=('bold', 22))
        master.label_head1.place(x=40, y=10)

        #master.label_sub1 = Label(master, text='S', fg='Black', font=('bold', 18))
        #master.label_sub1.place(x=25, y=80)

        OPTIONS1 = [
            "Single",
            "1-Sharing",
            "2-Sharing",
            "3-Sharing",
            "4-Sharing",
            "Guest",
            "ALL"
        ]
        master.var1 = StringVar(master)
        master.var1.set(OPTIONS1[6])

        master.opt_menu1 = OptionMenu(master, master.var1, *OPTIONS1)
        master.opt_menu1.place(x=95, y=80)

        master.ent_menu1 = Entry(master)
        master.ent_menu1.place(x=200, y=85)
        master.ent_menu1.focus()

        master.button_check1 = Button(master, text='Enter', bg='brown', fg='white', width=15, height=2,)
        master.button_check1.pack(fill=X, side=BOTTOM)


class Information:
    def __init__(self, master):
        self.master = master

        master.head_room = Label(master, text='Room Details', font=('bold', 35), width=20)
        master.head_room.place(x=90, y=40)
        master.label_roomcount = Label(master, text='Room Count', font=('bold', 17), width=20)
        master.label_roomcount.place(x=95, y=150)
        master.spin = Spinbox(master, from_=1, to=25)
        master.spin.place(x=355, y=150)
        master.label_1share = Label(master, text='1 - Share', font=('bold', 17), width=20)
        master.label_1share.place(x=98, y=210)
        master.spin_1 = Spinbox(master, from_=1, to=5)
        master.spin_1.place(x=355, y=210)
        master.label_2share = Label(master, text='2 - Share', font=('bold', 17), width=20)
        master.label_2share.place(x=98, y=270)
        master.spin_2 = Spinbox(master, from_=1, to=5)
        master.spin_2.place(x=355, y=270)
        master.label_3share = Label(master, text='3 - Share', font=('bold', 17), width=20)
        master.label_3share.place(x=98, y=330)
        master.spin_3 = Spinbox(master, from_=1, to=5)
        master.spin_3.place(x=355, y=330)
        master.label_4share = Label(master, text='4 - Share', font=('bold', 17), width=20)
        master.label_4share.place(x=98, y=390)
        master.spin_4 = Spinbox(master, from_=1, to=5)
        master.spin_4.place(x=355, y=390)
        master.label_guest = Label(master, text='Guest', font=('bold', 17), width=20)
        master.label_guest.place(x=108, y=450)
        master.spin_g = Spinbox(master, from_=1, to=5)
        master.spin_g.place(x=355, y=450)

        button_setup = Button(master, text='SETUP', bg='brown', fg='white', width=30, height=3)
        button_setup.pack(fill=X, side=BOTTOM)

        #button_update = Button(master, text='CREATE', bg='brown', fg='white', width=20)
        #button_update.place(x=280, y=530)

        menubar = Menu(master)
        menubar.add_command(label='<--', font='bold', command=self.close_panel)
        master.config(menu=menubar)

    def close_panel(self):
        self.master.destroy()


class DashBoard:
    def __init__(self, master):
        self.master = master
        #self.frame = Frame(master).pack()

        #master.heightbg = 740
        #master.imgbg = Image.open('bg3.png')
        #master.imgbg = master.imgbg.resize((master.widthbg, master.heightbg), Image.ANTIALIAS)
        #master.photoImgbg = ImageTk.PhotoImage(master.imgbg)
        #master.labbg = ttk.Label(master, image=master.photoImgbg)
        #master.labbg.place(x=0, y=0)

        menubar = Menu(master)
        menubar.add_command(label='File', underline=0)
        menubar.add_command(label='Navigate', underline=0)
        menubar.add_command(label='Help', underline=0)
        master.config(menu=menubar)

        master.width = 80
        master.height = 80
        master.img1 = Image.open('signup.png')
        master.img1 = master.img1.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg1 = ImageTk.PhotoImage(master.img1)
        master.button_sgnup = Button(master, image=master.photoImg1, border=0, command=self.registration)
        master.button_sgnup.place(x=414, y=35)
        master.label_signup = Label(master, text='Register', fg='brown', width=15, font=('bold', 15))
        master.label_signup.place(x=370, y=130)

        master.width = 80
        master.height = 80
        master.img2 = Image.open('admin-setting.png')
        master.img2 = master.img2.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg2 = ImageTk.PhotoImage(master.img2)
        master.button_config = Button(master, image=master.photoImg2, border=0, command=self.conf)
        master.button_config.place(x=544, y=35)
        master.label_config = Label(master, text='Config', fg='brown', width=15, font=('bold', 15))
        master.label_config.place(x=500, y=130)

        master.width = 75
        master.height = 80
        master.img3 = Image.open('member-info.png')
        master.img3 = master.img3.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg3 = ImageTk.PhotoImage(master.img3)
        master.button_minfo = Button(master, image=master.photoImg3, border=0, command=self.mem_info)
        master.button_minfo.place(x=674, y=35)
        master.label_minfo = Label(master, text='INFO', fg='brown', width=15, font=('bold', 15))
        master.label_minfo.place(x=625, y=130)

        master.width = 84
        master.height = 84
        master.img4 = Image.open('pay.png')
        master.img4 = master.img4.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg4 = ImageTk.PhotoImage(master.img4)
        master.button_pay = Button(master, image=master.photoImg4, border=0, command=self.payment)
        master.button_pay.place(x=804, y=35)
        master.label_pay = Label(master, text='Payment', fg='brown', width=15, font=('bold', 15))
        master.label_pay.place(x=760, y=130)

        master.width = 200
        master.height = 150
        master.img5 = Image.open('rooms-available.png')
        master.img5 = master.img5.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg5 = ImageTk.PhotoImage(master.img5)
        master.button_avail = Button(master, image=master.photoImg5, border=0, command=self.availability_room)
        master.button_avail.place(x=30, y=35)
        master.label_avail = Label(master, text='Room Availability', fg='brown', width=15, font=('bold', 15))
        master.label_avail.place(x=44, y=210)

        master.width = 80
        master.height = 60
        master.img6 = Image.open('courier.png')
        master.img6 = master.img6.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg6 = ImageTk.PhotoImage(master.img6)
        master.button_courier = Button(master, image=master.photoImg6, border=0, command=self.courier)
        master.button_courier.place(x=935, y=48)
        master.label_courier = Label(master, text='Courier', fg='brown', width=15, font=('bold', 15))
        master.label_courier.place(x=890, y=130)

        master.width7 = 90
        master.height7 = 80
        master.img7 = Image.open('bot.png')
        master.img7 = master.img7.resize((master.width7, master.height7), Image.ANTIALIAS)
        master.photoImg7 = ImageTk.PhotoImage(master.img7)
        master.button_config7 = Button(master, image=master.photoImg7, border=0, command=self.complaint)
        master.button_config7.place(x=1075, y=40)
        master.label_config7 = Label(master, text='Complaint', fg='brown', width=15, font=('bold', 15))
        master.label_config7.place(x=1036, y=130)

        master.button_logout = Button(master, text='LOGOUT', bg='brown', fg='white', width=30, height=3,
                                      command=self.logout)
        master.button_logout.pack(fill=X, side=BOTTOM)

    def complaint(self):
        complaint = Toplevel(self.master)
        complaint.title('PG[Complaint Management]')
        window_width = 1200
        window_height = 300
        screen_width = complaint.winfo_screenwidth()
        screen_height = complaint.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        complaint.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        complaint.resizable(0, 0)
        complaint.iconbitmap(r'pg.ico')
        complaint_obj = ComplaintMgmt(complaint)
        complaint.transient(self.master)
        complaint.grab_set()
        complaint.wait_window(self.master)

    def courier(self):
        courier = Toplevel(self.master)
        courier.title('Courier Info')
        window_width = 380
        window_height = 200
        screen_width = courier.winfo_screenwidth()
        screen_height = courier.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        courier.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        courier.resizable(0, 0)
        courier.iconbitmap(r'pg.ico')
        courier_obj = Courier(courier)
        courier.transient(self.master)
        courier.grab_set()
        courier.wait_window(self.master)

    def payment(self):
        pay = Toplevel(self.master)
        pay.title('PG[Payment Updation]')
        pay.resizable(0, 0)
        window_height = 280
        window_width = 650
        screen_width = pay.winfo_screenwidth()
        screen_height = pay.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        pay.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        pay.iconbitmap(r'pg.ico')
        pay_in = Payment(pay)
        pay.transient(self.master)
        pay.grab_set()
        pay.wait_window(self.master)

    def mem_info(self):
        mem = Toplevel(self.master)
        mem.title('PG[Member Information]')
        mem.resizable(0, 0)
        window_height = 280
        window_width = 800
        screen_width = mem.winfo_screenwidth()
        screen_height = mem.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        mem.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        mem.iconbitmap(r'pg.ico')
        mem_in = MemberInformation(mem)
        mem.transient(self.master)
        mem.grab_set()
        mem.wait_window(self.master)

    def availability_room(self):
        available = Toplevel(self.master)
        available.title('Rooms Availability')
        available.geometry('380x200')
        available.resizable(0, 0)
        available.iconbitmap(r'pg.ico')
        available_obj = Availability(available)
        available.transient(self.master)
        available.grab_set()
        available.wait_window(self.master)

    def conf(self):
        conf = Toplevel(self.master)
        conf.title('Admin-Configuration')
        conf.resizable(0, 0)
        window_height = 200
        window_width = 380
        screen_width = conf.winfo_screenwidth()
        screen_height = conf.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        conf.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        conf.iconbitmap(r'pg.ico')
        con = Configuration(conf)
        conf.transient(self.master)
        conf.grab_set()
        conf.wait_window(self.master)
        conf.mainloop()

    def logout(self):
        self.master.ms = box.askyesno('Confirm Exit', 'Are you sure you want to exit?')
        if self.master.ms > 0:
            self.master.destroy()
            main()

    def registration(self):
        root2 = Toplevel(self.master)
        root2.resizable(0, 0)
        window_height = 580
        window_width = 1000
        screen_width = root2.winfo_screenwidth()
        screen_height = root2.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        root2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        root2.title('Paying Guest[Registration]')
        root2.iconbitmap(r'pg.ico')
        registration = Registration(root2)
        root2.transient(self.master)
        root2.grab_set()
        root2.wait_window(self.master)


class ComplaintMgmt:
    def __init__(self, master):
        self.master = master

        lab_head = Label(master, text='Complaint Management', font=('bold', 20))
        lab_head.place(x=180, y=15)

        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Received Complaints... ')
        labelsFrame.place(x=12, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='feedback')
            mycursor = db.cursor()
            mycursor.execute('select * from feed_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[0], line[1], line[2], line[3]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2, 3, 4), height=6, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="Room No")
        tree.heading(3, text="General Query")
        tree.heading(4, text="Individual Query")

        tree.column(1, width=150)
        tree.column(2, width=80)
        tree.column(3, width=460)
        tree.column(4, width=460)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3]))

        master.button_ok = Button(master, text='Ok', bg='LightSteelBlue4', fg='white', width=30, height=2,
                                  command=self.ok)
        master.button_ok.pack(fill=X, side=BOTTOM)
        master.button_ok.focus()

    def ok(self):
        self.master.destroy()


class Courier:
    def __init__(self, master):
        self.master = master
        lab_he = Label(master, text='Courier Information', font=('bold', 20))
        lab_he.place(x=70, y=20)

        master.width = 60
        master.height = 60
        master.img1 = Image.open('add-new-courier.png')
        master.img1 = master.img1.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg1 = ImageTk.PhotoImage(master.img1)
        master.button_new = Button(master, image=master.photoImg1, border=0, command=self.new_reg)
        master.button_new.place(x=90, y=80)
        master.button_new.focus()
        master.label_new = Label(master, text='New', fg='brown', width=5, font=('bold', 15))
        master.label_new.place(x=10, y=90)

        master.width1 = 60
        master.height1 = 60
        master.img2 = Image.open('pending.png')
        master.img2 = master.img2.resize((master.width, master.height), Image.ANTIALIAS)
        master.photoImg2 = ImageTk.PhotoImage(master.img2)
        master.button_pending = Button(master, image=master.photoImg2, border=0, command=self.show_courier)
        master.button_pending.place(x=280, y=80)
        master.label_pending = Label(master, text='Pending', fg='brown', width=7, font=('bold', 15))
        master.label_pending.place(x=200, y=90)

        button_ok = Button(self.master, text='Ok', bg='LightSteelBlue4', fg='white', height=2, command=self.ok)
        button_ok.pack(fill=X, side=BOTTOM)

    def show_courier(self):
        show = Toplevel(self.master)
        show.title('Show[Courier Info]')
        window_width = 540
        window_height = 300
        screen_width = show.winfo_screenwidth()
        screen_height = show.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        show.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        show.resizable(0, 0)
        show.iconbitmap(r'pg.ico')
        new_obj = ShowCourier(show)
        show.transient(self.master)
        show.grab_set()
        show.wait_window(self.master)

    def ok(self):
        self.master.destroy()

    def new_reg(self):
        new = Toplevel(self.master)
        new.title('Add New[Courier Info]')
        window_width = 380
        window_height = 250
        screen_width = new.winfo_screenwidth()
        screen_height = new.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        new.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        new.resizable(0, 0)
        new.iconbitmap(r'pg.ico')
        new_obj = New(new)
        new.transient(self.master)
        new.grab_set()
        new.wait_window(self.master)


class ShowCourier:
    def __init__(self, master):
        self.master = master

        width = 40
        height = 40
        self.master.img = Image.open('delete.png')
        self.master.img = self.master.img.resize((width, height), Image.ANTIALIAS)
        self.master.photoImg = ImageTk.PhotoImage(self.master.img)
        but = Button(self.master, image=self.master.photoImg, border=0, command=self.dlte)
        but.place(x=450, y=15)

        lab_head = Label(master, text='Courier Information', font=('bold', 20))
        lab_head.place(x=150, y=15)

        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Complete Courier Info... ')
        labelsFrame.place(x=12, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='courier_info')
            mycursor = db.cursor()
            mycursor.execute('select * from courier_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[0], line[1], line[2], line[3]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2, 3, 4), height=6, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="E-Mail")
        tree.heading(3, text="Agency")
        tree.heading(4, text="Room No")

        tree.column(1, width=150)
        tree.column(2, width=180)
        tree.column(3, width=100)
        tree.column(4, width=70)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3]))

        master.button_ok = Button(master, text='Ok', bg='LightSteelBlue4', fg='white', width=30, height=2,
                                  command=self.ok)
        master.button_ok.pack(fill=X, side=BOTTOM)
        master.button_ok.focus()

    def dlte(self):
        dlte = Toplevel(self.master)
        dlte.title('Delete[Courier Info]')
        window_width = 300
        window_height = 150
        screen_width = dlte.winfo_screenwidth()
        screen_height = dlte.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        dlte.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        dlte.resizable(0, 0)
        dlte.iconbitmap(r'pg.ico')
        dlte_obj = Delete(dlte)
        dlte.transient(self.master)
        dlte.grab_set()
        dlte.wait_window(self.master)

    def ok(self):
        self.master.destroy()


class Delete:
    def __init__(self, master):
        self.master = master
        label_heading = Label(self.master, text='Re-Deliver Info', font=('bold', 15), width=20)
        label_heading.place(x=50, y=15)

        label_name = Label(self.master, text='Name', font=('bold', 15), width=10)
        label_name.place(x=5, y=55)

        OPTIONS4 = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='courier_info')
            mycursor = db.cursor()
            mycursor.execute('select * from courier_data ')
            rows = mycursor.fetchall()
            for line in rows:
                lst = [line[0]]
                OPTIONS4.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        master.var5 = StringVar(master)
        master.var5.set(OPTIONS4[0])

        master.opt_menu = OptionMenu(master, master.var5, *OPTIONS4, command=self.func)
        master.opt_menu.place(x=120, y=60)
        # name_selected = master.var5.get()

        master.button_dlte = Button(master, text='NEXT', bg='brown', fg='white', width=30, height=2,
                                      command=self.dlte)
        master.button_dlte.pack(fill=X, side=BOTTOM)
        master.button_dlte.focus()

    def func(self, value):
        global dlte_selected
        dlte_selected = value[0]

    def dlte(self):
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='courier_info')
            mycursor = db.cursor()
            mycursor.execute('delete from courier_data where name=(%s)', (dlte_selected, ))
            box.showinfo('Done', 'Successfully Delivered')
            self.master.destroy()
        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()


global name_got


class New:
    def __init__(self, master):
        self.master = master
        lab_he = Label(master, text='Add Courier Information', font=('bold', 20))
        lab_he.place(x=50, y=20)

        OPTIONS = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()
            for line in rows:
                lst = [line[1]]
                OPTIONS.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        master.var5 = StringVar(master)
        master.var5.set(OPTIONS[0])

        master.opt_menu = OptionMenu(master, master.var5, *OPTIONS, command=self.func)
        master.opt_menu.place(x=130, y=76)

        name_lab = Label(master, text='Name', font=('bold', 12))
        name_lab.place(x=60, y=80)

        master.width3 = 40
        master.height3 = 40
        master.img3 = Image.open('arrow.png')
        master.img3 = master.img3.resize((master.width3, master.height3), Image.ANTIALIAS)
        master.photoImg3 = ImageTk.PhotoImage(master.img3)
        master.button_new3 = Button(master, image=master.photoImg3, border=0, command=self.disp)
        master.button_new3.place(x=280, y=70)
        master.button_new3.focus()

        master.ent_lab = Label(master, text='Agency', font=('bold', 10))
        master.ent_lab.place(x=60, y=160)

        master.ent = Entry(master, width=30)
        master.ent.place(x=120, y=160)
        global note
        note = master.ent.get()

        button_update = Button(master, text='Update', bg='LightSteelBlue4', fg='white', height=2,
                               command=self.up_and_mail)
        button_update.pack(fill=X, side=BOTTOM)

    def up_and_mail(self):

        try:
            global name_got
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='courier_info')
            mycursor = db.cursor()
            mycursor.execute('insert into courier_data ( name, e_mail, Agency, room_no) VALUES ( %s, %s, %s, %s)',
                             (name_got, self.master.mail, self.master.ent.get(), self.master.room))
            box.showinfo('Done', 'Added Successfully')
            self.master.destroy()

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()
            #print(name_got, self.master.mail, note, self.master.room, 'hi', self.master.ent.get())
        """smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login('ramdhivakar333@gmail.com', '******password')
        smtp_obj.sendmail('ramdhivakar333@gmail.com', 'ramdhivakar333@gmail.com',
                          'Subject:Subject.\n Hi ,Sincerely,ram Courier test mail')
        smtp_obj.quit()"""

    def func(self, value):
        global name_got
        name_got = value[0]
        #print(name_got)

    def disp(self):
        try:
            global name_got
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select e_mail , r_no from member_data where mem_name like (%s)', (name_got, ))
            self.master.v = mycursor.fetchall()
            for rows in self.master.v:
                self.master.mail = rows[0]
                self.master.room = rows[1]

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()
            #print(self.master.mail, self.master.room)

        mail_lab = Label(self.master, text='E-Mail', font=('bold', 10))
        mail_lab.place(x=60, y=120)

        mail_entry = Entry(self.master)
        mail_entry.place(x=120, y=120)
        mail_entry.insert(0, self.master.mail)

        room_lab = Label(self.master, text='Room', font=('bold', 10))
        room_lab.place(x=260, y=120)

        room_entry = Entry(self.master, width=5)
        room_entry.place(x=300, y=120)
        room_entry.insert(0, self.master.room)


class Payment:
    def __init__(self, master):
        self.master = master

        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Basic Member Info... ')
        labelsFrame.place(x=20, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[1], line[3]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2), height=5, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="E- Mail")

        tree.column(1, width=150)
        tree.column(2, width=200)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1]))

        label_update_head1 = Label(master, text='Payment Information', font=('bold', 20))
        label_update_head1.place(x=180, y=15)
        button_update1 = Button(master, text='REFUND', bg='brown', fg='white', width=20, pady=5, underline=0,
                                command=self.refund)
        button_update1.place(x=450, y=80)
        button_update1.focus()
        button_clear1 = Button(master, text='Email', bg='brown', fg='white', width=20, pady=5, command=self.mail)
        button_clear1.place(x=450, y=140)
        button_cancel1 = Button(master, text='CANCEL', bg='brown', fg='white', width=20, pady=5, command=self.cancel)
        button_cancel1.place(x=450, y=200)

    def mail(self):
        content = 'Courier received in Pg \n by Ram'
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login('ramdhivakar333@gmail.com', '******password')
        smtp_obj.sendmail('ramdhivakar333@gmail.com', 'ramdhivakar333@gmail.com', content)
        smtp_obj.quit()
        box.showinfo('Done', 'Mail sent Successfully')

    def cancel(self):
        self.master.destroy()

    def refund(self):
        refund = Toplevel(self.master)
        window_height = 200
        window_width = 380
        screen_width = refund.winfo_screenwidth()
        screen_height = refund.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        refund.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        refund.title('PG[Confirmation]')
        refund.iconbitmap(r'pg.ico')
        conf = Confirmation(refund)
        refund.transient(self.master)
        refund.grab_set()
        refund.wait_window(self.master)


global nms


class Confirmation:
    def __init__(self, master):
        self.master = master
        global name_selected
        global aadhaar_db
        global name_fetched
        master.label_head = Label(master, text='Verification', fg='Black', font=('bold', 22))
        master.label_head.place(x=125, y=10)
        OPTIONS4 = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()
            for line in rows:
                lst = [line[1]]
                OPTIONS4.append(lst)
        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        master.var5 = StringVar(master)
        master.var5.set(OPTIONS4[0])

        master.opt_menu = OptionMenu(master, master.var5, *OPTIONS4, command=self.func)
        master.opt_menu.place(x=40, y=80)

        labframe = ttk.LabelFrame(master, text=' Aadhar Number... ')
        labframe.place(x=160, y=72)

        master.ent = Entry(labframe)
        master.ent.pack()

        master.button_check = Button(master, text='Delete Candidate', bg='brown', fg='white', width=15, height=2,
                                     command=self.show_alert)
        master.button_check.pack(fill=X, side=BOTTOM)
        master.button_check.focus()

    def func(self, value):
        global nms
        nms = value

    def show_alert(self):
        self.master.aadhaar_entered = self.master.ent.get()
        global nms
        self.master.name_sel = nms[0]
        #print(self.master.name_sel)
        #self.master.name_fetched = self.master.name_selected
        #print('Aadhaar Entered', self.master.aadhaar_entered, 'Name Selected', self.master.name_selected)
        self.master.ms = box.askyesno('Confirmation[Removal]', 'Are you sure you want to remove the Candidate?')

        if self.master.ms > 0:
            try:
                db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                             database='member_info')
                mycursor = db.cursor()
                mycursor.execute("select aadhaar_no from member_data where mem_name like (%s)",
                                 (self.master.name_sel, ))
                self.master.aadhaar = mycursor.fetchone()
                #print(self.master.aadhaar)
                self.master.aadhaar_db = self.master.aadhaar[0]
                #print(self.master.aadhaar_db)
            except Exception as e:
                print(e)
                print('Exception')

            finally:
                mycursor.close()
                db.commit()
                db.close()

            if self.master.aadhaar_db == self.master.aadhaar_entered:
                #print(self.master.aadhaar_entered, self.master.aadhaar_db)
                try:
                    db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                                 database='member_info')
                    mycursor = db.cursor()
                    mycursor.execute("delete from member_data where mem_name like (%s)", (self.master.name_sel, ))
                    self.master.destroy()
                    box.showinfo('Done', 'Successfully Removed')

                except Exception as e:
                    print(e)
                finally:
                    mycursor.close()
                    db.commit()
                    db.close()
            else:
                print(self.master.aadhaar_entered, self.master.aadhaar_db)
                box.showerror('Terminated', 'Aadhaar Mismatch!!')


class MemberInformation:
    def __init__(self, master):
        self.master = master
        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Basic Member Info... ')
        labelsFrame.place(x=20, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[1], line[6], line[8], line[9], line[10]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2, 3, 4, 5), height=5, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="Profession")
        tree.heading(3, text="Mobile No")
        tree.heading(4, text="Room Type")
        tree.heading(5, text="Room No")

        tree.column(1, width=130)
        tree.column(2, width=100)
        tree.column(3, width=100)
        tree.column(4, width=100)
        tree.column(5, width=100)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4]))

        label_update_head = Label(master, text='Member Information', font=('bold', 20))
        label_update_head.place(x=300, y=15)
        button_update = Button(master, text='UPDATE', bg='brown', fg='white', width=20, pady=5, underline=0
                               , command=self.update_data)
        button_update.place(x=610, y=80)
        button_update.focus()
        button_text = Button(master, text='View All', bg='brown', fg='white', width=20, pady=5, command=self.viewall)
        button_text.place(x=610, y=140)
        button_cancel = Button(master, text='CANCEL', bg='brown', fg='white', width=20, pady=5, command=self.cancel)
        button_cancel.place(x=610, y=200)

    def update_data(self):
        upall = Toplevel(self.master)
        upall.title('PG[Select Name]')
        upall.resizable(0, 0)
        window_height = 160
        window_width = 300
        screen_width = upall.winfo_screenwidth()
        screen_height = upall.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        upall.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        upall.iconbitmap(r'pg.ico')
        update_all = UpdateAll(upall)
        upall.transient(self.master)
        upall.grab_set()
        upall.wait_window(self.master)

    def viewall(self):
        viewall = Toplevel(self.master)
        viewall.title('PG[Complete-Member Information]')
        viewall.resizable(0, 0)
        window_height = 320
        window_width = 1150
        screen_width = viewall.winfo_screenwidth()
        screen_height = viewall.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        viewall.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        viewall.iconbitmap(r'pg.ico')
        view_all = ViewAll(viewall)
        viewall.transient(self.master)
        viewall.grab_set()
        viewall.wait_window(self.master)

    def cancel(self):
        self.master.destroy()


class ViewAll:
    def __init__(self, master):
        self.master = master

        lab_head = Label(master, text='Members Information', font=('bold', 20))
        lab_head.place(x=450, y=15)

        data = []

        labelsFrame = ttk.LabelFrame(master, text=' Complete Member Info... ')
        labelsFrame.place(x=12, y=70)
        master.data = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()

            for line in rows:
                lst = [line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                       line[10], line[11]]
                data.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        tree = ttk.Treeview(labelsFrame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height=6, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Name")
        tree.heading(2, text="State")
        tree.heading(3, text="E-Mail")
        tree.heading(4, text="Amount")
        tree.heading(5, text="Address")
        tree.heading(6, text="Profession")
        tree.heading(7, text="Aadhaar Number")
        tree.heading(8, text="Mobile Number")
        tree.heading(9, text="Room Type")
        tree.heading(10, text="Room No")
        tree.heading(11, text="Key No")

        tree.column(1, width=150)
        tree.column(2, width=90)
        tree.column(3, width=150)
        tree.column(4, width=60)
        tree.column(5, width=100)
        tree.column(6, width=100)
        tree.column(7, width=130)
        tree.column(8, width=100)
        tree.column(9, width=80)
        tree.column(10, width=70)
        tree.column(11, width=70)

        scroll = ttk.Scrollbar(labelsFrame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8],
                                           val[9], val[10]))
        master.button_ok = Button(master, text='Ok', bg='LightSteelBlue4', fg='white', width=30, height=3, command=self.ok)
        master.button_ok.pack(fill=X, side=BOTTOM)
        master.button_ok.focus()

    def ok(self):
        self.master.destroy()


global name_selected


class UpdateAll:

    def __init__(self, master):

        self.master = master
        master.label_head = Label(master, text='Select Name', fg='Black', font=('bold', 18))
        master.label_head.place(x=80, y=10)
        OPTIONS4 = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('select * from member_data ')
            rows = mycursor.fetchall()
            for line in rows:
                lst = [line[1]]
                OPTIONS4.append(lst)

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        master.var5 = StringVar(master)
        master.var5.set(OPTIONS4[0])

        master.opt_menu = OptionMenu(master, master.var5, *OPTIONS4, command=self.func)
        master.opt_menu.place(x=50, y=60)
        #name_selected = master.var5.get()

        master.button_logout = Button(master, text='NEXT', bg='brown', fg='white', width=30, height=2,
                                      command=self.next)
        master.button_logout.pack(fill=X, side=BOTTOM)
        master.button_logout.focus()

    def func(self, value):
        global name_selected
        name_selected = value

    def next(self):
        nxt = Toplevel(self.master)
        nxt.title('PG[Update-Member Information]')
        nxt.resizable(0, 0)
        window_height = 580
        window_width = 1000
        screen_width = nxt.winfo_screenwidth()
        screen_height = nxt.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        nxt.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        nxt.iconbitmap(r'pg.ico')
        nxt_page = NextUpdate(nxt)
        nxt.transient(self.master)
        nxt.grab_set()
        nxt.wait_window(self.master)


global r_n
global r_v


class NextUpdate:
    def __init__(self, master):
        self.master = master
        global name_selected
        self.master.up_name = name_selected[0]
        master.nme = StringVar()
        master.ste = StringVar()
        master.mail = StringVar()
        master.amt = StringVar()
        master.adr = StringVar()
        master.prof = StringVar()
        master.aadhar = StringVar()
        master.mbl = StringVar()
        master.key_no = StringVar()
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute("select * from member_data where mem_name like (%s)", (self.master.up_name, ))
            rows = mycursor.fetchall()
            for data in rows:
                master.nme = data[1]
                master.ste = data[2]
                master.mail = data[3]
                master.amt = data[4]
                master.adr = data[5]
                master.prof = data[6]
                master.aadhar = data[7]
                master.mbl = data[8]
                master.key_no = data[11]

        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

        label_reg_heading = Label(master, text='Update Member Details', font=('bold', 30), width=20)
        label_reg_heading.place(x=250, y=40)
        label_name = Label(master, text='Name', font=('bold', 15), width=20)
        label_name.place(x=80, y=120)
        label_state = Label(master, text='State', font=('bold', 15), width=20)
        label_state.place(x=80, y=170)
        label_email = Label(master, text='e-Mail', font=('bold', 15), width=20)
        label_email.place(x=80, y=220)
        label_amount = Label(master, text='Amount', font=('bold', 15), width=20)
        label_amount.place(x=80, y=270)
        label_address = Label(master, text='Address', font=('bold', 15), width=20)
        label_address.place(x=80, y=320)
        label_profession = Label(master, text='Profession', font=('bold', 15), width=20)
        label_profession.place(x=80, y=370)
        label_aadhaar = Label(master, text='Aadhaar No.', font=('bold', 15), width=20)
        label_aadhaar.place(x=80, y=420)
        label_mobile = Label(master, text='Mobile Number', font=('bold', 15), width=20)
        label_mobile.place(x=80, y=470)
        master.OPTIONS2 = [
            "Single",
            "2-Sharing",
            "3-Sharing",
            "4-Sharing",
            "Guest",
            "Select Room"
        ]
        self.master.var = StringVar(master)
        self.master.var.set(master.OPTIONS2[5])

        master.opt_menu = OptionMenu(master, self.master.var, *master.OPTIONS2, command=self.changed)
        master.opt_menu.place(x=824, y=120)

        label_room_v = Label(master, text='Room Varient', font=('bold', 15), width=20)
        label_room_v.place(x=577, y=120)
        label_alert = Label(master, text='*', font=('bold', 15), fg='red')
        label_alert.place(x=750, y=120)
        label_room = Label(master, text='Room Number', font=('bold', 15), width=20)
        label_room.place(x=580, y=170)
        label_alert = Label(master, text='*', font=('bold', 15), fg='red')
        label_alert.place(x=750, y=170)
        label_key = Label(master, text='Key Number', font=('bold', 15), width=20)
        label_key.place(x=577, y=220)

        master.n = StringVar()
        master.entry_name = Entry(master, textvariable=master.n)
        master.entry_name.place(x=290, y=120)
        master.entry_name.focus()
        master.entry_name.insert(0, master.nme)
        master.s = StringVar()
        master.entry_state = Entry(master, textvariable=master.s)
        master.entry_state.place(x=290, y=170)
        master.entry_state.insert(0, master.ste)
        master.e = StringVar()
        master.entry_email = Entry(master, textvariable=master.e)
        master.entry_email.place(x=290, y=220)
        master.entry_email.insert(0, master.mail)
        master.a = StringVar()
        master.entry_amount = Entry(master, textvariable=master.a)
        master.entry_amount.place(x=290, y=270)
        master.entry_amount.insert(0, master.amt)
        master.ad = StringVar()
        master.entry_address = Entry(master, textvariable=master.ad)
        master.entry_address.place(x=290, y=330)
        master.entry_address.insert(0, master.adr)
        master.p = StringVar()
        master.entry_profession = Entry(master, textvariable=master.p)
        master.entry_profession.place(x=290, y=370)
        master.entry_profession.insert(0, master.prof)
        master.ar = StringVar()
        master.entry_aadhaar = Entry(master, textvariable=master.ar)
        master.entry_aadhaar.place(x=290, y=420)
        master.entry_aadhaar.insert(0, master.aadhar)
        master.m = StringVar()
        master.entry_mobile = Entry(master, textvariable=master.m)
        master.entry_mobile.place(x=290, y=470)
        master.entry_mobile.insert(0, master.mbl)

        master.k = StringVar()
        master.entry_key = Entry(master, textvariable=master.k)
        master.entry_key.place(x=800, y=220)
        master.entry_key.insert(0, master.key_no)

        button_signup = Button(master, text='UPDATE', bg='LightSteelBlue4', fg='white', width=30, height=3,
                               command=self.update_fn)
        button_signup.pack(fill=X, side=BOTTOM)

        menubar = Menu(master)
        menubar.add_command(label='<--', font='bold', command=self.close_panel)
        master.config(menu=menubar)

    def changed(self, value, *args):
        global r_v
        r_v = value

        self.master.r_varient1 = self.master.OPTIONS2.index(self.master.var.get())

        OPTIONS3 = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='room_info')
            mycursor = db.cursor()

            #self.master.r_varient1 = self.master.OPTIONS2.index(self.master.var.get())
            # master.var.set(OPTIONS2[self.master.r_varient])

            if self.master.r_varient1 == 0:
                mycursor.execute("select room_no from one_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 1:
                mycursor.execute("select room_no from two_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 2:
                mycursor.execute("select room_no from three_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 3:
                mycursor.execute("select room_no from four_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            else:
                mycursor.execute("select room_no from guest")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
        except Exception as e:
            print(e)
        finally:
            db.commit()
            mycursor.close()
            db.close()

        self.master.var3 = StringVar(self.master)
        self.master.opt_menu3 = OptionMenu(self.master, self.master.var3, *OPTIONS3, command=self.func)
        self.master.opt_menu3.place(x=824, y=170)

    def func(self, value):
        global r_n
        r_n = value

    def update_fn(self):
        if self.master.var.get() == 'Select Room' or self.master.var3.get() == 'NIL':
            box.showerror('Error', 'Fill all Details')
        elif self.master.var.get() != 'Select Room' or self.master.var3.get() != 'NIL':
            self.master.nm = self.master.entry_name.get()
            self.master.st = self.master.entry_state.get()
            self.master.ma = self.master.entry_email.get()
            self.master.am = self.master.entry_amount.get()
            self.master.ada = self.master.entry_address.get()
            self.master.pr = self.master.entry_profession.get()
            self.master.aa = self.master.entry_aadhaar.get()
            self.master.mb = self.master.entry_mobile.get()
            self.master.ke = self.master.entry_key.get()
            try:
                db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                             database='member_info')
                mycursor = db.cursor()
                global r_n
                global r_v
                mycursor.execute("update member_data set "
                                 "mem_name=(%s),state=(%s),e_mail=(%s),"
                                 "amount=(%s),addr=(%s),profession=(%s),"
                                 "aadhaar_no=(%s),mobile_no=(%s),r_varient=(%s),"
                                 "r_no=(%s),key_num=(%s) where mem_name =(%s)",
                                 (self.master.nm, self.master.st, self.master.ma, self.master.am,
                                  self.master.ada, self.master.pr, self.master.aa, self.master.mb,
                                  r_v, r_n, self.master.ke, self.master.up_name))
            except Exception as e:
                print(e)

            finally:
                mycursor.close()
                db.commit()
                db.close()
            self.master.destroy()
            box.showinfo('Ok', 'Details Updated')
        else:
            print('Fine')

    def close_panel(self):
        self.master.destroy()


class Availability:
    def __init__(self, master):
        self.master = master
        master.label_head = Label(master, text='Check Availability', fg='Black', font=('bold', 22))
        master.label_head.place(x=85, y=10)

        master.label_sub = Label(master, text='Available Rooms', fg='Black', font=('bold', 18))
        master.label_sub.place(x=25, y=80)

        OPTIONS = [
            "Single",
            "1-Sharing",
            "2-Sharing",
            "3-Sharing",
            "4-Sharing",
            "Guest",
            "ALL"
        ]
        master.var = StringVar(master)
        master.var.set(OPTIONS[6])

        master.opt_menu = OptionMenu(master, master.var, *OPTIONS)
        master.opt_menu.place(x=265, y=80)

        master.button_check = Button(master, text='Check', bg='brown', fg='white', width=15, height=2, command=self.show_room)
        master.button_check.pack(fill=X, side=BOTTOM)

    def show_room(self):
        show = Toplevel(self.master)
        window_height = 200
        window_width = 380
        screen_width = show.winfo_screenwidth()
        screen_height = show.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        show.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        show.title('PG[Room Info]')
        show.iconbitmap(r'pg.ico')
        showing = Showing(show)
        show.transient(self.master)
        show.grab_set()
        show.wait_window(self.master)


class Showing:
    def __init__(self, master):
        self.master = master
        master.value_x = 50
        master.value_y = 50
        master.value_x1 = 53
        master.value_y1 = 80
        master.value_y2 = 110
        master.r = 5
        for val in range(0, master.r):
            master.bk = Button(master, text=val, bg='brown', fg='white', padx=18)
            master.bk.place(x=master.value_x, y=master.value_y)
            master.lk = Label(master, text='|', padx=18)
            master.lk.place(x=master.value_x1, y=master.value_y1)
            master.lk = Label(master, text=val, padx=18, bg='black', fg='white')
            master.lk.place(x=master.value_x, y=master.value_y2)
            master.value_x += 60
            master.value_x1 += 60


class Configuration:
    def __init__(self, master):
        self.master = master
        #self.pd = pd
        master.label_h = Label(master, text='Password Configuration', fg='Black', font=('bold', 15))
        master.label_h.place(x=70, y=10)
        master.old = Label(master, text='Old Password', font=('bold', 13))
        master.old.place(x=40, y=50)
        master.old_entry = ttk.Entry(master)
        master.old_entry.place(x=195, y=50)
        master.old_entry.focus()
        master.new = Label(master, text='New Password', font=('bold', 13))
        master.new.place(x=40, y=80)
        master.new_entry = ttk.Entry(master)
        master.new_entry.place(x=195, y=80)
        master.newre = Label(master, text='Re-New Password', font=('bold', 13))
        master.newre.place(x=40, y=110)
        master.new_reentry = ttk.Entry(master)
        master.new_reentry.place(x=195, y=110)
        master.but = Button(master, text='UPDATE', bg='LightSteelBlue4', fg='white', width=30, height=2, command=self.update)
        master.but.pack(fill=X, side=BOTTOM)

    def update(self):
        old = self.master.old_entry.get()
        new = self.master.new_entry.get()
        new_enter = self.master.new_reentry.get()
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='admin_info')
            mycursor = db.cursor()
            mycursor.execute('select * from admin_data ')
            ps = mycursor.fetchall()
            for line in ps:
                if old == line[2]:
                    if new == new_enter:
                        mycursor.execute('update admin_data set passwod = %s where id = %s', (new, 1))
                        db.commit()
                        db.close()
                        self.master.destroy()
                    else:
                        box.showerror('Invalid', 'Mismatch')

        except Exception as e:
            print(e)

        finally:
            mycursor.close()


class Registration:

    def __init__(self, master):
        self.master = master
        global r_varient1
        global date
        date = date.today()
        #print(date)
        label_reg_heading = Label(master, text='New Member Registration', font=('bold', 30), width=20)
        label_reg_heading.place(x=250, y=40)
        label_name = Label(master, text='Name', font=('bold', 15), width=20)
        label_name.place(x=80, y=120)
        label_state = Label(master, text='State', font=('bold', 15), width=20)
        label_state.place(x=80, y=170)
        label_email = Label(master, text='e-Mail', font=('bold', 15), width=20)
        label_email.place(x=80, y=220)
        label_amount = Label(master, text='Amount', font=('bold', 15), width=20)
        label_amount.place(x=80, y=270)
        label_address = Label(master, text='Address', font=('bold', 15), width=20)
        label_address.place(x=80, y=320)
        label_profession = Label(master, text='Profession', font=('bold', 15), width=20)
        label_profession.place(x=80, y=370)
        label_aadhaar = Label(master, text='Aadhaar No.', font=('bold', 15), width=20)
        label_aadhaar.place(x=80, y=420)
        label_mobile = Label(master, text='Mobile Number', font=('bold', 15), width=20)
        label_mobile.place(x=80, y=470)
        master.OPTIONS2 = [
            "Single",
            "2-Sharing",
            "3-Sharing",
            "4-Sharing",
            "Guest",
        ]

        master.var = StringVar(master)
        master.var.set(master.OPTIONS2[0])
        master.opt_menu = OptionMenu(master, master.var, *master.OPTIONS2, command=self.changed)
        master.opt_menu.place(x=824, y=120)

        label_room_v = Label(master, text='Room Varient', font=('bold', 15), width=20)
        label_room_v.place(x=577, y=120)
        label_room = Label(master, text='Room Number', font=('bold', 15), width=20)
        label_room.place(x=580, y=170)
        label_key = Label(master, text='Key Number', font=('bold', 15), width=20)
        label_key.place(x=577, y=220)
        label_date = Label(master, text='Date-Joining', font=('bold', 15), width=20)
        label_date.place(x=580, y=270)
        master.entry_name = Entry(master)
        master.entry_name.place(x=290, y=120)
        master.entry_name.focus()
        master.entry_state = Entry(master)
        master.entry_state.place(x=290, y=170)
        master.entry_email = Entry(master)
        master.entry_email.place(x=290, y=220)
        master.entry_amount = Entry(master)
        master.entry_amount.place(x=290, y=270)
        master.entry_address = Entry(master)
        master.entry_address.place(x=290, y=330)
        master.entry_profession = Entry(master)
        master.entry_profession.place(x=290, y=370)
        master.entry_aadhaar = Entry(master)
        master.entry_aadhaar.place(x=290, y=420)
        master.entry_mobile = Entry(master)
        master.entry_mobile.place(x=290, y=470)

        master.entry_key = Entry(master)
        master.entry_key.place(x=800, y=220)
        master.entry_date = Entry(master)
        master.entry_date.place(x=800, y=280)
        master.entry_date.insert(0, date)

        button_signup = Button(master, text='REGISTER', bg='LightSteelBlue4', fg='white', width=30, height=3,
                               command=self.connect_db)
        button_signup.pack(fill=X, side=BOTTOM)

        menubar = Menu(master)
        menubar.add_command(label='<--', font='bold', command=self.close_panel)
        master.config(menu=menubar)

    def close_panel(self):
        self.master.destroy()

    def changed(self, *args):
        self.master.r_varient1 = self.master.OPTIONS2.index(self.master.var.get())

        OPTIONS3 = []
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='room_info')
            mycursor = db.cursor()

            #self.master.r_varient1 = self.master.OPTIONS2.index(self.master.var.get())
            # master.var.set(OPTIONS2[self.master.r_varient])

            if self.master.r_varient1 == 0:
                mycursor.execute("select room_no from one_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 1:
                mycursor.execute("select room_no from two_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 2:
                mycursor.execute("select room_no from three_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            elif self.master.r_varient1 == 3:
                mycursor.execute("select room_no from four_num")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
            else:
                mycursor.execute("select room_no from guest")
                data = mycursor.fetchall()
                for rows in data:
                    OPTIONS3.append(rows[0])
        except Exception as e:
            print(e)
        finally:
            db.commit()
            mycursor.close()
            db.close()

        self.master.var3 = StringVar(self.master)
        self.master.opt_menu3 = OptionMenu(self.master, self.master.var3, *OPTIONS3)
        self.master.opt_menu3.place(x=824, y=170)

    def connect_db(self):
        mem_name = self.master.entry_name.get()
        state = self.master.entry_state.get()
        e_mail = self.master.entry_email.get()
        amount = self.master.entry_amount.get()
        addr = self.master.entry_address.get()
        profession = self.master.entry_profession.get()
        aadhaar_no = self.master.entry_aadhaar.get()
        mobile_no = self.master.entry_mobile.get()
        r_varient = self.master.var.get()
        r_no = self.master.var3.get()
        key_num = self.master.entry_key.get()
        j_date = self.master.entry_date.get()
        try:
            db = mysql.connector.connect(host='localhost', port='3535', user='root', passwd='root',
                                         database='member_info')
            mycursor = db.cursor()
            mycursor.execute('INSERT INTO member_data ( mem_name, state, e_mail, amount,'
                             ' addr, profession, aadhaar_no, mobile_no, r_varient, r_no, key_num, joining_date) '
                             'VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                             (mem_name, state, e_mail, amount, addr, profession,
                              aadhaar_no, mobile_no, r_varient, r_no, key_num, j_date))
            box.showinfo('Done', 'Added Successfully')
            self.master.entry_name.delete(0, 'end')
            self.master.entry_state.delete(0, 'end')
            self.master.entry_email.delete(0, 'end')
            self.master.entry_amount.delete(0, 'end')
            self.master.entry_address.delete(0, 'end')
            self.master.entry_profession.delete(0, 'end')
            self.master.entry_aadhaar.delete(0, 'end')
            self.master.entry_mobile.delete(0, 'end')
            self.master.entry_key.delete(0, 'end')
            self.master.entry_name.focus()
        except Exception as e:
            print(e)

        finally:
            mycursor.close()
            db.commit()
            db.close()

    def back(self, master):
        self.master = master
        self.master.destroy()


def main():
    root = Tk()
    #root.state('zoomed')
    root.resizable(0, 0)
    window_height = 500
    window_width = 980
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    root.title('Admin Login')
    root.iconbitmap(r'pg.ico')
    mainpanel = MainPanel(root)
    root.mainloop()


if __name__ == '__main__':
    main()
