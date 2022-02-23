from django.contrib import admin

from form_builders.models import FormGroupModel, FormModel, QuestionModel, AnswerTypModel, AnswerModel, BooleanModel, \
    CharModel, DateModel, FileModel, FloatModel, ImageModel, IntegerModel, JsonModel, TextModel, TimeModel, UrlModel

admin.site.register(FormGroupModel)
admin.site.register(FormModel)
admin.site.register(QuestionModel)
admin.site.register(AnswerTypModel)
admin.site.register(AnswerModel)
admin.site.register(BooleanModel)
admin.site.register(CharModel)
admin.site.register(DateModel)
admin.site.register(FileModel)
admin.site.register(FloatModel)
admin.site.register(ImageModel)
admin.site.register(IntegerModel)
admin.site.register(JsonModel)
admin.site.register(TextModel)
admin.site.register(TimeModel)
admin.site.register(UrlModel)
