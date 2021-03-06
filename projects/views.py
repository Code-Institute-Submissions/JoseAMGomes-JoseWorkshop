from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_projects(request):
    """ A view to show all projects, including sorting and search queries """

    projects = Project.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                projects = projects.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            projects = projects.order_by(sortkey)



    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('projects'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            projects = projects.filter(queries)


    current_sorting = f'{sort}_{direction}'

    context = {
        'projects': projects,
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'projects/projects.html', context)


def project_detail(request, project_id):
    """ A view to show individual project details """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'projects/project_detail.html', context)

@login_required
def add_project(request):
    """ Add a project """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Successfully added project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to add project. Please ensure the form is valid.')
    else:
        form = ProjectForm()
        
    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_project(request, project_id):
    """ Edit a project """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to update project. Please ensure the form is valid.')
    else:
        form = ProjectForm(instance=project)
        messages.info(request, f'Currently editing {project.name}')

    template = 'projects/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)

@login_required
def delete_project(request, project_id):
    """ Delete a project"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('projects'))