# StarLordBot
A simple bot written in python to get Nasa's APOD images

# Requirements
Python 3.7 or greater.

# How to use
Use StarLord is very simple, just follow this lines :)

## First install dependencies
`$ pip3 install beautifulsoup4 requests loguru`

## Now, put this lines inside a file of your choice, and you are ready to go!
```python
from bot.StarLordBot import StarLordBot

starLord = StarLordBot()

starLord.fetchApodArchive()

starLord.getListOfLinks(15)

starLord.getAllPictures()
```

## Or you can just call example.py :)
`$ python example.py`

# Docker
If you wish, you can run StarLordBot inside a Docker container

## Build Python image with StarLordBot's dependencies
`# docker build -t starlord-bot /path/to/Dockerfile`

## Run the container
`# docker run --rm -it -v "$PWD":/app starlord-bot python /app/example.py`

# Contribute!
Want to help? Clone this repo and open your PR!

This bot is a very basic piece of code, and it's, by no means, the best and the cleanest way to implement a bot, but feel free to use and redistribute any way you want.