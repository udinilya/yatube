# Проект - социальная сеть ‘yatube’

Стэк: Python, Django, DRF, API, SQLite, unittest, pytest, git.
Цель: Создание проекта - социальная сеть ‘yatube’ в котором пользователи могут регистрироваться, публиковать посты, оставлять комментарии на посты других пользователей, а также подписываться друг на друга. Проект был покрыт тестами. Были написаны тесты, проверяющие соответствие view-функции и html-шаблона, контекст html-шаблонов. Также были написаны тесты для форм.

Следуя инструкциям ниже, вы получите копию проекта, которая будет запущена на вашем локальном компьютере (Linux Ubuntu) с использованием контейнеризации Docker. Примечания о том, как развернуть проект приведены в разделе развертывание.

### Установка и развёртывание:

1. Самостоятельно установите на своём локальном компьютере Docker. Инструкция есть в официальной документации Docker.
2. Скопируйте на свой локальный компьютер файл с инструкцией docker-compose.yaml из репозитория. В соответствии с данной инструкцией на ваш компьютер будет установлен и развернут:
   - контейнер Docker с социальной сетью 'yatube' из образа, хранящегося в репозитории DockerHub
   - контейнер Docker с БД PostgreSQL из официального образа, хранящегося в репозитории DockerHub
   - автоматически будет выполнена миграция, для создания таблиц в установленной БД
3. Запустите приложение с использованием команды docker-compose up

```
sudo docker-compose up
```
4. Откройте проект в брайзере и убедитесь, что все работает
   
```
http://127.0.0.1:8000/
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

