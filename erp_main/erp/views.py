from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job_Information, File_Ref_No, Client, Cargo_Type, Cargo_Classification, From_Location, To_Location, Route, Supplier_Information, Loose_Cargo_Information, Container_Details
from .forms import Job_InformationForm, Supplier_InformationForm, Loose_Cargo_InformationForm, Container_DetailsForm,File_Ref_NoForm, ClientForm, Cargo_TypeForm, Cargo_ClassificationForm, From_LocationForm, To_LocationForm, RouteForm

# Create your views here.
def home(request):
    return render(request, 'erp/home/index.html')

# We are creating a view called job_information, that will use the job_information.html template, to display the information in the job_information model.
def job_information(request):
    if request.method == 'POST':
        form = Job_InformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_information')
    else:
        form = Job_InformationForm()

    # Create forms for modals
    route_form = RouteForm()
    from_location_form = From_LocationForm()
    to_location_form = To_LocationForm()
    cargo_classification_form = Cargo_ClassificationForm()
    cargo_type_form = Cargo_TypeForm()
    client_form = ClientForm()
    
    # jobinfo = Job_Information.objects.all()
    context = {'form': form,
               'route_form': route_form,
               'from_location_form': from_location_form,
               'to_location_form': to_location_form,
               'cargo_classification_form': cargo_classification_form,
               'cargo_type_form': cargo_type_form,
               'client_form': client_form,
               'supplier_information_form': Supplier_InformationForm,
               'loose_cargo_Information_form': Loose_Cargo_InformationForm,
               'container_details_form': Container_DetailsForm
    
               }
    return render(request, 'erp/user_operations/contract/job_information.html', context=context)


# view for the supplier_information view.
def supplier_information(request):
    if request.method == 'POST':
        form = Supplier_InformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_information')
    else:
        form = Supplier_InformationForm()

    supplier_information = Supplier_Information.objects.all()
    context = {'form': form, 'supplier_information': supplier_information}
    return render(request, 'erp/user_operations/master/supplier_information.html', context=context)

# view for loose_cargo_information view.
def loose_cargo_information(request):
    if request.method == 'POST':
        form = Loose_Cargo_InformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loose_cargo_information')
    else:
        form = Loose_Cargo_InformationForm()

    loose_cargo_information = Loose_Cargo_Information.objects.all()
    context = {'form': form, 'loose_cargo_information': loose_cargo_information}
    return render(request, 'erp/user_operations/master/loose_cargo_information.html', context=context)

# view for container_details view.
def container_details(request):
    if request.method == 'POST':
        form = Container_DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('container_details')
    else:
        form = Container_DetailsForm()

    container_details = Container_Details.objects.all()
    context = {'form': form, 'container_details': container_details}
    return render(request, 'erp/user_operations/master/container_details.html', context=context)


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
