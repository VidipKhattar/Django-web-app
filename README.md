# Campus Builder

## Prerequisites

1. Setting up Environment

	To start using the Django based web application, navigate to the project folder using your command prompt and type the following command to set up the virtual environment in said directory

		```$ python3 -m venv env```

	Once the virtual environment is set up, it will need to be activated using the following command:

	```$ source env/bin/activate```

	If the activation was successful, then you’ll see the name of your virtual environment, (env), at the beginning of your command prompt. This means that your environment setup is complete.

	Next Django, along with crispy forms, needs to be installed in order to run the application. Once you’ve created and activated your Python virtual environment, you can install Django into this dedicated development workspace using the following command:

```(env) $ python -m pip install Django``` 

```(env) $ python -m pip django-crispy-forms```

This command fetches the django and django-crispy-forms packages from the Python Package Index (PyPI) using pip.

Using shell to navigate to the directory containing the `manage.py` file. We can then use the following command to run the app server

```(env) $ python manage.py runserver```

You will get the following message

```shell
Watching for file changes with StatReloader

Performing system checks...

System check identified no issues (0 silenced).

March 03, 2022 - 09:20:52

Django version 4.0.3, using settings 'worldBuilder.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CONTROL-C.
```
The web app server will now be running at the location: ```http://127.0.0.1:8000/```

which can be copy pasted into any preferred web browser


## Concept:

We wanted to create an app that would allow our users to engage with the layout and terrain of Exeter University campus as well as the buildings that make up our University without requiring large amounts of time interacting with their phone. 

The primary aim of the game is to build streaks, which can be achieved by visiting more buildings in the university consecutively. These streaks are shown as plants that grow over time as the streak increases. Each building has a different plant associated with it so you can grow your virtual garden by checking in. There are collectables, such as gnomes or watering cans, set by the game keepers for building of the day which can help publicise events in that location and encourage exploration outside the buildings related to the degree.

To achieve this we have created a Campus Builder app. In its current prototype form and contains key functionality. The app has decided Garden/Wildlife theme, this will bring all the pages together and give the app a cottage core like aesthetic. This was chosen by showing it to potential users and seeing it had a very positive reaction. We have attempted to make the theme Dyslexia friendly and accessible using colours, which work with screen filters, and fonts.

## Walkthrough:


1. Welcome Page

When you first open up the app it will have a base page, on this page will be the options to register as a new user, login as an existing user, or to hear about the game's rules and instructions. All of our buttons have log icons to bring the garden theme to life.

2.  Registration Page

When you first register with our app you will put in some basic personal information. This will be stored in a database in accordance with DPA 2018 and GDPR 2018 standards. There will be a tick box to give permission for location use which will be used throughout the app.

3. Login Page

The login page will be very standard, although decorated with the same garden theme. It will ask for a username and password, set up during registration, and then direct them back to their map homepage

4. Map page

Our map page is one of our most complex pages and will be the default page once someone has logged in. There will be a map of the campus and you will be able to press a ‘check-in’ button to manually update your current place on the map. If this is the first entry of the day then this will be marked as a streak. It will display the closest building you have checked in at.

5. Profile Page

Our profile page will have access to all of the information we have about that user. It will also contain an area where users can look through the streaks they have earned by frequently visiting buildings. This also includes a shelf that contains all the plants for the buildings you have streaks with to encourage users to check in so as to grow their plant by achieving longer streaks.
