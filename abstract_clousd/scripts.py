from hackerforms import * 

# tesing scripts and utils of the hackerforms lib
# just run the script 

name = read("what is your name ?")
phone = read_phone("Phone number ?")
number = phone.raw # eg: 5521999999999
masked = phone.masked # eg: +55 (21) 99999-9999
email = read_email("What is your email?")
age = read_number("Age ? ")
ans = read_textarea("What kind of things are you building with Abstra Cloud?")
#display multple options (check boxes )
options = read_multiple_choice(
    "Are you",
    ["white","black","retarded"]
    )

# read a file  
fileResponse = read_file("Upload your .txt file")
file = fileResponse.file # File object
url = fileResponse.url # Url to the file
content = fileResponse.content # Raw file content

# cards with images
card = read_cards('Choose your character', [
{
  'title': 'Charmander',
  'image': 'https://img.pokemondb.net/sprites/sword-shield/icon/charmander.png',
  'description': 'Fire'
},
{
  'title': 'Bulbasaur',
  'image': 'https://img.pokemondb.net/sprites/sword-shield/icon/bulbasaur.png',
  'description': 'Grass'
},
{
  'title': 'Squirtle',
  'image': 'https://img.pokemondb.net/sprites/sword-shield/icon/squirtle.png',
  'description': 'Water'
}])

#drop down
drop_down = read_dropdown("Choose a color", ["Red", "Green", "Blue"])

# tags 
tags = read_tag("Type and press enter to add a tag",
initial_value=["Red", "Green", "Blue"])


#list of inputs (form)
item = ListItemSchema()
item.read("Name")
item.read_email("Email")
form = read_list(item,min=1,max=3)
# ans = [{'Name': '', 'Email': ''}]

#password reading 
passw = read_password("Insert your password below")

#rating 
rating = read_nps('How likely are you to recommend Abstra Cloud?', min_hint='No way!', max_hint='Hell yeah!')

#display label / text 
display("Hello world!")

#display image
display_image(
 "https://placekitten.com/200/200",
 subtitle="Meooow"
)

#display link
display_link(
 "https://console.abstracloud.com",
 link_text="Abstra Cloud Homepage"
)

#dowload link
display_file(
 "https://placekitten.com/200/300",
 download_text="Click here to reveal the secret"
)

#display plot
# figure is suppose to be a matplotlib object
figure = None
display_plotly(figure)


#display map
display_iframe("https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d2965.0824050173574!2d-93.63905729999999!3d41.998507000000004!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sWebFilings%2C+University+Boulevard%2C+Ames%2C+IA!5e0!3m2!1sen!2sus!4v1390839289319",
           width=300, height=250)

           
print(name)
print(phone)
print(age)
print(ans)
print(options)