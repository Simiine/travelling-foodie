# Travelling Foodie
Travelling Foodie...
![responsive design picture](static/images/)

## Planning
Working in Sprints
Developing Issues and a Project Board

## UX Design

### User Stories
#### Site User
#### Site Admin

### Site Owner Goals

### Design Choices
#### Typography
#### Colour Palette
#### Logo

### Wireframes
#### Desktop
#### Mobile

## Information Architecture
SQL Link - 
![SQL diagram](static/images/)

## Structure
### Flowchart 
![Flow chart picture](static/images/)

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