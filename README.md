# [Lucent Cavern](https://lucent-cavern.herokuapp.com/)


![Responsive Image](README-media/responsive-image.png)

This website is my final Milestone project in Code Institute. Project contains the use of  HTML, CSS, JavaScript, Django, Python, and a relational database. Website hosted on Heroku. Static and media files stored on an S3 Cloud storage from AWS. Project is connected to Stripe's payment processing platform.

## Contents
- [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

- [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

- [Database](#database)
	- [Database Schema](#database-schema)
    - [Database structure](#structure)

- [Testing](#testing)
	- [Validation](#validation)
	- [Browsers](#browsers)
	- [Design responsiveness](#design-responsiveness)
	- [Manual Testing](#manual-testing)

- [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Databases](#databases)
    - [Tools](#tools)

- [Deployment](#deployment)
	- [Local Deployment](#local-deployment)
    - [To Heroku](#to-heroku)

- [Credits](#credits)
    - [Media](#media)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)
    

# UX

## User Stories

### As a client I expect:

- A website were I can shop all products and make easy transaction.
- A website to have optimal layout and attractive design.
- A website to be intuitive, easy to navigate so that I would be able to find what I need as fast as possible.
- To find information about products easily.
- To easily sort products on a page and be able to search for a product by using search word.
- To be able to add products to the list where later I can find them without scrolling thru all production.
- To be able to find contact information and social media links for more info. 
- To be able to register, login easily and take less steps as possible.
- To be able to make a purchase with minimal amount of steps.
- To be able to get a confirmation after purchase is made. Be provided with details on a website and confirmation email.
- To be able to read store's Blog, have an ability to subscribe for a newsletter.
- To be able to use website on any device: laptop, tablet or mobile phone.
- To be informed after each request I make, like form completion, registration, login, log out and else.
- To be able to update/change my personal information, like an address or contact number.

### As a owner I expect:

- To be able to add products, edit their details or delete them.
- To be able to add Blog posts, edit them or delete

## Design

### Theme

I wanted to create a website that would create a feeling that you are in a lucent cavern. Main image on a home page is a base for all website's colours and backgrounds. Main goal of light colours is to provide lightweight and modern site.

### Colours

Colours taken from home image, to match whole website.

![Colours](README-media/sites-colours.png)

### Typography

Main font family is  [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) from Google Fonts.

## Wireframes
Wireframes were created by hand. They look simple and not very detailed, a bit different from final look because they were created before I started my project. Personally for me it's easier to put everything into places when project is in progress already, details like buttons forms and other elements.

#wireframes links#

# Features

## Current Features

<details>
	<summary>
		:open_book:
	</summary>

 ### Shared features:
 
 - Fixed Navbar:
	 - Brand name
	 - Home
	 - Products (links to categories)
	 - Blog
	 - Contact (link to the footer's Contact Us section)
	 - Search Bar with button for user to search product by word links to products page with search results
	 - My Account dropdown menu links to product management (admin only), profile (registered users), favorites list ( registered users), log out (registered users), registered, login)
	 - Cart icon to link user to their shopping bag page

- Toasts with messages for Success, Error, Info, Warning. Three main important messages:
	-  If user adds item to shopping bag, toast success provides shopping bag details table.
	-  If user adds/removes product to/from Favorites list, success message provides info on that action.
	- After user successfully completes order success toast appears with information and order number.

- Footer:
	- Lucent Cavern address section for physical store
	- Contact Us section with email link, working hours and phone number
	- Follow Us section with social media links
	- Copyright

### Individual features:

- My Favorites page (registered users only) contains:

	- Header Favorites list
	- Card element for each item in a Favorites list:
		- Product Image, name, price, category, edit/delete product icon buttons (admin only)

- Blog page contains:

	- Our Blog header
	- Blog posts list with cards:
		- Post title
		- Author, date
		- Content
		- Read more button which links to individual post details

- Blog post details page contains:

	- Post title
	- Subtitle
	- Author
	- Date when published
	- Blog post content
	- Back button which links user to Blog page 


- Home page contains:

	- Announcement section describing  website's content, button to link user to All Products page
	- Our Story section
	- Favorite Collections sections for users to check favorite categories - Raw Crystals, Jewellery, Salt Lamps. Added images to catch eye. Added button to link to All Products page.
	- Subscribe section contains  form where user can input their email address and subscribe a newsletter. Added submit button.

- Products page contains:

	- Two headers:
		- Products
		- Category name
	- Link to all products page, products count
	- Select dropdown to let users tot sort products (asc or desc) by price, name or category.
	- Product card for each product with product image, product name, price and category. Contains icon buttons which  allows admin only, edit product details or delete product
	
- Product detail page contains:

	- Product image
	- Product name
	- Product category
	- Heart icon button (registered users only), to add/remove product to user's Favourites list
	- Contains icon buttons which  allows admin only, edit product details or delete product
	- Description
	- Form for user to select product quantity
	- Continue Shopping button which links to all Products page
	- Add to bag button, which puts item to the shopping bag

- Edit Product page (admin only) contains:

	- Header for Product Management
	- Header for Edit Product
	- Form for:
		- Category options, Sku, Product name, description, price, Image URL, Choose File button to upload image
	- Cancel button to cancel Product Editing
	- Update Product button to update product details and save them

- Add Product page (admin only) contains:

	- Header for Product Management
	- Header for Edit Product
	- Form for:
		- Category options, Sku, Product name, description, price, Image URL, Choose File button to upload image
	- Cancel button to cancel Product Add
	- Add Product button to add product to DB

- Register page contains:

	- Header
	- Paragraph with link to login page
	- Form to input email, username, password
	- Button to Sign up
	- Button Back to Login which links to login page
	
- Login page contains:

	- Header
	- Paragraph with link to Register page
	- Form to input username, password
	- Button Home to link user to Home page
	- Button Sign In to let user login
	- Forgot Password link, to link user to the Reset Password page

- Password reset page contains:

	- Paragraph with instructions
	- Input field for Email address
	- Back to Login button
	- Reset my Password button
	
- Shopping Bag page contains:

	- Table with product details:
		- Button on image's left top corner to delete product from shopping bag
		- Product image
		- Name, price
		- Quantity input 
		- Update button, to update product quantity
		- Price for each item
		- Product subtotal
	- Bag Total
	- Delivery costs
	- Grand Total
	- Paragraph with sum left to spent for free delivery. If shopping bag total less than 30 euro.
	- Continue Shopping button to link user to Products page
	- Secure Checkout button to link user to the Checkout page

- Checkout page contains:

	- Header
	- Order list count
	- Item image, name, quantity subtotal
	- Total sum
	- Delivery costs if any
	- Grand Total
	- Form for personal details:
		- Name, Email Address
	- Form for delivery details:
		- Phone number, address
	-	Check field for registered user save details
	-	Stripe input element for user's card details
	-	Change Bag button, to link user to shopping if changes needs to made
	-	Complete Order button, to confirm user's order/transaction sends user to checkout success page and triggers email with order details to be sent to user

- Checkout Success page contains:

	- Header
	- Paragraph
	- Container with order details:
		- Date
		- Items, their quantity, each price
		- Delivery Information -  Full Name, Address, Phone Number
		-  Billing Information - Total, Delivery costs,
		- Grand Total
	- Button to link users to Products page
	- Back to Profile button, to link user back to the Profile if user came from there

- My Profile page contains:
	- Header My Profile
	- Table with Personal Order History:
		- Oder number which links to checkout success page where user could see order details.
		- Date
		- Items, their quantity
		- Order Total
	- Personal Default Delivery Information form:
		- Phone Number, Address
	- Update Information button to update form with new details


- Log Out page (registered users only) contains:

	- Header Sign Out
	- Question Paragraph
	- Cancel button
	- Sign Out button to confirm action
</details>

## Future Features 

<details>
<summary>
	:open_book:
</summary>

- Provide ability for user to leave a feedback for product, rate it.
- Provide ability for user login with social media account.
</details>

# Database

- For Development I used SQlite3 database which provided by Django. After deployment to Heroku database was switched to PostgreSQL.

## Database Schema
![Database Schema](README-media/db-schema.png)

## Structure

<details>
<summary>
	:open_book:
</summary>

### Category model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
name | CharField() | max_length=254
friendly_name | CharField() | max_length=254, null=True, blank=True

### Product model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
category | ForeignKey() | 'Category', null=True, blank=True, on_delete=models.SET_NULL
sku | CharField() | max_length=254, null=True, blank=True
name | CharField() | max_length=254, 
description | TextField() | 
price | DecimalField() | max_digits=6, decimal_places=2
image_url | URLField() | max_length=1024, null=True, blank=True
image | ImageField() | null=True, blank=True

### BlogPost model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
author | ForeignKey() | UserProfile, on_delete=models.CASCADE, related_name='blog_posts', null=False, blank=Trueblank=True, on_delete=models.SET_NULL
title | CharField() | max_length=120, null=True, blank=False 
subtitle | CharField() | max_length=180, null=True, blank=False 
content | TextField() |  
slug | SlugField() | unique=True, max_length=250, default=None
created_on | DateTimeField() | auto_now_add=True, null=False
updated_on | DateTimeField() | auto_now=True, null=False

### Order model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
order_number | CharField() | max_length=32, null=False, editable=False
user_profile | ForeignKey() | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' 
full_name | CharField() | max_length=50, null=False, blank=False
email | EmailField() | max_length=254, null=False, blank=False
phone_number | CharField() | max_length=20, null=False, blank=False
country | CountryField() | blank_label='Country *', null=False, blank=False 
postcode | CharField() | max_length=20, null=True, blank=True
town_or_city | CharField() | max_length=40, null=False, blank=False 
street_address1 | CharField() | max_length=80, null=False, blank=False
street_address2 | CharField() | max_length=80, null=True, blank=True
county | CharField() | max_length=80, null=True, blank=True 
date | DateTimeField() | auto_now_add=True 
delivery_cost | DecimalField() | max_digits=6, decimal_places=2, null=False, default=0
order_total | DecimalField() | max_digits=10, decimal_places=2, null=False, default=0 
grand_total | DecimalField() | max_digits=10, decimal_places=2, null=False, default=0
original_bag | TextField() | null=False, blank=False, default=''
stripe_pid | CharField() | max_length=254, null=False, blank=False, default=''

### OrderLineItem model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
order | ForeignKey() | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
product | ForeignKey() | Product, null=False, blank=False, on_delete=models.CASCADE
quantity | IntegerField() | null=False, blank=False, default=0
lineitem_total | DecimalField() | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

### UserFavoritesList model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
user_profile | OneToOneField() | UserProfile, on_delete=models.CASCADE, null=False, blank=False
favorited_products | ManyToManyField() | Product, related_name='userfavoriteslists'

### UserProfile model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
user  | OneToOneField()  |  User, on_delete=models.CASCADE
default_phone_number  |  CharField()  |  max_length=20, null=True, blank=True
default_street_address1  | CharField() |  max_length=80, null=True, blank=True
default_street_address2  |  CharField()  |  max_length=80, null=True, blank=True
default_town_or_city | CharField() | max_length=40, null=True, blank=True
default_county | CharField() | max_length=80, null=True, blank=True
default_postcode |  CharField() | max_length=20, null=True, blank=True
default_country | CountryField()  |  blank_label='Country', null=True, blank=True

### SubscriptionUser model

Field Name | Field Type | Requirements
------------- | ------------- | -------------
email | EmailField() | default=False, null=False, blank=False
subscription_date | DateTimeField() | auto_now_add=True
</details>

# Testing

## Validation

<details>
<summary>
	:open_book:
</summary>

### Results

Validator | Result 
------------- | ------------- 
[W3C validator HTML](https://validator.w3.org/) | :heavy_check_mark: 
[W3C validator JIGSAW CSS](https://jigsaw.w3.org/css-validator/) | :heavy_check_mark: (by direct CSS input)
[JSHint validator](https://jshint.com/) | :heavy_check_mark:
[PEP8 validator](http://pep8online.com/) | :heavy_check_mark:
</details>

## Browsers

<details>
<summary>
	:open_book:
</summary>

Website tested on Google Chrome, Microsoft Edge, Opera, Safari and Firefox browsers.
</details>

## Design responsiveness

<details>
<summary>
	:open_book:
</summary>

Website's design responsiveness tested on all devices provided by using Chrome Developer Tools with no issues. Designed to suit even smallest devices like Galaxy Fold. Examples of devices:

Screen resolutions | Devices 
------------- | ------------- 
1600x992px | Desktop
1280x802px | Laptop
768x1024px | Tablet
320X568PX | iPhone 5/SE
375x667px | iPhone 6,7,8
414x736px | iPhone 6,7,8 Plus
375x812px | iPhone X
360x640px | Galaxy S5
1024x1366px | iPad Pro
384x640px | Nexus 4
1080x2244px | Huawei Mate 20X(5G)
280x653px | Galaxy Fold

</details>

## Manual Testing

<details>
<summary>
	:open_book:
</summary>

<details>
<summary>
Navigation Bar
</summary>
			
+ Tests:
	+ :heavy_check_mark: Brand name, Home, Products, Blog, Contact, Seach Bar, My Account, Cart Icon displayed and aligned correctly.
	+ :heavy_check_mark: Home, Blog, Contact, Cart Icon items links to assigned pages or Home page sections like Contact Us section in a footer.
	+ :heavy_check_mark: Products Navbar item provides dropdown list with seven categories. Each list item links to assigned page.
	+ :heavy_check_mark: Search bar form submited without input, specifies that an input field must be filled out before submitting the form.
	+ :heavy_check_mark: Search bar form submited with input, links to products page with search results.
	+ :heavy_check_mark: (Loged in) My Account Navbar item provides dropdown list with links to Product Managment(admin only), My Profile, My Favorites, Log Out pages. Each list item links to assigned page.
	+ :heavy_check_mark: (Non registered) My Account Navbar item provides dropdown list with links to Register, Login pages. Both list items links to assigned page.
	+ :heavy_check_mark: Mobile/tablet website view: Navbar provides navbar toogler with dropdown, My Account dropdown and Cart icon link. All tests above done for mobile/tablet view, dropdowns provide list items with assigned links to correct pages.
</details>

<details>
<summary>
Footer
</summary>

+ Tests:
	+ :heavy_check_mark: Footer provides Address, Contact Us, Social Media Links cards which aligned as assigned. On the bottom of footer Copyright content displayed.
	+ :heavy_check_mark: Address Card content aligned to the right on big devices, no icon.
	+ :heavy_check_mark: Contact Us email mailto anchor opens user's device's default mail program.
	+ :heavy_check_mark: Contact Us phone number tel anchor provides call link to place a phone call.
	+ :heavy_check_mark: Follow Us card provides links to Social Media, all four links works. Opens links in a new tab (No Social Media account were created).
	+ :heavy_check_mark: All link tests above done for mobile/tablet view.
	+ :heavy_check_mark: Mobile/tablet view: Each footer card takes full column (12), and individual row.
	+ :heavy_check_mark: Address card content aligned to center, Map Icon provided (only on mobile/tablet view).
</details>

<details>
<summary>
Home page
</summary>
		
+ Tests:
	+ :heavy_check_mark: Intro container provides headers with small website description and statment about free delivery. Provides **SHOP NOW** button which links to Products page. Content aligned to center verticaly and horizontaly.
	+ :heavy_check_mark: About container contains header and content bellow. Centered verticaly and horizontaly.
	+ :heavy_check_mark: Products index container displays header, three product categories cards, and a button. Aligned and styled.
	+ :heavy_check_mark: Raw Crystals, Jewellery, Salt Lamps cards: 
		+ Images cards centered, takes three colums, has overlay.
		+ Category link names on images links to assigned Products category pages.
	+ :heavy_check_mark: Button **VIEW ALL CATEGORIES** links to All Products page.
	+ :heavy_check_mark: All link tests above done for mobile/tablet view.
	+ :heavy_check_mark: Mobile/tablet view: Each card takes 12 template colums per row.
	+ :heavy_check_mark: Subscribe section contains header, announcement, form for email input and a button, content aligned horizontaly and verticaly.
	+ :heavy_check_mark: Email input form:
		+ Email form submited without input, specifies that an input field must be filled out before submitting the form.
		+ Email form submited with random characters, specifies email address format and prevents form from being submited.
		+ Email form submited with correct email, triggers toast with success message about email address being added to subscription list.
		+ Email form submited with email address which already in a subscription list, triggers toast with error message about email address already subscribing a newsletter.
	+ :heavy_check_mark: **SUBMIT** button successfuly submits form if there is no exceptions mentioned above.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done for submit container.
	
</details>

<details>
<summary>
Products/category page
</summary>

+ Tests:
	+ :heavy_check_mark: Contains aligned components:
		+ Two headers
		+ Link to all Products page, product count and sort selector
		+ Aligned cards with details
	+ :heavy_check_mark: Products Home link, links to All Product page.
	+ :heavy_check_mark: Product count provides right ammount of products
	+ :heavy_check_mark: Sort Selector sorts (ascending & descending) by price, name and category. All sorting methods tested and provides correct results.
	+ :heavy_check_mark: Card element:
		+ Containes image which links to assigned product details page. Image responsive to styling.
		+ Product name links to assigned product details page. Aligned to left side.
		+ Correct price provided.
		+ Category link with hastag icon provided, link takes user to assigned Product/category page.
		+ Edit/Delete icon buttons (admin only). Edit button takes to product/edit page. Delete button deletes product and triggers toast with success message informing that product was successfuly deleted. Buttons aligned to the right side of card.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
</details>
	
<details>
<summary>
Products page
</summary>

+ Tests:
	+ :heavy_check_mark: Contains aligned components:
		+ Header
		+ product count and sort selector
		+ Aligned cards with details
	+ :heavy_check_mark: Product count provides right ammount of products
	+ :heavy_check_mark: Sort Selector sorts (ascending & descending) by price, name and category. All sorting methods tested and provides correct results.
	+ :heavy_check_mark: Card element:
		+ Containes image which links to assigned product details page. Image responsive to styling.
		+ Product name links to assigned product details page. Aligned to left side.
		+ Correct price provided.
		+ Category link with hastag icon provided, link takes user to assigned Product/category page.
		+ Edit/Delete icon buttons (admin only). Edit button takes to product/edit page. Delete button deletes product and triggers toast with success message informing that product was successfuly deleted. Buttons aligned to the right side of card.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
</details>

<details>
<summary>
Product detail page
</summary>

+ Tests:
	+ :heavy_check_mark: Product image on the left responsive to sizing. When clicked links to a new tab with image from source.
	+ :heavy_check_mark: On the right product name, price, description
	+ :heavy_check_mark: Favorites heart icon button (loged in users):
		+ When clicked, if user new, Favorites list created and products added to user's Favorites list. If user already has Favorites list, product added to it. Both scenarios triggers toast success message informing about product added to Favorites list.
		+ When clicked if product already in user's Favorites list, product being removed from list and triggers toast with success message informing that product removed from Favorites list.
	+ :heavy_check_mark: Edit/Delete icon buttons (admin only). Edit button takes to product/edit page. Delete button deletes product and triggers toast with success message informing that product was successfuly deleted. Buttons aligned to the right side of card.
	+ :heavy_check_mark: Quantity input form allows user to set product quantity by direct input on by using up/down arrow button.
	+ :heavy_check_mark: If user directly fills in number bigger than 20 and tries to add it product to the bag, form provides message with maximal value limit.
	+ :heavy_check_mark: If user directly fills in number less or equal to 0  and tries to add it product to the bag, form provides message with minimal value limit.
	+ :heavy_check_mark: Quantity form's Up/down arrow buttons being dissabled with JavaScript when quantity value get (minimum) 1, or (maximum) 20.
	+ :heavy_check_mark: **CONTINUE SHOPPING** button links user to Product page.
	+ :heavy_check_mark: **ADD TO BAG** button triggers success toast which contains:
		+ Statement informing that product (name) added to the bag.
		+ Provides paragraph with My Bag(product count).
		+ Row with column containing image, another column containg product name and quantity.
		+ If there is more different products in a shopping bag, vertical  scroll bar appears.
		+ Another row provides paragraph with counted bag total ammount
		+ If user's shopping bag total is less than 30euro, delivery cost percentage added from shopping bag total. Below Total, statment displayed, informing how much user needs to spent to get free delivery.
		+ **SECURE CHECKOUT** button links user to Checkout page.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
</details>

<details>
<summary>
Shopping Bag page
</summary>
	
+ Tests:
	+ :heavy_check_mark: Contains header
	+ :heavy_check_mark: Table with content:
		+ Product info: Responsive sizing image with X icon button on the left side top corner. When hovered on button, changes colour. When clicked product being removed from shopping bag with JavaScript's help. Removing triggers toast with success message informing that product was deleted from shopping bag.
		Product info also provides product name and sku unique number.
		+ Price: shows product's price (for each). 
		+ Quantity form:
			+ Quantity input form allows user to set product quantity by direct input on by using up/down arrow button.
			+ If user directly fills in number bigger than 20 and tries to update bag with **Update** link, form provides message with maximal value limit.
			+ If user directly fills in number less or equal to 0  and tries to update bag with **Update** link, form provides message with minimal value limit.
			+ Quantity form's Up/down arrow buttons being dissabled with JavaScript when quantity value get (minimum) 1, or (maximum) 20.
			+ If user provides right ammount and cliks **Update** button, triggers toast with success message informing about product quantity being updated.
		+ Subtotal:
			+ Right subtotal ammount provided (quantity multiplied by price)
	
	+ :heavy_check_mark: Bag Total displays right ammount.
	+ :heavy_check_mark: Delivery costs countent if shopping bag total less than 30 euro.
	+ :heavy_check_mark: Right ammount of grand total displayed.
	+ :heavy_check_mark: If user's shopping bag total less that 30 euro, paragraph displayed with information about how much user need to spent to get free delivery.
	+ :heavy_check_mark: **CONTINUE SHOPPING** button links to All products page
	+ :heavy_check_mark: **SECURE CHECKOUT** button links to Checkout Page
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>

<details>
<summary>
Checkout page
</summary>

+ Tests:
	+ :heavy_check_mark: Page Header
	+ :heavy_check_mark: Personal Details form:
		+ If user tries to complete order without filling input fields, form provides message informing that fields need to filled.
	+ :heavy_check_mark: Delivery Details form:
		+ If user tries to complete order without filling input fields, form provides message informing that fields need to filled. Required fields: Phone Number, Street Address 1, Town or City, Contry.
	+ :heavy_check_mark: (Non registered users) Bellow the form, paragraph with links to Create an account or login to save both forms information. Both links sends to asigned pages. Register or Login.
	+ :heavy_check_mark: (Loged in users) Bellow the form, checkbox with statment informing about opportunity to save delivery information to user's profile if checkbox checked.
	+ :heavy_check_mark: Stripe Payment element provided.
	+ :heavy_check_mark: Input field submited with **Payment succeeds** testing number: (4242 4242 4242 4242). Sends user to Checkout Success page, sends a Confirmation email with order details, Stripe/Payments confirms that payment is completed.
	+ :heavy_check_mark: Input field submited with **Payment requires authentication** testing number: (4000 0025 0000 3155). Opens modal, if chosen COMPLETE AUTHENTICATION, sends user to Checkout Success page, sends a Confirmation email with order details, Stripe/Payments confirms that payment is completed. If chosen FAIL AUTHENTICATION, under playment element, paragraph with message apears, informing that unable to authenticate payment method, choose different method and try again.
	+ :heavy_check_mark: Input field submited with **Payment is declined** testing number: (4000 0000 0000 9995). Provides paragraph with message that card has insufficient funds.
	+ :heavy_check_mark: If field filled with random numbers, message informs that card number is invalid.
	+ :heavy_check_mark: If user tries to submit form with incomplete card number field or empty, paragraph message informs about card number being incomplete.
	+ :heavy_check_mark: **CHANGE BAG** button  links to Shopping Bag page
	+ :heavy_check_mark: **COMPLETE ORDER** button links to (if transaction successfull) Checkout Success page
	+ :heavy_check_mark: On the right side of the page order details provided
	+ :heavy_check_mark: Order list (quantity)
	+ :heavy_check_mark: Row With Item and Subtotal
	+ :heavy_check_mark: Row with Product image, name and quantity, right ammount subtotal
	+ :heavy_check_mark: Total provides right ammount
	+ :heavy_check_mark: Delivery provides counted right ammount
	+ :heavy_check_mark: Grand Total counted and displayed
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>
	
<details>
<summary>
Checkout Success page
</summary>

+ Tests:
	+ :heavy_check_mark: page header, aligned to the left
	+ :heavy_check_mark: paragraph with information and email where order details were sent.
	+ :heavy_check_mark: Toast with success message, triggered by successful transaction informs that order processed, provides order number and email where confirmation email will be sent to.
	+ :heavy_check_mark: Confirmation container with details:
		+ Aligned to the left: 
			+ Order id info
			+ Order details: date, items
			+ Delivering to: Full name, Address 1, Address 2, County, Town or City, Postal Code, Country, Phone Number
			+ Billing info: Total, Delivery, Grand Total
		+ Aligned to the right:
			+ Date, time, items name, quantity, price for each. Users delivery details, billing total, delivery grand total with right ammounts
	+ :heavy_check_mark: **TAKE A LOOK AT OUR OTHER PRODUCTS** button links user to Product page
	+ :heavy_check_mark: **BACK TO PROFILE** button provided only if user came from Profile (loged in user) page, button links back to Profile page
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>

<details>
<summary>
Product Management Add Product (admin only) page
</summary>

+ Tests:
	+ :heavy_check_mark: Two headers displayed
	+ :heavy_check_mark: Form contains: select dropdown for categories, input fields for sku, name, description, price, image url, input for image
	+ :heavy_check_mark: If user tries to add product without filling input fields, form provides message informing that fields need to filled.
	+ :heavy_check_mark: After filling in required fields for product adding and clicking **Add Product**, new product added and user linked to product details page with newly added product details. Triggered toast with success message informing that product successfully added.
	+ :heavy_check_mark: **Cancel** button prings to Products page
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>

<details>
<summary>
Product Management Edit Product (admin only) page
</summary>

+ Tests:
	+ :heavy_check_mark: Two headers displayed
	+ :heavy_check_mark: Alert message toast displayed, informing that user edditing product
	+ :heavy_check_mark: Form contains prefilled inputs: select dropdown for categories, input fields for sku, name, description, price, image url, input for image
	+ :heavy_check_mark: If user tries to submit form without filling required input fields, form provides message informing that fields need to filled.
	+ :heavy_check_mark: After modifing form's input fields for product editing and clicking **Update Product**, product updated and user linked to product details page with newly added product details. Triggered toast with success message informing that product successfully updated.
	+ :heavy_check_mark: **Cancel** button prings to Products page
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>
	
<details>
<summary>
Profile (loged in users only) page
</summary>

+ Tests:
	+ :heavy_check_mark: Page header
	+ :heavy_check_mark: Personal Order History table provided: contains order number, Date, Items, Order Total.
	+ :heavy_check_mark: Table provides correct order details (if user ever placed order): date, items and their quantity, correctly countet order total.
	+ :heavy_check_mark: When clicked on order id number, user linked to Checkout success page, with order details. In Checkout Success page, toast for alert message displayed, informing that it's a past confirmation for order number XXXXXX. And that confirmation email was sent on the order date.
	+ :heavy_check_mark: Personal Default Delivery Information form provides correct input fields. If user placed the order before, and chose save the details, Pesonal Default Delivery Information form prefilled alredy with current user's info.
	+ :heavy_check_mark: form's input fields modified on click **UPDATE INFORMATION** information saved, triggered toast with success message informing that Profile updated successfully.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices as well.
</details>

<details>
<summary>
My Favorites (loged in users only) page
</summary>

+ Tests:
	+ :heavy_check_mark: Page header displayed
	+ Aligned cards with details
	+ :heavy_check_mark: Card element:
		+ Containes image which links to assigned product details page. Image responsive to styling.
		+ Product name links to assigned product details page. Aligned to left side.
		+ Correct price provided.
		+ Category link with hastag icon provided, link takes user to assigned Product/category page.
		+ Edit/Delete icon buttons (admin only). Edit button takes to product/edit page. Delete button deletes product and triggers toast with success message informing that product was successfuly deleted. Buttons aligned to the right side of card.
	+ :heavy_check_mark: If user's favorites list is empty, paragraph provided, stating that user's favorites list is empty. **CONTINUE BROWSING** button provided to link user to Products page.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
</details>
	
<details>
<summary>
Blog page
</summary>

+ Tests:
	+ :heavy_check_mark: Page header displayed
	+ :heavy_check_mark: Contains card element for each blog post
	+ :heavy_check_mark: Card element contains:
		+ Correct post's header
		+ Correct  author, date and time
		+ Correct content (limited content length)
		+ **READ MORE**  button links user to Blog Post details page
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
	
</details>
	
<details>
<summary>
Blog post details page
</summary>
	
+ Tests:
	+ :heavy_check_mark: Correct post title as header
	+ :heavy_check_mark: Correct post subtitle 
	+ :heavy_check_mark: Correct post Author
	+ :heavy_check_mark: Correct publishing date
	+ :heavy_check_mark: Correct post content
	+ :heavy_check_mark: All elements above centered horizontaly to sit in a center
	+ :heavy_check_mark: Aligned to the left **BACK** button, which links user back to Blog page.
	+ :heavy_check_mark: Mobile/tablet view: All tests above done. Set Layout grid responsive to small devices.
</details>

</details>

# Technologies

## Languages

- HTML5
- CSS3
- JavaScript
- Python3

## Libraries and Frameworks

- Django3
- Bootstrap (V.5)
- jQuery
- Font Awesome (V.5)
- Google Fonts

## Databases

- SQlite3
- PostgreSQL

## Tools

- Gitpod
- Github and Git
- Heroku
- Stripe
- AmazonS3

# Deployment

## Local Deployment

<details>
<summary>
	:open_book:
</summary>

1.  Log in to your  Gitpod account 
2.  Clone this project repository from GitHub
    -   Go to my [LuucentCavern repository](https://github.com/ErnestaMajute/lucentCavern) 
 3. Add Gitpod browser extension for Chrome:
    -   Go to  [GitPod Chrome Browser Extension](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki)
  4.  If you  installed the extension you should view a green Gitpod button on the top right corner of page. Next to Clone or Download button. 
  5. When clicked this button will allow you to open this repository directly in Gitpod.
6.  The following environment variables needs to be set:

KEY | VALUE
------------- | ------------- | 
DATABASE_URL | <DATABASE_URL>
AWS_ACCESS_KEY_ID | <AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY | <AWS_SECRET_ACCESS_KEY>
EMAIL_HOST_PASSWORD | <EMAIL_HOST_PASSWORD>
EMAIL_HOST_USER | <EMAIL_HOST_USER>
SECRET_KEY | <SECRET_KEY>
STRIPE_PUBLIC_KEY | <STRIPE_PUBLIC_KEY>
STRIPE_SECRET_KEY | <STRIPE_SECRET_KEY>
STRIPE_WH_SECRET | <STRIPE_WH_SECRET>
USE_AWS | True

7.  Download all the dependencies to run this project and listed in the  **requirements.txt**  by running command **pip3 install -r requirement.txt**.
8.  Create a local development server. In the workspace run the following command  **python3 manage.py runserver** . Now you should have a Gitpod link to the deployed app.
</details>

## To Heroku
<details>
<summary>
	:open_book:
</summary>

This [LucentCavern](https://lucent-cavern.herokuapp.com/) app was deployed through Heroku using the master branch of my GitHub [LuucentCavern repository](https://github.com/ErnestaMajute/lucentCavern). Link To Deplyed app also can be foud on a very top of page.


1. Install **gunicorn** to run the application on Heroku by running command **sudo pip3 install gunicorn**
2. Install **pycopg2** to connect to PostgreSQL by running command  **sudo pip3 install psycopg2**
3. Create a **requirements.txt** file by running command **sudo pip3 freeze --local > requirements.txt**
4. Create a new Heroku application by clicking **New** after **Create New App**. Give a name to your app and click **Create app**
5. Install PostgreSQL add-on by running command **heroku addons:create heroku-postgresql:hobby-dev**
6. Create a Procfile by running command **echo web: gunicorn lucent-cavern.wsgi:application > Procfile**
7. Following config variables needs to be set:

KEY | VALUE
------------- | ------------- | 
DATABASE_URL | <DATABASE_URL>
AWS_ACCESS_KEY_ID | <AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY | <AWS_SECRET_ACCESS_KEY>
EMAIL_HOST_PASSWORD | <EMAIL_HOST_PASSWORD>
EMAIL_HOST_USER | <EMAIL_HOST_USER>
SECRET_KEY | <SECRET_KEY>
STRIPE_PUBLIC_KEY | <STRIPE_PUBLIC_KEY>
STRIPE_SECRET_KEY | <STRIPE_SECRET_KEY>
STRIPE_WH_SECRET | <STRIPE_WH_SECRET>
USE_AWS | True

8. On Heroku in a Deploy page, choose **Connect Github** and **Enable Automatic Deployment** and new commits will be automaticly deployed to your neew Heroku application.
</details>

# Credits

### Media

- Images and background used for this project were found on:
	- [Pexels](https://www.pexels.com)
	- [PxHere](https://pxhere.com/)
	- [Unsplash](https://unsplash.com/)
	- [Pixabay](https://pixabay.com/)
	- Responsive Image from [Am I Responsive?](http://ami.responsivedesign.is/)
	- Image with colour palette from [Coolors](https://coolors.co/image-picker)

### Content

Project developed by following Boutique Ado(Code Institute) mini project lessons. I added comments to pieces which were taken and modified to fit my project functionality. Apps like: Shopping Bag, Checkout, Products, Profiles.


- Blog App was created with help from [Django central](https://djangocentral.com/building-a-blog-application-with-django/).
- [Button on Image Idea](https://www.w3schools.com/howto/howto_css_button_on_image.asp)
- [Ideas for Favorites](https://stackoverflow.com/questions/61561263/django-wishlist-feature-implementing)
- Ideas for Newsletter Subscription found on Slack
- [Style guide for Python Code](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
- [README dropdown header styling](https://stackoverflow.com/questions/47392245/show-dropdown-area-expandable-area-with-code-in-markdown-file)
- [README dropdown](https://gist.github.com/citrusui/07978f14b11adada364ff901e27c7f61#file-dropdown-md)

### Acknowledgements
I want to say huge thanks to my mentor Reuben Ferrante, who guided me through all Code Institute Course. Thankful for his patience, professionalism and good words which motivated me in past months.
As well thanks to Code Institute Tutors who helped me to deal with all issues. And somehow taught me - to ask for help when I need it. Before, I had issues with that :)
Thanks to all Code Institute's team for skills, knowledge, support, motivation and a chance to be a student again.
