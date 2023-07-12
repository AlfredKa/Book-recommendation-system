# BookMatch: Enhancing Reading Experience With a Book Recommendation System Using Content-Based Filtering.

BookMatch leverages the Goodreads dataset to suggest books to users based on their prefernces and interests. Content-based filtering is a recommendation approach that focuses on analyzing the content and characteristics of items to identify similarities and make recommendations using cosine similarity. In the context of books, this involves extracting relevant features such as genres, authors, publication dates, and user ratings from the Goodreads dataset. Hence, it allows for personalized recommendations by focusing on the specific interests and tastes of individual users.

Therefore, this system aims to enhance personalized book recommendations and contribute to the field of recommendation algorithms by leveraging the vast Goodreads dataset and content-based filtering techniques.

## Algorithm Used
- Cosine similarity
  
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

How does it decide which book is most similar to the books a user likes? It is a numerical value that ranges between zero to one which helps to determine how much two books are similar to each other on a scale of zero to one. This similarity score is obtained by measuring the similarity between the text details of both of the books. This is the similarity score which is the measure of similarity between given text details of two items.

## Environment and Repository Setup

- Steps:
1. Clone the repository in your local device
   
   `git clone https://github.com/AlfredKa/Book-recommendation-system.git`

2. Install requirements

   `pip install -r requirements.txt`

3. Then extract the bookdataset.zip in your directory, then change the path of dataset in the recomm.py file in line number 13 and 16.

4. Now simply run the server in terminal using

   `python run.py`

