from django.shortcuts import render,redirect
from .models import *
from django.db.models import F
def Homepage(request):
    pro = Product.objects.all()
    cust = Customer.objects.all()
    return render(request,"app/home.html",{'cust':cust,'pro':pro})

def Customers(request):
    return render(request,"app/customers.html")

def successpage(request):
    return render(request,"app/success.html")

def Productssss(request):
    return render(request,"app/productsss.html")
def abc(request):
    return render(request,"app/editpages.html")


def Productadddata(request):
    if request.method == 'POST':
        pname = request.POST['productname']
        pprice = request.POST['productprice']
        if pname and pprice:
            data = Product.objects.create(Product_name=pname,Unit_price=pprice)
            return redirect("orderpage")

        else:
            msg="All fields are required"
            return render(request,"app/productsss.html",{'err':msg})

def Addcust(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        pin = request.POST['pin']

        if fname and lname and contact and pin:
            data = Customer.objects.create(Firstname=fname,Lastname=lname,Contact=contact,Pincode=pin)
            return redirect("orderpage")
        else:
            
            msg="All field are required"
            return render(request,"app/customers.html",{'err':msg})

def Addorderss(request):
    if request.method == 'POST':
        cid = request.POST['c']
        pro = request.POST['pro']
        
        x = Customer.objects.filter(Firstname=cid)
        y = Product.objects.filter(Product_name=pro)
        q = request.POST['q']
        t = request.POST['total']
        pr = request.POST['price']
        cfk = x[0].id
       
        pfk = y[0].id
        
        if cid and pro and x and y and q and t and cfk and pfk and pr:
        
            data=Order.objects.create(Unit_price=pr,Quntity=q,Total_price=t,Customer_id=cfk,Productsss_id=pfk)
            o = Order.objects.all()
            return render(request,"app/order.html",{'o':o})
            
        else:

            msg="All field are required"
            return render(request,"app/home.html",{'err':msg})



def Editpage(request,pk):
    x = Order.objects.get(id=pk)
    return render(request,"app/editpages.html",{'data':x})
    


def Editdatatable(request,pk):
    data = Order.objects.get(id=pk)
    data.Unit_price = data.Unit_price if request.POST['unit'] else data.Unit_price
    data.Quntity = data.Quntity if request.POST['q'] else data.Quntity
    data.Total_price = data.Total_price if request.POST['tprice'] else data.Total_price
    data.save()
    print("Data Updated successfully")
    
    return redirect("s")

def Orderpage(request):
    z = Order.objects.all()
    return render(request,"app/order.html",{'p':z})


def Serch(request):
    s = request.GET['se'] 
    x= int(s)
    if x>1:
        data = Order.objects.get(id=s)
        return render(request,'app/serchsssss.html',{'data':data})
    else:
        msg="Record not found"
        return render(request,"app/success.html",{'err':msg})


def Deletedata(request,pk):
    data = Order.objects.get(id=pk)
    data.delete()
    return redirect("orderpage")


        
