# Family Photo Album
---
## Version 1.0
This is a simple family album based on Django(currently only displaying photos, video display function will be added later), which has an iframe interface for OpenWebUI and can be integrated with you AI

You will notice that there is a lot of things which are related to the word 'album2017'. That's because I split my family photos into two parts, one is photos before 2017 and the other one is after 2017. I'm lazy so I won't change it.

---
## Installation
There is no specific version of python, I used python 3.11.9. Of course, you can also create a virtual environment.
`git clone https://github.com/EMEMEMEMEMEMEMEMEMEM/FamilyPhotoAlbum.git`
`pip install django`
`pip install mysqlclient`

Makesure that your server has mysql on it
```
sudo apt update
sudo apt install mysql-server
mysql --version
    e.g.: mysql  Ver 8.0.42-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

And then create your database for you photos
```
mysql -u root -p
create database YOUR_DATABASE DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

Change the configuration in *FamilyPhotoAlbum/settings.py*
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_DATABASE_NAME',#Change it Here
        'USER': 'root',
        'PASSWORD': 'YOUR_PASSWORD',#Change it Here
        'HOST': '127.0.0.1',#default
        'PORT': 3306,#default
    }
}
```

The last thing before booting up the server
`python manage.py migrate`
`python manage.py makemigrations`

After a lot of configuration, boot up the server
`python manage.py runserver 0.0.0.0:8000`
Store your photos in */PhotoAlbum/static/media/XXXX/YYYY-MM-DD*
(I had written a python script which can sort photos into folders by the order of time,but I can't find it anywhere in my laptop, just use any AI to help you save some time.)

Access [http://YOURSERVER_IP:8000/mml/](http://YOURSERVER_IP:8000/mml/) Enter the absolute path of your photos in the */static/media/XXX/* and click the button.

Your photos will be shown in [http://YOURSERVER_IP:8000/album2017/](http://YOURSERVER_IP:8000/album2017/)

Replace the photos in */static/images/XXXXX* with your family members'photos.And change the things in **/static/templates/home.html**

For example:
`<img src="/static/images/male 001.JPG">`
There is a corresponding one above and below. Remember to change them all.

---
## OpenWebUI (optional)
In the *settings.py*, you can change the default settings your openwebui_url
`OPENWEBUI_URL = "http://localhost:8080"`
And change the settings in the *openwebui_embed.html*
```
<iframe id="openwebui-frame"
        src="http://YOUROPENWEBUI:8080"
        allow="clipboard-write; microphone">
</iframe>
```
A *wrong.html* is prepared.








<p style="text-align:right; margin: 0; font-size: 10px">
    Grade 9    2025/06/25
</p>