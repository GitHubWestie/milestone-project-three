# The Bike Shed

![mock-up img](/other-media/am-i-responsive.png)

## Strategy
The Bike Shed app is for cyclists who wish to keep a convenient collection of information about their bike/s and setup variables. The app allows users to create an account to login and store data securely before creating their bike or collection of bikes. Bikes can then be recalled for viewing, editing or deletion.

The intended user will be a cyclist who:
* Enjoys analysing data and fettling with their setup 
* Is looking to extract the most performance out of their bike/s
* Wants to record settings so they can easily be reverted back to if needed
* Wants to show their friends all the cool components on their bike 

The app will eventually also aim to connect riders via a ratings and selling platform.

The app is active and can be used [here](https://the-bike-shed-3d6351787c10.herokuapp.com/)

## Scope

### As a first time user I want:

* To have a convenient app to store data about my bikes
* To have a secure app to store sensitive data about my bikes such as a frame serial number or serial numbers for components
* To have sensitive information only visible to me 
* To intuitively understand how to use and navigate the app
* To easily add and remove bikes
* To easily add and remove and update components on those bikes
* To record settings for each of my bikes such as tyre pressures and suspension settings
* To input/upload service history

### As a returning user I want:

* To easily retrieve information about my bikes
* To easily retrieve settings for each bike
* To easily edit and otherwise manipulate information stored about my bikes
* To easily remove bike data 

## Features

### Sign Up/Sign In

![landing](/other-media/screenshots/landing.png) ![signup](/other-media/screenshots/signup.png) ![signin](/other-media/screenshots/sign-in.png)

Users will need to sign up and login to view their account and bike shed. User credential creation is controlled using form validation and passwords are hashed before being stored using Werkzeug.

After being successfully signed up or signing in users will be directed to the 'My Bike Shed' page to add their first bike.

### Navigation

![sidenav](/other-media/screenshots/sidenav.png)

All pages are accessible using the buttons within the app and these lead users through the app in an intuitive manner. For additional convenience, a sidenav is accessible from the top left burger menu which enables users to jump to any section quickly and easily.


### My Bike Shed

![my-bike-shed](/other-media/screenshots/mybikeshed.png)

This is where users bikes are stored and accessed once created. From here users can refer to their bike spec, edit bikes and delete bikes entirely. 

Bikes are easily identifiable at a glance by the manufacturer and model name. This is accompanied by a small icon to the left depicting the bike category.

    Settings for bikes can be accessed through each bike from here. User can record settings such as tyre pressures, suspension settings etc. 
    Record serial numbers for components where applicable and link to product pages.
    Leave themselves notes for when they return to tuning setup or a specific location.
    Last serviced/service due date

### Add bike

![add-bike-top](/other-media/screenshots/addbike-0.png) ![add-bike-bottom](other-media/screenshots/addbike-1.png)

An add bike function which will allow users to create a new bike and add it to their bike shed. Users will be presented with a form to complete which will capture various components. For the sake of convenience, at the point of creation users will only be required to complete the manufacturer and model fields and will be able to return to the bike at any time to complete the remaining fields. As the app can store potentially sensitive data such as frame serial number it will be hidden to all but the creator. 

### My Profile

![my-profile](/other-media/screenshots/myprofile.png)

Stores data about the user such as username, name, email etc. As the rider weight is crucial to bike setup this can also be captured here. 

### Future Feature Implementations
* Upload image of bike
* Upload invoice of most recent service
* Track service history
* Rate my ride - Enable users to view other users bikes and rate them
* Sell my bike/make me an offer - Users can sell or just make their bike available for offers if they're considering selling.
* Bike archive - bikes owned previously, date sold, how much for
* Choose if a bike is visible to other users
* Adjust app so that users bike form fields are entered into their own respective category databases on creation, building a collection of each category as they are created for example manufacturers, models etc.
* Polish look of app overall - The route functions and debugging plus customising Materialize took longer than I had anticipated and meant that I didnt get the app to look as good as originally planned.

## Structure

After careful consideration I opted for a non-relational database structure for this project. Realistically, relational or non-relational could have worked well, however I felt that given the potentially changeable nature of the data stored by users that a non-relational structure would suit the app better. 

![schema](/other-media/lucid-chart/the-bike-shed-schema.png)

The database schema helped to inform the presentation and flow of the app. The app structure follows the flow of the creation process and intuitively guides the user through that process using prompts to gather information about users bikes.

![flow chart](/other-media/lucid-chart/the-bike-shed-flow.png)

## Skeleton

![figma-lo-fi](/other-media/figma-files/My-Bike-Shed-lo-fi.png)

## Surface
![figma-hi-fi](other-media/figma-files/My-Bike-Shed-hi-fi.png)

## Testing

### User Stories

### Functionality
![test sheet]()

### Lighthouse Results

![add-bike-dt](other-media/lighthouse-results/add-bike-desktop-lighthouse.png) ![add-bike-mob](other-media/lighthouse-results/add-bike-mob-lighthouse.png)

![edit-bike-dt](other-media/lighthouse-results/edit-bike-desktop-lighthouse.png) ![edit-bike-mob](other-media/lighthouse-results/edit-bike-mob-lighthouse.png)

![landing-dt](other-media/lighthouse-results/landing-desktop-lighthouse.png) ![landing-mob](other-media/lighthouse-results/landing-mob-lighthouse.png)

![my-bike-dt](other-media/lighthouse-results/my-bike-desktop-lighthouse.png) ![my-bike-mob](other-media/lighthouse-results/my-bike-mob-lighthouse.png)

![my-bike-shed-dt](other-media/lighthouse-results/my-bike-shed-desktop-lighthouse.png) ![my-bike-shed-mob](other-media/lighthouse-results/my-bike-shed-mob-lighthouse.png)

![my-profile-dt](other-media/lighthouse-results/my-profile-desktop-lighthouse.png) ![my-profile-mob](other-media/lighthouse-results/my-profile-mob-lighthouse.png)

![sign-in-dt](other-media/lighthouse-results/sign-in-desktop-lighthouse.png) ![sign-in-mob](other-media/lighthouse-results/sign-in-mob-lighthouse.png)

![sign-up-dt](other-media/lighthouse-results/sign-up-desktop-lighthouse.png) ![sign-up-mob](other-media/lighthouse-results/sign-up-mob-lighthouse.png)

### Validator Results

![html](other-media/validator-results/html/add-bike-validation.png) ![html](other-media/validator-results/html/edit-bike-validation.png)

![html](other-media/validator-results/html/landing-validation.png) ![html](other-media/validator-results/html/my-bike-shed-validation.png)

![html](other-media/validator-results/html/my-bike-validation.png) ![html](other-media/validator-results/html/my-profile-validation.png)

![html](other-media/validator-results/html/sign-in-validation.png) ![html](other-media/validator-results/html/sign-up-validation.png)

![css](other-media/validator-results/css/css-validation.png)

## Technologies

### Languages Used
* HTML
* CSS
* JavaScript
* Python
* Jinja

### Frameworks and Libraries
* [Materialize](https://materializecss.com/about.html) by Google
* [MongoDB](https://www.mongodb.com/) by MongoDB Inc.

## Deployment & Local Development

### Github

This project can be cloned or forked in order to make a local copy on your own system.

You will need to install packages found within the *requirements.txt* file and set environment variables in an *env.py* file saved to the root directory.

* `pip install -r requirements.txt`.

env.py

    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
    os.environ.setdefault("MONGO_URI", "YOUR_MONGO_URI")
    os.environ.setdefault("MONGO_DBNAME", "the_bike_shed")

#### How to Fork

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/GitHubWestie/milestone-project-three)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

#### How to Clone

You can clone the repository by following these steps:

1. Go to the [The Bike Shed GitHub repository](https://github.com/GitHubWestie/milestone-project-three) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	* `git clone https://github.com/GitHubWestie/milestone-project-three.git`
7. Press Enter to create your local clone.
8. Install required packages according to the requirements.txt In your IDE terminal type:
    * `pip install -r requirements.txt`
9. Create env.py file in root directory and assign environment variables
10. Create a new empty repo on GitHub - do not initialise with a README
11. In your IDE terminal type the following commands to setup your repository:
    * `git remote add origin https://github.com/your-username/new-repo.git`
    * `git push -u origin main`

### MongoDB

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To set up a MongoDB Database URI, sign-up on the MongoDB site, then follow these steps:

* The name of the database on MongoDB should be "__the_bike_shed__".
* The collection(s) needed for this database should be "__my_bike_shed__", "__categories__", and "__users__.
* Click on the __the_bike_shed__ name created for the project.
* Click on the __Connect__ button.
* Click __Drivers__.
* Copy the connection string and assign it as the MONGO_URI value in the env.py file, making sure to replace `<password>` with your database password (not your account password) and insert the database name after mongodb.net/

    `mongodb+srv://<username>:<password>@cluster0.6wq2wyp.mongodb.net/<database_name>?retryWrites=true&w=majority&appName=Cluster0`
* Finally, navigate to __network access__ in the left pane and change the IP address in the IP access list 0.0.0.0

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com)

Deployment steps are as follows:

This process connects your GitHub repository to Heroku. Alternatively you can follow the instructions on Heroku to deploy using the Heroku CLI

1. Select __New__ in the top-right corner of your Heroku Dashboard, and select __Create new app__ from the dropdown menu.
2. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select __Create App__.
3. From the new app __Settings__, click __Reveal Config Vars__, and set your environment variables.

| Key | Value |
| --- | --- |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | the_bike_shed |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

4. Back in the deploy tab in Heroku choose connect to github and connect your github account. 
5. Type or paste the repository name into the search box and select your repository
6. Select __Automatic Deployment__ from the Heroku app.
7. Select the __main__ branch to deploy from and click __deploy__

Heroku will now build the app. When finished click view or open app from Heroku to visit the deployed version.

### __IMPORTANT__

A Procfile must be present for Heroku to deploy correctly and all requirements packages must be installed. These are included in the github repo.

You can install this project's requirements using:

- `pip install -r requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace __app.py__ with the name of your primary Flask app name; the one at the root-level*

__NOTE:__ The Procfile uses a capital P and doesn't have a file extension on the end.


