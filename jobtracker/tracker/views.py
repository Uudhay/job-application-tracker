from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import JobApplication

def home(request):
    return render(request, 'home.html')

def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/jobs/')
    else:
        form = JobApplicationForm()

    return render(request, 'add_job.html', {'form': form, 'page_type': 'add'})

def job_list(request):
    query = request.GET.get('q')
    status = request.GET.get('status')

    jobs = JobApplication.objects.all()

    if query:
        jobs = jobs.filter(company_name__icontains=query) | jobs.filter(job_role__icontains=query)

    if status:
        jobs = jobs.filter(status=status)

    return render(request, 'job_list.html', {'jobs': jobs, 'total_jobs': jobs.count()})

def delete_job(request, id):
    job = JobApplication.objects.get(id=id)
    job.delete()
    return redirect('/jobs/')
def edit_job(request, id):
    job = JobApplication.objects.get(id=id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/jobs/')
    else:
        form = JobApplicationForm(instance=job)

    return render(request, 'add_job.html', {'form': form, 'page_type': 'edit'})