from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET',])
def project_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        projects = Project.objects.filter(is_visible=True)
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)
