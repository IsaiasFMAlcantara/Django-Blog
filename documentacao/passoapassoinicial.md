# [<-](https://github.com/IsaiasFMAlcantara/Django-Blog) Passo a passo inicial
1. Criar ambiente virtual
    ```sh
    python3 -m venv myenv
    ```
1. Instalar Django
    ```sh
    pip install django
    ```
1. Criando projeto
    ```sh
    django-admin startproject myblog .
    ```
1. Criando app
    ```sh
    django-admin startapp core
    ```
1. Realizando o migrate
    ```sh
    python3 manage.py migrate
    ```
1. Startando o projeto
    ```sh
    python3 manage.py runserver
    ```
1. Criando super usuário (admin admin)
    ```sh
    python manage.py createsuperuser
    ```