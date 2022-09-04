from hackerforms import * 

# testing how to make a single page

contact = Page().read("Name") \
                .read_email("Email") \
                .run("Send")

email = contact["Email"]
name = contact["Name"]

#or 
# Name, Email = contact.values()

Page().display(email)\
      .display(name)\
      .run("Got it!")
# Alternative way to use values

# get url params 
#abstra.run/:formId?token=123
#print(url_params) # { 'token': 123 } 