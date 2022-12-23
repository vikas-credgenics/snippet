from rest_framework import serializers

from community.models import Vendor, Testimonial


class VendorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'about', 'website', 'headquarters', 'created_at', 'updated_at')


class TestimonialSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user_id = serializers.CharField(source="user.id", read_only=True)
    written_by = serializers.CharField(source="user.first_name", read_only=True)
    vendor_id = serializers.CharField(source="vendor.id", read_only=True)
    vendor_name = serializers.CharField(source="vendor.name", read_only=True)

    class Meta:
        model = Testimonial
        fields = ('id', 'user_id', 'written_by', 'vendor_id', 'vendor_name', 'content', 'service_rating',
                  'response_time_rating', 'digitisation_rating', 'customer_support_rating', 'overall_rating',
                  'created_at', 'updated_at')
