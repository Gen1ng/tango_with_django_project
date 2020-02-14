from django import template
from rango.models import Category

register = template.Library()

def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}