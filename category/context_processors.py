from .models import Category


def menu_links(request):
    all_cat = Category.objects.all()
    return dict(links=all_cat)
