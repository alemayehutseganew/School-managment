from django.shortcuts import render, redirect
from . import forms
from .models import District
from .forms import *
from .models import *


# Create your views here.


def teacher_registration(request):
    form = PersonalInfoForm()
    address_forms = AddressInfoForm()
    education_form = EducationInfoForm()
    training_form = TrainingInfoForm()
    job_form = JobInfoForm()
    experience_form = ExperienceInfoForm()
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        address_form = AddressInfoForm(request.POST)
        education_form = EducationInfoForm(request.POST)
        training_form = TrainingInfoForm(request.POST)
        job_form = JobInfoForm(request.POST)
        experience_form = ExperienceInfoForm(request.POST)
        if form.is_valid() and address_form.is_valid() and education_form.is_valid() and training_form.is_valid() and job_form.is_valid() and experience_form.is_valid():
            address_info = address_form.save()
            education_info = education_form.save()
            training_info = training_form.save()
            job_info = job_form.save()
            experience_info = experience_form.save()
            personal_info = form.save(commit=False)
            personal_info.address = address_info
            personal_info.education = education_info
            personal_info.training = training_info
            personal_info.job = job_info
            personal_info.experience = experience_info
            personal_info.save()
            return redirect('teacher-list')

    context = {
        'form': form,
        'address_forms': address_forms,
        'education_form': education_form,
        'training_form': training_form,
        'job_form': job_form,
        'experience_form': experience_form
    }
    return render(request, 'teacher/teacher-registration.html', context)


def teacher_list(request):
    teacher = PersonalInfo.objects.filter(is_delete=False)
    context = {'teacher': teacher}
    return render(request, 'teacher/teacher-list.html', context)


def teacher_profile(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher/teacher-profile.html', context)


def teacher_delete(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    teacher.is_delete = True
    teacher.save()
    return redirect('teacher-list')


def teacher_edit(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    form = PersonalInfoForm(instance=teacher)
    address_forms = AddressInfoForm(instance=teacher.address)
    education_form = EducationInfoForm(instance=teacher.education)
    training_form = TrainingInfoForm(instance=teacher.training)
    job_form = JobInfoForm(instance=teacher.job)
    experience_form = ExperienceInfoForm(instance=teacher.experience)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=teacher)
        address_form = AddressInfoForm(request.POST, instance=teacher.address)
        education_form = EducationInfoForm(request.POST, instance=teacher.education)
        training_form = TrainingInfoForm(request.POST, instance=teacher.training)
        job_form = JobInfoForm(request.POST, instance=teacher.job)
        experience_form = ExperienceInfoForm(request.POST, instance=teacher.experience)
        if form.is_valid() and address_form.is_valid() and education_form.is_valid() and training_form.is_valid() and job_form.is_valid() and experience_form.is_valid():
            address_info = address_form.save()
            education_info = education_form.save()
            training_info = training_form.save()
            job_info = job_form.save()
            experience_info = experience_form.save()
            personal_info = form.save(commit=False)
            personal_info.address = address_info
            personal_info.education = education_info
            personal_info.training = training_info
            personal_info.job = job_info
            personal_info.experience = experience_info
            personal_info.save()
            return redirect('teacher-list')
    context = {
        'form': form,
        'address_form': address_forms,
        'education_form': education_form,
        'training_form': training_form,
        'job_form': job_form,
        'experience_form': experience_form
    }
    return render(request, 'teacher/teacher-edit.html', context)
