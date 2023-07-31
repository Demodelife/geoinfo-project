# API проекта GeoName
API с различными методами работы с информацией о географических объектах на основе DRF.

## Основные внешние библиотеки
* Django 4.1.7
* djangorestframework 3.14.0
* drf-spectacular 0.26.4
* и др.

## Установка
1. Клонируйте все содержимое репозитория в свою рабочую директорию.
2. Установите все библиотеки из файла requirements.txt (из geoinfo-project):
    * `pip install -r requirements.txt`
3. Запустите миграцию в корневой директории проекте (из geoinfo):
    * `python manage.py migrate`
4. Выполните команду для загрузки сущностей в БД из файла RU.txt:
    * `python manage.py load_db`
5. Запустите сервер одной из команд:
    * `python manage.py runserver` или `python script.py`
6. Перейдите к предложенному URL-адресу в консоли `127.0.0.1:8000`.

## Реализованные Методы

1. `GET /api/geoinfo/geonameid/` Метод принимает идентификатор "geonameid" и возвращает информацию об объекте.
   ### Пример запроса 200 OK
    * `GET /api/geoinfo/555555/`
   ### Ответ
    * Успешно прошедший запрос возвращает информацию об объекте, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
      "geonameid": 555555,
      "name": "Ivankovo",
      "asciiname": "Ivankovo",
      "alternatenames": "Ivankovo,Иванково",
      "latitude": "60.28333",
      "longitude": "44.08333",
      "feature_class": "P",
      "feature_code": "PPL",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "85",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 0,
      "elevation": 0,
      "dem": 137,
      "timezone": "Europe/Moscow",
      "modification_date": "2012-01-17"
    }
   ```
   ### Пример запроса 404 Not Found
    * `GET /api/geoinfo/777777/`
   ### Ответ
    * Если объект не найден, статус 404:
   ``` 
    HTTP 404 Not Found
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
       "detail": "Not found."
    } 
   ```
   
2. `GET /api/geoinfo/` Метод возвращает список географических объектов:
   ### Пример запроса 200 OK
    * `GET /api/geoinfo/`
   ### Ответ
    * Успешно прошедший запрос возвращает список объектов, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
    "links": {
    "next": "http://127.0.0.1:8000/api/geoinfo/?page=2",
    "previous": null
    },
    "total_count": 368268,
    "page_size": 10,
    "results": [
       {
         "geonameid": 451747,
         "name": "Zyabrikovo",
         "asciiname": "Zyabrikovo",
         "alternatenames": "",
         "latitude": "56.84665",
         "longitude": "34.70480",
         "feature_class": "P",
         "feature_code": "PPL",
         "country_code": "RU",
         "cc2": "",
         "admin1_code": "77",
         "admin2_code": "",
         "admin3_code": "",
         "admin4_code": "",
         "population": 0,
         "elevation": 0,
         "dem": 204,
         "timezone": "Europe/Moscow",
         "modification_date": "2011-07-09"
         },
         {
         "geonameid": 451748,
         "name": "Znamenka",
         "asciiname": "Znamenka"
         ...
   ```

