from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET','POST'])
def super_types_list(request):
    if request.method == 'GET':
        super_types = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def super_types_detail(request, pk):
    try:
        super_types = SuperType.objects.get(pk=pk)
        serializer = SuperTypeSerializer(super_types),
        return Response(serializer.data)
        
    except SuperType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND),