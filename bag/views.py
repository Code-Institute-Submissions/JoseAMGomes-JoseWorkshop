from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(1)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_bag(request, item_id):
    """Remove the item from the shopping bag"""
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag.pop(item_id)
       
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
