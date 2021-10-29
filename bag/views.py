from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from projects.models import Project

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    project = Project.objects.get(pk=item_id)
    
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[item_id] = 1
    messages.success(request, f'Added {project.name} to your bag')


    request.session['bag'] = bag
    return redirect(reverse('projects'))


def remove_bag(request, item_id):
    """Remove the item from the shopping bag"""
    project = Project.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, f'Removed {project.name} from your bag')   
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
    try:
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {project.name} from your bag')
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(request, f'Error found! {e} ')
        return HttpResponse(status=500)