from django.shortcuts import render
from . models import Job 
from django.core.paginator import Paginator
# Create your views here.



def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list, 3) # Show 25 contacts per 
    # بس هنا المفروض ال pagenator هيعمل باجينتور لا يه ؟ المفروض هيعمل للمتغير للمتغير بتاع كل الوظايف وبعدها بنحدد العدد اللى عايزينه 
    #page_number = request.GET.get('page')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs' :page_obj} #template name
    #context = {'jobs' : job_list }
    return render (request , 'job/job_list.html',context)  

def job_detail(request , slug ):
    job_detail=Job.objects.get(slug=slug)
    context = {'job': job_detail }
    return render (request, 'job/job_detail.html',context)

