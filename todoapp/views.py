from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . models import *


def firstpg(request):
    return render(request, 'firstpg.html')
def logintodo(request):
    if request.method=='POST':
        try:
            usernm=request.POST['uname']
            passwd=request.POST['password']
            userinfo=Login.objects.get(username=usernm, password=passwd)
            request.session['id']=userinfo.id
            return redirect('hometodo')
        except:
            return render(request,'logintodo.html',{'message':'Invalid userdetails'})   
    return render(request,'logintodo.html')
def signout(request):
    del request.session['id']
    return redirect('firstpg')    
def craccount(request):
    if request.method=='POST':
        try:
            firname=request.POST['fname']
            lastname=request.POST['lname']
            usernm=request.POST['em']
            passwd=request.POST['pswrd']
            
            logdetails=Login(username=usernm, password=passwd)
            logdetails.save()
            usrdetails=Udetails(firstname=firname, lastname=lastname, loginid=logdetails)
            usrdetails.save()
            request.session['id']=logdetails.id
            return redirect('hometodo')
            
        except: 
            return render(request,'craccount.html',{'msg':'error'})       
    return render(request,'craccount.html')     
def login2(request):    
    usrname=request.GET['uname']
    ucheck=Login.objects.filter(username=usrname).exists() 
    print(ucheck)
    if ucheck:
        return JsonResponse({
            'msg':True
         })
    else:
        return JsonResponse({
            'msg':False
        })  
                
def hometodo(request):
    logid=request.session['id'] 
    if request.method=='POST':
        try:
            nwtask=request.POST['newtask']
            nwdate=request.POST['ndate']
            nwtime=request.POST['ntime']
            print(nwtask)
            mytask=Task(newtask=nwtask, date=nwdate, time=nwtime, status='active', loginid_id=logid)
            mytask.save()
            tasks=Task.objects.filter(Q(loginid=logid), status='active')    
            print(tasks)
            return render(request, 'hometodo.html', { 'tsk':tasks}) 
        except: 
            tasks=Task.objects.filter(Q(loginid=logid), status='active')   
            return render(request,'hometodo.html' ,{'msg':'Please enter all fields', 'tsk':tasks})
    tasks=Task.objects.filter(Q(loginid=logid), status='active')    
    udetails=Udetails.objects.get(loginid=logid)  
    return render(request,'hometodo.html',{'tsk':tasks,'userdata':udetails}) 

def updatetask(request,itmid):
    logid=request.session['id'] 
    if request.method=='POST':
        item=request.POST['nwitm']
        updt=request.POST['nwdt']
        uptime=request.POST['nwtim']
        Task.objects.filter(id=itmid).update(newtask=item, date=updt, time=uptime)    
        return redirect('hometodo') 
    else: 
        udetails=Udetails.objects.get(loginid=logid)  
        edititm=Task.objects.get(id=itmid)  
        return render(request, 'edit.html', { 'userdata':udetails, 'edititm':edititm,})     
    
def notes(request):
    logid=request.session['id']
    if request.method=='POST':
        try:
            note=request.POST['note']
            color=request.POST['colorpick']
            print(color)
            nwnote=Notes(mynote=note, mycolor=color, loginid_id=logid)
            nwnote.save()
            print('checkif----------------------')
            return render(request, 'notes.html',{'msge':'Added Successfully'})
        except:  
            return render(request, 'notes.html',{'msge':'Error'})  
    return render(request, 'notes.html')

def notes2(request):
    logid=request.session['id']
    if request.method=='POST':
        srchnote=request.POST['note']
        search_note=Notes.objects.filter(Q(mynote__icontains=srchnote), loginid=logid)
        return render(request, 'notes2.html',{'notes':search_note})
    else:    
        nts=Notes.objects.filter(loginid=logid)   
        return render(request, 'notes2.html', {'notes': nts}) 
          
def lists(request):
    logid=request.session['id'] 
    tasks=Task.objects.filter(Q(loginid=logid), status='inactive')
    tasks2=Task.objects.filter(Q(loginid=logid), status='active')
    if request.method=='POST':
        srch=request.POST['search'] 
        srchitm=Task.objects.filter(Q(newtask__icontains=srch)|Q(date__icontains=srch)|Q(time__icontains=srch), loginid=logid) 
        return render(request,'lists.html', {'tasksearch':srchitm })   
    else:    
        tasks=Task.objects.filter(Q(loginid=logid), status='inactive')
        tasks2=Task.objects.filter(Q(loginid=logid), status='active')
        taskitems=Task.objects.filter(loginid=logid)
        return render(request, 'lists.html', {'taskdata':taskitems, 'task':tasks, 'activetask':tasks2}) 

def delete(request,dltitmid):
    logid=request.session['id']
    updtstatus=Task.objects.filter(id=dltitmid).update(status='inactive')
    return redirect('hometodo')

def delnotes(request,noteid):
    delnote=Notes.objects.filter(id=noteid).delete()  
    return redirect('notes2') 

def dltitm(request,dltid):
    dellists=Task.objects.filter(id=dltid).delete()
    return redirect('lists')     

def deleteacc(request): 
    logindata=request.session['id']
    delaccount=Udetails.objects.get(loginid=logindata).delete() 
    return redirect('logintodo') 

