import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from .models import Job_Information, Client, Cargo_Type, Cargo_Classification, From_Location, To_Location, Route, Supplier_Information, Loose_Cargo_Information, Container_Details, JobFile
from .forms import Job_InformationForm, Supplier_InformationForm, Loose_Cargo_InformationForm, Container_DetailsForm, ClientForm, Cargo_TypeForm, Cargo_ClassificationForm, From_LocationForm, To_LocationForm, RouteForm

# Create your views here.
def home(request):
    return render(request, 'erp/home/index.html')

# Creating a View to handle the AJAX request for generating job file number.
logger = logging.getLogger(__name__)
@method_decorator(csrf_exempt, name='dispatch')
class GenerateJobFileNumberView(View):
    def post(self, request, file_id):
        try:
            job_file = get_object_or_404(JobFile, file_id=file_id)
            job_file.generate_job_file_number()
            return JsonResponse({'success': True, 'job_file_number': job_file.job_file_number})
        except Exception as e:
            logger.exception(f"Error generating job file number: {str(e)}")
            return JsonResponse({'success': False, 'error': 'Failed to generate job file number'}, status=500)



class CreateJobFileView(View):
    template_name = 'erp/user_operations/contract/job_information.html'

    def get_forms(self, job_file=None, post_data=None):
        kwargs = {'prefix': 'job'}
        if post_data:
            kwargs['data'] = post_data
        if job_file:
            kwargs['instance'] = getattr(job_file, 'job_information', None)
        return {
            'job_information': Job_InformationForm(**kwargs),
            'supplier_information': Supplier_InformationForm(data=post_data if post_data else None, prefix='supplier', instance=getattr(job_file, 'supplier_information', None)),
            'loose_cargo_information': Loose_Cargo_InformationForm(data=post_data if post_data else None, prefix='loose', instance=getattr(job_file, 'loose_cargo_information', None)),
            'container_details': Container_DetailsForm(data=post_data if post_data else None, prefix='container', instance=getattr(job_file, 'container_details', None)),
            # Including my modal forms
            'route_form':RouteForm(),
            'from_location_form':From_LocationForm(),
            'to_location_form':To_LocationForm(),
            'cargo_classification_form':Cargo_ClassificationForm(),
            'cargo_type_form':Cargo_TypeForm(),
            'client_form':ClientForm(),
        }
    
    def get(self, request, file_id=None):
        try:
            if file_id:
                job_file = get_object_or_404(JobFile, file_id=file_id)
            else:
                job_file = JobFile.objects.create()

            forms = self.get_forms(job_file)
            return render(request, self.template_name, {'forms': forms, 'job_file': job_file})
        except Exception as e:
            logger.error(f"Error in get request: {str(e)}")
            return JsonResponse({'success': False, 'error': 'Failed to load job file form'}, status=500)
    
    
    @transaction.atomic
    def post(self, request, file_id=None):
        try:
            if file_id:
                job_file = get_object_or_404(JobFile, file_id=file_id)
            else:
                job_file = JobFile.objects.create()

            # Handle job file number generation
            if request.POST.get('generate_job_file_number'):
                job_file.generate_job_file_number()
                return JsonResponse({'success': True, 'job_file_number': job_file.job_file_number})
            
            # Process form submission
            forms = self.get_forms(job_file, request.POST)

            if all(form.is_valid() for form in forms.values()):
                try:
                    with transaction.atomic():
                        for form in forms.values():
                            if hasattr(form, 'save'): # Check if the form has a save method
                                instance = form.save(commit=False)
                                instance.job_file = job_file
                                instance.save()
                                form.save_m2m() # Save many-to-many fields related to the instance

                    return JsonResponse({
                        'success': True,
                        'message': 'Job file saved successfully',
                        'redirect_url': reverse('job_file', kwargs={'file_id': job_file.file_id})
                    })
                except Exception as e:
                    logger.error(f"Error saving forms: {str(e)}")
                    raise ValidationError('Failed to save form data')
            else:
                # Collect all form errors
                errors = {}
                for form_name, form in forms.items():
                    if form.errors:
                        errors[form_name] = {
                            field: [str(error) for error in field_errors]
                            for field, field_errors in form.errors.items()
                        }
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            
        except ValidationError as e:
            return JsonResponse({'success': False, 'errors': str(e)}, status=400)
        except Exception as e:
            logger.error(f"Unexpected Error in form submission: {str(e)}")
            return JsonResponse({'success': False, 'errors': 'An unexpected error occured, please try again later'}, status=500)


        
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
