from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg='black')
root.resizable(False, False)
      
def signup():
    
    username= user.get()
    password= code.get()
    password_conf = code2.get()
    
    while True:
        if password_conf == password:
            if password  and username:
            
                try:
                    file= open('datasheet.txt', 'r+')
                    d=file.read()
                    r = ast.literal_eval(d)
                    dict2={username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()
                        
                    file =open ('datasheet.txt', 'w')
                    w=file.write(str(r))
                    messagebox.showinfo('Sucessfully','usúario criado com sucesso')
                    window.destroy()
                    break
                except:
                    file= open('datasheet.txt', 'r+')
                    pp=str({'username': 'password'})
                    file.write(pp)
                    file.close()
                    break
            else:
                messagebox.showerror('Invalido', 'Invalido')
                break
    
        elif password_conf != password:
            messagebox.showerror('Erro na senha', 'As senhas não confere')
            break
    
        

#-------------------------------------------------------------------

img = PhotoImage(file='imgs/login.png')
Label(root, image=img,bg='black').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading= Label(frame,text='Cadastro de usúario', fg='#57a1f8', bg ='white',
               font=('Microsoft Yahi UI Light',23,'bold'))
heading.place(x=25,y=5)
#-------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e): 
    name = user.get()
    if name == '':
        user.insert(0, 'Nome de usúario')
             
user = Entry(frame,width=25, fg='black', border=0,bg='white',font=('Microsoft Yahi UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Nome de usúario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,heigh=1,bg='black').place(x=25,y=107)
#-------------------------------------------------------------------

def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e): 
    name = code.get()
    if name == '':
        code.insert(0, 'Senha')
        
code = Entry(frame,width=25, fg='black', border=0,bg='white',font=('Microsoft Yahi UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Senha')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

#-------------------------------------------------------------------
def on_enter(e):
    code2.delete(0, 'end')
    
def on_leave(e): 
    name = code2.get()
    if name == '':
        code2.insert(0, 'Confirmar senha')
        
code2 = Entry(frame,width=25, fg='black', border=0,bg='white',font=('Microsoft Yahi UI Light',11))
code2.place(x=30,y=215)
code2.insert(0,'Confirmar senha')
code2.bind('<FocusIn>', on_enter)
code2.bind('<FocusOut>', on_leave)
#-------------------------------------------------------------------
Frame(frame,width=295,heigh=1,bg='black').place(x=25,y=177)
Frame(frame,width=295,heigh=1,bg='black').place(x=25,y=245)
Button(frame,width=39, pady=7, text='Cadastrar',bg='green', fg='white', border=0,command=signup).place(x=35,y=260, )

root.mainloop()

