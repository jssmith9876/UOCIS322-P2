# UOCIS322 - Project 2 #

A "getting started with Docker" project for CIS 322, Introduction to Software Engineering, at the University of Oregon.

NOTE: This project is going to require Docker, therefore use * testium * instead of the default development server (ix-dev).
NOTE: Should you experience a permission error while using Docker on the server, email systems and ask them to "add you to the docker group".

# Getting started on this project

* Go to the web folder in the repository. Read every line of the docker file and the simple flask app.

* Build the simple flask app image using

  ```
  docker build -t your-name-cis322-2 .
  ```
  **Make sure to use a unique name if you're running on testium.**
* Run the container using

  ```
  docker run -d -p port:5000 your-name-cis322-2
  ```
NOTE: Make sure to change the port (both in the flask API so that it reads from credentials.init, and here in the run command. This is to ensure that you and your classmates don't end up using the same port and that tests do not interfere with each other.)
* Launch http://hostname:5000 using web browser and check the output "UOCIS docker demo!".

## Author: Jordan Smith, jsmith37@uoregon.edu ##
