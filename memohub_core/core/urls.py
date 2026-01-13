from django.urls import path
from core.views import  get_track, create_track, get_track_by_id, update_track
from core.views import  get_supervisor, get_supervisor_by_id, create_supervisor, update_supervisor, delete_supervisor
from core.views import  get_memories, get_memory_by_id, create_memory, delete_memory
from core.views import  get_keywords, create_keyword

urlpatterns = [
    # PATH POUR LES FILIERES...
    path('tracks/', get_track, name="get-track"),
    path('tracks/<int:track_id>/', get_track_by_id, name="get-track-by-id"),
    path('tracks/create', create_track, name="create-track"),
    path('tracks/update/<int:track_id>/', update_track, name="update-track"),
    # PATH POUR LES ENCADREURS...
    path('supervisors/',get_supervisor, name="get-supervisor"),
    path('supervisors/<int:supervisor_id>/',get_supervisor_by_id, name="get-supervisor-by-id"),
    path('supervisors/create', create_supervisor, name="create-supervisor"),
    path('supervisors/update/<int:supervisor_id>/',update_supervisor, name="update-supervisor"),
    path('supervisors/delete/<int:supervisor_id>/',delete_supervisor, name="delete-supervisor"),
    # PATH POUR LES MEMOIRES
    path('memories/', get_memories, name="get-memories"),
    path('memories/<int:memory_id>/', get_memory_by_id, name="get-memories-by-id"),
    path('memories/create', create_memory, name="create-memory"),
    path('memories/delete/<int:memory_id>/',delete_memory, name="delete-memory"),
    # PATH POUR LES MOTS CLÉS
    path('keywords/', get_keywords, name="get-keywords"),
    path('keywords/create', create_keyword, name="create-keyword"),
    
]
