from rest_framework import generics, permissions
from rest_framework import status
from django.db.models import Sum, Avg
from django.http.response import Http404
from community.models import Vendor, Testimonial
from rest_framework.views import APIView
from rest_framework.response import Response
from community.serializers import VendorSerializer, TestimonialSerializer


# Create your views here.
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)


class VendorDetail(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    model = Vendor
    serializer_class = VendorSerializer

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = self.serializer_class(vendor)
        serializer_data = dict(serializer.data)
        serializer_data['overall_rating'] = Testimonial.objects.filter(
            vendor_id=pk).aggregate(Avg('overall_rating')).get('overall_rating__avg')
        return Response(serializer_data, status=status.HTTP_200_OK)


class TestimonialView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAuthenticated,)
    model = Testimonial
    serializer_class = TestimonialSerializer

    def get(self, request, pk):
        testimonials = Testimonial.objects.filter(vendor_id=pk)
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TestimonialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, vendor=Vendor.objects.get(id=pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
