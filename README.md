# Wall App 
## Wall App is a website that allows users to register, login, and write on a wall.

## Prerequisites
* Django [https://www.djangoproject.com/download/](https://www.djangoproject.com/download/)
* VirtualEnv [here](https://virtualenv.pypa.io/en/latest/installation/)


## How to run
```
git clone https://github.com/BolaNasr/django_wallApp
cd django_wallApp
virtualenv env
. env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata data.json
```

## How to configure the mailing feature  
set the following env variables
```
export EMAIL_HOST_USER="your.email@gmail.com"
export EMAIL_HOST_PASSWORD="your password"
```
**Note**: you might need to configure your email to be used by less secure apps, for gmail use the following link [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps) 

# Run Server
```
python3 manage.py runserver

```

### **Note**: if you have loaded the fixture you will be able to login to the admin panel using the following creds  
**username:** admin  
**password:** admin1234  

### you will find also another user created, you can access this one using the following creds  

**username:** user1_test  
**password:** user1234  
