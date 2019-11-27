Innovaccer Summergeeks
==============================================

### Problem Statement

Given the visitors that we have in office and outside, there is a need to for an entry management
software.

### Technology Stack

-   Django

-   Javascript

-   HTML, CSS

-   Twilio SMS Services

### Instructions to install

1. Clone this repository:

   ```git clone <https://github.com/richa031/EntrySystem.git>```

2. Change directory

   ```cd visit```

3. Install dependencies

   ```pip install django```

   ```pip install django_twilio```

   ```pip install crispy_forms```

4. Generate Account SID, Authentication Token , Phone no

   Refer to this link - <https://www.twilio.com/>

5. Create a config.py file and add below mentioned details in it.
   ```
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_USE_TLS = True
   EMAIL_PORT = 587
   EMAIL_HOST_USER = 'HOST EMAIL ADDRESS'
   EMAIL_HOST_PASSWORD = 'YOUR PASSWORD'


   TWILIO_ACCOUNT_SID = 'TWILIO ACCOUNT SID'
   TWILIO_AUTH_TOKEN = 'TWILIO AUTHENTICATION TOKEN'
   TWILIO_PHONE_NUMBER= 'TWILIO PHONE NUMBER'


   SECRET_KEY = 'YOUR SECRET KEY'
   ```

6. Start the server

   ```python manage.py runserver```

You should get something like this when every step has been followed correctly:
   ```
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).
   November 26, 2019 - 17:22:45
   Django version 2.2.7, using settings 'visit.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

### Folder Structure:
![Capture](https://user-images.githubusercontent.com/32764563/69664139-c349c600-10ad-11ea-9f09-9dddc2835d6b.PNG)


![Capture1](https://user-images.githubusercontent.com/32764563/69664168-cfce1e80-10ad-11ea-9089-621e073cd2a0.PNG)


APP/ ENTRY SYSTEM
---------------

### 1\. WELCOME Page

Enter your phone number which you need to get entry with.

 - http://127.0.0.1:8000/ 

SAMPLE IMAGE -


![Screenshot (33)](https://user-images.githubusercontent.com/32764563/69664417-58e55580-10ae-11ea-81d8-3f18e131fdec.png)


### 2\. Enter your Details

Enter all the details of Visitor and Host given in the form and click CHECKIN button

http://127.0.0.1:8000/records  (methods supported - POST)

SAMPLE IMAGE -

![Screenshot (35)](https://user-images.githubusercontent.com/32764563/69691225-73dab880-10f4-11ea-89a0-e330beeb3949.png)

SAMPLE IMAGE - Email which the HOST gets after visitor checks in

![Capture4](https://user-images.githubusercontent.com/32764563/69691579-7a1d6480-10f5-11ea-80d3-0a0e8da2eca4.PNG)

![Capture5](https://user-images.githubusercontent.com/32764563/69691630-a802a900-10f5-11ea-9357-134b24b594fe.PNG)

SAMPLE IMAGE - SMS which the HOST gets after visitor checks in

![Capture3](https://user-images.githubusercontent.com/32764563/69691464-39255000-10f5-11ea-8ac5-fdd558df62c2.PNG)


 
### 3\. Checkout Page with Details

Details of visitor displayed

http://127.0.0.1:8000/checkout  (methods supported - POST)

SMAPLE IMAGE - 

SAMPLE IMAGE - Email which the VISITOR gets after visitor checks out (Checkout button)


### CONTACT

Richa Agarwal

Ph-9511510325

[Email01 -17ucs126@lnmiit.ac.in](mailto:Email-17ucs126@lnmiit.ac.in)

[Email02 ](mailto:Email-17ucs126@lnmiit.ac.in)<-richahp031@gmail.com>

