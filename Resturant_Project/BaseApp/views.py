from django.shortcuts import render,redirect
from django.http import HttpResponse
from BaseApp.models import ItemList,Items,Feedback,Book_table,UserInfo

# Create your views here.

def Home(request):
    
    return render(request,"home.html")

    # feedback = Feedback.objects.all()
    # return render(request,"home.html",{'feedback':feedback})

def Menu(request):

    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request,"menu.html", {'items':items, 'list':list})

def Book_Table(request):

    if request.method == "GET":
        return render(request,"book_table.html")
    else:
        uname = request.POST["uname"]
        phone = request.POST["phone"]
        mail = request.POST["mail"]
        total_person = request.POST["total_person"]
        booking_date = request.POST["booking_date"]

        data = Book_table(Name=uname, Phone=phone, Email=mail, Total_person=total_person, Booking_date=booking_date)
        data.save()
    return render(request,"book_table.html")
    


def About(request):
    return render(request,"about.html")

def Feedbackk(request):
    feeds = Feedback.objects.all()
    return render(request,"feedback.html",{'feeds':feeds})


def SignUp(request):
    if request.method == "GET":
        return render(request,"signup.html")
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        info = UserInfo(username=uname,password=pwd)
        info.save()
    return render(request,"signup.html")

def Login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
         uname = request.POST["uname"]
         pwd = request.POST["pwd"]

         try:
                user = UserInfo.objects.get(username=uname,password=pwd)
         except:
                return redirect(Login)
         else:
                #Add user to session
                request.session["uname"]=uname
                return redirect(Home)

def Logout(request):
     request.session.clear()
     return redirect(Home)

def Viewdetails(request,id):
     if request.method == "GET":
          item = Items.objects.get(id=id)
          cat = ItemList.objects.all()
          return render(request,"viewdetails.html",{'item':item, 'cat':cat})
     else:
          pass
          
         

    
        