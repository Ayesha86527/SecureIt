from tkinter import *
from PIL import Image, ImageTk
import random
import string

def gen():
    clear_window()
    canvas.create_image(0,0,anchor="nw",image=img)
    def gen_pw():
        s1=string.ascii_uppercase
        s2=string.ascii_lowercase
        s3=string.digits
        s4=string.punctuation
        pw_len=plen.get()
        s=[]
        s.extend(list(s1))  
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        result="".join(random.sample(s,pw_len))
        entry_gen.insert(0,result)
    plen=IntVar()
    gen=StringVar()
    canvas.create_text(
    450, 100,  
    text="Generate Password!", 
    fill="white", 
    font=("Times New Roman", 38, "bold")  
)
    canvas.create_text(
    450, 190,  
    text="Enter the password length:", 
    fill="white", 
    font=("Times New Roman", 24, "bold")  
)
    entry_plen=Entry(m,textvariable=plen,font=("Times New Roman",16))
    canvas.create_window(
        450,250,
        window=entry_plen
    )
    b1= Button(m, text="Generate", font=("Times New Roman", 16), bg="#3b5998", fg="white",width=18,command=gen_pw)
    canvas.create_window(450, 300, anchor="center", window=b1) 
    entry_gen=Entry(m,textvariable=gen,font=("Times New Roman",16))
    canvas.create_window(
        450,350,
        window=entry_gen
    )

def strength():
    clear_window()
    canvas.create_image(0,0,anchor="nw",image=img)
    def check():
        p=password.get()
        if any(char.isalpha() for char in p) and any(char.isdigit() for char in p) and any(not char.isalnum() for char in p):
          if len(p)>6:
            vs_btn=Button(m,text="Very Strong",font=("Times New Roman",16,"bold"),bg="green",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=vs_btn)   
          elif len(p)>=4 or len(p)<6:
            s_btn=Button(m,text="Strong",font=("Times New Roman",16,"bold"),bg="ORANGE",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=s_btn) 
        elif any(char.isalpha() for char in p) and any(char.isdigit() for char in p):
          if len(p)>6:
            s_btn=Button(m,text="Strong",font=("Times New Roman",16,"bold"),bg="ORANGE",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=s_btn) 
          elif len(p)>=4 or len(p)<6:
            m_btn=Button(m,text="Medium",font=("Times New Roman",16,"bold"),bg="#FFA500",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=m_btn) 
        elif any(char.isalpha() for char in p):
          if len(p)>=6:
            w_btn=Button(m,text="Weak",font=("Times New Roman",16,"bold"),bg="red",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=w_btn) 
          else:
            vw_btn=Button(m,text="Very Weak",font=("Times New Roman",16,"bold"),bg="brown",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=vw_btn)
        elif any(char.isdigit() for char in p):
          if len(p)>=6:
            w_btn=Button(m,text="Weak",font=("Times New Roman",16,"bold"),bg="red",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=w_btn) 
          else:
            vw_btn=Button(m,text="Very Weak",font=("Times New Roman",16,"bold"),bg="brown",fg="white",width=8)    
            canvas.create_window(450, 350, anchor="center", window=vw_btn)
            

    password=StringVar()
    canvas.create_text(
    450, 100,  
    text="Check Strength!", 
    fill="white", 
    font=("Times New Roman", 38, "bold")  
)
    canvas.create_text(
    450, 190,  
    text="Enter your password:", 
    fill="white", 
    font=("Times New Roman", 24, "bold")  
)
    entry_pass=Entry(m,textvariable=password,font=("Times New Roman",16))
    canvas.create_window(
        450,250,
        window=entry_pass
    )
    b2= Button(m, text="Check", font=("Times New Roman", 16), bg="#3b5998", fg="white",width=18,command=check)
    canvas.create_window(450, 300, anchor="center", window=b2) 
    

def clear_window():
    canvas.delete("all")


m=Tk()

#Screen setting

m.geometry("900x500")
m.title("SecureIt")
m.iconbitmap("C:/Users/AAC/Downloads/cyber-security.ico")
m.maxsize(width=900,height=500)
bg="C:/Users/AAC/Documents/hacking-3112539_1280.png"
bg_img=Image.open(bg)
bg_img=bg_img.resize((900,500))
img=ImageTk.PhotoImage(bg_img)
canvas=Canvas(m,width=900,height=500)
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0,anchor="nw",image=img)

#first window gui
canvas.create_text(
    450, 100,  
    text="Welcome To SecureIt", 
    fill="white", 
    font=("Times New Roman", 38, "bold")  
)

canvas.create_text(
    450, 350,  
    text="Your Key To Unbreakable Passwords!.", 
    fill="white", 
    font=("Times New Roman", 16)  
)


check_btn = Button(m, text="Check Password Strength",font=("Times New Roman", 16), bg="#3b5998", fg="white",width=18,command=strength)
gen_btn = Button(m, text="Generate Password", font=("Times New Roman", 16), bg="#3b5998", fg="white",width=18,command=gen)

canvas.create_window(450, 210, anchor="center", window=check_btn) 
canvas.create_window(450, 270, anchor="center", window=gen_btn)  


m.mainloop()
