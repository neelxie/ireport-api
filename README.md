# ireport-api
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

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

# Application Demo 

*   UserInterface ``` https://neelxie.github.io/iReport/UI/ ```

# Features

  | REQUESTS | APP ROUTES | FUNCTION 
  |----------|------------|---------
  |  GET | /api/v1/red-flags | Fetch all red-flags records.
  |  GET | /api/v1/red-flags/[red_flag_id] | Fetch a specific red-flag by id.
  |  PATCH | /api/v1/red-flags/[red_flag_id]/location | Edit location of red-flag.
  |  PATCH | /api/v1/red-flags/[red_flag_id]/comment | Edit comment of red-flag.
  |  POST | /api/v1/red-flags | Create a red-flag record.
  |  POST | /api/v1/users | ye  

# Installation:

*  Clone git repo to local directory ``` https://github.com/neelxie/ireport-api.git ```
``` cd ireport-api ```
*  Create a virtual environment:
``` virtualenv venv ```
*  Activate virtual environment:
``` venv\Scripts\activate ```
*  Install dependencies:
``` pip install -r requirements.txt ```
*  Do not forget to run this in the develop branch:
``` git checkout develop ```

# Running the application:

Inside the iReport-api folder.
``` python run.py ```

# Running the tests:

*  Run this command in the project directory.
``` pytest ```

#Deployment

*  This app has been deployed on Heroku at the url below:
``` https://.herokuapp.com/api/v1/ ```

# Contribute

*  Join me and let us create super amazing stuff together.
``` https://github.com/neelxie/ ```

# Credits

*  I thank GOD, to whom everything plays out ALWAYS.
*  I thank all LevelUp 35 team, facilitators and attendees
   for the help offered to better me.
*  I would like to thank Andela for the opportunity to change the world.

# Author

*  Sekidde Derrick