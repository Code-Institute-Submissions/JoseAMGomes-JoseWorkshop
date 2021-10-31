![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

#JOSEWORKSHOP website
[View the live project!](https://joseworkshop.herokuapp.com/)

This website was created for my forth milestone project and its goal is to provide an easy and elegant way of finding and buying interfaces.
## User Experience (UX)
 ### User Stories
     
    1.1- As a costumer 
        1.1.1- I need to view a list of projects;
        1.1.2- I need to view indivudual project details;
        1.1.3- I need to know how much is in my shopping bag going to cost me as a navigate through website;
        1.1.4- I need to sort a list of projects;
        1.1.5- I need to search a project by name or description;
        1.1.6- I need to see what projects I have in shopping bag;
        1.1.7- I need to be able to pay without complications;
        1.1.8- I need to view an order confirmation after making the payment;
        1.1.9- I want to easily recognise what the website is about;
        1.1.10- I need to navigate easily and fluidly through the website;
    
    1.2- As a user
        1.2.1- I must be able to sign in and out together with register without problems with warnings in case any errors are made;
        1.2.2- I want to recover my password in case i forget it;
        1.2.3- I want to receive an email after registering;
        1.2.4- I want to be able to see my order history;

    1.3- As an owner
        1.3.1- I want to add, edit and remove projects;
    
2.1-Homepage Wireframe
[Home Desktop Wireframe](https://share.balsamiq.com/c/dGPZyL1vLp6BsEsih4piae.png)


2.2-projects page Wireframe
[projects Desktop Wireframe](https://share.balsamiq.com/c/6rvDUUcwwGCVdPmbsBTErM.png)


2.3-My Account page Wireframe
[My Account Desktop Wireframe](https://share.balsamiq.com/c/rb6T1zzqTRFR7heJCWewfN.png)


### Design

    3.1- Color Scheme
    The colors used are black and white and blue.

    3.2- Typography
    In this website the home page title is written in dancing script while all the other text is Lato. 

    3.3- Images
    The included in the website to give context and information do not belong to the user including the actual projects that thet portray. They are used for example purposes only.
## Features

    4.1- Website designed to be responsive on all sizes;
    4.2- Website uses font awesome to make the looks more appealing and functional.
    4.3- All CRUD (Create, Read, Update, Delete) are working together with a search funtionality that is key to any website.
    4.4- All static files are saved in s3.

## Technologies Used

### Languages Used

    5.1- HTML5;
   
    5.2- CSS3;

    5.3- Javascript

    5.4- Python3

### Frameworks, Libraries and Programs Used

    6.1- Bootstrap 4.4.1:
    Used to style and make website responsive;

    6.2- Javascript:
    Used to initialize some components;

    6.3- Google Fonts:
    Used to import Dancing Script;

    6.4- jQuery:
    Used to make navigation bar responsive and make the dropdown button work together with some materialize options;

    6.5- GitHub:
    Used to store and manage the project;

    6.6- Balsamiq:
    Used to create my Wireframes;

    6.7-Django:
    Used to make all the project;

    6.8- Heroku:
    Used to deploy project;

    6.9- s3:
    Used to save static files;

## Testing

The website's code passed both W3C HTML5 test and CSS3 test.

### Testing User Stories
1.1.1- I need to view a list of projects;
    Test #: 1
    Action Taken: Went to projects page.
    ﻿"After" State: All projects shown.
    ﻿Test Result: Successful.

1.1.2- I need to view indivudual project details;
    Test #: 1
    Action Taken:  Pressed image on projects.
    ﻿"After" State: Project details page opened
    ﻿Test Result: Successful

1.1.3- I need to know how much is in my shopping bag going to cost me as a navigate through website;
    Test #: 1
    Action Taken:  Added a project and roamed through all pages.
    ﻿"After" State: Shopping bag amount remained correct on all pages
    ﻿Test Result: Successful

1.1.4- I need to sort a list of projects;
    Test #: 1
    Action Taken:  Pressed sort by rating.
    ﻿"After" State: All projects were shown sorted by rating
    ﻿Test Result: Successful

    Test #: 2
    Action Taken:   Pressed sort by price.
    ﻿"After" State:  All projects were shown sorted by price
    ﻿Test Result: Successful

1.1.5- I need to search a project by name or description;


    Test #: 1
    Action Taken:  Checked if no results were found page would crash.
    ﻿"After" State: No reviews shown but page works as intended
    ﻿Test Result: Successful

    Test #: 2
    Action Taken:  Searched for example1
    ﻿"After" State: Project with example1 in name was found.
    ﻿Test Result: Successful

1.1.6- I need to see what projects I have in shopping bag;
    Test #: 1
    Action Taken:  Pressed shoping bag icon.
    ﻿"After" State: All projects on shopping bag were listed correctly
    ﻿Test Result: Successful


1.1.7- I need to be able to pay without complications;

    Test #: 1
    Action Taken:  Tried payment funtionality.
    ﻿"After" State: Order details shown in the end after successfully paying.
    ﻿Test Result: Successful

1.1.8- I need to view an order confirmation after making the payment;
    As tested before
    Test #: 1
    Action Taken:  Tried payment funtionality.
    ﻿"After" State: Order details shown in the end after successfully paying.
    ﻿Test Result: Successful
1.1.9- As a user I want to easily recognise what the website is about.

    Home page clealy explains what the purpose of the website is.
    
    Test #: 1
    Action Taken: Tried link "go" in home page.
    ﻿"After" State: Taken to projects page.
    ﻿Test Result: Successful
    
1.1.10- I need to navigate easily and fluidly through the website;

    All Navigator links work perfectly and are responsive. Turns into dropdown menu when it is supose to;
    
    Test #: 
    Action Taken: Click on all links in Nav bar
    ﻿"Before" State: No hoover or change.
    ﻿"After" State: Correct HTMLs were loaded.
    ﻿Test Result: Successful
    


1.2.1- I must be able to sign in and out together with register without problems with warnings in case any errors are made;

    Register is working as intended and in case of error it gives a warning massage.

    Test #: 1
    Action Taken: Tried pressing register:
    ﻿"After" State: Register page opened
    ﻿Test Result: Successful

    Test #: 2
    Action Taken: Tried registering new account
    ﻿"After" State: new user was created message received
    ﻿Test Result: Successful

    Test #: 3
    Action Taken: Tried submiting with empty fields
    ﻿"After" State: "Please fill out this field" message received on whatever field is blank.
    ﻿Test Result: Successful

    Test #: 4
    Action Taken: Tried submiting with previously used fields on other users
    ﻿"After" State: Expected warning provided.
    ﻿Test Result: Successful

1.2.2- I want to recover my password in case i forget it;
    Test #: 1
    Action Taken:  Clicked recover password.
    ﻿"After" State: Funtionality went through as intended
    ﻿Test Result: Successful

1.2.3- I want to receive an email after registering;
    Test #: 1
    Action Taken:  Registered under temp email.
    ﻿"After" State: Email received asking for confirmation.
    ﻿Test Result: Successful

1.2.4- I want to be able to see my order history;
    Test #: 1
    Action Taken:  Pressed profile page as registered user.
    ﻿"After" State: Order history shown.
    ﻿Test Result: Successful

1.3.1- I want to add, edit and remove projects;
    
     Test #: 1
    Action Taken: Tried going to add page.
    ﻿"After" State: Empty box ready for user input on one of the fields
    ﻿Test Result: Successful

     Test #: 2
    Action Taken: Tried submiting a new project on add page.
    ﻿"After" State: New project added
    ﻿Test Result: Successful

     Test #: 3
    Action Taken: Tried pressing Edit button
    ﻿"After" State: Edit page open with project fields.
    ﻿Test Result: Successful

     Test #: 4
    Action Taken: Tried submiting edited info.
    ﻿"After" State: Details were edited successfully
    ﻿Test Result: Successful
  
     Test #: 5
    Action Taken: Tried deleting a project
    ﻿"After" State: Projected was deleted message and my project page opens without deleted review.
    ﻿Test Result: Successful

## Further Testing

    Website was tested on Firefox and Chrome on all diferent sizes from mobile to desktop.
    Friends and family tested and critiqued website which helped with some last few design details.

## Credits

### Code 

Website was made based on the walkthrough project provided by code institute on boutique ado.


### Content 

    All content was written by the developer or taken/adapted from walkthrough project.

### Media

    Homepage is from the google images and all other images where taken from bootstrap themes.

## Deployment 

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account so that we can modify it without being worried about changing the orinal repository.

    1-To do this log in to GitHub and locate the GitHub Repository;

    2-At the top of the Repository just above the "Settings" Button press the "Fork" Button;

    3-You will now have a forked vertion of the original repository in your GitHub account;

### Making a Local Clone

    1-Log in to GitHub and locate the GitHub Repository;

    2-Under the repository name, click "Clone or download";

    3-To clone the repository using HTTPS, under "Clone with HTTPS", copy the link;

    4-Open Git Bash;

    5-Change the current working directory to the location where you want the cloned directory to be made;

    6-Type git clone, and then paste the URL you copied previously;

    7-$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

    8-Press Enter. Your local clone will be created.

## Acknoledgements

My Mentor for guiding me and making sure I dont skip important steps. Special thanks to code institute online tutors that helped me through all this course. I work for NHS(englands health service) and try how to code part-time. So without the tutor helping me solve and teach me I would never have been able to complete my projects. So THANK YOU!