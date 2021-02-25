# "Shopping Cart Project"

An example Python application for students to practice processing and validating user inputs in Python

## Installation

Fork this [remote repository](https://github.com/mcoyne16/CoolShoppingCart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

## Setup

First, create and activate a new virtual environment, perhaps called "shopping-env"
# conda create =n shopping_env python=3.8
# conda activate shopping-env


Next, in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired tax rate:

    USER_NAME = "Firstname Lastname"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Use

Now you are ready to use the tool.  You can enter or scan any number corresponding to a product id in the products list.  If you make an invalid entry, the program will prompt you to try again.

Once you are finished entering the selected products, type "done" and press enter.  Your receipt will then be generated showing information about the location, time, subtotal, and a list of items purchased.


