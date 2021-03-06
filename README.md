# ireport-api
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that need government intervention.

[![Build Status](https://travis-ci.org/neelxie/ireport-api.svg?branch=develop)](https://travis-ci.org/neelxie/ireport-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a439c5890cce4f94b3b50e53036c014e)](https://www.codacy.com/app/neelxie/ireport-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=neelxie/ireport-api&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/neelxie/ireport-api/badge.svg?branch=develop)](https://coveralls.io/github/neelxie/ireport-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/aee377f03ebc940278a0/maintainability)](https://codeclimate.com/github/neelxie/ireport-api/maintainability)

<b> Site has been built with.</b>
*   Language - Python
*   Serverside Framework - Flask
*   Testing Framework - Pytest
*   Linting Framework - Pylint
*   Style GuideLine - Autopep8

## Application Demo 

*   Check out the [User Interface](https://neelxie.github.io/iReport/UI/)

## Features

  | REQUESTS | APP ROUTES | FUNCTION | ROLE 
  |----------|------------|----------|-----
  |  GET | /api/v1/ | Default/Home Page. | All
  |  GET | /api/v1/red-flags | Fetch all red-flags records. | User 
  |  GET | /api/v1/auth/users | Get all app users. | Admin
  |  GET | /api/v1/auth/users/[user_id] | Get a single user details | Admin
  |  GET | /api/v1/red-flags/[red_flag_id] | Fetch a specific red-flag by id. | User
  |  GET | /api/v1/auth/users/[user_id]/red-flags | Fetch a specific red-flag by id. | User
  |  PATCH | /api/v1/red-flags/[red_flag_id]/location | Edit/Change location of red-flag. | User
  |  PATCH | /api/v1/red-flags/[red_flag_id]/comment | Edit/Change comment of red-flag. | User
  |  PATCH | /api/v1/red-flags/[red_flag_id]/status | Change status of red-flag. | Admin
  |  DELETE | /api/v1/red-flags/[red_flag_id] | Delete red-flag. | User
  |  POST | /api/v1/red-flags | Create a red-flag record. | User
  |  POST | /api/v1/auth/signup | Register for an account as a user. | All
  |  POST | /api/v1/auth/login | Log into app account. | All

## Installation:

*  Clone [this](https://github.com/neelxie/ireport-api.git) git repo to local directory.
``` cd ireport-api ```
*  Create a virtual environment:
``` virtualenv venv ```
*  Activate virtual environment:
``` venv\Scripts\activate ```
*  Install dependencies:
``` pip install -r requirements.txt ```
*  Do not forget to run this in the develop branch:
``` git checkout develop ```

## Running the application:

Inside the iReport-api folder.
``` python run.py ```

## Running the tests:

*  Run this command in the project directory.
``` pytest --cov=.```

## Deployment

*  This app has been deployed on Heroku at the url [here.](https://ireporta.herokuapp.com/api/v1/)

## Contribute

*  Join me [here](https://github.com/neelxie/ireport-api/tree/develop) and let us create super amazing stuff together.

## Credits

*  I thank GOD, to whom everything plays out ALWAYS.
*  I thank all LevelUp 35 team, facilitators and attendees
   for the help offered to better me.
*  I would like to thank Andela for the opportunity to change the world.

## Author

*  Sekidde Derrick