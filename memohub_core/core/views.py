# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
#Importation des modèles...
from .models import Track, Supervisor, Memories, Backup, StatisticsConsultation, KeyWord
# Importation des serializers
from .serializers import (
    TrackSerializer, SupervisorSerializer, 
    MemoriesSerializer, KeyWordSerializer, StatisticsConsultationSerializer
)
# Gestion des vues pour les tracks/filières
"""GET TRACKS"""
@api_view(['GET'])
def get_track(request):
    # Récupère les données depuis la base de données
    tracks = Track.objects.all()
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


"""GET ID TRACKS"""
@api_view(['GET'])
def get_track_by_id(request, track_id):
    try:
        # Récupère les données depuis la base de données
        track = Track.objects.get(id=track_id)
    except Track.DoesNotExist:
        return Response(
            {"error": "Track not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Supprimez many=True car vous sérialisez un seul objet
    serializer = TrackSerializer(track)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""POST/CREATE TRACKS"""
@api_view(['POST'])
def create_track(request):
    serializer = TrackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""UPDATE TRACKS"""
@api_view(['PATCH'])
def update_track(request, track_id):
    try:
        # Récupère les données depuis la base de données
        track = Track.objects.get(id=track_id)
    except Track.DoesNotExist:
        return Response(
            {"error": "Track not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = TrackSerializer(track,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  # Sauvegarde les modifications
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Gestion des vues pour les supervisors/encadreurs
"""GET SUPERVISORS"""
@api_view(['GET'])
def get_supervisor(request):
    # Récupère les données depuis la base de données
    supervisors = Supervisor.objects.all()
    serializer = SupervisorSerializer(supervisors, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

"""GET ID SUPERVISORS"""
@api_view(['GET'])
def get_supervisor_by_id(request, supervisor_id):
    try:
        # Récupère les données depuis la base de données
        supervisor = Supervisor.objects.get(id=supervisor_id)
    except Supervisor.DoesNotExist:
        return Response(
            {"error": "Supervisor not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Supprimez many=True car vous sérialisez un seul objet
    serializer = SupervisorSerializer(supervisor)
    return Response(serializer.data, status=status.HTTP_200_OK)

"""POST/CREATE SUPERVISORS"""
@api_view(['POST'])
def create_supervisor(request):
    serializer = SupervisorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""UPDATE/PATCH SUPERVISORS"""
@api_view(['PATCH'])
def update_supervisor(request, supervisor_id):
    try:
        # Récupère les données depuis la base de données
        supervisor = Supervisor.objects.get(id=supervisor_id)
    except Supervisor.DoesNotExist:
        return Response(
            {"error": "Supervisor not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Supprimez many=True car vous sérialisez un seul objet
    serializer = SupervisorSerializer(supervisor,data=request.data, partial=True)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""DELETE SUPERVISORS"""
@api_view(['DELETE'])
def delete_supervisor(request, supervisor_id):
    try:
        # Récupère les données depuis la base de données
        supervisor = Supervisor.objects.get(id=supervisor_id)
    except Supervisor.DoesNotExist:
        return Response(
            {"error": "Supervisor not found"},
            status=status.HTTP_404_NOT_FOUND
        )
        
    supervisor.delete()
    return Response(
            {"success": "Supervisor has successfuly deleted"},
            status=status.HTTP_202_ACCEPTED
        )

# Gestion des vues pour les memories/mémoires
"""GET MEMORIES"""
@api_view(['GET'])
def get_memories(request):
    # Récupère les données depuis la base de données
    memories = Memories.objects.all()
    serializer = MemoriesSerializer(memories, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

"""GET ID MEMORIES"""
@api_view(['GET'])
def get_memory_by_id(request, memory_id):
    try:
        # Récupère les données depuis la base de données
        memory = Memories.objects.get(id=memory_id)
    except Memories.DoesNotExist:
        return Response(
            {"error": "Memory not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Supprimez many=True car vous sérialisez un seul objet
    serializer = MemoriesSerializer(memory)
    return Response(serializer.data, status=status.HTTP_200_OK)

"""POST/CREATE MEMORIES"""
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_memory(request):
    serializer = MemoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""DELETE MEMORIES"""
@api_view(['DELETE'])
def delete_memory(request, memory_id):
    try:
        # Récupère les données depuis la base de données
        memory = Memories.objects.get(id=memory_id)
    except Memories.DoesNotExist:
        return Response(
            {"error": "Memory not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    memory.delete()
    return Response(
            {"success": "Memory has successfuly deleted"},
            status=status.HTTP_202_ACCEPTED
        )

# Gestion des vues pour les mots clés/keywords
"""GET KEYWORDS"""
@api_view(['GET'])
def get_keywords(request):
    # Récupère les données depuis la base de données
    keywords = KeyWord.objects.all()
    serializer = KeyWordSerializer(keywords, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

"""POST/CREATE KEYWORDS"""
@api_view(['POST'])
def create_keyword(request):
    serializer = KeyWordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
