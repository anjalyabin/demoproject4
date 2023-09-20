from django.shortcuts import render

# Create your views here.
from ecommerceapp.models import Product


# Create your views here.
def product_view(request, myid):
    product = Product.objects.filter(id=myid).first()
    feature = Feature.objects.filter(product=product)
    reviews = Review.objects.filter(product=product)
    data = cartdata(request)
    items = data['items']
    order = data['order']
    cartitems = data['cartitems']

    if request.method == "POST":
        content = request.POST['content']
        review = Review(customer=customer, content=content, product=product)
        review.save()
        return redirect(f"/product_view/{product.id}")
    return render(request, "product_view.html",
                  {'product': product, 'cartitems': cartItems, 'feature': feature, 'reviews': reviews})