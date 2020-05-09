from rest_framework import serializers
from .models import Student, Teacher

# TODO: Implement for all the models


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=32)
    last_name = serializers.CharField(required=True, max_length=32)
    list = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        return Student.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.list = validated_data.get('list', instance.list)
        instance.save()
        return instance

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'list']


class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=32)
    last_name = serializers.CharField(required=True, max_length=32)
    key = serializers.CharField(required=True, max_length=64)
    subjects = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        return Teacher.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.key = validated_data.get('key', instance.key)
        instance.save()
        return instance

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'key', 'subjects']
