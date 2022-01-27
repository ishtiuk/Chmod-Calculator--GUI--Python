from tkinter import *

root = Tk()

root.config(bg='black')
root.title('|Chmod Calculator|')

software_name = Label(text="ᴄʜᴍᴏᴅ ᴄᴀʟᴄᴜʟᴀᴛᴏʀ", font=("calibri", 23), bg='#1b1a1a', fg='#3b86d1', bd=10).place(x=220, y=1)
rights = Label(root, text="Copyright © 2021. All rights reserved by Md. Ishtiuk Ahammed.", font=('calibri', 8), bg='black', fg='#c6c2c2').place(x=350, y=700)

owner = Label(text="Owner", font=("calibri", 21), bg='black', fg='#2bff4a')
group = Label(text="Group", font=("calibri", 21), bg='black', fg='cyan')
public = Label(text="Public", font=("calibri", 21), bg='black', fg='#ffe934')


disp = Label(text="ʟɪɴᴜx ᴘᴇʀᴍɪꜱꜱɪᴏɴ:", font=("calibri", 16), bg='grey17', fg='#2bff4a', bd=10, width=16)
output = Label(font=("calibri", 16), bg='#d5d4d4', fg='grey17', bd=10, width=8)
output_perm = Label(font=("calibri", 16), bg='#d5d4d4', fg='grey17', bd=10, width=15)
linuX_permission_num = Label(text='ᴘᴇʀᴍɪꜱꜱɪᴏɴ ɴᴜᴍʙᴇʀ :>', font=("calibri", 16), bg='#262424', fg='#2bff4a', width=22)
permsission_num_input = Entry(font=("calibri", 16), bg='#565454', fg='#2bff4a')
helping_warning = Label(text="⚠ the number must contain 3 digits only❏", fg='#ff3939', bg='black')
permsission_num_output = Label(font=("Arial", 13), bg='#201f1f', width=62)

owr = IntVar()
oww = IntVar()
owx = IntVar()

gwr = IntVar()
gww = IntVar()
gwx = IntVar()

pur = IntVar()
puw = IntVar()
pux = IntVar()

owner_read_box = Checkbutton(text="Read", font=("calibri", 13), bg='#717270', fg='#2bff4a', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=owr)
owner_write_box = Checkbutton(text="Write", font=("calibri", 13), bg='#717270', fg='#2bff4a', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=oww)
owner_exe_box = Checkbutton(text="Execute", font=("calibri", 13), bg='#717270', fg='#2bff4a', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=owx)

group_read_box = Checkbutton(text="Read", font=("calibri", 13), bg='#717270', fg='cyan', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=gwr)
group_write_box = Checkbutton(text="Write", font=("calibri", 13), bg='#717270', fg='cyan', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=gww)
group_exe_box = Checkbutton(text="Execute", font=("calibri", 13), bg='#717270', fg='cyan', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=gwx)

public_read_box = Checkbutton(text="Read", font=("calibri", 13), bg='#717270', fg='#ffe934', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=pur)
public_write_box = Checkbutton(text="Write", font=("calibri", 13), bg='#717270', fg='#ffe934', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=puw)
public_exe_box = Checkbutton(text="Execute", font=("calibri", 13), bg='#717270', fg='#ffe934', activeforeground='red', activebackground='darkgreen', selectcolor='#1e1d1d', variable=pux)


