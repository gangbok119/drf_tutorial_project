from rest_framework import serializers

from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )

#
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='rainbow_dash')
#
#     def create(self, validated_data):
#         '''
#
#         :param validated_data:
#         :return:
#         '''
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         '''
#
#         :param instance:
#         :param validated_data:
#         :return:
#         '''
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         # instance.save()
#         #      for item in ['title','code','linenos','language','style']:
#         #          setattr(instance, item, validated_data.get(item)) or getattr(instance)
#         instance.save()
#         return instance
