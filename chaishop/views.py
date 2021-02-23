from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import Category
from .models.order import Order

from .models.customer import Customer
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
  
    if request.method=='GET':
         
         return render(request, 'login.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')

        customer=Customer.get_customer_by_email(email)
        error_msg=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customerid']=customer.id
                request.session['email']=customer.email
                return render(request,'index.html')
            else:
                error_msg = "Email or Password Invalid !!"
        else:
            error_msg = "Email or Password Invalid !!"

        return render(request, 'login.html', {'error': error_msg})


def validateuser(customer):
    error_msg = None
    if not customer.firstname:
        error_msg = "First name is required"
    elif not customer.lastname:
        error_msg = "Last name is required"
    elif not customer.password:
        error_msg = "Password is required"
    elif len(customer.password) < 6:
        error_msg = "Password should have more than 6 character"
    elif customer.isExist():
        error_msg = "Email id is already Exist"
    return error_msg

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
       
        customer = Customer(firstname=firstname,
                        lastname=lastname,
                        email=email,
                        password=password)
        error_msg=None
        error_msg=validateuser(customer)
        
        if not error_msg:
             customer.password=make_password(customer.password)
             customer.register()
             return render(request,'login.html')
        else:
            data={
                'error':error_msg
            }
            return render(request,'signup.html',data)


def store(request):
        
        category=Category.get_category()
        
        category_id=request.GET.get('category')
        print(Category.get_category_name(category_id))
        print(category_id)
        if category_id:
            products=Product.get_all_product_by_category(category_id)
        else:    
            products=Product.get_all_product()
        
        data={
            'category':category,
            'products':products
        }
        return render(request, 'store.html',data)
   

    


def orders(request):
    if request.method == "GET":
        customer=request.session.get('customerid')
        order=Order.get_orders_by_customer(customer)
        print(order)
        return render(request, 'orders.html',{'orders':order})

def product(request):
    if request.method=="GET":
        cart=request.session.get('cart')
        if not cart:
            cart={}
        product_id=request.GET.get('product')
        product=Product.get_product_by_id(product_id)
        print(product)
        return render(request,'product.html',{'product':product})
    else:
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            print(quantity)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        
        
        request.session['cart']=cart
        print(request.session['cart'])
        product_id=request.GET.get('product')
        print(product)
        product=Product.get_product_by_id(product_id)
        print(product)
        return render(request,'product.html',{'product':product})

def cart(request):
    cart=request.session.get('cart')

    if not cart:
        return render(request,'cart.html')
    else:
        ids=list(request.session.get('cart').keys())
        product=Product.get_cart_products_by_id(ids) 
        print(product)
        return render(request,'cart.html',{'products':product})

def logout(request):
    request.session.clear()
    return render(request, 'index.html')

def checkout(request):
    if request.session.get('customerid'):
        if request.method=="POST":
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            customer=request.session.get('customerid')
            cart=request.session.get('cart')
            products=Product.get_cart_products_by_id(list(cart.keys()))
            print(address,phone,customer,cart,products)
            for p in products:
                 order=Order(  customer=Customer(id=customer),
                                 product=p,
                                 price=p.price,
                                 address=address,
                                 phone=phone,
                                 quantity=cart.get(str(p.id))
                           )
                 order.placeOrder()
            
            return redirect('orders')
            
    else:
        return redirect('login')
