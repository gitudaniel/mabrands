# Notes to the challenge. make h1
------------------------------------------------------------------

## Initial assessment
My initial assessment of the information sent via email was as follows:
- The API back-end takes precedence over the Admin Dashboard
- The properties of my collected data will constitute my API models
- Deployment and continuous integration are significant

## Personal assessment
I carried out an audit of the task at hand, my skill level and the available time.

From prior experience, I have learned that at my current level it can be done.
The bigger question is in how long.

Given that I may not be able to implement all the features I had to come up with a plan of action to approach this problem.

I had heard about django rest framework but had never used it before.
Considering this was critical to the assignment, I had to find out how to use it.

Once the API was built and running, the next priority would be deployment.
Deployment tends to take longer than expected but once its done, hopefully it's a matter of updating the code

Depending on how much time was left, a determination of the features to build on the admin dashboard would be made.
From a high level review, the initial set was the superuser login and ability to view all the data and view data from specific users.
The rationale behind this is that before you can edit and update the data, you must first be able to view it.
You also wouldn't want just anybody being able to view the data from the admin side so a registration and a login are essential.

When it comes to tests, the unfortunate thing is that is takes so long in the short run but saves time in the long run.
For me it will take even longer since I am just getting conversant with testing.
Given the nature of the assignment I choose to build a working application over writing tests.
Testing requires one to be able to envision the end goal without actually seeing it.
Having never built an API before this would have been impossible.
This would also provide a valuable learning experience on working with APIs.

For deployment, I intended to serve my files with nginx over gunicorn and translate the same to my local machine.

Docker and continuous integration did not seen key to the working of the project.
By this I mean that the project could work just as well without them but better with them.
For this reason they took last position in my list of priorities.

##Final outline of tasks
Get enough knowledge to build a working API

Deploy said API

Assess time left and build basic features of the admin dashboard

Get deployment up to date

Write tests

Implement continuous integration

Set up containerization with Docker
