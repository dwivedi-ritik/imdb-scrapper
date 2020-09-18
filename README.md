# Flask-Imdb-api (based on webscrapping)

-  Hosted on Heroku `https://imdb-scaper-api.herokuapp.com/get_movie/id=movie id/`
-  eg - this is the normal link `https://www.imdb.com/title/tt0816692/` . its id is `tt0816692`
-  url route for getting response `/get_movie/id="your_Movie_id/`
-  wrong url will through error
-  support for getting high quality movie poster 
-  more feature will be added soon
-  url *https://imdb-scaper-api.herokuapp.com/get_movie/id=tt0816692/*


# Response
![carbon (1)](https://user-images.githubusercontent.com/58474947/93593300-b661d000-f968-11ea-941b-fa911e99b386.png)

# Warning
- This API is based on web scrapping . so it will work until IMDb don't change their html elements.
- I did't included the support for upcomming movies , so if you are going to pass the id of a movies which is not released yet, this will response error.
- API is will load the whole page then pick the element so this is little slow than offical API.



