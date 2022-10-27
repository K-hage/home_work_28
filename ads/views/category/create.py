import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from ads.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Category
    fields = [
        'name',
    ]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        cat = Category.objects.create(
            name=data['name'],
        )

        return JsonResponse({
            'id': cat.pk,
            "name": cat.name,
        }, status=201, safe=False)
