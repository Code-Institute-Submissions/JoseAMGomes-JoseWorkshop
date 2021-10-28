from django.conf import settings
from django.shortcuts import get_object_or_404
from projects.models import Project

def bag_contents(request):

    bag_items = []
    total = 0
    project_count = 0
    bag = request.session.get('bag', {})

    for item_id in bag.items():
        project = get_object_or_404(Project, pk=item_id)
        total += project.price
        project_count += 1
        bag_items.append({
            'item_id': item_id,
            'project': project,
        })


    
    context = {
        'bag_items': bag_items,
        'total': total,
        'project_count': project_count,
    }

    return context