## Метод получения списка объектов с дополнительными параметрами
1. Метод принимает страницу (`page`) и количество отображаемых на странице объектов (`count`) и возвращает список объектов с их информацией.
   ### Пример запроса 200 OK
    * `GET /api/geoinfo/?page=4&count=4`
   ### Ответ
    * Успешно прошедший запрос возвращает список объектов, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
    "links": {
    "next": "http://127.0.0.1:8000/api/geoinfo/?count=4&page=5",
    "previous": "http://127.0.0.1:8000/api/geoinfo/?count=4&page=3"
    },
    "total_count": 368268,
    "page_size": 4,
    "results": [
        {
        "geonameid": 451759,
        "name": "Urochishche Zakaznik",
        "asciiname": "Urochishche Zakaznik",
        "alternatenames": "",
        "latitude": "56.89212",
        "longitude": "34.56952",
        "feature_class": "L",
        "feature_code": "LCTY",
        "country_code": "RU",
        "cc2": "",
        "admin1_code": "77",
        "admin2_code": "",
        "admin3_code": "",
        "admin4_code": "",
        "population": 0,
        "elevation": 0,
        "dem": 219,
        "timezone": "Europe/Moscow",
        "modification_date": "2011-07-09"
    },
    {
        "geonameid": 451760,
        "name": "Zador’ye",
        "asciiname": "Zador'ye",
        "alternatenames": "",
        "latitude": "56.85239",
        "longitude": "34.49864",
    ...

   ```
   ### Пример запроса 404 Not Found
    * `GET /api/geoinfo/?page=XX&count=4`
   ### Ответ
    * Если ошибка в параметрах запроса или превышение параметров, статус 404:
   ``` 
    HTTP 404 Not Found
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "detail": "Invalid page."
    } 
   ```

2. Метод принимает параметр `search` и выводит подсказки с возможными продолжениями названий объектов.
   ### Пример запроса 200 OK
    * `GET /api/geoinfo/?search=Kolh`
   ### Ответ
    * Успешно прошедший запрос возвращает список совпадений, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "links": {
            "next": null,
            "previous": null
        },
        "total_count": 6,
        "page_size": 10,
        "results": [
            "Kolkhoz Mayak",
            "Kolkhoz Leninskaya Iskra",
            "Kolkhoz Krasnyy Prozhektor",
            "Krasnaya Gorka",
            "Shkolkhe",
            "Kolhoz Zarya"
        ]
    } 
   ```
   > Обратите внимание, что поиск дополнительно проходит еще и по альтернативным названиям объектов.
   ### Пример запроса без совпадений
    * `GET /api/geoinfo/?search=zxc`
   ### Ответ
    * Если совпадений не найдено, возвращается пустой ответ, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "links": {
            "next": null,
            "previous": null
        },
        "total_count": 0,
        "page_size": 10,
        "results": []
    }
   ```

3. Метод принимает названия двух объектов (`g1`, `g2`), 
включая название на русском языке и выводит их полную и сравнительную информацию:
    * Объект, находящийся севернее;
    * Совпадают ли часовые пояса;
    * Разницу часовых поясов (в часах).
   ### Пример запроса 200 OK
    * `GET /api/geoinfo/?g1=Москва&g2=Владивосток`
   ### Ответ
    * Успешно прошедший запрос возвращает полную и сравнительную информацию, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
    "links": {
        "next": null,
        "previous": null
    },
    "total_count": 2,
    "page_size": 10,
    "results": [
        {
            "geonameid": 524894,
            "name": "Moskva",
            "asciiname": "Moskva",
            "alternatenames": "Maskva,Moscou,Moscow,Moscu,Moscú,Moskau,Moskou,Moskovu,Moskva,Məskeu,Москва,Мәскеу",
            "latitude": "55.76167",
            "longitude": "37.60667",
            "feature_class": "A",
            "feature_code": "ADM1",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "48",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 13010112,
            "elevation": 0,
            "dem": 161,
            "timezone": "Europe/Moscow",
            "modification_date": "2023-01-12"
        },
        {
            "geonameid": 2013348,
            "name": "Vladivostok",
            "asciiname": "Vladivostok",
            "alternatenames": "Bladibostok,Uladzivastok,VVO,Vladivostok,Vladivostoka,Vladivostokas,Vladivostokium,Vlagyivosztok,Wladiwostok,Wladywostok,Władywostok,beulladiboseutokeu,fladyfwstwk,hai can wai,hai can wei,urajiosutoku,vilativostok,vladivastak,vladivostoka,w la di wx s txkh,wladywstwk,wldywwstwq,Βλαδιβοστόκ,Владивосток,Уладзівасток,Վլադիվոստոկ,וולאדיוואסטאק,ולדיווסטוק,فلاديفوستوك,ولادیوستوک,ولادی‌وؤستؤک,ولادی‌وستوک,ولاڈیووسٹوک,व्लादिवोस्तॉक,व्लादिवोस्तोक,விலாடிவொஸ்டொக்,ವ್ಲಾಡಿವಾಸ್ಟಾಕ್,วลาดีวอสตอค,ვლადივოსტოკი,ウラジオストク,海参崴,海參崴,블라디보스토크",
            "latitude": "43.10562",
            "longitude": "131.87353",
            "feature_class": "P",
            "feature_code": "PPLA",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "59",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 604901,
            "elevation": 0,
            "dem": 40,
            "timezone": "Asia/Vladivostok",
            "modification_date": "2022-09-17"
        }
    ],
    "comparison": {
        "geographical_object_1": {
            "name": "Moskva",
            "population": 13010112,
            "latitude": 55.76167,
            "timezone": "Europe/Moscow"
        },
        "geographical_object_2": {
            "name": "Vladivostok",
            "population": 604901,
            "latitude": 43.10562,
            "timezone": "Asia/Vladivostok"
        },
        "The object is located north": "Moskva",
        "Time zones the same": false,
        "Time zone difference": "-7:00:00"
        }
    }
   ```
   ### Пример запроса без найденного объекта(-ов)
    * `/api/geoinfo/?g1=Москва&g2=Абвгд`
   ### Ответ
    * Возвращается ответ с указанием объекта(-ов), который(-ых) не удалось найти, статус `200 OK`:
   ```
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        "Not found object g2 to comparison."
    ]
   ```

