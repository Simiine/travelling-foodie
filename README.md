# Travelling Foodie
Travelling Foodie is more than just a site for people to share recipes from around the world. It is a site that allows people to share their travel experiences that centers around food. For the lovers of food and travel. A way of learning about different cultures, connecting with people on something as wonderful and wholesome as food. 

![responsive design picture](static/images/responsive-design-picture.png)

## Planning
Working in Sprints
Developing Issues and a Project Board

## UX Design

### User Stories
#### Site User
- As a Site User I can see a list of posts so that I can choose which one to view
- As a site user I can click on a post so that I can view the post details
- As a Site User I can view the number of likes on a post so that I can see which recipes are more popular
- As a Site User I can like or unlike a post so that I can interact with the content
- As a Site User I can view the comments on a post so that I can read the conversation
- As a Site User I can comment on posts so that I can be part of the conversation
- As a Site User I can create, read, update and delete posts so that I can manage the site's content
- As a Site User I can register an account so that I can have access to the site
- As a Site User I can log in/out so that I can interact with the site
- As a Site User I can view a paginated list of posts so that I can easily select a post to view
#### Site Admin
- As a Site Admin I can view the number of likes on a post so that I can see which recipes are more popular
- As a Site Admin I can view the comments on a post so that I can read the conversation
- As a Site Admin I can approve or disapprove comments so that I can filter out inappropriate comments
- As a Site Admin I can create, read, update and delete posts so that I can manage the site's content
- As a Site Admin I can tell users about the website so that I can inform users about the site and why they should return

### Site Owner Goals
As the owner of this site, my goals are to:
- Create a site where people can create and posts
- Create a site where people can see posts on different experiences
- Create a site where people can like and unlike posts
- Create a site where people can see the number of likes on a post
- Create a site where people can comment on posts
- Create a site where people can view comments on posts
- Create a site where people can register an account
- Create a site where people can log in and out 

### Design Choices
#### Typography
#### Colour Palette
I chose to go for a very rich colourful palette. To complement the theme of site all about experiencing amazing food around the world. I chose to go for a cobination of oranges, reds and teals. The colour palette I generated is available at https://coolors.co/f7a133-f47a33-f14738-dc3c35-369184-61bda9
![Colour Palette](static/images/Colour-palette.png)
#### Logo
In order to showcase the theme of the site I designed a logo to showed a stack of plates with a plane going around it.

![Logo](static/images/logo.png)

### Wireframes
#### Desktop
#### Mobile

## Information Architecture
![SQL diagram](static/images/sql-diagram.png)

## Features
### Existing Features
#### Home Page
![name](static/images/)

#### About Page
![name](static/images/)

#### Log In Page
![name](static/images/)

#### Registration Page
![name](static/images/)

#### Experience Details Page
![name](static/images/)

#### Add experience Page
![name](static/images/)

#### Like
![name](static/images/)

#### Comment
![name](static/images/)

### Future Features

## Testing

### Manual Testing
#### Easy to navigate and clear instructions
#### View Experiences
#### Register
#### Login
#### Like
#### Comment
#### Add experience
#### Edit experience
#### Delete experience

### Automated Testing

#### PEP8
I passed the code through [PEP8](http://pep8online.com/) and the result showed all right with no issues.
![PEP 8 Picture](static/images/)

#### HTML

#### CSS

#### Javascript

#### Lighthouse

### Bugs
#### Adding django ratings field 
Following the steps to add the ratings field. The last step was python manage.py syncdb but the terminal gave an error of SyntaxError: invalid syntax
#### Summernote error
clean() got an unexpected keyword argument 'styles'

I fixed this iss with summernote by removing the summernote import from the top of the models.py file and changing....

## Deployment
The live deployment can be found using the following URL - https://events-planner-p3.herokuapp.com/

I deployed this project in Heroku using the following steps:
1. Log In to Heroku
2. From the Heroku dashboard, click on "New" and in the drop-down click "Create new app"
3. Create a unique name for the project, select your region and click "Create app"
4. Navigate to the Settings tab
5. Scroll down to config var and click on "Reveal Config Vars"
   - In the field for KEY enter CREDS 
   - In the field for VALUE paste in all the content from the creds.json file. 
   - Click "Add"
6. Using the code institute template, you must add another config var
   - In the field for KEY enter PORT
   - In the field for VALUE enter 8000
7. Scroll down to buildpacks and click on "Add buildpack"
   - Select python and click "Save changes"
   - Select nodejs and click "Save changes"
   - Make sure python is on top and nodejs underneath
8. Navigate to the Deploy tab at the top of the page
9. Go to deployment method and select "GitHub"
10. Confirm you want to connect to GitHub by clicking "Connect to GitHub"
    - Insert repository name and click "Search"
    - Click "Connect" to link up Heroku app to the GitHub repository code
11. Scroll down and choose a deployment method 
    - In manual deploy click "Deply Branch"
    - Then click on "Enable Automatic Deploys" 
      - This allows Heroku to rebuild your app every time you push a new change to your code to GitHub

## Technologies Used
* Python
* Javascript
* HTML
* CSS
* Bootstrap 4
* Django
* Cloudiary
* Heroku

## Credits

## Support
* Richard Wells Code Institute Mentor.