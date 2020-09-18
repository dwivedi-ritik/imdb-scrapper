import requests
from bs4 import BeautifulSoup
import re

class Movie():
	def __init__(self,movie_id):
		self.url = "https://www.imdb.com/title/"
		self.movie_id = movie_id
		self.response = requests.get(self.url+self.movie_id).content
		self.soup = BeautifulSoup(self.response , "html.parser")
		self.creator = {}
	
	def get_title_data(self):
		upper_data = self.soup.find(class_="title_wrapper")
		self.creator["title"] = upper_data.h1.text.replace('\xa0','')
		self.creator["duration"] = upper_data.time.text.strip()

		for x in upper_data.find_all("a"):
			if "releaseinfo" in x["href"]:
				self.creator["releaseinfo"] = x.text.replace("\n" ,"")
			elif "genres" in x["href"]:
				self.creator["genres"] = x.text


	def cast_data(self):
		summary = self.soup.find_all(class_ = "credit_summary_item")
		for i in summary:
		    if len(i.find_all("a")) > 1:
		        self.creator[i.h4.text] = [str(x.text) for x in i.find_all("a") if x.get("href") != "fullcredits/"]
		    else:
		        self.creator[i.h4.text] = i.a.text
	
	def get_summary(self):
		story = self.soup.find(class_="summary_text")
		self.creator["summary"] = story.text.strip()
	
	def get_rating(self):
		rating = self.soup.find(class_="ratings_wrapper")
		self.creator["votes"] = rating.a.text
		self.creator["rating"] = rating.strong.text
	
	def get_img(self):
		poster = self.soup.find(class_="poster")
		link = poster.find("img").get("src")
		l = link.rfind("U")+1
		img_links = [link[:l+1]+"1280", link[:l+1]+"480" , link[:l+1]+"320"]
		self.creator["poster_img"] = img_links

	def render(self):
		self.get_title_data()
		self.cast_data()
		self.get_summary()
		self.get_rating()
		self.get_img()
		return self.creator