## Дополнительная информация
## Тестирование
1. Создание фикстур для тестов:  
   * `python manage.py dump_fixtures`
2. Запуск всех тестов:
   * `python manage.py test geoinfo_apiapp.tests`

## Работа с административной панелью Django
1. Создать суперпользователя:
   * `python manage.py createsuperuser`
2. Зайти в админку http://127.0.0.1:8000/admin/ зарегистрированным суперпользователем.

# GeoName Project API
API with different methods for working with information on geographical objects, based DRF.

## Main External Libraries
* Django 4.1.7
* djangorestframework 3.14.0
* drf-spectacular 0.26.4
* et al.

## Installation
1. Clone all the contents of the repository to your working directory.
2. Install all libraries from the requirements.txt file (from geoinfo-project):
     * `pip install -r requirements.txt`
3. Run the migration in the root directory of the project (from geoinfo):
     * `python manage.py migrate`
4. Run the command to load entities into the database from the RU.txt file:
     * `python manage.py load_db`
5. Start the server with one of the commands:
     * `python manage.py runserver` or `python script.py`
6. Navigate to the suggested URL in the console `127.0.0.1:8000`.

## Implemented Methods

1. `GET /api/geoinfo/geonameid/` The method takes the identifier "geonameid" and returns information about the object.
    ### Request example 200 OK
     * `GET /api/geoinfo/555555/`
    ### Response
     * A successful request returns information about the object, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
       "geonameid": 555555,
       "name": "Ivankovo",
       "asciiname": "Ivankovo",
       "alternatenames": "Ivankovo,Ivankovo",
       "latitude": "60.28333",
       "longitude": "44.08333",
       "feature_class": "P",
       "feature_code": "PPL",
       "country_code": "RU",
       "cc2": "",
       "admin1_code": "85",
       "admin2_code": "",
       "admin3_code": "",
       "admin4_code": "",
       population: 0
       elevation: 0
       "dem": 137
       "timezone": "Europe/Moscow",
       "modification_date": "2012-01-17"
     }
    ```
    ### 404 Not Found request example
     * `GET /api/geoinfo/777777/`
    ### Response
     * If the object is not found, the status is 404:
    ```
     HTTP 404 Not Found
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
        "detail": "Not found."
     }
    ```
2. `GET /api/geoinfo/` The method returns a list of geographic objects:
    ### Request example 200 OK
     * `GET /api/geoinfo/`
    ### Response
     * A successful request returns a list of objects, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept

     {
     "links": {
     "next": "http://127.0.0.1:8000/api/geoinfo/?page=2",
     "previous": null
     },
     "total_count": 368268,
     "page_size": 10,
     "results": [
        {
          "geonameid": 451747,
          "name": "Zyabrikovo",
          "asciiname": "Zyabrikovo",
          "alternatenames": "",
          "latitude": "56.84665",
          "longitude": "34.70480",
          "feature_class": "P",
          "feature_code": "PPL",
          "country_code": "RU",
          "cc2": "",
          "admin1_code": "77",
          "admin2_code": "",
          "admin3_code": "",
          "admin4_code": "",
          population: 0
          elevation: 0
          "dem": 204,
          "timezone": "Europe/Moscow",
          "modification_date": "2011-07-09"
          },
          {
          "geonameid": 451748,
          "name": "Znamenka",
          "asciiname": "Znamenka"
          ...
    ```