class Chmod_Calculator:
    def __init__(self) -> None:
        self.__Developer = "Ishtiuk Ahammed"

    def number_to_linux_permission(self, number):
        self.number_lst = [int(i) for i in str(number)]     # list comprehension 😎
        self.rules = ((4, 'r'), (2, 'w'), (1, 'x'))
        self.permisssion_result = ''

        for num in self.number_lst:
            for value, access_m in self.rules:
                if num >= value:
                    self.permisssion_result += access_m
                    num -= value
                else:
                    self.permisssion_result += '-'
        return self.permisssion_result

    def getting_permissions(self):
        self.diction_tuple = ({'4': owr.get(), 'prm': 'r'}, {'2': oww.get(), 'prm': 'w'}, {'1': owx.get(), 'prm': 'x'},
                        {4: gwr.get(), 'prm': 'r'}, {2: gww.get(), 'prm': 'w'}, {1: gwx.get(), 'prm': 'x'},
                        {4.1: pur.get(), 'prm': 'r'}, {2.1: puw.get(), 'prm': 'w'}, {1.1: pux.get(), 'prm': 'x'})
        self.result = [0, 0, 0]
        self.access_mode = ''
        self.final_linux_perm = ''

        for itm in self.diction_tuple:
            for key, value in itm.items():
                if self.diction_tuple.index(itm) <= 2 and value == 1:
                    self.result[0] += int(key)
                    self.access_mode += itm['prm']
                elif self.diction_tuple.index(itm) > 2 and self.diction_tuple.index(itm) <= 5 and value == 1:
                    self.result[1] += key
                    self.access_mode += itm['prm']
                elif self.diction_tuple.index(itm) > 5 and self.diction_tuple.index(itm) <= 8 and value == 1:
                    self.result[2] += int(key)
                    self.access_mode += itm['prm']
            else:
                self.access_mode += '-' 


        self.rules = ((4, 'r'), (2, 'w'), (1, 'x'))
        self.permisssion_result_str = ''

        for num in self.result:
            for value, access_m in self.rules:
                if num >= value:
                    self.permisssion_result_str += access_m
                    num -= value
                else:
                    self.permisssion_result_str += '-'
        
        self.final_linux_perm = ''.join(list(map(str, self.result)))
        return self.final_linux_perm, self.permisssion_result_str


obj = Chmod_Calculator()

def clear_out():
    output.config(text='')
    output_perm.config(text='')

clear_button = Button(text="ᴄʟᴇᴀʀ", font=("Arial", 14), bg='#ff2626', fg='white', activebackground='yellow', bd=3, width=6, command=clear_out)

def out_put_fucntion():
    tup = obj.getting_permissions()

    disp.place(x=50, y=330)
    output.config(text=tup[0])
    output_perm.config(text=tup[1])
    output.place(x=275, y=329)
    output_perm.place(x=412, y=329)
    clear_button.place(x=526, y=395)

Calculate_button = Button(text="Calculate", bd=7, width=15, font=("calibri", 18), bg='#2bff4a', fg='gray17', activeforeground='red', activebackground='darkgreen', command=out_put_fucntion).place(x=222, y=255)

def permission_number():
    number = str(permsission_num_input.get()).strip()
    if number.isnumeric() and len(number) == 3 and int(number) <= 777:
        outp = f"\nPermission:      {obj.number_to_linux_permission(number)}\n"
        permsission_num_output.config(text=outp, fg='#2bff4a')
    elif number.isalpha():
        outp = f'''⚠Error!
 ________________________
| 🛈 the number must be Digits |
-------------------------------------'''
        permsission_num_output.config(text=outp, fg='#ff3939')
    elif len(number) > 3:
        outp = f'''⚠Error!
 __________________________________
| 🛈 the number must contain 3 digits only  |
---------------------------------------------------'''
        permsission_num_output.config(text=outp, fg='#ff3939')
    else:
        outp = f'''⚠Error!
____________________________________________________
|               🛈 the number must contain 3 digits & all must be       |
|   numerical & lesser than |778|.  (Like: 001, 777, 101 or 203)  |
------------------------------------------------------------------------------'''
        permsission_num_output.config(text=outp, fg='#ff3939')


Ok_button = Button(text="ᴏᴋ", font=("Arial", 14), bg='#ffe934', fg='brown', activebackground='green', bd=4, width=5, command=permission_number)

linuX_permission_num.place(x=50, y=468)
helping_warning.place(x=50, y=503)
permsission_num_input.place(x=305, y=469)
permsission_num_output.place(x=41, y=537)
Ok_button.place(x=537, y=466)

exit_button = Button(text='EXIT', font=('Calibri', 13), bg='#ff2626', fg='white', bd=3, width=7, command=root.destroy).place(x=531, y=645)
owner.place(x=50, y=70)
owner_read_box.place(x=52, y=120)
owner_write_box.place(x=52, y=160)
owner_exe_box.place(x=52, y=200)

group.place(x=280, y=70)
group_read_box.place(x=280, y=120)
group_write_box.place(x=280, y=160)
group_exe_box.place(x=280, y=200)

public.place(x=510, y=70)
public_read_box.place(x=510, y=120)
public_write_box.place(x=510, y=160)
public_exe_box.place(x=510, y=200)



root.geometry("650x720")
root.mainloop()







































