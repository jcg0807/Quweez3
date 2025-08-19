

# OBJOR Quiz No.3

# Django Job Finder

This is a simple Django application that allows users to register, post jobs with optional images, and view a feed of newly uploaded jobs.

## Features

- User register, login and logout.
- Create Job Openings with text and optional image uploads.
- View a list of all posted jobs. .

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Clone the Repository

```bash
https://github.com/jcg0807/Quweez3.git
cd Activity
```

### Install Pillow
```bash
python -m pip install Pillow
```
### Make migrations & migrate
```bash
python manage.py makemigrations 
python manage.py migrate 
```
### Run the Server
```bash
py manage.py runserver
```

## How to Use

Register an Account
Navigate to http://127.0.0.1:8000/register/.
Fill out the registration form.

Login
If you registered, you'll be automatically logged in.

Create a Job post
Once logged in, click on the "Click Here to a Create Job Opening" link or navigate to http://127.0.0.1:8000/tweet/create/.
Enter your text.
or, upload an image.
Click "Publish" to post.

View Newly Added Jobs
The home page (http://127.0.0.1:8000/) displays all Jobs posted even when logged out.
