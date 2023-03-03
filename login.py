
# Rafael Guedes
# 3/2/2023
# Github https://github.com/guedes2142

'''
 _____ ______   ________     ___    ___ _________  _______   ________  _____ ______      
|\   _ \  _   \|\   __  \   |\  \  /  /|\___   ___|\  ___ \ |\   __  \|\   _ \  _   \    
\ \  \\\__\ \  \ \  \|\  \  \ \  \/  / \|___ \  \_\ \   __/|\ \  \|\  \ \  \\\__\ \  \   
 \ \  \\|__| \  \ \   __  \  \ \    / /     \ \  \ \ \  \_|/_\ \   __  \ \  \\|__| \  \  
  \ \  \    \ \  \ \  \ \  \  /     \/       \ \  \ \ \  \_|\ \ \  \ \  \ \  \    \ \  \ 
   \ \__\    \ \__\ \__\ \__\/  /\   \        \ \__\ \ \_______\ \__\ \__\ \__\    \ \__\
    \|__|     \|__|\|__|\|__/__/ /\ __\        \|__|  \|_______|\|__|\|__|\|__|     \|__|
                            |__|/ \|__|                                                  
 '''

from tkinter import *
from tkinter import messagebox
import ast
import pyautogui
import cryptocode
from tkinter import *
import datetime
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
import webbrowser
import pdfkit
from random import randint

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg='black')
root.resizable(False, False)

def signin():

    username = user.get()
    password = code.get()
    file= open('datasheet.txt', 'r+')
    d=file.read()
    r = ast.literal_eval(d)
    file.close()
    
    if username in r.keys() and password in r.values():
        messagebox.showinfo('Sucesso',f'seja bem vindo{username}')
        
        open_main()
        
    else:
        messagebox.showerror('Ivalido', 'Nome de usúario ou senha invalido')
        

################################################################################################     
def signup_command():
    
    window=Toplevel(root)
    
   
    root.title('Login')
    root.geometry('925x500+300+200')
    root.config(bg='black')
    root.resizable(False, False)
        
    def signup2():
        
        username= user.get()
        password= code.get()
        password_conf = code2.get()
        
        while True:
            if password_conf == password:
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
                    pyautogui.hotkey('alt', 'f4')
                    break
                except:
                    file= open('datasheet.txt', 'r+')
                    pp=str({'username': 'password'})
                    file.write(pp)
                    file.close()
                    break

            elif password_conf != password:
                messagebox.showerror('Erro na senha', 'As senhas não confere')
                break
            else:
                messagebox.showerror('Invalido', 'Invalido')
                break

    #-------------------------------------------------------------------

    img = PhotoImage(file='imgs/ads.png')
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
    Button(frame,width=39, pady=7, text='Cadastrar',bg='green', fg='white', border=0,command=signup2).place(x=35,y=260, )

    root.mainloop()

