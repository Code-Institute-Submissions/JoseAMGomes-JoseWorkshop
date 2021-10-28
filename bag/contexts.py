from django.conf import settings
from django.shortcuts import get_object_or_404
from projects.models import Project

def bag_contents(request):

    bag_items = []
    grand_total = 0
    project_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        project = get_object_or_404(Project, pk=item_id)
        grand_total += quantity * project.price
        project_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'project': project,
        })
    
    context = {
        'bag_items': bag_items,
        'project_count': project_count,
        'grand_total': grand_total,
    }

    return context