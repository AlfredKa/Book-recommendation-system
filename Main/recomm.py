import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recom(book):
    def get_title_from_index(index):
        return df[df.index == index]["Title"].values[0]

    def get_index_from_title(title):
        return df[df.Title == title]["index"].values[0]

    books = pd.read_csv(r"C:\Users\Alfred Karanja\Downloads\Book_Recommendation_System_main\BookDataset\Bookz.csv")
    books = books[:1000]
    df = books
    img = pd.read_csv(r"C:\Users\Alfred Karanja\Downloads\Book_Recommendation_System_main\BookDataset\Imagez.csv")

    features = ['Title', 'Author', 'Publisher']
    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_features(row):
        try:
            return row['Title'] + " " + row['Author'] + " " + row['Publisher']
        except:
            print("Error:", row)

    df["combined_features"] = df.apply(combine_features, axis=1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)

    books_index = get_index_from_title(book)
    similar_books = list(enumerate(cosine_sim[books_index]))
    sorted_similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)

    output = []
    index = []

    for i, element in enumerate(sorted_similar_books):
        if i > 9:
            break
        book_index = element[0]
        output.append(get_title_from_index(book_index))
        index.append(get_index_from_title(output[i]))

    imgg = []
    year = []
    author = []
    final_list = []
    for i in index:
        imgg.append(img["Image-URL-M"][i - 1])
        year.append(books["Year"][i - 1])
        author.append(books["Author"][i - 1])

    for i in range(len(index)):
        temp = []
        temp.append(output[i])
        temp.append(imgg[i])
        temp.append(year[i])
        temp.append(author[i])
        final_list.append(temp)

    return final_list




def bookdisp():
	books=pd.read_csv(r"C:\Users\Alfred Karanja\Downloads\Book_Recommendation_System_main\BookDataset\Bookz.csv")
	img=pd.read_csv(r"C:\Users\Alfred Karanja\Downloads\Book_Recommendation_System_main\BookDataset\Imagez.csv")

	title=[]
	imgg=[]
	year=[]
	author=[]
	finallist=[]

	r=np.random.randint(2,1000,10)

	for i in r:
		title.append(books["Title"][i-1])
		imgg.append(img["Image-URL-M"][i-1])
		year.append(books["Year"][i-1])
		author.append(books["Author"][i-1])

	for i in range(10):
		temp=[]
		temp.append(title[i])
		temp.append(imgg[i])
		temp.append(year[i])
		temp.append(author[i])
		finallist.append(temp)

	return finallist