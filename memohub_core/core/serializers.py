from rest_framework import serializers
from .models import Track, Supervisor, KeyWord, Memories, StatisticsConsultation

class TrackSerializer(serializers.ModelSerializer):
    memos = serializers.IntegerField(source='nb_memos', read_only=True)
    encadreurs = serializers.IntegerField(source='nb_encadreurs', read_only=True)
    derniereAnnee = serializers.IntegerField(source='derniere_annee', read_only=True)
    
    class Meta:
        model = Track
        fields = '__all__'

class SupervisorSerializer(serializers.ModelSerializer):
    nom_specialite = serializers.CharField(source='specialite.nom', read_only=True)
    memos = serializers.IntegerField(source='nb_memos',read_only=True)
    class Meta:
        model = Supervisor
        fields = ['id', 'nom', 'specialite','nom_specialite', 'avatar', 'depuis','memos', 'description']

class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = '__all__'

class MemoriesSerializer(serializers.ModelSerializer):
    nom_filiere = serializers.CharField(source='filiere.nom', read_only=True)
    nom_encadreur = serializers.CharField(source='encadreur.nom', read_only=True)
    taille = serializers.CharField(source='taille_fichier', read_only=True)
    motsCles_list = serializers.SlugRelatedField(many=True, read_only=True,slug_field='mot', source='motsCles')
    
    class Meta:
        model = Memories
        fields = [
            'id', 'titre', 'auteur', 'encadreur', 'nom_encadreur',
            'filiere', 'nom_filiere', 'annee', 'fichier','fichier_pdf', 
            'taille', 'motsCles', 'motsCles_list',
            'date_ajout', 'date_modification'
        ]

class StatisticsConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsConsultation
        fields = '__all__'