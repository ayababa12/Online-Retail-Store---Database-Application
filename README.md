# FOUR3THREE Online Shop

The FOUR3THREE Store is an online shopping website developed using Flask and PostgreSQL. It offers a variety of clothing and cosmetic items. Users can browse different categories, view products, add items to their cart, and complete the checkout process.

## Table of Contents
- [A-Database-Design-for-FOUR3THREE](#A-Database-Design-for-FOUR3THREE)
- [Usage](#usage)
- [Signup/Login](#Signup/Login)
- [HomePage](#HomePage)
- [cart](#cart)
- [profile](#profile)
## A Database Design for FOUR3THREE
This document contains a detailed description of the design process, including the ER diagram, mapping, normalization, and SQL DDL code
## Usage

1. First open the main.py file and make sure to replace the password on line 9 with your own password for PostgreSQL
2. You need to have PostgreSQL, and the psycopg2 module on python. The database is found in the file 'four3three.sql'. Create the database by running this SQL code on pgadmin.
3. Run main.py
4. Visit [http://localhost:5000](http://localhost:5000).

## Signup/Login

1. Press the login button on the top right of the page to go to the login page.
2. If you already have an account then you could enter your email and password to login.
3. If not then you need to navigate to the signup page by pressing the signup here button on the bottom.
4. To signup you need to fill the information accordingly having a requiring to fill atleast the email,date of birth, and password.(Email has to include an @ and . to make it a valid email)
5. After successfully signing up the website redirects you to the login page and you are now able to login to our website.
6. If you want to go back to the main page, you can always press on the logo FOUR3THREE to continue your browsing

## HomePage

1. To navigate the home page you could type in the text box of the search box whatever item you may be looking for and after pressing enter or the search button it then displays the items it found corresponding to what you searched.
2. To go back to the main page you could simply click on our FOUR3THREE logo and it takes you back to the home page.
3. You can also scroll down and see multiple sections such as our hot deals/best sellers/highlights from our cosmetic line and you could flip through the items by simply clicking on the next or prev button and the numbers are there to specify how many items are listed.
4. To show specific clothing/accessory/cosmetic item categories for example Jackets you could do that by clicking on Jackets which is shown on the top of the page in a bar that shows the multiple different categories.

## cart

1. For any item you would like to view or know any details about it then you could simply click on the picture or name of that item.
2. If you would like to add an item to a cart then you first need to inspect it as said in the step above then click on the Add to cart button.
3. To view your cart you can simply click on the top right of the screen where a small cart icon is shown and now you could view your whole cart and each items specific information and the total price.
4. If you change your mind on any item you can simply remove it by clicking on the Remove from cart button which is on the same row of that item.
5. Finally, to checkout your items, click the Checkout button.
6. You can always navigate back to the main page by pressing on the logo FOUR3THREE or pressing on a category of your liking showing at the top of the page or by searching an item in the search bar.

## profile

1. To check your profile you first need to be logged in. To login check #Signup/Login.
2. After you have logged in the profile icon is now shown on the top right of your screen left to the cart button.
3. To view your profile you can now click on that icon and now all your information as well as past orders are shown.
4. To navigate back to the main page, click on the FOUR3THREE icon which is found on the top of the page.

