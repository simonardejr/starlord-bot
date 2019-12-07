import requests
from loguru import logger
from bs4 import BeautifulSoup

class StarLordBot():

    soup = None
    links = None
    result = None
    picture = None
    quantity_of_images = 5
    base_url = 'https://apod.nasa.gov'
    apod_archive = base_url + '/apod/archivepix.html'

    def __init__(self):
        print('   _____ __             __                   ______        __  ') 
        print('  / ___// /_____ ______/ /   ____  _________/ / __ )____  / /_ ')
        print('  \__ \/ __/ __ `/ ___/ /   / __ \/ ___/ __  / __  / __ \/ __/ ')
        print(' ___/ / /_/ /_/ / /  / /___/ /_/ / /  / /_/ / /_/ / /_/ / /_   ')
        print('/____/\__/\__,_/_/  /_____/\____/_/   \__,_/_____/\____/\__/   ')
        print('')
        print('✨ A simple bot to get Nasa\'s APOD images ✨')
        print('')

    def fetch(self, url):
        logger.opt(ansi=True).info(f'<b>Fetch</b>: <blue>{url}</blue>')
        self.result = requests.get(url)

    def fetchApodArchive(self):
        logger.opt(ansi=True).info(f'<b><yellow>Fetching Archive</yellow></b>')
        self.fetch(self.apod_archive)

    def getListOfLinks(self, quantity_of_images=None):
        logger.opt(ansi=True).info(f'<yellow>Getting</yellow> ' + \
            f'<b>{quantity_of_images}</b> <yellow>links</yellow>')

        if quantity_of_images is None:
            quantity_of_images = self.quantity_of_images

        if self.parseContent():
            links = self.soup.find_all("a")
            self.list_of_links = links[3:(quantity_of_images + 3)]

    def getAllPictures(self): 
        for link in self.list_of_links:
            link_to_fetch = self.adjustLink('apod/' + link["href"])
            self.fetch(link_to_fetch)
            if not self.getPictureOfTheDay():
                logger.opt(ansi=True).error(f'<b>Picture not found</b>... ' + \
                    f'Skipping...')

    def getPictureOfTheDay(self):
        if self.parseContent():
            if self.findPictureElement():
                logger.opt(ansi=True).success(f'<b>Picture found</b>: ' + \
                    f'<blue>{self.picture}</blue>')
                return True

        return False

    def findPictureElement(self):
        link = self.soup.find("img")
        if link is not None:
            self.picture = self.adjustLink(link["src"])
            return True

        return False

    def parseContent(self):
        if hasattr(self.result, 'text'):
            self.soup = BeautifulSoup(self.result.text, 'html.parser')
            return True

        return False

    def addHostToUrl(self, url):
        return self.base_url + '/' + url

    def hasHost(self, url):
        return 'http' in url

    def adjustLink(self, url):
        if not self.hasHost(url):
                url = self.addHostToUrl(url)

        return url
