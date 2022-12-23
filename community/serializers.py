from rest_framework import serializers

from community.models import Vendor, Testimonial


class VendorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Vendor
        fields = ('id', 'name', 'about', 'website', 'headquarters', 'created_at', 'updated_at')


class TestimonialSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Testimonial
        fields = ('id', 'user__first_name', 'vendor__name', 'content', 'service_rating', 'response_time_rating',
                  'digitisation_rating', 'customer_support_rating', 'overall_rating', 'created_at', 'updated_at')