################################################################################################ 
def open_main():
    
    window=Toplevel(root)
    root.geometry('1080x495')
    root.config(bg='black')
    root.resizable(width=False, height=False)
    root.title('MaxTeamApps')
    root.iconphoto(False, PhotoImage(file='imgs/4434053531595501194-128.png'))

    # --------------------------------------------------------------------------
    data = datetime.datetime.now()
    dia = data.day
    mes = data.month
    ano = data.year
    # --------------------------------------------------------------------------


    def pdf():

        while True:

            random = randint(1, 1000)
            pass_word_confirma = text_right_one.get("1.0", "end-1c")

            if pass_word_confirma == '':
                messagebox.showerror('Erro', 'Insira uma senha para salvar')
                break

            else:
                config = pdfkit.configuration(
                    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\bin\wkhtmltopdf.exe")

                pdfkit.from_string(pass_word_confirma,
                                f'{random},passwords.pdf', configuration=config)

                pass_word_confirma = text_right_one.get("1.0", "end-1c")
                messagebox._show('Importante', 'Não esqueça sua senha pois ela é a unica que ira descriptograr a sua messagem\n'
                                'Sua senha foi salva em um arquivo .txt e um arquivo pdf')
                with open('password.txt', 'a') as file:
                    file.writelines(f'{pass_word_confirma}\n')
                break

    # --------------------------------------------------------------------------


    def criptografar():

        while True:

            pass_word = text_right_one.get("1.0", "end-1c")
            text = text_leftDown.get("1.0", "end-1c")

            if pass_word == '':
                messagebox.showerror(
                    'Erro', 'Você precisa escolher uma senha primero')
                break
            elif text == '':
                messagebox.showerror(
                    'Erro', 'você deixou o campo criptografar vazio')
                break

            crypt = cryptocode.encrypt(text, pass_word)
            with open('Criptografados.txt', 'a') as f:
                f.writelines(f'Criado em {dia}/{mes}/{ano}: {crypt}\n')
                messagebox.showwarning(
                    'Sucesso', 'Atenção proteja seu arquivo salvo')
                l_one['text'] = crypt

                break

    # --------------------------------------------------------------------------


    def descriptografar():

        while True:

            text = text_leftDown_two.get("1.0", "end-1c")
            pass_word = text_right_one.get("1.0", "end-1c")

            if pass_word == '':
                messagebox.showerror(
                    'Erro', 'Você precisa enserir sua senha para descriptografar')
                break
            elif text == '':
                messagebox.showerror(
                    'Erro', 'você deixou o campo criptografar vazio')
                break

            decrypt = cryptocode.decrypt(text, pass_word)
            with open('Descriptografados.txt', 'a') as f:
                f.writelines(f'{decrypt}\n')
                messagebox.showwarning(
                    'Sucesso', 'Atenção proteja seu arquivo salvo')
                l_one['text'] = decrypt

                break


    # --------------------------------------------------------------------------
    f_one_banner = Frame(root, width=713, height=102, bg='black')
    f_one_banner.grid(row=0, column=0)

    # --------------------------------------------------------------------------
    logotipo = Image.open('imgs/banner.png')
    logotipo = logotipo.resize((713, 102), Image.LANCZOS)
    logotipo = ImageTk.PhotoImage(logotipo)
    app_logo = Label(f_one_banner, width=715, image=logotipo,
                    compound=LEFT, relief='flat', anchor='center', bg='black')
    app_logo.grid(row=0, column=0)

    # --------------------------------------------------------------------------
    f_two = Frame(root, width=715, height=377, bg='black')
    f_two.grid(row=1, column=0, pady=5)
    text_leftDown = Text(f_two, width=30, height=18, font=('Verdana 10 italic'))
    text_leftDown.place(x=5, y=50)
    b_one = Button(f_two, width=29, height=1, command=criptografar,
                text='Criptografar', font=('Verdana 10 italic'), bg='green', relief='solid')
    b_one.place(x=6, y=345)
    text_leftDown_two = Text(f_two, width=30, height=18,
                            font=('Verdana 10 italic'))
    text_leftDown_two.place(x=255, y=50)
    b_two = Button(f_two, width=29, height=1, command=descriptografar,
                text='Descriptografar', font=('Verdana 10 italic'), bg='yellow', relief='solid')
    b_two.place(x=256, y=345)
    l_one = Label(f_two, height=2, width=61, text='Resultado',
                font=('Verdana 10 italic'))
    l_one.place(x=5, y=6)
    # --------------------------------------------------------------------------

    l_two = Label(f_two, width=20, height=1, bg='white',
                fg='black', text='Senha', fon=('verdana 10'))
    l_two.place(x=520, y=5)
    text_right_one = Text(f_two, width=20, height=1,
                        font=('Verdana 10 italic'), bg='white')
    text_right_one.place(x=521, y=40)
    b_tree_pass = Button(f_two, width=22, height=1, command=pdf,
                        bg='green', fg='white', text='Salvar senha', relief='solid')
    b_tree_pass.place(x=521, y=68)
    l_frame = Frame(f_two, width=200, height=270, bg='white')
    l_frame.place(x=506, y=100)
    logotipo_ads_1 = Image.open('imgs/ads.png')
    logotipo_ads_1 = logotipo_ads_1.resize((200, 270), Image.LANCZOS)
    logotipo_ads_1 = ImageTk.PhotoImage(logotipo_ads_1)
    app_logo_ads_1 = Label(l_frame, width=200,  image=logotipo_ads_1,
                        compound=LEFT, anchor='center', bg='black')
    app_logo_ads_1.grid(row=0, column=0, sticky=NSEW)

    # --------------------------------------------------------------------------


    def vac():

        webbrowser.open(
            'https://www.vakinha.com.br/vaquinha/ajuda-para-continuar-os-estudos-e-projetos')


    # --------------------------------------------------------------------------
    f_six_ads = Frame(root, width=300, height=375, bg='black')
    f_six_ads.place(x=722, y=10)
    logotipo_ads = Image.open('imgs/Ajude faça um pix.png')
    logotipo_ads = logotipo_ads.resize((330, 450), Image.LANCZOS)
    logotipo_ads = ImageTk.PhotoImage(logotipo_ads)
    app_logo_ads = Label(f_six_ads, width=350,  image=logotipo_ads,
                        compound=LEFT, anchor='center', bg='black')
    app_logo_ads.grid(row=0, column=0, sticky=NSEW)
    ajd = Button(f_six_ads, height=1, command=vac, width=50,
                text='Click aqui para ajudar', bg='red', fg='white', relief='solid')
    ajd.grid(row=1, column=0, sticky=W)

    tk.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

img = PhotoImage(file='imgs/login.png')
Label(root, image=img,bg='black').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading= Label(frame,text='Sign in', fg='#57a1f8', bg ='white',
               font=('Microsoft Yahi UI Light',23,'bold'))
heading.place(x=100,y=5)
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

Frame(frame,width=295,heigh=1,bg='black').place(x=25,y=177)

Button(frame,width=39, pady=7, text='Entrar',bg='#57a1f8', fg='white', border=0,command=signin).place(x=35,y=204, )
label = Label(frame,text='Não tem uma conta?', fg='black', bg='white',font=('Microsoft Yahi UI Light ',9))
label.place(x=75, y=270)

sing_up = Button(frame,width=6, text='Cadastre', border=0, bg='white', fg='#57a1f8', command=signup_command)
sing_up.place(x=215, y=270)

root.mainloop()

