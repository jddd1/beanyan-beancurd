from django.shortcuts import render,redirect
from .models import *
from .forms import *

def Main(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def CartItems(request):
    tub = Product.objects.filter(category="Tub") | Product.objects.filter(category="Cup") | Product.objects.filter(category="Soya Milk")
    adds = Product.objects.filter(category="Add Ons")
    context = {'tubs':tub,
                'adds':adds
                }

    if request.method == "POST":
        custom_name = request.POST['custom_name']
        custom_number = request.POST['custom_number']
        mainProduct = request.POST['mainProduct']
        total_amount = request.POST['total_amount']
        custom_add = request.POST['custom_add']
        custom_message = request.POST['custom_message']
        status = "Pending"

        user = Customer(
            name = custom_name,
            phone = custom_number,
            address = custom_add 
            )

        cart = Cart(
            product_name = mainProduct,
            amount = total_amount
            )
        order = Order(
            message = custom_message,
            status = status
            )
        user.save()
        cart.save()
        order.save()

    return render(request,'cart.html', context)

def Menu(request):
    menu = Product.objects.all()

    return render(request,'menu.html', {'products':menu},)

def OrderPage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    carts = Cart.objects.all()

    context = {'orders':orders,
        'customers':customers,
        'carts':carts

    }

    # if request.method == "POST":
    #     custom_name = request.POST['custom_name']
    #     custom_number = request.POST['custom_number']
    #     food_name = request.POST['food_name']
    #     add_ons = request.POST['add_ons']
    #     number_order = request.POST['number_order']
    #     date_time = request.POST['date_time']
    #     custom_add = request.POST['custom_add']
    #     custom_message = request.POST['custom_message']
    #     cus = Order(custom_name = custom_name,
    #     custom_number = custom_number,
    #     food_name = food_name,
    #     add_ons = add_ons,
    #     number_order = number_order,
    #     date_time = date_time,
    #     custom_add = custom_add,
    #     custom_message = custom_message
    #     )
        
    #     cus.save()

    # else:
    #     return render(request,'order.html')
    # cuss =   Order.objects.all()
    return render(request,'order.html', context)

def Review(request):
    review = Feedback.objects.all()
    return render(request,'review.html', {'review':review})

def Contact(request):
    if request.method == "POST":
        customername = request.POST['customername']
        customeremail = request.POST['customeremail']
        customerphone = request.POST['customerphone']
        customeraddress = request.POST['customeraddress']
        customerconcern = request.POST['customerconcern']
        customermessage = request.POST['customermessage']
        feedback = Feedback(customername = customername,
            customeremail = customeremail,
            customerphone = customerphone,
            customeraddress = customeraddress,
            customerconcern = customerconcern,
            customermessage = customermessage
            )

        feedback.save()
    else:
        return render(request, 'contact.html')
    feeds = Feedback.objects.all()
    return render(request,'contact.html',{'feeds':feeds})

def AdminLogin(request):
    return render(request,'adminlogin.html')

def AdminProduct(request):
    menu = Product.objects.all()

    context = {
        'products':menu
    }
    return render(request,'adminproduct.html', context)

def AdminCustomer(request):
    customer = Customer.objects.all()

    context = {'customers':customer}
    
    return render(request,'admincustomer.html', context)

def AdminOrder(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    carts = Cart.objects.all()

    context = {'orders':orders,
        'customers':customers,
        'carts':carts
    }    
    return render(request,'adminorder.html',context)


def createProduct(request):

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/adminproduct/')

    context = {'form':form}

    return render(request,'forms.html', context)
def updateProduct(request,pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/adminproduct')
    context = {'form':form}

    return render(request,'forms.html', context)

def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/adminproduct')
    context = {'item':product}
    return render(request,'delete.html', context)

def updateCustomer(request,pk):

    cus = Customer.objects.get(id=pk)
    form = CustomerForm(instance=cus)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=cus)
        if form.is_valid():
            form.save()
            return redirect('/admincustomer')
    context = {'form':form}

    return render(request,'forms.html', context)

def deleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/adminproduct')
    context = {'item':customer}
    return render(request,'delete2.html', context)

def updateOrder(request,pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/adminorder')
    context = {'form':form}

    return render(request,'forms.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/adminproduct')
    context = {'item':order}
    return render(request,'delete2.html', context)