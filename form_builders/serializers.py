from rest_framework.serializers import ModelSerializer
from form_builders.models import FormModel, FormGroupModel, QuestionModel, AnswerTypModel, AnswerModel, BooleanModel, \
    CharModel, DateModel, FileModel, FloatModel, ImageModel, IntegerModel, JsonModel, TextModel, TimeModel, UrlModel


class FormModelSerializer(ModelSerializer):
    class Meta:
        model = FormModel
        fields = '__all__'


#################################################################

class DetailFormGroupSerializer(ModelSerializer): 
    forms = FormModelSerializer(many=True, read_only=True)

    class Meta:
        model = FormGroupModel
        # fields = ['title', 'forms']
        fields = '__all__'


################################################################
class FormGroupModelSerializer(ModelSerializer):
    class Meta:
        model = FormGroupModel
        fields = '__all__'


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'


class AnswerTypModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerTypModel
        fields = '__all__'


class AnswerModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'


class BooleanModelSerializer(ModelSerializer):
    class Meta:
        model = BooleanModel
        fields = '__all__'


class CharModelSerializer(ModelSerializer):
    class Meta:
        model = CharModel
        fields = '__all__'


class DateModelSerializer(ModelSerializer):
    class Meta:
        model = DateModel
        fields = '__all__'


class FileModelSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'


class FloatModelSerializer(ModelSerializer):
    class Meta:
        model = FloatModel
        fields = '__all__'


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class IntegerModelSerializer(ModelSerializer):
    class Meta:
        model = IntegerModel
        fields = '__all__'


class JsonModelSerializer(ModelSerializer):
    class Meta:
        model = JsonModel
        fields = '__all__'


class TextModelSerializer(ModelSerializer):
    class Meta:
        model = TextModel
        fields = '__all__'


class TimeModelSerializer(ModelSerializer):
    class Meta:
        model = TimeModel
        fields = '__all__'


class UrlModelSerializer(ModelSerializer):
    class Meta:
        model = UrlModel
        fields = '__all__'
