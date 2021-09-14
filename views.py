
from django.shortcuts import render
import pyrebase
# Create your views here.

Config={
    'apiKey': "AIzaSyBH6RHwD8qt_okcO1IYd5B6aoTHHsCu-pw",
    'authDomain': "test-94280.firebaseapp.com",
    'databaseURL':"https://test-94280-default-rtdb.firebaseio.com",
    'projectId': "test-94280",
    'storageBucket': "test-94280.appspot.com",
    'messagingSenderId': "517281756557",
    'appId': "1:517281756557:web:eebb5e6235616242eaf9c4",
    'measurementId': "G-SZL9XTQ6B5"
}
firebase=pyrebase.initialize_app(Config)
authe=firebase.auth()
database=firebase.database()

def index(request):
    labour_name=database.child('labour').child('name').get().val()
    labour_sal=database.child('labour').child('sal').get().val()
    labour_sal12hr=database.child('labour').child('sal12hr').get().val()
    labour_sal8hr=database.child('labour').child('sal8hr').get().val()
    working_days=database.child('labour').child('day').get().val()
    
    return render(request,'index.html',{
        'labour_name':labour_name,
        'labour_sal':labour_sal,
        'labour_sal12hr':labour_sal12hr,
        'labour_sal8hr':labour_sal8hr,
        'working_days':working_days
        })