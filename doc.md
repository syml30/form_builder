# Form Builder Service

با استفاده از این سرویس فرم های مورد نیاز با تمام جزپیات و فیلدهای مربوط سایت ساخته می شود.

## تکنولوژی‌های استفاده شده

- python
- django
- drf
- swagger

## ای‌پی‌آی‌ها

- ListForm
- ListFormGroup
- CreateForm
- CreateFormGroup
- CreateQuestion
- CreateAnswerTyp
- CreateAnswer
- CreateBooleanKind
- CreateCharKind
- CreateDateKind
- CreateFileKind
- CreateFloatKind
- CreateImageKind
- CreateIntegerKind
- CreateJsonKind
- CreateTextKind
- CreateTimeKind
- CreateUrlKind
- RetrieveForm

### ListForm

با استفاده از این ای پی آی لیست تمام فرم های موجود نشان داده می شود.

### ListFormGroup

بااستفاده از این ای پی آی لیست تمام گروه بندی های مربوط به فرم ها نشان داده می شود.

### CreateForm

با استفاده از این ای پی آی فرم مورد نیاز ساخته می شود.

### CreateFormGroup

با استفاده از این ای پی آی گروه بندی مورد نظر برای فرم ها ایجاد می شود.

### CreateQuestion

با استفاده از این ای پی آی سوالات ایجاد می شود.

### CreateAnswerTyp

با استفاده از این ای پی آی نوع و جنس باسخ ها ایجاد می شود.

### CreateAnswer

با استفاده از این ای پی آی پاسخ های مورد نظر ایجاد می شود.

### CreateBooleanKind

با استفاده از این ای پی فیلد های مربوط از جنس boolean یا true یا false ایجاد می شود.

### CreateCharKind

با استفاده از این ای پی فیلد های مربوط از جنس کاراکتر ایجاد می شود.

### CreateDateKind

با استفاده از این ای پی فیلد های مربوط از جنس روز ایجاد می شود.

### CreateFileKind

با استفاده از این ای پی فیلد های مربوط از جنس فایل ایجاد می شود.

### CreateFloatKind

با استفاده از این ای پی فیلد های مربوط از جنس عدد های اعشاری ایجاد می شود.

### CreateImageKind

با استفاده از این ای پی فیلد های مربوط از جنس عکس ایجاد می شود.

### CreateIntegerKind

با استفاده از این ای پی فیلد های مربوط از جنس عددی ایجاد می شود.

### CreateJsonKind

با استفاده از این ای پی فیلد های مربوط از جنس جیسون حالت کی و ولیو ایجاد می شود.

### CreateTextKind

با استفاده از این ای پی فیلد های مربوط از جنس متن و یا متن های طولانی ایجاد می شود.

### CreateTimeKind

با استفاده از این ای پی فیلد های مربوط از جنس زمان و ساعت ایجاد می شود.

### CreateUrlKind

با استفاده از این ای پی فیلد های مربوط از جنس لینک یا یو آر ال ایجاد می شود.

### RetrieveForm

با استفاده از این ای پی جزپیات مربوط به یک فرم با استفاده از پرایمری کی نشان داده می شود.

#### ریز مشخصات فنی

OPTIONS /api/records/retrieve_record/1

HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept

### retrieve record service

#### نحوه‌ی استفاده

```bash
$ curl: (6) Could not resolve host: GET
{"id":1,"user":"یاسمن","data":"1126","create_date_time":"2022-02-22T10:13:49.110947+03:30"}%   
```

#### خروجی مورد انتظار

```json
{
  "name": "Retrieve Record Model",
  "description": "",
  "renders": [
    "application/json",
    "text/html"
  ],
  "parses": [
    "application/json",
    "application/x-www-form-urlencoded",
    "multipart/form-data"
  ]
}
```

### list record service

#### نحوه‌ی استفاده

```bash
$ curl: (6) Could not resolve host: GET
{"count":3,"next":null,"previous":null,"results":[{"id":1,"user":"یاسمن","data":"1126","create_date_time":"2022-02-22T10:13:49.110947+03:30"},{"id":2,"user":"سیمین","data":"0730","create_date_time":"2022-02-22T10:14:14.493795+03:30"},{"id":3,"user":"changiz","data":"1111","create_date_time":"2022-02-22T10:21:52.800648+03:30"}]}%   
```

#### خروجی مورد انتظار

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": "یاسمن",
      "data": "1126",
      "create_date_time": "2022-02-22T10:13:49.110947+03:30"
    },
    {
      "id": 2,
      "user": "سیمین",
      "data": "0730",
      "create_date_time": "2022-02-22T10:14:14.493795+03:30"
    },
    {
      "id": 3,
      "user": "changiz",
      "data": "1111",
      "create_date_time": "2022-02-22T10:21:52.800648+03:30"
    }
  ]
}
```

### create record service

#### نحوه‌ی استفاده

```bash
$ / curl -X POST -F 'user=test' -F 'data=test' 'http://127.0.0.1:8000/api/records/create_record'
{"id":4,"user":"test","data":"test","create_date_time":"2022-02-22T11:39:06.217166+03:30"}%  
```

#### خروجی مورد انتظار

```json
{
  "id": 5,
  "user": "test",
  "data": "test",
  "create_date_time": "2022-02-22T11:40:47.696499+03:30"
}


```
