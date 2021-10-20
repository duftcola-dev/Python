
** default credentials
    port : **usually 465 for most smtp servers
    host : **smtp.gmail.com when using gmail hosts
    user: somegmailaccount@gmail.com
    password : password of somegmailaccount@gmail.com

*** test mail address created for this app 

    pythonappservicemail@gmail.com
    pythonappservice


sudo python -m smtpd -c DebuggingServer -n localhost:1025

** being localhost the address and 1025 the port