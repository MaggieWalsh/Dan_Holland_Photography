# Dan Holland Photography


I created this website for the 4th Milestone Project on Full Stack Frameworks with Django, at Code Institute's Diploma in Software Development course. 

Visit the live [website.](https://dan-holland-photography.herokuapp.com/)

I wanted to create a website to showcase a professional photographer.  
The website features an initial landing page with a call to action button to discover more.

![Am I Responsive image of how the landing page looks across different browser sizes](docs/readme-files/am-i-responsive.png)

# Table of Contents
  * [UX and UI](#ux-and-ui)
    * [Project Research](#project-research)
        + [Research Analysis](#research-analysis)
    * [Persona and Their Goals](#persona-and-their-goals)
    * [Owner Goals](#owner-goals)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
  * [Design](#design)
    * [Colour Scheme](#colour-scheme)
    * [Favicon](#favicon)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Layout](#layout)
  * [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be Implemented in Future](#features-to-be-implemented-in-future)
  * [Information Architecture](#information-architecture)
    * [User Table](#user-table)
    * [Product Table](#product-table)
    * [Order Table](#order-table)
  * [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks and Libraries](#frameworks-and-libraries)
  * [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Additional Testing](#additional-testing)
    * [Resolved Bugs](#resolved-bugs)
  * [Deployment](#deployment)
    * [Forking a GitHub Repository](#forking-a-github-repository)
    * [Cloning a repository using the command line](#cloning-a-repository-using-the-command-line)
  * [Credits](#credits)
    * [Imagery](#imagery)
    * [Code](#code)
    * [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# UX and UI

  * ## Project Research

    I spoke with the photographer and ascertained what he would like to achieve from the website.

    * ## Research Analysis

      A simple website with a neutral theme to allow the images to be the focal point is desired. 

  * ## Persona and Their Goals

    * The ideal customer is looking for some prints to hang with pride of place in their home.
    
    * They see the value in having beautiful pieces in their home. 

  * ## Owner Goals
    1. Increase sales.
    2. Improve interaction with existing and potential customers.
    3. Build the brand.
    3. Get people interested in the beauty of nature.
  * ## User Stories
    1. As a user visiting the site for the first time, I want to navigate the site intuitively.
    2. As a user, I want to know what the site is for.
    3. As a user, I want to be able to find out the cost of the products available, including delivery.
    4. As a user, I want to know a little bit more about the owner.
    5. As a user, I want to be able to contact the company.
  * ## Wireframes
    * Mobile, Tablet, and Desktop wireframes are all available [here.](docs/wireframes.pdf)
  * ## Design
    * ## Colour Scheme
      I wanted a neutral colour scheme that wasn't going to detract from the images for sale. 
      
      I settled on my hero image very early on as it is a very important image to the photographer.
    * ## Favicon 
      I used the [Favicon.io](https://favicon.io/) website to create a favicon for my website. I kept the background white with a simple black font 'DH|P'.
    * ## Typography
      I kept the font simple with Lato.
    * ## Imagery
      All imagery was sourced from the photographer Dan Holland. Chosen by himself to represent the brand.

    * ## Layout
      I decided on a multi-page website because I felt like each section deserved it's own dedicated page. I wanted the hero image to take up the entire space above the fold on the landing page, in order to make a good first impression. The only other element on this page is the 'Discover' button to enter the site.
  * ## Features
    * ## Existing Features
      * Every page (excluding the landing page) has the following features from left to right, top to bottom :
        * Logo - Photographers name. I made sure to use the word 'Photographer' in the websites name so that it is clear from the outset. The logo also serves as a function to return to the landing page from all other pages. The logo is hidden on smaller screens and is replaced with a 'Home' link in the dropdown navbar.

        * Navbar - The heart of the website. This allows users to intuitively navigate the site. It contains important information that a user would expect to find in the navbar. Including a 'call to action' form on the contact page.

          The navbar is designed to toggle from the hamburger navigation icon to a standard menu once the screen size goes past that of 991px wide. This is to satisfy the mobile first criteria of this project.

        * Content - Each page has details relating to the header of said page.

      * Home - This page contains the hero image and a simple 'Discover' button to prompt users to enter the site.

      * About - Brief description about the owner.

      * Shop - Lists all products available to buy, and their costs.

      * Contact - This page contains a form for the user to make an enquiry. 
      
        The user must submit certain details on the form in order for it to be successful. Once done, a prompt appears in the message window, top right, to let the user know that the enquiry has been submitted, and that someone will be in touch with them soon. The user is redirected to the products page.

      * 404 Error - This page is a purpose made error page to link to the email address in the footer. There is a return to home link which directs the user back to the websites landing page.

    * ## Features to be Implemented in Future
      * Ability to choose product sizes.
      * Email confirmation of orders.
      * Email verification for account sign up.
  * ## Information Architecture
    * ## Data Storage
      ### User Table

        | Title | DB Key | Form Validation | Data Type |
        | --- | --- | --- | --- |
        | Account id | _id | No Validation | Primary Key |
        | First Name | first_name | max length 20 | CharField |
        | Last Name  | last_name | hashed min length 8 | CharField |
        | E-mail Address | email | '@' & '.com' required | Email |
        | Street Address | default_street_address1 | max length 128 | CharField |
        | Street Address 2 | default_street_address2 | max length 128 | CharField |
        | City Or Town | default_city_town | max length 128 | CharField |
        | County/State | default_county_state | max length 64 | CharField |
        | Post Code | default_postcode | max length 12 | CharField |
        | Contact Number | default_telephone_number | Number max length 20 | CharField |
        | Country | country | pycountry select | Option |

      ### Product Table

        | Title | DB Key | Form Validation | Data Type |
        | --- | --- | --- | --- |
        | Product id | _id | No Validation | Primary Key |
        | Product Name | name | max length 254 | CharField |
        | Product Category  | category | max length 100 | CharField |
        | Price | price | max 6 digits with 2 decimals | DecimalField |
        | Description | description | no | CharField |
        | Image | image | Null True Blank True | ImageField |
        
      ### Order Table

        |  Title | Key In Database | Form Validation | Data Type |
        | --- | --- | --- | --- |
        | Order Number | order_number | No Validation | Primary Key |
        | User Profile | user_profile | text | Foreign Key |
        | First Name | first_name | max length 100 | CharField |
        | Last Name | last name | max length 100 | CharField |
        | email | email | max length 100 | CharField |
        | telephone Number | telephone_number | max length 20 | CharField |
        | street address 1| street_address1 | max length 100 | CharField |
        | street address 2 | street_address2 | max length 100 | CharField |
        | City Town | city_town | max length 100 | CharField |
        | County/State | county_state | max length 100 | CharField |
        | Postcode | postcode | max length 8 | CharField |
        | Country | country | country select | Option |
        | Order Date | order_date | datetime.date.today | DateField |
        | Total Order | total_order | max digits 10 | DecimalField |
        | Delivery Charge | delivery_charge | max digits 5 | DecimalField |
        | Grand total | grand_total | max digits 10 | DecimalField |

  * ## Technologies Used
    * ## Languages
      * [HTML5](https://en.wikipedia.org/wiki/HTML5)
      * [CSS](https://en.wikipedia.org/wiki/CSS)
      * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
      * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * ## Frameworks
      * [Bootstrap v.5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
      * [Django](https://www.djangoproject.com/)
    * ## Libraries and Tools
      * [Sweet Alert](https://sweetalert2.github.io/)
      * [Stripe Payments](https://stripe.com/)
      * [Google Fonts](https://fonts.google.com/)
      * [Font Awesome](https://fontawesome.com/)
      * [Coolors.co](https://coolors.co)
      * [Favicon.io](https://favicon.io)
      * [Balsamiq](https://balsamiq.com/)
      * [VS Code](https://code.visualstudio.com/)
      * [GitHub](https://github.com/)
      * [Autoprefixer](https://autoprefixer.github.io/)
      * [Am I Responsive](http://ami.responsivedesign.is/)
      * [AWS](https://aws.amazon.com/s3/)
      * [Heroku](https://www.heroku.com)
      * [Git](https://git-scm.com/)
      * [Postgres](https://www.postgresql.org/)
  * ## Testing
    Testing for this website was done using the Google Chrome Browser, using Chrome Developer Tools to check the different screensizes. Testing was also done on an iPhone 8 using Safari, as sometimes Safari can cause issues with how the website renders. No such errors were found.
    * ## User Stories Testing
      1. As a user visiting the site for the first time, I want to navigate the site intuitively.
         * A user can navigate to the landing page from any page in the website. Either via the navigation menu, or the logo. As is standard with most navigation these days.
      2. As a user, I want to know what the site is for.
         * A user can immediately tell that this is a photographers website.
         * Products are available to view and be purchased.
      3. As a user, I want to be able to find out the cost of the products available, including delivery.
         * A user can find out of the delivery in the banner on all pages, the cost of the products is below each one.
      4. As a user, I want to know a little bit more about the owner.
         * A user can get some insight into the owner via the About page.
      5. As a user, I want to be able to contact the company.
         * A user can contact the company via the form on the contact page.
    * ## Manual Testing 
      * Navigation - Repeated steps on all pages.
        * Click on logo to confirm that it navigates to landing page.
        * Click on all navigation links to verify that they direct to the indicated page.
        * Verify that the current page the user is on, is highlighted as active in the menu.
        * Verify that the navigation menu shifts to from hamburger on screens of 991px and above. 
      * Landing page
        * Verify that the link enter site works
      * Shop and products details pages
        * Verify that the image carousel is functional, and clicks through the images.
        * Verify that images are confined to the carousel and not overflowing it.
        * Verify that all buttons work accordingly and add or remove from the bag.
      * Contact
        * Verify that all elements that are set to required are working.
        * Verify that valid email address is needed with relevant '@' included.
        * Verify that the page automatically redirects the user to the products as indicated.
    * ## Additional Testing 
      * [W3 - Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
      * [W3C - HTML Validator](https://validator.w3.org/)
      * [PEP8 - Python Validator](https://peps.python.org/pep-0008/)
    * ## Resolved Bugs
      * Many errors were encountered along the way. These were usually down to spelling errors or incorrect paths. Early on I encountered an error which was particularly hard to debug due to how it presented itself. Django was telling me that there was an error with my path to my index page. This path had not been altered, so it was confusing. After quite some time it was discovered that the issue lay in needing to clear the cookies on the page as I had just started using 'session' in creating the shopping bag.
      * I accidentally committed my secret keys without realising it. I have since regenerated these and hidden them in my env file.

  * ## Deployment

    Below is an example of how to deploy this site locally based on using *VsCode IDE*, deploying to Heroku using *Amazon S3* for hosting of static and media files. This will allow the site to deploy automatically with commits to the master branch. The code can also be run locally.

    ### Deployment Requirements

    - [VS Code](https://code.visualstudio.com/) IDE Local development tool
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) Documentation is based on Python v3.8
    - PIP package installer
    - [Stripe](https://stripe.com/gb) Payment infrastructure

    ### Deploying Locally

    1. Clone a copy of the repository by clicking code at the top of the page and selecting 'Download Zip' when this has downloaded, extract the files to your folder of choice.
    Alternatively if you have git installed on your client you can run the following command from the terminal.

    ```bash
    git clone https://github.com/MaggieWalsh/Dan_Holland_Photography
    ```

    1. Open us your local IDE (For this example we will be using VScode as linked in the requirements) and open the working folder.

    1. Ideally you will want to work within a virtual environment to allow all packages to be kept within the project, this can be installed using the following command (please note some IDE's require pip3 instead of pip, please check with the documentation for your chosen IDE)

    ```bash
    pip install pipenv
    ```

    1. In your root dir, create a new folder called .venv (ensure you have the .)

    1. To activate the virtual environment navigate to the below dir and run activate.bat

    ```bash
    [folderinstalled]\scripts\activate\activate.bat
    ```

    If you're using Linux or Mac use the below command 

    ```bash
    source .venv/bin/activate
    ```

    1. Next we need to install all modules required by the project to run, use the follow

    ```bash
    pipenv install -r requirements.txt
    ```

    1. Create a new folder within the root dir called env.py. Within this file add the following lines to set up the environmental variables.

    ```bash
    import os

    os.environ["SECRET_KEY"] = "[Your Secret Key]"
    os.environ["DEV"] = "1"
    os.environ["HOSTNAME"] = "0.0.0.0"
    os.environ["STRIPE_PUBLIC_KEY"] = "[Your Stripe Key]"
    os.environ["STRIPE_SECRET_KEY"] = "[Your Stripe Secret Key]"
    os.environ["DATABASE_URL"] = "[Your DB URL]"
    ```

    ### Database setup

    1. To set up your database you will first need to run the following command

    ```bash
    python manage.py migrate
    ```

    1. To create a super user to allow you to access the admin panel run the following command in your terminal and complete the required information as prompted

    ```bash
    python manage.py createsuperuser
    ```

    1. From there you should now be able to run the server using the following command

    ```bash
    python manage.py runserver
    ```

    1. If everything has been correctly configure you should not get a message giving you a link to your locally hosted site usually at http://127.0.0.1:8000

    1. Next close the server in your terminal using ctrl+c (cmd+c on mac) and run the following commands to populate the database

    ```bash
    python manage.py loaddata store/fixtures/categories.json
    python manage.py loaddata store/fixtures/products.json
    python manage.py loaddata clients/fixtures/clients.json
    ```

    ### Deploying to Heroku

    To run this application in an online environment you will need to deploy the code to *Heroku*.
    Before moving on to this section please ensure you have followed the instructions for local deployment and this has been successful

    1. Either create an account at [Heroku](https://www.heroku.com/) or log in to your account
    1. Set up a new app under a unique name
    1. In the resources section, in the addons field type the below command and select the free cost option

    ```bash
    heroku Postgres
    ```

    1. in the settings tab select Reveal Config Vars and copy the pre populated DATABASE_URL into your settings.py file in your project
    1. in the Config Vars in Heroku you will need to populate with the following keys

    |          Key          |     Value    |
    |:---------------------:|:------------:|
    | AWS_ACCESS_KEY_ID     | [your value] |
    | AWS_SECRET_ACCESS_KEY | [your value] |
    | SECRET_KEY            | [your value] |
    | STRIPE_PUBLIC_KEY     | [your value] |
    | STRIPE_SECRET_KEY     | [your value] |
    | USE_AWS               | TRUE         |
    | DATABASE_URL          | [Your Value] |

    1. Now this has been configured you will now migrate the local database to the cloud database using the migrate command as below

    ```bash
    python manage.py migrate
    ```

    1. Next you will need to create a super user and populate the database as described in the database set up section
    1. When the migrations and data has been loaded, in your *Heroku* dashboard select the Deploy tab
    1. From here select the Github option and connect the repository from GitHub and select the branch (Master) to deploy from.
    1. It is advised to select automatic deployment to ensure for each push to Github the hosted version is up to date.
    1. When this has deployed select open app from the top bar of the *Heroku* App.

    * ## Forking a GitHub Repository
        1. Login to GitHub.
        2. Locate your desired repository.
        3. Locate the fork option in the top-right hand corner of the repository page.    
        4. You will be asked where you want to fork it to.

    * ## Cloning a repository using the command line
        1. On GitHub, navigate to the main page of the repository.
        2. Above the list of files, click download code.
        3. To clone the repository using HTTPS, under "Clone with HTTPS", click clipboard icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click *Use SSH*, then click clipboard icon. To clone a repository using GitHub CLI, click Use *GitHub CLI*, then click clipboard icon.
        4. Open Terminal.
        5. Change the current working directory to the location where you want the cloned directory.
        6. Type ```git clone```, and then paste the URL you copied earlier.

            ```
            $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
            ```

        7. Press Enter to create your local clone.

            ```
            $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
            ```

            \> Cloning into \`Spoon-Knife`\...

            \> remote: Counting objects: 10, done.

            \> remote: Compressing objects: 100% (8/8), done.

            \> remove: Total 10 (delta 1), reused 10 (delta 1)

            \> Unpacking objects: 100% (10/10), done.

  * ## Credits
    * ## Imagery
        * Dan Holland
    * ## Code
      * Bootstrap was the base for the entire website in order to ensure it's responsivity.
      * The bones of this project are from the Boutique Ado walkthrough which I have adapted as best I can in a short timeframe
      * Credit to Stack Overflow for some solutions that I have commented in my code.
    * ## Acknowledgements
      * A special thank you to my mentor Richard Wells for all his help along the way.
      * Another special thank you to my peers in my Discord group for the moral support.


