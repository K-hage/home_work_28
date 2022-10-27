from .delete import AdDeleteView
from .create import AdCreateView
from .update import AdUpdateView
from .upload import AdUploadImage
from .view import AdListView, AdDetailView

__all__ = [
    'AdUploadImage',
    'AdDetailView',
    'AdListView',
    'AdCreateView',
    'AdUpdateView',
    'AdDeleteView'
]
