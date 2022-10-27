from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from ads.models import Category


class CatListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cat_qs = self.object_list.order_by('name')

        categories = cat_qs.all()

        item_list = [
            {
                "id": cat.pk,
                "name": cat.name,
            }
            for cat in categories]

        return JsonResponse(item_list, safe=False)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse(
            {
                'id': cat.pk,
                "name": cat.name,
            },
            safe=False)
