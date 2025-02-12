# Этапы разработки
[Бекенд первый этап](docs/backend-step1.md)
# Swagger
https://editor.swagger.io/?url=https://raw.githubusercontent.com/ivartm/bbbs-stage2/master/docs/swagger.json
# Примеры запросов
## Авторизация - получение токена
### запрос
`curl --location --request POST 'http://127.0.0.1:8000/api/v1/token/' 
--header 'Content-Type: application/json' 
--data-raw '{  "username": "admin",  "password": "admin"}'`
### ответ
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDU4NTM1NSwianRpIjoiNGY5YTc5ZmZmNDEzNDM5NmJlNjhlZTVhNjk4MWNjMDgiLCJ1c2VyX2lkIjoxfQ.9pi-sEjkVsU7yxnP26Xvf-E98CVp9HgRvE_sHI7Mi_E",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNDk5MjU1LCJqdGkiOiI3N2Q1MWNmNWM1ZGU0YzBmYjE3MDVlMDgzYjU4YjYyMSIsInVzZXJfaWQiOjF9.jPP3p030SSA4H72m1JpElYh-R-bF20CBcLwnxI7Lxjs"
}
```
После авторизации во все запросы добавляем заголовок
`--header 'Authorization: Bearer "значение access"'`
## Получение списка городов
`curl --location --request GET 'http://127.0.0.1:8000/api/v1/cities/' 
--header 'Content-Type: application/json'`
```json
[
    {
        "id": 1,
        "name": "Москва",
        "isPrimary": true
    },
    {
        "id": 2,
        "name": "Воронеж",
        "isPrimary": false
    }
]
```
## Получение - обновление профайла пользователя, текущего города пользователя и т.д.
### запрос
```bash
curl --location --request GET 'http://127.0.0.1:8000/api/v1/profile/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNTM4OTMzLCJqdGkiOiIwOWZlNWUxNmI1MjI0YmM3ODJiYTc1YmM1OWExZWUzZSIsInVzZXJfaWQiOjF9._cDyG8Vp2HWzPPp-Hrm-P5FD5P0zcywVd4o4Gt2FL2M'
```
### ответ
```json
{
  "id": 1,
  "user": 1,
  "city": 2
}
```
## Получение главной страницы
Для авторизованого пользователя город для поиска событий берется из профайла, 
неавторизованный пользователь отпровляет id города в GET параметре city
### запрос
`curl --location --request GET 'http://127.0.0.1:8000/api/v1/main/' --header 'Content-Type: application/json'`
### ответ
```json
{
    "event": {
        "id": 11,
        "tags": [
            {
                "id": 111,
                "name": "Волонтёры",
                "slug": "volunteers"
            },
            {
                "id": 112,
                "name": "Дети",
                "slug": "children"
            }
        ],
        "title": "Субботний meet up: учимся проходить интевью",
        "startAt": "2021-05-08T19:22:00Z",
        "endAt": "2021-05-08T21:22:00Z",
        "address": "Садовническая наб., д. 77 стр. 1 (офис компании Ernst&Young)",
        "contact": "Александра, +7 926 356-78-90",
        "remainSeats": 5,
        "description": "Наконец-то наступила весна и мы пережили эту долгую зиму! И возможно, что внутренних сил и ресурса сейчас не так много, а до окончания учебного года ещё целых несколько месяцев. Поэтому приглашаем вас на встречу нашего ресурсного клуба \"Наставник PRO\", которую мы хотим посвятить теме поиска моральных сил, смыслов и внутреннего ресурса для общения и взаимодействия с нашими подопечными.",
        "booked": true
    },
    "history": {
        "id": 21,
        "imageUrl": "https://picsum.photos/870/520",
        "title": "История Марины и Алины"
    },
    "place": {
        "chosen": true,
        "id": 31,
        "title": "Сплав на байдарках в две строки",
        "name": "усадьба Архангельское в две строки",
        "info": "Девока, 10 лет. Активный отдых",
        "description": "Аннотация статьи в несколько абзацев. В тот момент, как ребёнок научился говорить, и не одно слово, а задавать бесконечное количество вопросов, жизнь меняется. Вы будете не понимать друг друга,  потом понимать чуть лучше и, Аннотация статьи в несколько абзацев. В тот момент, как ребёнок научился говорить, и не одно слово, а задавать бесконечное количество вопросов, жизнь меняется. Вы будете не понимать друг друга,  потом понимать чуть лучше и,\nАннотация статьи в несколько абзацев. В тот момент, как ребёнок научился говорить, и не одно слово, а задавать бесконечное количество вопросов, жизнь меняется. Вы будете не по Аннотация статьи в несколько абзацев. В тот момент, как ребёнок научился говорить, и не одно слово, а задавать бесконечное количество вопросов, жизнь меняется.",
        "imageUrl": "https://picsum.photos/1125/394",
        "link": "https://www.moscowzoo.ru/"
    },
    "articles": [
        {
            "id": 41,
            "color": "#C8D1FF",
            "title": "Развитие детей-сирот отличается от развития детей, живущих в семьях. Все  этапы развития у детей-сирот проходят с искажениями и имеют ряд негативных  особенностей. "
        },
        {
            "id": 42,
            "color": "#8CDD94",
            "title": "У таких детей возникает ощущение отверженности. Оно приводит к напряженности и  недоверию к людям и, как итог, к реальному неприятию себя и окружающих."
        }
    ],
    "movies": [
        {
            "id": 51,
            "imageUrl": "https://picsum.photos/420/239",
            "title": "Жутко громко и запредельно близко",
            "info": "Василий Сигарев, Борисов-Мусотов (Россия), 2009 год",
            "link": "https://youtu.be/8VzzlhOyOSI",
            "tags": [
                {
                    "id": 551,
                    "name": "рубрика",
                    "slug": "rubric"
                },
                {
                    "id": 552,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ]
        },
        {
            "id": 52,
            "imageUrl": "https://picsum.photos/420/239",
            "title": "Жутко громко и запредельно близко",
            "info": "Василий Сигарев, Борисов-Мусотов (Россия), 2009 год",
            "link": "https://youtu.be/8VzzlhOyOSI",
            "tags": [
                {
                    "id": 551,
                    "name": "рубрика",
                    "slug": "rubric"
                },
                {
                    "id": 552,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ]
        },
        {
            "id": 53,
            "imageUrl": "https://picsum.photos/420/239",
            "title": "Жутко громко и запредельно близко",
            "info": "Василий Сигарев, Борисов-Мусотов (Россия), 2009 год",
            "link": "https://youtu.be/8VzzlhOyOSI",
            "tags": [
                {
                    "id": 551,
                    "name": "рубрика",
                    "slug": "rubric"
                },
                {
                    "id": 552,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ]
        },
        {
            "id": 54,
            "imageUrl": "https://picsum.photos/420/239",
            "title": "Жутко громко и запредельно близко",
            "info": "Василий Сигарев, Борисов-Мусотов (Россия), 2009 год",
            "link": "https://youtu.be/8VzzlhOyOSI",
            "tags": [
                {
                    "id": 551,
                    "name": "рубрика",
                    "slug": "rubric"
                },
                {
                    "id": 552,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ]
        }
    ],
    "video": {
        "id": 61,
        "title": "Эфир с выпускником нашей программы",
        "info": "Иван Рустаев, выпускник программы",
        "link": "https://youtu.be/H980rXfjdq4",
        "imageUrl": "https://picsum.photos/1199/675",
        "duration": 134
    },
    "questions": [
        {
            "id": 71,
            "tags": [
                {
                    "id": 771,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ],
            "title": "Я боюсь, что ребёнок ко мне слишком сильно привяжется. Что делать?"
        },
        {
            "id": 72,
            "tags": [
                {
                    "id": 771,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ],
            "title": "Возможно ли продлить срок участия в программе, если и я и мой «младший» хотим остаться в программе?"
        },
        {
            "id": 73,
            "tags": [
                {
                    "id": 771,
                    "name": "рубрика",
                    "slug": "rubric"
                }
            ],
            "title": "Что делать если Ваш младший решил закрыть пару, т.к. слишком занят с учебой и друзьями?"
        }
    ]
}
```
## Работа с календарем
### Список событий
Для авторизованого пользователя город для поиска событий берется из профайла, 
неавторизованный пользователь отпровляет id города в GET параметре city
```bash
curl --location --request GET 'http://127.0.0.1:8000/api/v1/afisha/events/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNTM4NDU2LCJqdGkiOiIwMTJjMTMzNGQ5MjM0MWI4YWU1YmJhMDExYjAyMTdjOCIsInVzZXJfaWQiOjF9.S4JVKaVnUzr_XmLXOs6pfYKsLBhzEzm9Rhj1jnW6fhc'`
```
### ответ
флаг booked - зарегистрирован пользователь на это событие или нет
```json
[
    {
        "id": 1,
        "booked": true,
        "address": "Садовническая наб., д. 77 стр. 1 (офис компании Ernst&Young)",
        "contact": "Александра, +7 926 356-78-90",
        "title": "Субботний meet up: учимся проходить интевью",
        "description": "Наконец-то наступила весна и мы пережили эту долгую зиму! И возможно, что внутренних сил и ресурса сейчас не так много, а до окончания учебного года ещё целых несколько месяцев. Поэтому приглашаем вас на встречу нашего ресурсного клуба \"Наставник PRO\", которую мы хотим посвятить теме поиска моральных сил, смыслов и внутреннего ресурса для общения и взаимодействия с нашими подопечными.",
        "startAt": "2021-05-10T06:00:00Z",
        "endAt": "2021-05-10T08:00:00Z",
        "seats": 100,
        "takenSeats": 0,
        "city": 1
    }
]
```
## Записаться на событие
### запрос
```bash
curl --location --request POST 'http://127.0.0.1:8000/api/v1/afisha/event-participants/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNTM4OTMzLCJqdGkiOiIwOWZlNWUxNmI1MjI0YmM3ODJiYTc1YmM1OWExZWUzZSIsInVzZXJfaWQiOjF9._cDyG8Vp2HWzPPp-Hrm-P5FD5P0zcywVd4o4Gt2FL2M' \
--data-raw '{"event": 1}'
```
### ответ
```json
{
  "id": 2,
  "event": 4
}
```
