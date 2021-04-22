from django.db import models

Type = (
	 ('BATEAU', 'Bateau'),
	 ('AVION', 'Avion'),
	 ('CAMION', 'Camion'),
)

status = (
	 ('EN COURS', 'En Cours'),
	 ('LIVRER', 'Livrer'),

)

statusDepot = (
	 ('Active', 'active'),
	 ('No Active', 'no active'),

)
class Envoi(models.Model):
    reference = models.CharField(max_length=50, blank=False,primary_key=True)
    capaciter = models.DecimalField(max_digits=8, decimal_places=2)
    typeEnvoi = models.CharField(max_length=8, choices=Type, blank=False)
    lieuDepart = models.CharField(max_length=50, blank=False)
    lieuArriver = models.CharField(max_length=50, blank=False)
    dateDepart = models.DateField('Date_depart', blank=False)
    dateArriver = models.DateField('Date_arriver',blank=True,null=True)
    status = models.CharField(max_length=20, choices=status, blank=False)
    #nombreColis = models.PositiveIntegerField()
    #totalRecette = models.DecimalField(max_digits=8, decimal_places=2)
    #totalDepense = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return '{}'.format(self.reference)


class Client(models.Model):
	numeroClient = models.PositiveIntegerField(primary_key= True, blank=False)
	nomClient = models.CharField(max_length=250, blank=False)
	email = models.EmailField(max_length=50)
	numeroTel = models.CharField(max_length=50)
	numeroWhatsapp = models.CharField(max_length=50)


class Depot(models.Model):
	#numeroDepot = models.PositiveIntegerField(unique=True, blank=False)
	nomDepot = models.CharField(max_length=50, blank=False)
	lieu = models.CharField(max_length=50, blank=False)
	statusDp = models.CharField(max_length=20, choices=statusDepot, blank=False)
	adresse = models.CharField(max_length=100)
	#respo = models.CharField(max_length=80)


class Employer(models.Model):
	#numeroEmployer = models.PositiveIntegerField(unique=True)
	nomEmployer = models.CharField(max_length=250, blank=False)
	email = models.EmailField(max_length=50)
	numeroTel = models.CharField(max_length=50)
	numeroWhatsapp = models.CharField(max_length=50)
	depot = models.ForeignKey(Depot,on_delete=models.CASCADE)



class Coli(models.Model):
	qRCode = models.CharField(max_length=250,unique=True)
	nombrePiece = models.PositiveIntegerField()
	volume = models.DecimalField(max_digits=8, decimal_places=2)
	longueur = models.DecimalField(max_digits=8, decimal_places=2)
	largeur = models.DecimalField(max_digits=8, decimal_places=2)
	prixUnitaire = models.DecimalField(max_digits=8, decimal_places=2)
	prixTotal = models.DecimalField(max_digits=8, decimal_places=2)
	Tva = models.DecimalField(max_digits=8, decimal_places=2)
	status = models.CharField(max_length=20, choices=status)
	envoi = models.ForeignKey(Envoi,on_delete=models.CASCADE)
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
#	employer = models.ForeignKey(Employer,on_delete=models.CASCADE)
	depot = models.ForeignKey(Depot,on_delete=models.CASCADE)








# Create your models here.
