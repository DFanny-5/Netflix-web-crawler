# Netflix data crawler

This is the web crawler you can use to scrap the metadata of all the movies and tv shows available on Canadian Netflix

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## Technologies
Project is created with:
* Python 3.9


The scrapped dataset will include 13 different attributes of each movie include:
1. movie/tv show title : string
2. genre : list[string]
3. cast : list[string]
4. director : list[string]
5. time duration : int
6. added date : timestamp
7. added month : int 
8. added year : int
9. parent control level : string
10. original language : string
11. subtitle options : list[string]
12. description : string


I tried to implement all the OOP programing concept I learn from the real work experience. So I refactored the code to improve its readability and maintainability.

1. src folder:
   1. This is the folder hold all the source script
2. 