<h1 align="center">Alura Barber Website</h1>

<p align="center"><a href="https://ge-barbearia-alura.herokuapp.com"><img src="https://img.shields.io/static/v1?label=&message=Live_Demo&color=FC5C65&style=for-the-badge&logo=heroku" style="align-items:center"/></a></p>

<br>

Web Full-Stack project created to enhance my development skills. The Alura Platform proposed the website design on the HTML/CSS Training. Based on the course, I've developed the front-end using HTML, CSS, and a little bit of Javascript, while on the back-end, I've used the Django Framework from Python.
After all development, I deployed the website on Heroku, and you can access it on the Badge above.

</br>

# 🏁 Content Table

- [🏁 Content Table](#-content-table)
- [💻 How to Use It](#-how-to-use-it)
  - [⚠️ Requirements](#️-requirements)
  - [🔨 Installing and Configuring](#-installing-and-configuring)
  - [📄 Update Files](#-update-files)
  - [🚩 Running the Project](#-running-the-project)
  - [📝 Project Structure](#-project-structure)
- [🛠 Technology](#-technology)
- [✒️ Author](#️-author)


</br>

# 💻 How to Use It

## ⚠️ Requirements
Before starting, you'll need to have installed the following tools:

* [Git](https://git-scm.com)
* [Python](https://www.python.org/)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Besides that, you're going to need a code editor of your preference. I am used to the [VSCode](https://code.visualstudio.com/), but you are free to choose.

</br>

## 🔨 Installing and Configuring
</br>

```bash
# Clone this repository
$ git clone https://github.com/GeovanaSLima/Ge_Barber_Website.git
```

```python
## On the terminal, Access the Project Folder
$ cd C:/ProjectFolder

## Creat the Virtual Env
$ python -m venv ./venv       

## Activating the virtual env
$ ./venv/Scripts/activate    

## Install Django
$ pip install django          
```

## 📄 Update Files
</br>

On the ```./venv/Scripts``` folder, create a new file ```manage.bat``` and write:
```
@python "%VIRTUAL_ENV%\..\manage.py" %*
```

>_This code creates a windows executable file that refers to the manage.py path. So it lets you use 'manage' to run the ```manage.py``` from any folder_

</br>

This part is optional, only do it if you want to change the website language and time zone.

On the ```settings.py``` file:
```python
## Change the Language and Time Zone
LANGUAGE_CODE = 'pt_br'
TIME_ZONE = 'America/Sao_Paulo'
```

## 🚩 Running the Project
</br>

```python
## On the terminal (with the virtual en active)
$ manage runserver 
```

You should see the following message on the terminal:

<img src="https://raw.githubusercontent.com/GeovanaSLima/Ge_Recipes_Website/main/runserver.PNG">

</br>

When you click on the message [link](http://127.0.0.1:8000/), you'll be redirected to the project web browser.

</br>

## 📝 Project Structure
- BarberProject
  - barbearia
    - core
      - static
        - css
          - _reset.css_
          - _style.css_
        - img
      - templates
        - partials
          - __messages.html_
        - _base.html_
        - _contato.html_
        - _index.html_
        - _produtos.html_
      - _--init--.py_
      - _admin.py_
      - _apps.py_
      - _models.py_
      - _tests.py_
      - _views.py_
    - _--init--.py_
    - _asgi.py_
    - _settings.py_
    - _urls.py_
    - _wsgi.py_
  - _.gitignore_
  - _manage.py_
  - _Procfile_
  - _README.md_
  - _requirements.txt_


</br>

# 🛠 Technology

The following technologies were used on this project

</br>

<p align="center">
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="50" height="50"/> </a><a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="50" height="50"/> </a><a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="50" height="50"/> </a><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="50" height="50"/> </a><a href="https://www.postgresql.org" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="50" height="50"/> </a>

</p>

</br>

# ✒️ Author

<a href="https://learningdata.dev/sobre">  
 <img src="https://raw.githubusercontent.com/GeovanaSLima/GeovanaSLima/main/GitProfile.png" alt="Geovana Sousa"/>
  <p><b>Geovana Sousa 🚀</b></p></a>
<p><i>A passionate Developer ❤️</i></br>
   Get in touch! 👋🏽</p>


[![LearningData Badge](https://img.shields.io/badge/-LearningData-%23FC5C65?style=&logo=ghost)](https://learningdata.dev)
[![Portfolio Badge](https://img.shields.io/badge/-Portfolio-%238390A2?style=&logo=adobe)](https://geovanasousa.com)
[![Linkedin Badge](https://img.shields.io/badge/-Geovana-blue?style=&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/geovana--sousa/)](https://www.linkedin.com/in/geovana--sousa/) 
[![Gmail Badge](https://img.shields.io/badge/-geovanasslima-c14438?style=&logo=Gmail&logoColor=white&link=mailto:geovanasslima@gmail.com)](mailto:geovanasslima@gmail.com)
