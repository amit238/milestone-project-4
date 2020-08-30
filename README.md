# Fitness Freaks

Milestone Project 4

This website is an e-commerce website where you can purchase Fitness Plans suited for you and You're also able to create blogs. You can find a demo to the website [here](https://fitness-freaks-ms4.herokuapp.com/)

# UX

The aim i have for this project is to create a fitness plan page where users are able to purchase 'Fitness Plans' which suits them. For example purchasing the "Bulk Up" plan will be ideal for users who want to get really big.

## User Stories

1. A user wants to be able to purchase fitness plans
2. A user would want to be able to add to the blog page
3. A user would be able to access pages through the navbar
4. A user wants to be able to go back to the homepage by clicking on the logo on the navbar
5. A user wants to be able to see a log out option on the navbar when 'logged in'
6. A user is able to see where they can contact us if they have an issue.
7. A user wants a safe and easy to use Checkout.

### Strategy

My aim was to make the website a user-friendly website where users can purchase fitness plans that fits for them, and safely purchase it through my checkout page.

### Scope

The scope of the website was for users to be able to view, select and purchase their plan simply. This also applies to my blog page where users can easily add a post.

### Structure

I wanted the structure of the website to look consistant, by using jumbotrons for all my headings of my pages and by having a consistant theme accross my website i was able to achieve this. I also had my fitness plans in bootstrap Cards to give it a responsive feel.

### Skeleton

All my wireframes can be viewed in my `Technologies Used` section.

### Surface

I focused on only having 2 main colours for webpage to help with my `Structure` of the page.

# Features

#### Existing Features

* Homepage - Users can see the main page of the Website, they can also Login and Register within the bootstrap card.
* Plans - Users are able to purchase Fitness plans through this page.
* Register - Users can register to the website
* Login - Users can log in, When loggin in they're able to purchase a fitness plan and create a blog.
* Blog - Allows users to see other users blog posts and are able to add their own.
* Contact - Users are able to contact us if there is any issue. They can also see an interactive map which they can see our 'HQ'

#### Features left to implement

* Add a edit and delete function for my blogs page to create a better user interface.

# Technologies Used

1. HTML

* Used to create the website

2. CSS

* Used to style the website

3. Python

* Using Python3 i was able to create the app,routes and functions within the routes.

4. Django

* Used their framework for the project

5. Bootstrap 4

* Bootstrap Grid that I have deployed throughout the website, for it to be responsive on all platforms.
* Bootstrap Cards that I have also deployed throughout the website, to give it a more aesthetic look.

6. Github

* Used to remotely store the sourece code in a repository.

7. Heroku

* Used to deploy the whole website

8. Wireframes

* Used to create template of my project.

### My Wireframe can be seen here:

#### Desktop

[Home](https://wireframe.cc/xaR8RA)
[Plans](https://wireframe.cc/L7u8Qn)
[Blog](https://wireframe.cc/f5mkvE)
[Login](https://wireframe.cc/GouWz6)
[Register](https://wireframe.cc/G8e3yD)
[Contact Us](https://wireframe.cc/J9JvwF)

#### Tablet

[Home](https://wireframe.cc/SaI7Ma)
[Plans]()
[Blog]()
[Login]()
[Register]()
[Contact Us]()

#### Mobile

[Home]()
[Plans]()
[Blog]()
[Login]()
[Register]()
[Contact Us]()


# Testing

I had tested my website manually, i achieved this by acting as a new user when entering my webpage. I tested countless of different functionalities:

##### Register

* If i typed my email wrong a second time an error message will pop out same with retyping my password
* If i completed the form and was able to register
* If i typed in a common password

##### Login/Log Out

* If i typed in a wrong password, an error message will appear
* Typing in an email that doesnt exist as a user, an error will appear
* By clicking on the log out button to see if it will log me out successfully


##### Checkout

* Clicking checkout with nothing in the cart will redirect you to the Plans page.
* Removing a Plan from the cart will actually remove the Plan

##### Stripe

* By using [Stripe's testing doc](https://stripe.com/docs/testing#cards) to help me test if my stripe payment works. I did this by using the 4242 card number as that is used testing stripe.


##### General

* Seeing if all hyperlinks work on my page
* Being able to view the google maps API with no loading error.
* Able to add a blog successfully to my page.

My project was made, using Google Chrome. This helped as i was able to use Chromes Developer tools to help me debug a few issues happening with my webpage. It also helped when viewing my webpage on different screen sizes

I was able to view my page on these devices:

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro

These tests were done throughtout my project which have also been tested on different web browsers which were:

* Safari
* Mozilla Firefox
* Google Chrome

# Deployment

I had written this code using GitPod and deployed my project. Using GitPod i was able to GitHub to store my project in a repository.

* The way i added to GitHub:

 1. In my Terminal, i had typed in ``` git add . ``` and ``` git commit -m ``` to initialise my commit.
 2. By using ``` git push ``` i was able to add everything i had from GitPod to my repository.

When building this website, it has had consistent version control with the use of GitHub and GitPod. This is to ensure that if any issues were to occur during the building phase, I would be able to revert back when needed to tackle it. When i was roughly done i had deployed on Heroku. 

With Heroku, i have stored all my Keys and Secret Key within the config variables to make sure it is user friendly.

* To deploy on Heroku, as my GitHub is linked with it. I would push anything to my repository and then after pushing type ``` git push heroku master ``` to then push it to my heroku.

All images and other static files have been stored externally with AWS S3.

#### Cloning my Repo

1. You will need to go to my GitHub [Repo](https://github.com/amit238/milestone-project-4)
2. On the right hand side you will be able to see a Clone or download dropdown button. Click that.
3. After that, click on the clipboard icon located to the right of the GitHub link
4. Now you need to open up your preffered IDE e.g. GitPod.
5. Go into the terminal window. Once in, follow the steps to then clone of this repository.


#### Cloning my Repo Using GitPod

If you have GitPod theres a much simpler way to clone it.

1. You will need to go to my GitHub [Repo](https://github.com/amit238/milestone-project-4)
2. Click on the GitPod button on the right hand side (Right next to Clone)
3. It will then take you to the repository which then can save by clicking on `File`, `Save Workspace As...`.

# Credits

I would like to thank my Mentor for helping me throughout my project.

I would also like to thank [Dennis Ivy](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) & [John Elder](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) for helping me build my Blog page and Checkout page.

## Media

I had got my Logo using [Wix Logo Creater](https://www.wix.com/logo/maker)

I got my Plans images using this [Illlustrations](https://illlustrations.co/) webpage