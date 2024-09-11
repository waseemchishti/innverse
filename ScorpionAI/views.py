from django.http import HttpResponse
from django.shortcuts import render
from contactform.models import Contactform
from blog.models import Blog

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def career(request):
    return render(request,'career.html')
def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html', {'blogs': blogs})

def blog_category(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request,'blog_category.html', {'blog': blog})

def news(request):
    return render(request,'news.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Contactform(name=name,email=email,phone=phone,subject=subject,message=message)
        data.save()
        m="Your data Has Been Inserted!" 
        return render(request,'contact.html',{'m':m})

    return render(request,'contact.html')
def retail(request):
    return render(request,'retail.html')
def fintech(request):
    return render(request,'fintech.html')
def health(request):
    return render(request,'health.html')
def waste(request):
    return render(request,'waste.html')
def real(request):
    return render(request,'real.html')
def ecommerce(request):
    return render(request,'ecommerce.html')
def customizeAI(request):
    return render(request,'customizeAI.html')
def generative(request):
    return render(request,'generative.html')
def nlp(request):
    return render(request,'nlp.html')
def dataScience(request):
    return render(request,'data-science.html')
def computerVision(request):
    return render(request,'computer-vision.html')
def bigData(request):
    return render(request,'big-data.html')
def dataEngineering(request):
    return render(request,'data-engineering.html')
def aiStrategy(request):
    return render(request,'ai-strategy.html')
def webDevelopment(request):
    return render(request,'web-development.html')
def appDevelopment(request):
    return render(request,'app-development.html')
def seo(request):
    return render(request,'seo.html')
def digitalMarketing(request):
    return render(request,'digital-marketing.html')
def life(request):
    return render(request, 'life.html')