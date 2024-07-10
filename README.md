# The Bike Shed

![mock-up img]()

## Strategy
The bike shed app is for cyclists who wish to keep a convenient collection of information about their bike/s and setup variables. 

The intended user will be a cyclist who enjoys analysing data and fettling with their setup to extract the most performance out of their bike/s in a variety of different environments. The app will also aim to connect riders via a ratings and selling platform.

## Scope

### As a first time user I want:

* To have a convenient app to store data about my bikes
* To have a secure app to store sensitive data about my bikes
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

## Features

### Login/register
    Users will need to sign up and login to view their account and bike shed
    After successful sign up navigated directly to 'My Bike Shed' page to prompt user to add their first bike
    
### Add bike
    An add bike function which will allow users to create a new bike and add it to their bike shed.
    Users will be prompted for information during the creation process(be nice if it was a modal)
    Sensitive information such as frame number will only be visible to the creator
    An example bike will be pre-made in the bike shed which the user can delete at any time.

### My Bike Shed
    Initially populated with an example bike for new users to experiment with
    This is where users bikes are stored and accessed once created
    Setting for bikes accessed through each bike from here. User can record settings such as tyre pressures, suspension settings etc. 
    Record serial numbers for components where applicable and link to product pages.
    Leave themselves notes for when they return to tuning setup or a specific location.
    Last serviced/service due date

### My Profile
    Stores data about the user such as user name, name, email etc.

### Future Feature Implementations
    Upload invoice of most recent service evidence
    Track service history
    Rate my ride - Users can view other users bikes and rate them
    Sell my bike/make me an offer - Users can sell or just make their bike available for offers if they're considering selling.
    Bike archive - bikes owned previously, date sold, how much for
    Choose if a bike is visible to other users

## Structure

The data structure will be in the form of a NRDBS as this seems the most suitable data structure for this project.
The app structure will follow the flow of the creation process and intuitively guide the user through that process using prompts to gather information about users bikes.
Should an error occur an error page will display that will provide a link back home
The front-end will likely follow a tree structure but will experiment with nested lists, hub and spoke and dashboard.
Would be useful if certain options were saved after being created for example bike manufacturer once created by a user could be available for all users from a list, gradually creating a user generated list.

![flow chart]()

## Skeleton

![figma files]()

## Surface
![more figma]()

![screenshots]()

## Technologies

### Languages Used
* HTML
* CSS
* Python
* Jinja

### Frameworks and Libraries
* [Materialize](https://materializecss.com/about.html) by Google
* [MongoDB](https://www.mongodb.com/) by MongoDB Inc.
