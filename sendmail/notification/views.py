from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "BDMTrZsskCQCVOq0mIVRV0Af-glf-ZgYXZlNemn8GKKmn9KejcrEv78vaVZ7pFjcaqm-UPgZlC1l0BWSDFJWv1Y"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())
    
def send(request):
    resgistration  = [
    ]
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")


def main(request):
    
    return render(request, 'index.html')


def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyDHG4AtAV99u6qXc-RyspPJZnCrW52gy0M",' \
         '        authDomain: "sendmail-4d49f.firebaseapp.com",' \
         '        databaseURL: "",' \
         '        projectId: "sendmail-4d49f",' \
         '        storageBucket: "sendmail-4d49f.appspot.com",' \
         '        messagingSenderId: "823058153927",' \
         '        appId: "1:823058153927:web:16a8014122f3fe57f699e2",' \
         '        measurementId: "G-YSEK1QR2N8"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")