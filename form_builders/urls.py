from django.urls import path
from form_builders.views import ListForm, ListFormGroup, CreateForm, CreateFormGroup, CreateQuestion, CreateAnswerTyp, \
    CreateAnswer, CreateBooleanKind, CreateCharKind, CreateDateKind, CreateFileKind, CreateFloatKind, CreateImageKind, \
    CreateIntegerKind, CreateJsonKind, CreateTextKind, CreateTimeKind, CreateUrlKind, RetrieveForm

app_name = "form_builders"
urlpatterns = [
    path('list_form', ListForm.as_view(), name='list_form'),
    path('list_form_group', ListFormGroup.as_view(), name='list_form_group'),
    path('create_form', CreateForm.as_view(), name='create_form'),
    path('create_form_group', CreateFormGroup.as_view(), name='create_form_group'),
    path('create_question', CreateQuestion.as_view(), name='create_question'),
    path('create_answer_typ', CreateAnswerTyp.as_view(), name='create_answer_typ'),
    path('create_answer', CreateAnswer.as_view(), name='create_answer'),
    path('create_boolean', CreateBooleanKind.as_view(), name='create_boolean'),
    path('create_char', CreateCharKind.as_view(), name='create_char'),
    path('create_date', CreateDateKind.as_view(), name='create_date'),
    path('create_file', CreateFileKind.as_view(), name='create_file'),
    path('create_float', CreateFloatKind.as_view(), name='create_float'),
    path('create_image', CreateImageKind.as_view(), name='create_image'),
    path('create_integer', CreateIntegerKind.as_view(), name='create_integer'),
    path('create_json', CreateJsonKind.as_view(), name='create_json'),
    path('create_text', CreateTextKind.as_view(), name='create_text'),
    path('create_time', CreateTimeKind.as_view(), name='create_time'),
    path('create_url', CreateUrlKind.as_view(), name='create_url'),
    path('retrieve_form/<int:pk>', RetrieveForm.as_view(), name='retrieve_form'),

]
