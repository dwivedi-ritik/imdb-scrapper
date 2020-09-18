# Flask-Imdb-api (based on webscrapping)

-  Hosted on Heroku `https://imdb-scaper-api.herokuapp.com/get_movie/id=movie id/`
-  eg - this is the normal link `https://www.imdb.com/title/tt4154796/` . its id is `tt4154796`
-  url route for getting response `/get_movie/id="your_Movie_id/`
-  wrong url will through error
-  support for getting high quality movie poster 
-  more feature will be added soon


# Response

{<br /> 
&nbsp;&nbsp;"data": {<br /> 
&nbsp;&nbsp;"title": "Avengers: Endgame(2019) ",<br /> 
&nbsp;&nbsp;"duration": "3h 1min",<br /> 
&nbsp;&nbsp;"genres": "Drama",<br /> 
&nbsp;&nbsp;"releaseinfo": "26 April 2019 (USA)",<br /> 
&nbsp;&nbsp;"Directors:": [<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"Anthony Russo",<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"Joe Russo"<br /> 
&nbsp;&nbsp;],<br /> 
&nbsp;&nbsp;"Writers:": [<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"Christopher Markus",<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"Stephen McFeely",<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"14 more credits"<br /> 
&nbsp;&nbsp;],<br /> 
&nbsp;&nbsp;"Stars:": [<br /> 
&nbsp;&nbsp;"Robert Downey Jr.",<br /> 
&nbsp;&nbsp;"Chris Evans",<br /> 
&nbsp;&nbsp;"Mark Ruffalo"<br /> 
&nbsp;&nbsp;],<br /> 
&nbsp;&nbsp;"summary": "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once &nbsp;&nbsp;more in order to reverse Thanos' actions and restore balance to the universe.",<br /> 
&nbsp;&nbsp;"votes": "760,560",<br /> 
&nbsp;&nbsp;"rating": "8.4",<br /> 
&nbsp;&nbsp;"poster_img": [<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX1280",<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX480",<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_UX320"<br /> 
&nbsp;&nbsp;&nbsp;&nbsp;]<br /> 
&nbsp;&nbsp;}<br /> 
}




# Warning
- This API is based on web scrapping . so it will work until IMDb don't change their html elements.
- I did't included the support for upcomming movies , so if you are going to pass the id of a movies which is not released yet, this will response error.
- API is will load the whole page then pick the element so this is little slow than offical API.



