"""
import spacy and create nlp variable
"""
import spacy

nlp = spacy.load("en_core_web_md")


def recommend_movie(description):
    """
    function to find most similar movie based on description
    :param description: description of movie
    :type description: string
    """
    with open("movies.txt", "r") as f:
        processed_movies = []
        movies = f.readlines()
        for movie in movies:
            processed_movies.append(movie)
    doc = nlp(description)
    similarities_dict = {}
    for movie in processed_movies:
        similarity = nlp(movie).similarity(doc)
        similarities_dict[similarity] = movie
        print(f"{movie}: {similarity}")
    max_sim = max(similarities_dict.keys())
    recommendation = similarities_dict[max_sim]
    print(f"\nYour recommendation is:\n{recommendation}")


"""
call function on planet hulk description
"""
recommend_movie("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the "
                "Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in "
                "peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained "
                "as a gladiator.")