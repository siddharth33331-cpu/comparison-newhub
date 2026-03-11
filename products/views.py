from django.shortcuts import render
from .models import Product, Category


def home(request):
    return render(request, "home.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

from .models import Product, Category

def category_page(request, category_name):
    category = Category.objects.get(name__iexact=category_name.replace("-", " "))
    products = Product.objects.filter(category=category)

    return render(request, "category.html", {
        "category": category,
        "products": products
    })



def compare_products(request):

    categories = Category.objects.all()

    category_id = request.GET.get("category")

    products = None
    selected_products = None

    if category_id:
        products = Product.objects.filter(category_id=category_id)

    selected_ids = request.GET.getlist("products")

    if selected_ids:
        selected_products = Product.objects.filter(id__in=selected_ids)

    return render(request, "compare.html", {
        "categories": categories,
        "products": products,
        "selected_products": selected_products
    })
from .models import DiscussionThread, Post


def forum_home(request):

    threads = DiscussionThread.objects.all().order_by("-created_at")

    return render(request, "forum.html", {
        "threads": threads
    })


def thread_page(request, thread_id):

    thread = DiscussionThread.objects.get(id=thread_id)

    posts = Post.objects.filter(thread=thread)

    return render(request, "thread.html", {
        "thread": thread,
        "posts": posts
    })