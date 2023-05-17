from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from . models import message
from . models import item,cartitem

# Create your views here.
def loginpage(request):
    uname=request.POST.get("uname")
    pas=request.POST.get("pass")
    if uname is not None and pas is not None:
        usr=authenticate(username=uname,password=pas)
        if usr is not None:
            login(request,usr)
            return redirect("http://localhost:8000/home")
        else:
            request.session["msg"]="Invalid login"
    return render(request,"loginpage.html",None)

def logout(request):
    logout(request)
    return redirect("http://localhost://8000/loginpage/")


def signuppage(request):
    ftname=request.POST.get("firstname")
    ltname=request.POST.get("lastname")
    pas=request.POST.get("password")
    com=request.POST.get("confirm_password")
    uname=str(ftname)+str(ltname)
    if pas==com:
        if uname is not None and pas is not None:
            obj=User.objects.create_user(username=uname,password=pas)
            obj.save()

    return render(request,"signuppage.html",None)




@login_required(login_url="http://localhost:8000/loginpage")
def home(request):
    obj=item.objects.all()
    return render(request,"home.html",{"item":obj})

def aboutus(request):
    return render(request,"aboutus.html",None)

def cart(request):
    obj=cartitem.objects.all()


    return render(request,"cart.html",{'item':obj})

def addtocart(request):
  
    id=request.GET.get("id")
    name=request.GET.get("name")
    price=request.GET.get("price")
    img=request.GET.get("img")


    obj=cartitem(id=id,name=name,price=price,img=img)
    obj.save()
    return redirect("http://localhost:8000/cart")


def product(request):
    id = request.GET.get("id")
    row = item.objects.filter(id=id)

    return render(request,"product.html",{'pow': row[0]})


def livechat(request):
    '''txt=request.POST.get("text")
    if txt is not None:
        obj=message(text=txt,sender="",time="")
        obj.save()
    x=message.objects.all()'''

    return render(request,"livechat.html",None)

def delete(request):

    id=request.GET.get("id")
    cartitem.objects.filter(id=id).delete()
    return redirect("http://localhost:8000/cart/")


def payment(request):
    return render(request,"payment.html",None)