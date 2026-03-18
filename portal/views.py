from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q, Sum
from .models import Resource, Category
from .forms import RegisterForm


# =========================
# REGISTER
# =========================
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'portal/register.html', {'form': form})


# =========================
# DASHBOARD
# =========================
@login_required
def dashboard(request):

    categories = Category.objects.all()

    # =========================
    # TEACHER DASHBOARD
    # =========================
    if request.user.profile.role == 'teacher':

        # Upload resource
        if request.method == "POST":

            title = request.POST.get('title')
            description = request.POST.get('description')
            category_id = request.POST.get('category')
            file = request.FILES.get('file')

            if title and file and category_id:
                Resource.objects.create(
                    title=title,
                    description=description,
                    category_id=category_id,
                    file=file,
                    uploaded_by=request.user
                )

            return redirect('dashboard')

        # Teacher resources
        resources = Resource.objects.filter(uploaded_by=request.user)

        # Stats
        teacher_upload_count = resources.count()

        teacher_total_downloads = resources.aggregate(
            total=Sum('downloads')
        )['total'] or 0

        # Top resources
        top_resources = resources.order_by('-downloads')[:3]

        context = {
            'resources': resources,
            'categories': categories,
            'top_resources': top_resources,
            'teacher_upload_count': teacher_upload_count,
            'teacher_total_downloads': teacher_total_downloads
        }

        return render(request, 'portal/teacher_dashboard.html', context)

    # =========================
    # STUDENT DASHBOARD
    # =========================
    else:

        resources = Resource.objects.all()

        # SEARCH
        query = request.GET.get('q')
        if query:
            resources = resources.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )

        # CATEGORY FILTER
        category_id = request.GET.get('category')
        if category_id:
            resources = resources.filter(category_id=category_id)

        # Top resources
        top_resources = Resource.objects.order_by('-downloads')[:3]

        # Latest resources
        latest_resources = Resource.objects.order_by('-uploaded_at')[:3]

        # Stats
        total_resources = Resource.objects.count()
        total_categories = Category.objects.count()
        total_downloads = Resource.objects.aggregate(
            total=Sum('downloads')
        )['total'] or 0

        context = {
            'resources': resources,
            'categories': categories,
            'top_resources': top_resources,
            'latest_resources': latest_resources,
            'total_resources': total_resources,
            'total_categories': total_categories,
            'total_downloads': total_downloads
        }

        return render(request, 'portal/student_dashboard.html', context)


# =========================
# DELETE RESOURCE
# =========================
@login_required
def delete_resource(request, resource_id):

    resource = get_object_or_404(Resource, id=resource_id)

    # Only uploader can delete
    if request.user == resource.uploaded_by:
        resource.delete()

    return redirect('dashboard')


# =========================
# DOWNLOAD RESOURCE
# =========================
@login_required
def download_resource(request, resource_id):

    resource = get_object_or_404(Resource, id=resource_id)

    # 🔥 Auto increase downloads
    resource.downloads += 1
    resource.save()

    return HttpResponseRedirect(resource.file.url)