def diet(request):
    logid=request.session['id']
    
    if request.method=='POST':
        try:
            dietdtls=Diet.objects.filter(loginid=logid)
            if dietdtls:
                age=request.POST['age']
                weight=request.POST['weight']
                height=request.POST['height']
                medclcondition=request.POST['condition']
                print('----------------')
                Diet.objects.filter(loginid=logid).update(age=age, weight=weight, height=height, medcondition=medclcondition)
                return render(request, 'plan2.html')
            else:  
                age=request.POST['age']
                weight=request.POST['weight']
                height=request.POST['height']
                medclcondition=request.POST['condition']      
                dietdetails=Diet(age=age, weight=weight, height=height, medcondition=medclcondition, loginid_id=logid)
                dietdetails.save()
                return render(request, 'plan2.html')
        except:
            return render(request, 'diet.html', {'msg':'Please enter this fields'}) 
    dietdtls=Diet.objects.filter(loginid=logid)
    if dietdtls: 
        dietdt=Diet.objects.get(loginid=logid)      
        return render(request, 'diet.html', {'dietdata':dietdt})
    else:
       return render(request, 'diet.html')               
       
def plan2(request):
    return render(request, 'plan2.html')
def snacks(request):
    return render(request, 'snacks.html')
def water(request):
    return render(request, 'water.html') 
def sunday(request):
    return render(request, 'sunday.html')    
def day2(request):
    return render(request, 'day2.html')
def day3(request):
    return render(request, 'day3.html') 

def pendinglist(request):
    logid=request.session['id']
    tasks=Task.objects.filter(loginid=logid, status='active')   
    udetails=Udetails.objects.get(loginid=logid)  
    return render(request, 'pendinglist.html', {'usrname':udetails,'tsk':tasks })    

def profile(request):
    logid=request.session['id']
    logindetails=Login.objects.get(id=logid)
    udetails=Udetails.objects.get(loginid=logid) 
    dietdtls=Diet.objects.filter(loginid=logid)
    if dietdtls:
        dietdt=Diet.objects.get(loginid=logid) 
        return render(request, 'profile.html', {'userdetails':udetails, 'ldetails':logindetails, 'dietplan':dietdt})  
    else:
        return render(request, 'profile.html', {'userdetails':udetails, 'ldetails':logindetails})        

def today(request):
    logid=request.session['id']
    udetails=Udetails.objects.get(loginid=logid) 
    mrng=Myfood.objects.filter(loginid=logid) 
    noon=Mylunch.objects.filter(loginid=logid)
    night=Mydinner.objects.filter(loginid=logid)
    if mrng and noon and night:
        breakfast=Myfood.objects.get(loginid=logid) 
        lunch=Mylunch.objects.get(loginid=logid)
        dinner=Mydinner.objects.get(loginid=logid)
        return render(request, 'today.html', {'usrname':udetails, 'breakfast':breakfast, 'lunch':lunch, 'dinner':dinner}) 
    elif mrng and noon:
        breakfast=Myfood.objects.get(loginid=logid) 
        lunch=Mylunch.objects.get(loginid=logid)     
        return render(request, 'today.html', {'usrname':udetails, 'breakfast':breakfast, 'lunch':lunch})  
    elif mrng and night:  
        breakfast=Myfood.objects.get(loginid=logid) 
        dinner=Mydinner.objects.get(loginid=logid)  
        return render(request, 'today.html', {'usrname':udetails, 'breakfast':breakfast, 'dinner':dinner}) 
    elif noon and night:
        lunch=Mylunch.objects.get(loginid=logid)
        dinner=Mydinner.objects.get(loginid=logid)  
        return render(request, 'today.html', {'usrname':udetails, 'lunch':lunch, 'dinner':dinner}) 
    elif mrng:  
        breakfast=Myfood.objects.get(loginid=logid)
        return render(request, 'today.html', {'usrname':udetails, 'breakfast':breakfast})
    elif noon:
        lunch=Mylunch.objects.get(loginid=logid)   
        return render(request, 'today.html', {'usrname':udetails, 'lunch':lunch })
    elif night:
        dinner=Mydinner.objects.get(loginid=logid) 
        return render(request, 'today.html', {'usrname':udetails, 'dinner':dinner})   
    else:
        return render(request, 'today.html', {'usrname':udetails})

def food(request):
    logid=request.session['id']
    if request.method=='POST':
        checkbrkfast=Myfood.objects.filter(loginid=logid)
        if checkbrkfast:
            mrng=request.POST['brkfst']
            Myfood.objects.filter(loginid=logid).update(morning=mrng) 
            return redirect('plan2')
        else:    
            mrng=request.POST['brkfst']  
            brfood=Myfood(morning=mrng, loginid_id=logid)   
            brfood.save()
            return redirect('plan2')
    else:    
        return render(request, 'plan2.html',{'msg':'error'})    

def lunch(request):
    logid=request.session['id']
    if request.method=='POST':  
        checklnch=Mylunch.objects.filter(loginid=logid)
        if checklnch:
            lnch=request.POST['noon'] 
            lnobj=Mylunch.objects.filter(loginid=logid).update(lunch=lnch)
            return redirect('plan2')
        else: 
            lnch=request.POST['noon']    
            lnfood=Mylunch(lunch=lnch, loginid_id=logid) 
            lnfood.save()
            return redirect('plan2')
    else:    
        return render(request, 'plan2.html',{'mesg':'error'})        

def dinner(request):
    logid=request.session['id']
    if request.method=='POST':  
        checkdnr=Mydinner.objects.filter(loginid=logid)
        if checkdnr:
            dnr=request.POST['night'] 
            dnrobj=Mydinner.objects.filter(loginid=logid).update(dinner=dnr)
            return redirect('plan2')
        else: 
            dnr=request.POST['night'] 
            dnfood=Mydinner(dinner=dnr,loginid_id=logid)
            dnfood.save()
            return redirect('plan2')
    else:    
        return render(request, 'plan2.html',{'mssg':'error'})                