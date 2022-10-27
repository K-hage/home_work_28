from .create import CatCreateView
from .delete import CatDeleteView
from .update import CatUpdateView
from .view import CatListView, CatDetailView

__all__ = [
    'CatDetailView',
    'CatListView',
    'CatUpdateView',
    'CatDeleteView',
    'CatCreateView'
]