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

OPTIONS /api/form_buiders/list_form

HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "List Form",
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

## ListForm

#### نحوه‌ی استفاده

```bash

$ curl GET http://127.0.0.1:8000/api/form_buiders/list_form 
```

#### خروجی مورد انتظار

```json

[
  {
    "id": 1,
    "title": "سلامت یک",
    "group": 1
  },
  {
    "id": 2,
    "title": "سلامت دو",
    "group": 2
  },
  {
    "id": 3,
    "title": "seh",
    "group": 2
  }
]

```

## ListFormGroup

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/list_form_group

HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "List Form Group",
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

#### نحوه‌ی استفاده

```bash
$ curl curl GET http://127.0.0.1:8000/api/form_buiders/list_form_group

```

#### خروجی مورد انتظار

```json
[
  {
    "id": 1,
    "title": "فرم گروه یک"
  },
  {
    "id": 2,
    "title": "فرم گروه دو"
  },
  {
    "id": 3,
    "title": "chahar"
  }
]
```

## CreateForm

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_form

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Form",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"title": {
"type": "string",
"required": true,
"read_only": false,
"label": "Title",
"max_length": 200 },
"group": {
"type": "field",
"required": true,
"read_only": false,
"label": "Group"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'title=seh' -F 'group=2' http://127.0.0.1:8000/api/form_buiders/create_form

```

#### خروجی مورد انتظار

```json
{
  "id": 3,
  "title": "seh",
  "group": 2
}

```

## CreateFormGroup

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_form_group

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Form Group",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"title": {
"type": "string",
"required": true,
"read_only": false,
"label": "Title",
"max_length": 500 } } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'title=chahar' http://127.0.0.1:8000/api/form_buiders/create_form_group

```

#### خروجی مورد انتظار

```json
{
  "id": 3,
  "title": "chahar"
}
```

## CreateQuestion

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_question

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Question",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"title": {
"type": "string",
"required": true,
"read_only": false,
"label": "Title",
"max_length": 200 },
"number": {
"type": "integer",
"required": true,
"read_only": false,
"label": "Number"
},
"form": {
"type": "field",
"required": true,
"read_only": false,
"label": "Form"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'title=chahar' -F 'number=123' -F 'form=1' http://127.0.0.1:8000/api/form_buiders/create_question
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "title": "chahar",
  "number": 123,
  "form": 1
}
```

## CreateAnswerTyp

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_answer_typ

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Answer Typ",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"title": {
"type": "string",
"required": true,
"read_only": false,
"label": "Title",
"max_length": 200 } } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'title=testpostman' http://127.0.0.1:8000/api/form_buiders/create_answer_typ
```

#### خروجی مورد انتظار

```json
{
  "id": 3,
  "title": "testpostman"
}
```

## CreateAnswer

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_answer

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Answer",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"typ": {
"type": "field",
"required": true,
"read_only": false,
"label": "Typ"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'type=2' http://127.0.0.1:8000/api/form_buiders/create_answer
```

#### خروجی مورد انتظار

```json
{
  "id": 3,
  "typ": 2
}
```

## CreateBooleanKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_boolean

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Boolean Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value=true' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_boolean
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": true,
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateCharKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_char

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Char Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "string",
"required": true,
"read_only": false,
"label": "Value",
"max_length": 512 },
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value=yas' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_char
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "yas",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateDateKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_date

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Date Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "date",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value=2022-02-23' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_date
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "2022-02-23",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateFileKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_file

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create File Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "file upload",
"required": true,
"read_only": false,
"label": "Value",
"max_length": 100 },
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'value=http://127.0.0.1:8000/images/328933bd-6609-494d-a849-11ea73a98223/f069bf5f-9977-49e6-aba1-4634cb03240d.jpg' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_file

```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "http://127.0.0.1:8000/images/328933bd-6609-494d-a849-11ea73a98223/f069bf5f-9977-49e6-aba1-4634cb03240d.jpg",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateFloatKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_float

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Float Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "float",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'value=12.3' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_float
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": 12.3,
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateImageKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_image

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Image Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "image upload",
"required": false,
"read_only": false,
"label": "Value",
"max_length": 100 },
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'value="http://127.0.0.1:8000/images/0f657c56-877a-47e7-a3be-876adfdc7175/3c1d4d12-8c22-442d-99e0-6834cfc62583.jpg"' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_image
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "http://127.0.0.1:8000/images/0f657c56-877a-47e7-a3be-876adfdc7175/3c1d4d12-8c22-442d-99e0-6834cfc62583.jpg",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateIntegerKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_integer

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Integer Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "integer",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'value=123456789' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_integer
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": 123456789,
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateJsonKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_json

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Json Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "field",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$ curl -X POST -F 'value={"firstName": "yasaman"}' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_json
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": {
    "firstName": "yasaman"
  },
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateTextKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_text

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Text Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "string",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value= جهت تست در پست من' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_text
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "جهت تست در پست من",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateTimeKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_time

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Time Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "time",
"required": true,
"read_only": false,
"label": "Value"
},
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value=07:53:02' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_time
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "07:53:02",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## CreateUrlKind

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/create_url

HTTP 200 OK Allow: POST, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Create Url Kind",
"description": "",
"renders": [
"application/json",
"text/html"
],
"parses": [
"application/json",
"application/x-www-form-urlencoded",
"multipart/form-data"
],
"actions": {
"POST": {
"id": {
"type": "integer",
"required": false,
"read_only": true,
"label": "ID"
},
"value": {
"type": "url",
"required": true,
"read_only": false,
"label": "Value",
"max_length": 700 },
"required": {
"type": "boolean",
"required": false,
"read_only": false,
"label": "Required"
},
"help_text": {
"type": "string",
"required": false,
"read_only": false,
"label": "Help text"
},
"place_holder": {
"type": "string",
"required": false,
"read_only": false,
"label": "Place holder",
"max_length": 215 },
"is_active": {
"type": "boolean",
"required": true,
"read_only": false,
"label": "Is active"
},
"extra_attribute": {
"type": "field",
"required": true,
"read_only": false,
"label": "Extra attribute"
},
"answer": {
"type": "field",
"required": true,
"read_only": false,
"label": "Answer"
} } } }

#### نحوه‌ی استفاده

```bash
$  curl -X POST -F 'value=https://www.time.ir/' -F 'answer=1' -F 'is_active=true' -F 'extra_attribute={"firstName": "yasaman"}' http://127.0.0.1:8000/api/form_buiders/create_url
```

#### خروجی مورد انتظار

```json
{
  "id": 2,
  "value": "https://www.time.ir/",
  "required": false,
  "help_text": null,
  "place_holder": null,
  "is_active": true,
  "extra_attribute": {
    "firstName": "yasaman"
  },
  "answer": 1
}
```

## RetrieveForm

#### ریز مشخصات فنی

OPTIONS /api/form_buiders/retrieve_form/1

HTTP 200 OK Allow: GET, HEAD, OPTIONS Content-Type: application/json Vary: Accept

{
"name": "Retrieve Form",
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

#### نحوه‌ی استفاده

```bash
$ curl GET http://127.0.0.1:8000/api/form_buiders/retrieve_form/1  
```

```json
{
  "id": 1,
  "title": "سلامت یک"
}
```






















