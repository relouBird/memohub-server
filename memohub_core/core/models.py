import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Track(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=512)
    icon = models.CharField(max_length=50, default='fas fa-book')
    def __str__(self):
        return self.nom
    @property
    def nb_memos(self):
        # Si tu as défini related_name='memoires' dans le champ filiere de Memories
        return self.memoires.count()
    @property
    def nb_encadreurs(self):
        # Si tu as défini related_name='encadreurs' dans le champ specialite de Supervisor
        return self.encadreurs.count()
    @property
    def derniere_annee(self):
        dernier = self.memoires.order_by('-annee').first()
        return dernier.annee if dernier else 2025

class Supervisor(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True, related_name='encadreurs')
    avatar = models.CharField(max_length=10, blank=True, null=True)
    depuis = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    description = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.nom
    
    @property
    def nb_memos(self):
        return self.supervisor_memories.count()
    

class KeyWord(models.Model):
    mot = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.mot
    

class Memories(models.Model):
    titre = models.CharField(max_length=300)
    auteur = models.CharField(max_length=100)
    encadreur = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, related_name='supervisor_memories')
    filiere = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True, related_name='memoires')
    annee = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)]
    )
    fichier_pdf = models.FileField(upload_to='', null=True)
    fichier = models.CharField(max_length=256,null=True)
    taille_fichier = models.CharField(max_length=20, blank=True)  # Ex: "3.2 MB"
    motsCles = models.ManyToManyField(KeyWord, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-annee', 'titre']
        verbose_name = "Mémoire"
        verbose_name_plural = "Mémoires"
    
    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        # Calcul automatique de la taille si non spécifiée
        if self.fichier_pdf and not self.taille_fichier:
            size = self.fichier_pdf.size
            if size < 1024*1024:  # Moins d'1 MB
                self.taille_fichier = f"{size/1024:.1f} KB"
            else:
                self.taille_fichier = f"{size/(1024*1024):.1f} MB"
        else:
            self.taille_fichier = "0 KB"
        self.fichier = self.fichier_pdf.name if self.fichier_pdf else ""
        super().save(*args, **kwargs)
    

class Backup(models.Model):
    nom_fichier = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='backups/')
    date_creation = models.DateTimeField(auto_now_add=True)
    taille = models.CharField(max_length=20, blank=True)
    reussi = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date_creation']
    
    def __str__(self):
        return self.nom_fichier


class StatisticsConsultation(models.Model):
    memoire = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='consultations')
    date_consultation = models.DateTimeField(auto_now_add=True)
    # Tu pourrais ajouter : utilisateur, durée, etc.
    
    class Meta:
        ordering = ['-date_consultation']


# Ce "receiver" s'exécute automatiquement après la suppression d'une instance
@receiver(post_delete, sender=Memories)
def suppression_fichier_pdf(sender, instance, **kwargs):
    if instance.fichier_pdf:
        if os.path.isfile(instance.fichier_pdf.path):
            os.remove(instance.fichier_pdf.path)