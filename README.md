# fuji

## About

fuji is a web-application that takes in a video and returns music dynamically generated to fit the video, developed by Will Ledig and Joel Abraham for HackRice 8.

### How it Works

Whenever a user uploads a video, fuji samples individual frames from the video at a specified time interval, and inputs those frames into a variety of APIs (including Microsoft Azure's Vision and Emotion APIs) to compute valence and arousal values (aka data on mood) throughout the video's duration. Once that's complete, this data is processed through a neural network to generate a MIDI file representative of the video's visuals.


## Setting up the Application

### Running Flask App

Navigate to current working directory. Enter `export FLASK_APP=server.py` in Terminal to point the Flask environment variable towards the desired Python script. Then, execute `python3 -m flask run` to run the app.

### Configuring Chrome

(On Mac) Close all Chrome tabs and then enter `open -a Google\ Chrome --args --disable-web-security --user-data-dir=""` in Terminal to run Chrome with the proper settings.

### Running Polymer

First, make sure polymer-cli is installed. Once it is, navigate to the root of the repo and run `polymer serve` and enter the returned URL in Chromem to get to the application.