## Method for getting a list of objects with additional parameters
1. The method accepts a page (`page`) and the number of objects displayed on the page (`count`) and returns a list of objects with their information.
    ### Request example 200 OK
     * `GET /api/geoinfo/?page=4&count=4`
    ### Response
     * A successful request returns a list of objects, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept

     {
     "links": {
     "next": "http://127.0.0.1:8000/api/geoinfo/?count=4&page=5",
     "previous": "http://127.0.0.1:8000/api/geoinfo/?count=4&page=3"
     },
     "total_count": 368268,
     "page_size": 4,
     "results": [
         {
         "geonameid": 451759,
         "name": "Urochishche Zakaznik",
         "asciiname": "Urochishche Zakaznik",
         "alternatenames": "",
         "latitude": "56.89212",
         "longitude": "34.56952",
         "feature_class": "L",
         "feature_code": "LCTY",
         "country_code": "RU",
         "cc2": "",
         "admin1_code": "77",
         "admin2_code": "",
         "admin3_code": "",
         "admin4_code": "",
         population: 0
         elevation: 0
         "dem": 219
         "timezone": "Europe/Moscow",
         "modification_date": "2011-07-09"
     },
     {
         "geonameid": 451760,
         "name": "Zador'ye",
         "asciiname": "Zador'ye",
         "alternatenames": "",
         "latitude": "56.85239",
         "longitude": "34.49864",
     ...

    ```
    ### 404 Not Found request example
     * `GET /api/geoinfo/?page=XX&count=4`
    ### Response
     * If there is an error in the request parameters or the parameters are exceeded, the status is 404:
    ```
     HTTP 404 Not Found
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
         "detail": "Invalid page."
     }
    ```
2. The method accepts the `search` parameter and displays hints with possible continuations of object names.
    ### Request example 200 OK
     * `GET /api/geoinfo/?search=Kolh`
    ### Response
     * A successful request returns a list of matches, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
         "links": {
             "next": null
             "previous": null
         },
         "total_count": 6,
         "page_size": 10,
         "results": [
             Kolkhoz Mayak,
             Kolkhoz Leninskaya Iskra,
             Kolkhoz Krasnyy Prozhektor,
             Krasnaya Gorka,
             "Shkolkhe",
             "Kolhoz Zarya"
         ]
     }
    ```
    > Please note that the search additionally goes through alternative names of objects.
    ### Sample query without matches
     * `GET /api/geoinfo/?search=zxc`
    ### Response
     * If no match is found, an empty response is returned, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
         "links": {
             "next": null
             "previous": null
         },
         "total_count": 0,
         "page_size": 10,
         "results": []
     }
    ```
3. The method accepts the names of two objects (`g1`, `g2`),
including the name in Russian and displays their full and comparative information:
     * Object located to the north;
     * Do the time zones match;
     * Time zone difference (in hours).
    ### Request example 200 OK
     * `GET /api/geoinfo/?g1=Moscow&g2=Vladivostok`
    ### Response
     * A successful request returns complete and comparative information, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     {
     "links": {
         "next": null
         "previous": null
     },
     "total_count": 2,
     "page_size": 10,
     "results": [
         {
             "geonameid": 524894,
             "name": "Moscow",
             "asciiname": "Moskva",
             "alternatenames": "Maskva,Moscou,Moscow,Moscu,Moscú,Moskau,Moskou,Moskovu,Moskva,Məskeu,Moscow,Maskeu",
             "latitude": "55.76167",
             "longitude": "37.60667",
             "feature_class": "A",
             "feature_code": "ADM1",
             "country_code": "RU",
             "cc2": "",
             "admin1_code": "48",
             "admin2_code": "",
             "admin3_code": "",
             "admin4_code": "",
             "population": 13010112,
             elevation: 0
             "dem": 161,
             "timezone": "Europe/Moscow",
             "modification_date": "2023-01-12"
         },
         {
             "geonameid": 2013348,
             "name": "Vladivostok",
             "asciiname": "Vladivostok",
             "alternatenames": "Bladibostok,Uladzivastok,VVO,Vladivostok,Vladivostoka,Vladivostokas,Vladivostokium,Vlagyivosztok,Wladiwostok,Wladywostok,Władywostok,beulladiboseutokeu,fladyfwstwk,hai can wai,hai can wei,urajiosutoku,vi lativostok, vladivastak, vladivostok, w la di wx s txkh,wladywstwk,wldywwstwq,Βλαδιβοστόκ,Vladivostok,Uladzivastok,Վլադիվոստոկ,וולאדיוואסטאק,ולדיווס , व्लादिवोस्तॉक व्लादिवोस्तोक ವ್ಲಾಡಿವಾಸ್ಟಾಕ್,วลาดีวอสตอค,ვლადივოსტოკი,ウラジオストク, 海参崴,海參崴,블라디보스토크",
             "latitude": "43.10562",
             "longitude": "131.87353",
             "feature_class": "P",
             "feature_code": "PPLA",
             "country_code": "RU",
             "cc2": "",
             "admin1_code": "59",
             "admin2_code": "",
             "admin3_code": "",
             "admin4_code": "",
             "population": 604901,
             elevation: 0
             "dem": 40,
             "timezone": "Asia/Vladivostok",
             "modification_date": "2022-09-17"
         }
     ],
     "comparison": {
         "geographical_object_1": {
             "name": "Moscow",
             "population": 13010112,
             latitude: 55.76167,
             "timezone": "Europe/Moscow"
         },
         "geographical_object_2": {
             "name": "Vladivostok",
             "population": 604901,
             latitude: 43.10562,
             "timezone": "Asia/Vladivostok"
         },
         "The object is located north": "Moskva",
         "Time zones the same": false,
         "Time zone difference": "-7:00:00"
         }
     }
    ```
    ### Sample request without found object(s)
     * `/api/geoinfo/?g1=Moscow&g2=Abcgd`
    ### Response
     * A response is returned indicating the object(s) that could not be found, status `200 OK`:
    ```
     HTTP 200 OK
     Allow: GET, HEAD, OPTIONS
     Content-Type: application/json
     Vary:Accept
    
     [
         "Not found object g2 to comparison."
     ]
    ```
## Additional Information
## Testing
1. Creating fixtures for tests:
    * `python manage.py dump_fixtures`
2. Run all tests:
    * `python manage.py test geoinfo_apiapp.tests`

## Working with the Django admin panel
1. Create a superuser:
    * `python manage.py createsuperuser`
2. Go to the admin panel http://127.0.0.1:8000/admin/ as a registered superuser.