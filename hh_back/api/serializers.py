from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company()
        company.name= validated_data.get('name','No name')
        company.description = validated_data.get('description', 'No description')
        company.city = validated_data.get('city', 'No city')
        company.address = validated_data.get('address', 'No address')
        company.save()
        return company


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        #fields = ('name','description','salary')
        fields = '__all__'


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    vacancies = serializers.StringRelatedField(many = True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancies')