from django.db import models

# Create your models here.

# The Route model
class Route(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The From Location model
class From_Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# The To Location model
class To_Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# The Cargo Classification model
class Cargo_Classification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Cargo Type model
class Cargo_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# The Client model
class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# The File Ref No model (This is auto filed by the lot no)
class File_Ref_No(models.Model):
    lot_no = models.CharField(max_length=100)

    def __str__(self):
        return self.lot_no


# <----------------------- XXXXXXXXXXX -------------------------->
# Create a model named "job_information" with the following fields:
# Payment After, Bill on, Contract Type, Contract Date, Job No, Route,
# From, To, Weight, Cargo Classification, Cargo Type, Cargo Job Description,
# Client, Head of Contarct, Loading Point, Lot No, Offloading Point.
class Job_Information(models.Model):
    #Payment After should be int.
    payment_after = models.IntegerField()
    #Bill on should be date.
    bill_on = models.DateField()
    #Contract Type should be char.
    contract_type = models.CharField(max_length=100)
    #Contract Date should be date.
    contract_date = models.DateField()
    # Job No is an auto generated field.
    job_no = models.AutoField(primary_key=True)

    # Foreign Key Relationships
    #Route should be char.
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    #From should be char.
    from_location = models.ForeignKey(From_Location, on_delete=models.CASCADE)
    #To should be char.
    to_location = models.ForeignKey(To_Location, on_delete=models.CASCADE)


    #Weight should be int.
    weight = models.IntegerField()

    # Foreign Key Relationships
    #Cargo Classification should be char.
    cargo_classification = models.ForeignKey(Cargo_Classification, on_delete=models.CASCADE)
    #Cargo Type should be char.
    cargo_type = models.ForeignKey(Cargo_Type, on_delete=models.CASCADE)
    
        
    #Cargo Job Description should be char.
    cargo_job_description = models.CharField(max_length=100)

    # Foreign Key Relationships
    #Client should be char.
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


    #Head of Contarct should be char.
    head_of_contract = models.CharField(max_length=100)
    #Loading Point should be char.
    loading_point = models.CharField(max_length=100)


    # Foreign Key Relationships
    #Lot No should be char.
    lot_no = models.ForeignKey(File_Ref_No, on_delete=models.CASCADE)


    #Offloading Point should be char.
    offloading_point = models.CharField(max_length=100)

# <----------------------- XXXXXXXXXXX -------------------------->
# We are creating a model named Supplier Information with the following fields:
# File Ref No, Consignor, Consignee
class Supplier_Information(models.Model):
    # File Ref No should be char.
    file_ref_no = models.CharField(max_length=100)
    # Consignor should be char.
    consignor = models.CharField(max_length=100)
    # Consignee should be char.
    consignee = models.CharField(max_length=100)

# <----------------------- XXXXXXXXXXX -------------------------->
# We are creating a model named Loose Cargo Information with the following fields:
# Cargo Classification, Make, Chasis No, Truck Planned, Model, MTN, Engine No, Commodity, No. of Packages, Invoice No.
class Loose_Cargo_Information(models.Model):
    # Cargo Classification should be char.
    cargo_classification = models.CharField(max_length=100)
    # Make should be char.
    make = models.CharField(max_length=100)
    # Chasis No should be char.
    chasis_no = models.CharField(max_length=100)
    # Truck Planned should be char.
    truck_planned = models.CharField(max_length=100)
    # Model should be char.
    model = models.CharField(max_length=100)
    # MTN should be int.
    mtn = models.IntegerField()
    # Engine No should be char.
    engine_no = models.CharField(max_length=100)
    # Commodity should be char.
    commodity = models.CharField(max_length=100)
    # No. of Packages should be int.
    no_of_packages = models.IntegerField()
    # Invoice No should be char.
    invoice_no = models.CharField(max_length=100)

# <----------------------- XXXXXXXXXXX -------------------------->
# We are creating a model named Container Details with the following fields:
# Container Type, Container No, Truck Planned, MTN, Commodity, No. of Packages, Seal No., Invoice No.
class Container_Details(models.Model):
    # Container Type should be char.        
    container_type = models.CharField(max_length=100)
    # Container No should be char.
    container_no = models.CharField(max_length=100)
    # Truck Planned should be char.        
    truck_planned = models.CharField(max_length=100)
    # MTN should be int.
    mtn = models.IntegerField()
    # Commodity should be char.
    commodity = models.CharField(max_length=100)
    # No. of Packages should be int.
    no_of_packages = models.IntegerField()
    # Seal No. should be char.
    seal_no = models.CharField(max_length=100)
    # Invoice No should be char.
    invoice_no = models.CharField(max_length=100)
