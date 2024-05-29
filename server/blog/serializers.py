from rest_framework import serializers
from blog.models import BlogList

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogList
        fields = '__all__'
        # fields = (
        #     'BlogId',
        #     'Title',
        #     'Catego',
        #     'Tag',
        #     'Desc',
        #     'Author',
        #     'Content',
        #     'PubTime',
        #     'Enable',
        #     'Press',
        #     'Like',
        # )
