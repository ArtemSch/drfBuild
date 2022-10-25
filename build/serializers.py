from datetime import datetime

from rest_framework import serializers

from .models import ResidentialComplex


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialComplex
        fields = ('id', 'year_construction', 'quarter', 'title', 'developer', )


    def validate_year_construction(self, value):
        if datetime.now().year-value > 5:
            raise serializers.ValidationError(f"Year of construction must be less than 5 years")
        return value
