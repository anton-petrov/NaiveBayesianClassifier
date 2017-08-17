from classifier import *

classifier = Classifier()


def print_hypothesis(opinion, classifier):
    print("Review:\n")
    print(opinion + "\n")
    for item in classifier.get_hypothesis(opinion):
        print("Hypothesis: ", item[0], ", Probability: ", item[1], "\n")


classifier.train("""Actually, there is practically nothing to say about the film,
                 Because in the end we did not even see the movie.
                 Creation of actors alternated with frames in style
                 "How not to shoot a movie," while the scriptwriter
                 Was preparing for the control work on natural sciences,
                 And the highly respected director attended the sessions
                 On correcting the inherent mental inferiority.""", "-")
classifier.train("""To say that I was satisfied with what I saw would be
                 Not entirely correct, rather the whole story is left
                 Me completely indifferent, which is quite strange.
                 I always watch movies very emotionally. In almost every
                 Film, even the most trashy, there are episodes,
                 Which are remembered to me.""", "-")
classifier.train("""I went to this film on the very first day of the rental.
                 Expected a lot of just the trailer
                 When I first saw him at the cinema,
                 I wanted to see the film itself because of the humor, firstly.
                 I was not disappointed. Perhaps the only drawback
                 You can call the story itself - a bit trivial, and cruel.
                 But everything else, if compared with other
                 Russian paintings, at a high level. So, I will describe.""", "+")
classifier.train("""Probably, only in mediocre and stereotyped
                 Things can be seen most important.
                 Alexander Chernyaev's film "The Irony of Love" - a bright
                 An example of an eternal pass-through fairytale story,
                 As the princess falls in love with the usual "Ivan", the plot,
                 Transferred to our realities. The film can be scolded
                 As many as you like, but it was once again noticed
                 Much interesting about the psychology of modern man""", "+")

opinion = """In general, the film should be perceived as a pleasant
              A sweet picture that makes you smile, smile,
              Empathize with the heroes. I advise you to watch the girls,
              Dreaming of a prince on a white horse and believing in love."""
print_hypothesis(opinion, classifier)

opinion = """A crappy, boring film. While I watched it, I slept
              three times. Do not waste time on this misunderstanding."""
print_hypothesis(opinion, classifier)