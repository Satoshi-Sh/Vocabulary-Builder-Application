## Demo Video
https://youtu.be/QVxQBU1VZRY

## Application 

Users can build up more vocabulary through quiz. The user can 
choose the quiz level according to their needs (up to three levels). Registered users' mistakes will be recorded so they can review their mistakes. The review page shows words and definitions the user answered wrong, it also shows how many times and when they answered wrong and they can archive words once they reviewed. 


## Distinctiveness and Complexity

The application loads wordlist of the user's choice, and make quizes by looking up dictionary api, and then put the data to each section of the page. This application does have only two models, but heavily rely on JavaScript works to provide the service. Naturally, JavaScript is more complex. I also added a gif picture, icons, and animation to make the application more user-friendly. This time, I added infinite scroll to the review page instead of pagination. 

## Technologies Used
The application backend was made by Django. Bootstrap was used for the design of the pages. Javascript was used to interact with the server from the client browser. Python was used to make most of a free dictionary api. 

## Files 

### word_game/word_list
This directory has wordlist text files from grade 1 to grade 12, and a
python script to process copied text from the website. The website detail is on the credit section.

### word_game/word_api.py 
This python script is used to look up words with a dictionary api. The api detail is on the credit seciton. 

On this script, I made a quiz class to organize the data and make quiz. 


## How to run

You can type "python manage.py runserver" in the console.


## To be implemented
I made this application since building vocabulary is quite a work for kids and language learners. If I have more resource(the dictionary api I used often has empty strings), I would like to add more types of quiz such as choosing synonyms and antonyms. Also it will be nicer if I make a dash board showing users stats of scores. I need to research a lot how to do it. 

## Lastly 

Thank you for the great courses as always. I started cs50x this June, and loved your teaching styles. I have completed CS50x, CS50P, CS50AI, and CS50Web (I'm waiting for grading of the AI course though) since then. These courses helped me a lot to be a better programmer. I liked making videos for each project. I can practice how to explain things and also can show the videos to the potential employears in my portfolio website. 

I'm still looking for a job related to IT and Data, but I'm more confident now to be successful in my career.  From now, I will focus on making more my personal projects and apply for jobs. I would recommend these courses anyone who likes to get into the Tech industry. Looking forward to seeing you guys on the technical interview preparation seminar. 



## Credit 

use this free dictionary api to look up definitions of words
https://dictionaryapi.dev/ 

word_list file was extracted from this website.
https://www.greatschools.org/gk/articles/vocabulary-words-for-1st-through-12th-graders/

(forgot keeping notes of the links of favicon and loading-wating.gif.. )
