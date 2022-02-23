from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from form_builders.models import FormModel, FormGroupModel, QuestionModel, AnswerTypModel, AnswerModel, BooleanModel, \
    CharModel, DateModel, FileModel, FloatModel, ImageModel, IntegerModel, JsonModel, TextModel, TimeModel, UrlModel
from form_builders.serializers import FormModelSerializer, FormGroupModelSerializer, QuestionModelSerializer, \
    AnswerTypModelSerializer, AnswerModelSerializer, BooleanModelSerializer, CharModelSerializer, DateModelSerializer, \
    FileModelSerializer, FloatModelSerializer, ImageModelSerializer, IntegerModelSerializer, JsonModelSerializer, \
    TextModelSerializer, TimeModelSerializer, UrlModelSerializer, DetailFormGroupSerializer


########### list s ###
class ListForm(ListAPIView):
    serializer_class = FormModelSerializer
    queryset = FormModel.objects.all()


class ListFormGroup(ListAPIView):
    serializer_class = FormGroupModelSerializer
    queryset = FormGroupModel.objects.all()


######   create s #####
class CreateForm(CreateAPIView):
    serializer_class = FormModelSerializer
    queryset = FormModel.objects.all()


class CreateFormGroup(CreateAPIView):
    serializer_class = FormGroupModelSerializer
    queryset = FormGroupModel.objects.all()


class CreateQuestion(CreateAPIView):
    serializer_class = QuestionModelSerializer
    queryset = QuestionModel.objects.all()


class CreateAnswerTyp(CreateAPIView):
    serializer_class = AnswerTypModelSerializer
    queryset = AnswerTypModel.objects.all()


class CreateAnswer(CreateAPIView):
    serializer_class = AnswerModelSerializer
    queryset = AnswerModel.objects.all()


class CreateBooleanKind(CreateAPIView):
    serializer_class = BooleanModelSerializer
    queryset = BooleanModel.objects.all()


class CreateCharKind(CreateAPIView):
    serializer_class = CharModelSerializer
    queryset = CharModel.objects.all()


class CreateDateKind(CreateAPIView):
    serializer_class = DateModelSerializer
    queryset = DateModel.objects.all()


class CreateFileKind(CreateAPIView):
    serializer_class = FileModelSerializer
    queryset = FileModel.objects.all()


class CreateFloatKind(CreateAPIView):
    serializer_class = FloatModelSerializer
    queryset = FloatModel.objects.all()


class CreateImageKind(CreateAPIView):
    serializer_class = ImageModelSerializer
    queryset = ImageModel.objects.all()


class CreateIntegerKind(CreateAPIView):
    serializer_class = IntegerModelSerializer
    queryset = IntegerModel.objects.all()


class CreateJsonKind(CreateAPIView):
    serializer_class = JsonModelSerializer
    queryset = JsonModel.objects.all()


class CreateTextKind(CreateAPIView):
    serializer_class = TextModelSerializer
    queryset = TextModel.objects.all()


class CreateTimeKind(CreateAPIView):
    serializer_class = TimeModelSerializer
    queryset = TimeModel.objects.all()


class CreateUrlKind(CreateAPIView):
    serializer_class = UrlModelSerializer
    queryset = UrlModel.objects.all()


class RetrieveForm(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DetailFormGroupSerializer
    queryset = FormModel.objects.all()
