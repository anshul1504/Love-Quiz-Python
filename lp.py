from tkinter import *
import random
t=Tk()
t.title("Gift")
t.resizable(0,0)
w=750
h=650
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
t.configure(bg="white")

questions=["Kya Main Tumse Pyar Krta hu ?","Kya Tum Mujhse Se Nafrat Krti ho ?","Maine Tumhe Kya Nick Name Diya H ?","Kya Kabhi Mujh KO Dekhker Chid Hui?","Kya Kabhi Mujhko Ko Block Krne ki ichha hui ?"]
answers_choice=[["Han,Bilkul Shidato Wala","Nhi"],["Yes ","No"],["Pari","Sabeen"],["Hn","Kabhi Nahi"],["No Never","Tumne Kabhi Ese Kam HE Nh Kiye"]]

user_answer=[]

answers=[1,2,1,2,2]

indexes=[]
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    labelimage=Label(t,bg="#ffffff",bd=0)
    labelimage.pack(pady=150)
    labelresulttext=Label(t,font=("Sylfaen",18),bg="#ffffff")
    labelresulttext.pack()
    if score>=20:
        img=PhotoImage(file="download (7).png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You are really Excellent!!\nYou really Like me Sabeen")
    elif (score>=10 and score < 20):
        img=PhotoImage(file="download (1).png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Can Be Better !!\n Talk more with Me. Sabeen")
    elif (score>=0 and score <20):
        img=PhotoImage(file="download (15).png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Really Broken My Heart !!\n I didn't expect with you. Sabeen")
def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score=score + 5
        x+=1
    #print(score)
    showresult(score)

ques = 1 
def selected():
    global radiovar,user_answer
    global lblquestion,r1,r2
    global ques
    x=radiovar.get()
    #print(x)
    user_answer.append(x)
    radiovar.set(-1) 
    if ques <5:
        lblquestion.config(text=questions[indexes[ques]])
        r1["text"]=answers_choice[indexes[ques]][0]
        r2["text"]=answers_choice[indexes[ques]][1]
        ques+=1
    else:
        calc()
 
def startquiz():
    global lblquestion,r1,r2
    lblquestion=Label(t,text=questions[indexes[0]],font=("consola",16,"bold"),bg="#ffffff",width=500,justify="center",wraplength=400)
    lblquestion.pack(pady=(250,30))
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)    
    r1=Radiobutton(t,text=answers_choice[indexes[0]][0],font=("arial",14),bg="#ffffff",value=1,variable=radiovar,command=selected)
    r1.pack(pady=5)
    r2=Radiobutton(t,text=answers_choice[indexes[0]][1],font=("arial",14),bg="#ffffff",value=2,variable=radiovar,command=selected)
    r2.pack(pady=5)
    
def startimpressed():
    #i1.destroy()
    u1.destroy()
    u3.destroy()
    #i2.destroy()
    b1.destroy()
    u4.destroy()
    gen()
    startquiz()
    

i1=PhotoImage(file="The-8.png")
u1=Label(image=i1,bg="white")
u1.pack()
u3=Label(text="Read The Rules And\nClick Start Once You Are Ready ",font=("arial",14,"bold","underline"),bg="white")
u3.place(x=230,y=370)
i2=PhotoImage(file="star6.png")
b1=Button(image=i2,relief=FLAT,border=0,bg="white",command=startimpressed)
b1.place(x=270,y=450,height=63,width=200)

u4=Label(text="This Challenge Contain Only 05 Question\nEvery Question Are Compulsory To Attend\nOnce You Select A Option That Will Be A Final Choice\nHence Think Before Select ",font=("",12),bg="black",fg="gold",justify="center")
u4.place(x=0,y=571,width=750)

t.mainloop()