from unittest import result
from django.http import HttpResponse
from django.shortcuts import render, redirect



import mysql.connector as sql
# Create your views here.
fn=''
ln=''
s=''
em=''
pwd=''
qu = ''
def index(request):
    return render(request, 'index.html')



def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Gagana@2001",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'feed.html')

    return render(request,'login_page.html')




def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Gagana@2001",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')


def feed(request):
    mydb = sql.connect(host="localhost",user="root",password="Gagana@2001",database="website")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT question FROM addqu")
    myresult = mycursor.fetchall()
    list_questions = [lis[0] for lis in myresult]
    list_questions.reverse()

    return render(request,'feed.html',{'result':list_questions})




def add(request):
    
    global em,qu
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Gagana@2001",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="question":
                qu=value
            c="insert into website.addqu (email, question) Values('{}','{}')".format(em,qu)
        cursor.execute(c)
        m.commit()
        
    return render( request, ('add.html'))

def aboutus(request):
    return render(request, "aboutus.html")


def profile(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="Gagana@2001",database='website')
        cursor=m.cursor()
        d=request.POST
        c="select * from users'".format(fn, ln, s,em)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            result =print(t)
        return render(request,'profile.html',result='x')
    return render(request, 'profile.html')