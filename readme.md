# VICKI'S ONLINE SHOP

Trello Board: 

---

## Overview
This app will be an online shop for small business owners to sell their wares. The app will provide a user view point to buy items and a business owner viewpoint to upload and sell items. 
The user interface will be clear and simple, focusing on the items that the business owner is selling. The user will be able to create an account to track their purchases and keep items in their basket.  
The business owner (admin) interface will allow the owner to add, remove, and update the items for sale. There will be a page to view their orders and mark the status of the order to easily keep track. There will also be a page to track sales.

---

## Install Steps

You will need the latest version of python and the pip package manager to complete the installation steps. Once you have python and pip, the steps are as follows:

- Clone the repository: `git clone https://github.com/rheal3/receipt_app`
- Change directory into the repository: `cd receipt_app`
- Make sure venv is installed: `pip install venv`
- Create the virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the dependencies from requirments.txt: `pip3 install -r requirements.txt`
- Run the app: `python src/main.py`

---

## Wireframes

### Customer Interface

#### Landing Page
The landing page will have details about the business as well as photo's to entice the customer to continue further into the website.  
The background image will scroll through different product images with the business logo appearing ontop in the center of the page.
![]()

#### Customer Profile
The customer profile page will be a place for the customer to view their purchases and order history. By creating an account and logging in the customer will be able to come back to their basket items after leaving the website.
![]()

#### Shop
The shop page will contain 'item cards' that have images of the items for sale with the item name and price below. When the customer clicks on the item card a pop up will display (and the background will blur/become opaque) containing the item name, image, description, price, quantity, different options for the item and an add to cart button.  
On the left hand of the page will be a category selection where the customer can choose the category of item they wish to browse. There will also be a sorting button to sort A-Z, Z-A, or by price.
![]()

#### Basket/Cart
The cart page will display the items that the customer has selected and give the customer options to remove, change quantity, or proceed to checkout.
![]()

#### Checkout
The checkout page will take the customers details and securely checkout their purchase. The customer will receive an order number and receipt.
![]()

#### Contact
The contact page will have a simple for the customer can fill out providing their name, email, subject and message that will be sent through email to the business owner.
![]() 

### Admin Interface
The admin will be able to view and access the customer interface in the same manner as the customers, however in the drop down after logging in they have options for: managing the shop, managing orders, viewing statistics, and viewing customers.
![]()

#### Manage Shop
When the admin clicks on an item card the same pop up will appear, but will fields for editing. There will be extra fields for the category of the item and the admin will be able to add or delete item options. The admin will be able to update, delete, or archive the item card. The admin can access archived items through the archive tab under the add item tab on the left hand side. They will also be able to add categories on the left hand side at the bottom of the categories list.
![]()

#### Orders
Orders will be ordered by order id. There will be a filtering option to filter by order status. When the admin clicks on the order it will show which items have been ordered, when, and the quantity; whether the customers payment has been received; and the shipping details. The admin will be able to change the status of the order within this popup.
![]()

#### Statistics
<!-- Currently unsure about what statistics are important... -->
<!-- ![]() -->

#### Customers
<!-- This page will list all customers who have made accounts and allow the admin to send a password reset email to the customer. ??? -->
<!-- ![]() -->