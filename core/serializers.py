from rest_framework import serializers
from .models import Post

# Django’s serialization framework provides a mechanism for “translating” Django models into other formats
# For example Json format

# The ideia behind the PostSerializers, it's similar to the forms structure of Django.
# Transformation of the Post model in a Json, that contains this two fields: title and description
# These fields are returned when something it's requested, through the GET method(Postman)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description', 
            'owner'
        )
