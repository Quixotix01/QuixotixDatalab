To create a dataset of Tamil music artists and their most played songs on Spotify, you can follow these steps. You'll need to access the Spotify API, which requires some setup and programming skills. Here's a breakdown of the tools and the procedure for this project:
Tools Required
Spotify for Developers Account

To access the Spotify API, you’ll need to create a developer account and obtain API credentials.
Spotify Web API

Spotify provides a Web API that allows developers to retrieve information about artists, albums, tracks, and playlists.
Python

Python is a popular programming language for working with APIs and data. You'll need to use libraries like spotipy, requests, and pandas to retrieve and manipulate the data.
Spotipy

Spotipy is a lightweight Python library that provides easy access to the Spotify Web API.
Jupyter Notebook or any IDE (e.g., VS Code, PyCharm)

You’ll need a development environment to write and test your code.
Pandas

A Python library to manage and structure your data in DataFrames.

Procedure
Step 1: Set Up Spotify Developer Account
Go to Spotify Developer and create an account.
Create an application to get your Client ID and Client Secret.
Add a Redirect URI (you can use http://localhost:8888/callback for testing).

To create an application on Spotify and obtain your Client ID and Client Secret, follow these steps:

Step-by-Step Guide
Step 1: Create a Spotify Developer Account
Go to the Spotify Developer Dashboard.
Log in with your existing Spotify account. If you don’t have an account, you can create one for free.
Step 2: Create a New Application
Once logged in, click on "Create an App" in the top right corner of the dashboard.

Fill in the required details:

App Name: Enter a name for your application (e.g., "Tamil Music Data Collector").
App Description: Briefly describe your application (e.g., "An application to retrieve Tamil music artists' top songs from Spotify").
Website: You can leave this blank for now or provide a website if you have one.
Redirect URIs: Enter a redirect URI that Spotify can use to send you back the authorization token. If you're developing locally, you can use http://localhost:8888/callback.
After filling out the details, click on "Create".

Step 3: Retrieve Your Client ID and Client Secret
After creating the app, you'll be taken to the app's dashboard.
Here, you'll see your Client ID on the dashboard. This is a unique identifier for your application.
Click on "Show Client Secret" to reveal your Client Secret. This is a secret key that you need to keep secure, as it provides access to Spotify’s API on behalf of your application.
Step 4: Configure Redirect URI (if needed)
Under your app's settings, you'll see a section for Redirect URIs.
If you haven't already, click on "Edit Settings" and add a redirect URI (e.g., http://localhost:8888/callback).
Click "Save".

Step 2: Install Required Libraries
You'll need to install the following libraries using pip:
pip install spotipy pandas requests

Get to the Script/
