from django.shortcuts import render, redirect
from django.views import View
from django.db import transaction
# from django.http import HttpResponse
from .models import Job_Information, File_Ref_No, Client, Cargo_Type, Cargo_Classification, From_Location, To_Location, Route, Supplier_Information, Loose_Cargo_Information, Container_Details, JobFile
from .forms import Job_InformationForm, Supplier_InformationForm, Loose_Cargo_InformationForm, Container_DetailsForm,File_Ref_NoForm, ClientForm, Cargo_TypeForm, Cargo_ClassificationForm, From_LocationForm, To_LocationForm, RouteForm

# Create your views here.
def home(request):
    return render(request, 'erp/home/index.html')

class CreateJobFileView(View):
    template_name = 'erp/user_operations/contract/job_information.html'

    def get_forms(self, job_file=None):
        return {
            'job_information': Job_InformationForm(prefix='job', instance=getattr(job_file, 'job_information', None)),
            'supplier_information': Supplier_InformationForm(prefix='supplier', instance=getattr(job_file, 'supplier_information', None)),
            'loose_cargo_information': Loose_Cargo_InformationForm(prefix='loose', instance=getattr(job_file, 'loose_cargo_information', None)),
            'container_details': Container_DetailsForm(prefix='container', instance=getattr(job_file, 'container_details', None)),
            # Including my modal forms
            'route_form':RouteForm(),
            'from_location_form':From_LocationForm(),
            'to_location_form':To_LocationForm(),
            'cargo_classification_form':Cargo_ClassificationForm(),
            'cargo_type_form':Cargo_TypeForm(),
            'client_form':ClientForm(),
        }
    
    def get(self, request, file_id=None):
        if file_id:
            job_file = JobFile.objects.get(file_id=file_id)
            forms = self.get_forms(job_file)
        else:
            forms = self.get_forms()
        return render(request, self.template_name, {'forms': forms})
    
    @transaction.atomic
    def post(self, request, file_id=None):
        if file_id:
            job_file = JobFile.objects.get(file_id=file_id)
        else:
            job_file = JobFile.objects.create()
        forms = {
            'job_information': Job_InformationForm(request.POST, prefix='job', instance=getattr(job_file, 'job_information', None)),
            'supplier_information': Supplier_InformationForm(request.POST, prefix='supplier', instance=getattr(job_file, 'supplier_information', None)),
            'loose_cargo_information': Loose_Cargo_InformationForm(request.POST, prefix='loose', instance=getattr(job_file, 'loose_cargo_information', None)),
            'container_details': Container_DetailsForm(request.POST, prefix='container', instance=getattr(job_file, 'container_details', None)),
        }

        if all([form.is_valid() for form in forms.values()]):
            for form in forms.values():
                instance = form.save(commit=False)
                instance.job_file = job_file
                instance.save()
            return redirect('job_file_detail', file_id=job_file.file_id)
        return render(request, self.template_name, {'forms': forms})

def file_ref_no(request):
    if request.method == 'POST':
        form = File_Ref_NoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('file_ref_no')
    else:
        form = File_Ref_NoForm()

    filerefno = File_Ref_No.objects.all()
    context = {'form': form, 'filerefno': filerefno}
    return render(request, 'erp/user_operations/master/file_ref_no.html', context=context)

def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        form = ClientForm()

    client = Client.objects.all()
    context = {'form': form, 'client': client}
    return render(request, 'erp/user_operations/master/client.html', context=context)

def cargo_type(request):
    if request.method == 'POST':
        form = Cargo_TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_type')
    else:
        form = Cargo_TypeForm()

    cargo_type = Cargo_Type.objects.all()
    context = {'form': form, 'cargo_type': cargo_type}
    return render(request, 'erp/user_operations/master/cargo_type.html', context=context)

def cargo_classification(request):
    if request.method == 'POST':
        form = Cargo_ClassificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_classification')
    else:
        form = Cargo_ClassificationForm()

    cargo_classification = Cargo_Classification.objects.all()
    context = {'form': form, 'cargo_classification': cargo_classification}
    return render(request, 'erp/user_operations/master/cargo_classification.html', context=context)

def from_location(request):
    if request.method == 'POST':
        form = From_LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('from_location')
    else:
        form = From_LocationForm()

    from_location = From_Location.objects.all()
    context = {'form': form, 'from_location': from_location}
    return render(request, 'erp/user_operations/master/from_location.html', context=context)

def to_location(request):
    if request.method == 'POST':
        form = To_LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('to_location')
    else:
        form = To_LocationForm()

    to_location = To_Location.objects.all()
    context = {'form': form, 'to_location': to_location}
    return render(request, 'erp/user_operations/master/to_location.html', context=context)

def route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route')
    else:
        form = RouteForm()

    route = Route.objects.all()
    context = {'form': form, 'route': route}
    return render(request, 'erp/user_operations/master/route.html', context=context)

# Create a view to for the dashboard in the user_operations folder, to didplay the contents of the html file
def operations_dashboard(request):
    return render(request, 'erp/user_operations/dashboard.html')
