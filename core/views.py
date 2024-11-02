from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import *
from .filters import*

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo, {user.username}!")
                return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(error)
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})   

@login_required
def logout_view(request):
    logout(request) 
    return redirect('login') 

@login_required
def home(request):
    paciente_filter = PacienteFilter(request.GET, queryset=Paciente.objects.all())
    count = paciente_filter.qs.count()

    paginator = Paginator(paciente_filter.qs, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)

    return render(request, 'home.html', {'page_obj': page_obj, 'filter': paciente_filter, 'count': count})

@login_required
def register_patients(request, id=None):
    patient = get_object_or_404(Paciente, pk=id) if id else None
    if request.method == "POST":
        form = RegisterPatientsForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(error)
    else:
        form = RegisterPatientsForm(instance=patient)

    return render(request, 'register_patients.html', {'form':form, 'patient':patient})


@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Paciente, pk=id)
    if patient:
        patient.delete()

    return redirect('home')    

@login_required
def assessment_list(request):
    assessment_filter = AvaliacaoFilter(request.GET, queryset=AvalicoesSaude.objects.all())
    
    count = assessment_filter.qs.count()


    paginator = Paginator(assessment_filter.qs, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)

    return render(request, 'list_assessment.html', {'page_obj': page_obj, 'filter': assessment_filter , 'count': count})

@login_required
def submit_assessment(request, id=None, patient_id=None):
    assessment = get_object_or_404(AvalicoesSaude, pk=id) if id else None
    patient = get_object_or_404(Paciente, pk=patient_id) if patient_id else None
    if request.method == "POST":
        form = SubmitAssessmentForm(request.POST, instance= assessment)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.user = request.user  
            assessment.paciente = patient
            assessment.save()
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(error)
    else:
        form = SubmitAssessmentForm(instance= assessment)

    return render(request, 'submit_assessment.html', {'form':form, 'patient': patient})                


@login_required
def delete_assessment(request, id):
    assessment = get_object_or_404(AvalicoesSaude, pk=id)
    if assessment:
        assessment.delete()
        
    return redirect('assessment_list')  