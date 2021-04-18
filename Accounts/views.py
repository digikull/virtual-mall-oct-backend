from django.shortcuts import render
from django.contrib.auth.models import User
from . models import Profile
from .serializers import ProfileSerializer

from django.http import JsonResponse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from hashids import Hashids


from rest_framework.response import Response

from rest_framework.decorators import api_view

import smtplib




@api_view(['POST'])
def Sendemail(request):
    user_email = User.objects.filter(email = request.data['email']).values_list('email')
    if user_email.exists():
        sender_email = "gingertestuser1245@gmail.com"
        rec_email = user_email[0][0]
        password = "stoxvnvworbwyxcs"
        user_id = User.objects.filter(email = request.data['email']).values_list('id')
        gen_id = user_id[0][0]
        hashids = Hashids()
        encrypted_User_id= hashids.encode(gen_id)
        print(encrypted_User_id)
        # do_encrypt = token_hex(encrypted_User_id)
        forget_passwordlink = " http://localhost:3000/ResetPassword "
        message = 'MIMEText(u"<a href="'+forget_passwordlink+'">abc</a>","html")' + encrypted_User_id
        msg = MIMEMultipart('alternative')
        msg['Subject'] = " this is the link"
        msg['From'] = "gingertestuser1245@gmail.com"
        msg['To'] = "kadamsandy34@gmail.com"
        frontend_url = "http://localhost:3000/Resetpassword"
        text = "Hi!\nHow are you?\nHere is the link you wanted:"
        html = '<html> <head></head> <body><p>Hi!<br> How are you?<br> Here is the <a href="{0}/{1}">http://localhost:3000/Resetpassword</a> you wanted.</p></body></html>'.format(frontend_url, encrypted_User_id)
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)
      
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        
        server.sendmail(sender_email, rec_email, msg.as_string())
        server.quit()

        return Response({'msg':'email sent','email':encrypted_User_id})
    else:
        return Response({'msg':'invalid email!'})

@api_view(['PUT'])
def password_change(request,id):
    hashids = Hashids()
    dec_id = hashids.decode(id)
    decrypted_id = dec_id[0]
    print(decrypted_id)
    person = User.objects.get(id = decrypted_id)
    person.set_password(request.data['password'])
    person.save()
    try:
        return Response({'msg':'password update Successfully','id':decrypted_id})
    except Exception as e:
        print(str(e))

     
    
        
