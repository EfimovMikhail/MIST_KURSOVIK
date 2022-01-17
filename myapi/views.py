from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Merop
from .serializers import MeropSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def merop_list(request):
    if request.method == 'GET':
        merops = Merop.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            merops = merops.filter(title__icontains=title)

        merops_serializer = MeropSerializer(merops, many=True)
        return JsonResponse(merops_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        merop_data = JSONParser().parse(request)
        merop_serializer = MeropSerializer(data=merop_data)
        if merop_serializer.is_valid():
            merop_serializer.save()
            return JsonResponse(merop_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(merop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Merop.objects.all().delete()
        return JsonResponse({'message': '{} Merops were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def merop_detail(request, pk):
    try:
        merop = Merop.objects.get(pk=pk)
    except Merop.DoesNotExist:
        return JsonResponse({'message': 'The merop does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        merop_serializer = MeropSerializer(merop)
        return JsonResponse(merop_serializer.data)

    elif request.method == 'PUT':
        merop_data = JSONParser().parse(request)
        merop_serializer = MeropSerializer(merop, data=merop_data)
        if merop_serializer.is_valid():
            merop_serializer.save()
            return JsonResponse(merop_serializer.data)
        return JsonResponse(merop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        merop.delete()
        return JsonResponse({'message': 'Merop was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def merop_list_published(request):
    merops = Merop.objects.filter(published=True)

    if request.method == 'GET':
        merops_serializer = MeropSerializer(merops, many=True)
        return JsonResponse(merops_serializer.data, safe=False)

