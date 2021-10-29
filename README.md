# FeedbackBot: An AI based chatbot
Feedbackbot accepts user input for the movie they watched.\
It then asks for a review/feedback on said movie, and performs sentiment analysis on input review.

Sentiment classification is done using a Naive Bayes machine learning model, trained on IMDB movie reviews dataset.\
If the review is classified as with positive intent, the bot recommends top 3 similar movies to the movie watched (input at the beginning).\
If the review is classified as negative, the bot replies with an apology.

Movie recommendation is by done computing cosine similarity of input movie and all movies in the dataset.\
Since the input for the movie recommender is limited (only movie name), cosine similarity is computed on the movies overview, rather than its name, director, cast, genre, etc.\
The dataset used for this is MovieLens dataset.


