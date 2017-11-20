# Data science blog finder

Finds the latest data science blogs across the internet in order to make it easier for data scientists across the world to stay up to date with the latest best practices and news in data science.

## Breakdown
* Extracts the latest blogs from the rss feeds of a predefined set of sources of data science blogs
* Uses a naive bayes classifier to discard blogs that do not correspond to the topic of data science
* Stores blogs in sqlite3 database
* This database serves as the backend for a Django website, which displays the data science blogs stored in the database by latest publication date

## Installation

Clone or download repository onto local computer

```bash
git clone https://github.com/SamLubbers/datascience_blogfinder.git
```
install necessary dependecies (preferably in a virtualenv, to avoid conflicts with existing packages in your computer)

```bash
cd datascience_blogfinder
pip3 install -r requirements.txt
```

## Usage

### Run blog finder

within the project directory run the following command in order for the application to find data science blogs and store it in the database (_This may take about 5 minutes to complete as it is has to deal with numerous http get requests_). 

```bash
python3 find_blogs.py
```

### Run django front end

Once you have completed the previous step a database will be created that will serve as the backend for our django website, to view the website we must complete two steps.

First we need to migrate the changes applied to our database

```bash
python3 manage.py migrate
```
Next, we can run our django server

```bash
python3 manage.py runserver
```
Development server will be started at `http://127.0.0.1:8000/`