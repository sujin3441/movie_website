import fresh_tomatoes
import media

beauty_and_the_beast = media.Movie("Beauty and the Beast",
"Belle (Emma Watson), a bright, beautiful and independent young woman, is taken prisoner by a beast (Dan Stevens) in its castle.",
"http://t2.gstatic.com/images?q=tbn:ANd9GcRfYpMZYI-nnFJZ6vmdH7w8qNCp_G2OwqWQqszSdhMbfLR_CHvi",
"https://www.youtube.com/watch?v=e3Nl_TCQXuw"
)

begin_again = media.Movie("Begin Agin",
"Gretta (Keira Knightley) and her songwriting partner/lover Dave (Adam Levine) head for New York when he lands a record deal with a major label.",
"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSDS-OOQKIXQ11bqxhRpIQXp2nYojEkg3PVo1xcpiMffvFZ9ezvOCcKFw",
"https://www.youtube.com/watch?v=uTRCxOE7Xzc"
)

grey = media.Movie("50 shades darker",
"When a wounded Christian Grey (Jamie Dornan) tries to entice a cautious Anastasia Steele (Dakota Johnson) back into his life, she demands a new arrangement before she will give him another chance.  ",
"http://t0.gstatic.com/images?q=tbn:ANd9GcTm7vaHWXiIkfKAWAwrxRGyfZFCLQ1tVPIVnyQYVUfV74fwws5P",
"https://www.youtube.com/watch?v=OItKvc13gws"
)

notebook = media.Movie("Notebook",
"In 1940s South Carolina, mill worker Noah Calhoun (Ryan Gosling) and rich girl Allie (Rachel McAdams) are desperately in love. ",
"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcStp4k_zMt3Rt2ZtucjjWzLra1b9O1stanlWgooeDK4A0bs5J8n",
"https://www.youtube.com/watch?v=4M7LIcH8C9U"
)

star_wars = media.Movie("Star Wars: The Last Jedi",
"The further adventures of Luke Skywalker (Mark Hamill), Leia (Carrie Fisher) and Rey (Daisy Ridley).",
"http://t0.gstatic.com/images?q=tbn:ANd9GcTJ3OoSVXz96xWVQ1ak86U4_g4vfHfmqvj3FNnudF5SS3JAf_2_",
"https://www.youtube.com/watch?v=GAOZA8zqk4g"
)

if_only = media.Movie("If Only",
"A man (Paul Nicholls) tries to avert destiny when he gets an opportunity to relive the day his lover (Jennifer Love Hewitt) died in an auto accident.",
"http://www.gstatic.com/tv/thumb/movieposters/160181/p160181_p_v8_ae.jpg",
"https://www.youtube.com/watch?v=3z5XDNHmBco"
)

movies = [beauty_and_the_beast, begin_again, grey, notebook, star_wars, if_only]
fresh_tomatoes.open_movies_page(movies)
