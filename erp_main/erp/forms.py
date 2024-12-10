 # We will now use all the fields in the Job_Information model, in models.py        
from django import forms
from .models import Job_Information, File_Ref_No, Client, Cargo_Type, Cargo_Classification, From_Location, To_Location, Route
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit, Row

class Job_InformationForm(forms.ModelForm):
    class Meta:
        model = Job_Information
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Job_InformationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-job_information_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'job_information'
        self.helper.layout = Layout(
            Row(
                Field('payment_after', css_class='form-group col-md-6 mb-0'),
                Field('bill_on', css_class='form-group col-md-6 mb-0', widget=forms.DateInput(attrs={'type': 'date'})),
            ),
            Row(
                Field('contract_type', css_class='form-group col-md-6 mb-0'),
                Field('contract_date', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('client', css_class='form-group col-md-6 mb-0'),
                Field('head_of_contract', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('consignor', css_class='form-group col-md-6 mb-0'),
                Field('consignee', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('cargo_classification', css_class='form-group col-md-6 mb-0'),
                Field('cargo_type', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('cargo_job_description', css_class='form-group col-md-6 mb-0'),
                Field('weight', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('from_location', css_class='form-group col-md-6 mb-0'),
                Field('to_location', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('route', css_class='form-group col-md-6 mb-0'),
                Field('job_no', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Field('loading_point', css_class='form-group col-md-6 mb-0'),
                Field('offloading_point', css_class='form-group col-md-6 mb-0'),
            ),
            Field('lot_no'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary'),
            )
        )



class File_Ref_NoForm(forms.ModelForm):
    class Meta:
        model = File_Ref_No
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class Cargo_TypeForm(forms.ModelForm):    
    class Meta:
        model = Cargo_Type
        fields = '__all__'

class Cargo_ClassificationForm(forms.ModelForm):
    class Meta:
        model = Cargo_Classification
        fields = '__all__'

class From_LocationForm(forms.ModelForm):
    class Meta:
        model = From_Location
        fields = '__all__'

class To_LocationForm(forms.ModelForm):
    class Meta:
        model = To_Location
        fields = '__all__'

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'