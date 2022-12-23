from rest_framework import generics, permissions
from rest_framework import status
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


class VendorDetail(generics.RetrieveUpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class TestimonialView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        import pdb;pdb.set_trace()
        testimonials = Testimonial.objects.filter(vendor_id=pk)
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TestimonialSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
