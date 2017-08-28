##HOW TO USE THE API
-------------------------------------------------------------------------------
This is a guide on the brands API

I made the assumption that some users may be coming from the mobile application.
For those users all they'd have to do is to go to the /api-auth/ page, enter their credentials to obtain their JSONWebToken.

Using a rest client like Postman(https://www.getpostman.com/apps) or the mozilla rest client browser add-on(https://addons.mozilla.org/en-US/firefox/addon/restclient/), add this token as a header to your POST, PUT or GET request.

To view an individual Get request add the suffix /users/<id> to the url to view.

