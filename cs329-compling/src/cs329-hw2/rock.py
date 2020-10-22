import json
from enum import Enum, auto
from typing import Dict, Any, List

from emora_stdm import KnowledgeBase, DialogueFlow, Macro, Ngrams
from spotify_query import requester

# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    GENREQUESTION = auto()
    GENREQUESTION2 = auto()
    ERR = auto()
    ROCK = auto()
    OTHERMUSIC = auto()
    ERR2 = auto()
    ROCKDYING = auto()
    ROCKDYING2 = auto()
    ROCK_ERROR = auto()
    ROCK_ERROR2 = auto()
    ROCK_ERROR3 = auto()
    ROCK_ERROR4 = auto()
    RES2 = auto()
    ROCKAGREE = auto()
    ROCKDISAGREE = auto()
    POPULARITY = auto()
    POPULARITY2 = auto()
    POPROCKBANDS = auto()
    POPROCKBANDS2 = auto()
    ROCK_ERROR5 = auto()
    ROCK_ERROR6 = auto()
    ROCK_ERROR7 = auto()
    ROCK_ERROR8 = auto()
    ROCKIMAGE = auto()
    ROCKANS = auto()
    ROCKANS2 = auto()
    ROCK_ERROR9 = auto()
    ROCK_ERROR10 = auto()
    ROCKREPRESENT = auto()
    ROCKCOSTLY = auto()
    DIFFSOUND = auto()
    ROCKDONTKNOW = auto()
    ROCKARTISTS = auto()
    ROCKSTORY = auto()
    ROCKINSTRUMENTS = auto()
    YESAGING = auto()
    NOAGING = auto()
    AGINGIDK = auto()
    ROCKSONG = auto()
    ROCKSONG2 = auto()
    SONGARTIST = auto()
    SONGARTISTOPIN = auto()
    ROCK_ERROR11 = auto()
    ROCK_ERROR12 = auto()
    SONGARTIST1 = auto()
    ROCKCONCERT = auto()
    ROCKTICKETS = auto()



sp_requester = requester()
ontology = json.loads(open('ontology.json').read())



knowledge = KnowledgeBase()
knowledge.load_json(ontology)


df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.GENREQUESTION, '"What\'s your favorite music genre?"')

df.add_user_transition(State.GENREQUESTION, State.ROCK, '[{rock, Rock}]')
df.set_error_successor(State.GENREQUESTION, State.ROCK_ERROR)
# Error
df.add_system_transition(State.ROCK_ERROR, State.GENREQUESTION2, '"Sorry, I didn\'t catch that. What\'s your favorite music genre?"')
df.add_user_transition(State.GENREQUESTION2, State.ROCK, '[{rock, Rock}]')
df.set_error_successor(State.GENREQUESTION2, State.ROCK_ERROR2)
df.add_system_transition(State.ROCK_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')

# Turn 1
df.add_system_transition(State.ROCK, State.ROCKDYING, '"So you like rock music?! I don\'t know about that."'
                                                      '"I heard the genre is dying out; wouldn\'t you agree?"')
df.add_user_transition(State.ROCKDYING, State.ROCKAGREE, '[#ONT(yes)]')
df.add_user_transition(State.ROCKDYING, State.ROCKDISAGREE, '[#ONT(no)]')
# Error
df.set_error_successor(State.ROCKDYING, State.ROCK_ERROR3)
df.add_system_transition(State.ROCK_ERROR3, State.ROCKDYING2, '"Sorry, I didn\'t catch that. Don\'t you agree?"')
df.add_user_transition(State.ROCKDYING2, State.ROCKAGREE, '[#ONT(yes)]')
df.add_user_transition(State.ROCKDYING2, State.ROCKDISAGREE, '[#ONT(no)]')
df.set_error_successor(State.ROCKDYING2, State.ROCK_ERROR4)
df.add_system_transition(State.ROCK_ERROR4, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')



df.add_system_transition(State.ROCKAGREE, State.POPULARITY, '"Yes, I also think that the popularity of rock music is declining."'
                                                            '"Pop, hip-hop, and EDM are becoming more popular, and a lot of people say that rock is dead."'
                                                            '"What do you think is the main reason that led to this decline?"')
df.add_system_transition(State.ROCKDISAGREE, State.POPROCKBANDS, '"No, you don\'t think so? I suppose you consider pop rock"'
                                                                 '"bands of today like Imagine Dragons or Fallout Boy rock music,"'
                                                                 '"but I\'m a purist. Why do you think rock music is still so popular?"')

# Turn 2
df.add_user_transition(State.POPULARITY, State.ROCKIMAGE, '[{image, brand}]')
df.add_system_transition(State.ROCKIMAGE, State.ROCKANS, '"Yeah, a lot of big labels refuse to sign new rock bands because rock"'
                                                        '"in the past has been associated with a hedonistic image. Do you think that rock music"'
                                                         '"is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPULARITY, State.ROCKREPRESENT, '[#ONT(rockrepresentation)]')
df.add_system_transition(State.ROCKREPRESENT, State.ROCKANS, '"Yeah, rock music now is purchased mostly by white males."'
                                                             '"This could be because most rock stars in the past were white and male, but now"'
                                                             '"people are more attracted to artists that look like them."'
                                                             '"In a survey conducted in 2002, 52% of white people indicated that they"'
                                                             '"enjoy rock, while only 29% of non-whites said the same. Do you think that rock music"'
                                                             '"is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPULARITY, State.ROCKCOSTLY, '[#ONT(discount)]')
df.add_system_transition(State.ROCKCOSTLY, State.ROCKANS, '"You\'re right, it\'s expensive for new rock bands to be able to afford the equipment"'
                                                      '"to produce the sounds associated with rock music in the past, so distributing rock music"'
                                                      '"is a lot more difficult today. Do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPULARITY, State.DIFFSOUND, '[{sound, tone, beat, beats}]')
df.add_system_transition(State.DIFFSOUND, State.ROCKANS, '"Yes, \"rock\" bands like Imagine Dragons are making too much of an effort"'
                                                         '"to appeal to pop music listeners that the original sound quality of rock music has been lost."'
                                                         '"Do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPULARITY, State.ROCKDONTKNOW, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.add_system_transition(State.ROCKDONTKNOW, State.ROCKANS, '"Well, some people think that it\'s because rock artists don\'t really represent"'
                                                             '"the demographics of music fans anymore, while others think that rock music is too expensive to produce now."'
                                                            '"Do you think that rock music is now associated with an aging demographic of listeners?"')
# Error
df.set_error_successor(State.POPULARITY, State.ROCK_ERROR5)
df.add_system_transition(State.ROCK_ERROR5, State.POPULARITY2, '"Sorry, I didn\'t catch that. Why do you think rock is losing its popularity?"')
df.add_user_transition(State.POPULARITY2, State.ROCKIMAGE, '[{image, brand}]')
df.add_user_transition(State.POPULARITY2, State.ROCKREPRESENT, '[#ONT(rockrepresentation)]')
df.add_user_transition(State.POPULARITY2, State.ROCKCOSTLY, '[#ONT(discount)]')
df.add_user_transition(State.POPULARITY2, State.DIFFSOUND, '[{sound, tone, beat, beats}]')
df.add_user_transition(State.POPULARITY2, State.ROCKDONTKNOW, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.set_error_successor(State.POPULARITY2, State.ROCK_ERROR6)
df.add_system_transition(State.ROCK_ERROR6, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


df.add_user_transition(State.POPROCKBANDS, State.ROCKARTISTS, '[{artists, people, musicians, band, bands}]')
df.add_system_transition(State.ROCKARTISTS, State.ROCKANS, '"Yes, some artists like Metallica are still very true to the genre,"'
                                                           '"but other supposedly rock bands like Coldplay or Fall Out Boy are leaning more towards pop."'
                                                            '"Do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKSTORY, '[{story, meaning}]')
df.add_system_transition(State.ROCKSTORY, State.ROCKANS, '"That\'s true, a lot of unwavering rock fans love the genre because every song has a story they can relate to."'
                                                             '"But do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKINSTRUMENTS, '[{sound, instruments, guitar, drums, beat, beats, tone}]')
df.add_system_transition(State.ROCKINSTRUMENTS, State.ROCKANS, '"Yes, rock music is known for its instruments, but some say that there\'s only"'
                                                               '"so much you can do with an electric guitar or bass until it gets repetitive."'
                                                               '"Do you think that rock music is now associated with an aging demographic of listeners?"')
# Error
df.set_error_successor(State.POPROCKBANDS, State.ROCK_ERROR7)
df.add_system_transition(State.ROCK_ERROR7, State.POPROCKBANDS2, '"Sorry, I didn\'t catch that. Why do you think rock is still so popular?"')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKARTISTS, '[{artists, people, musicians, band, bands}]')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKSTORY, '[{story, meaning}]')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKINSTRUMENTS, '[{sound, instruments, guitar, drums, beat, beats, tone}]')
df.set_error_successor(State.POPROCKBANDS2, State.ROCK_ERROR8)
df.add_system_transition(State.ROCK_ERROR8, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


# Turn 3
df.add_user_transition(State.ROCKANS, State.YESAGING, '[#ONT(yes)]')
df.add_system_transition(State.YESAGING, State.ROCKSONG, '"You\'re right. A survey conducted in 2018 reported that almost 60% of respondents over the age of 50"'
                                                         '"listened to rock music within the past month, while less than 35% of 18 to 29-year-olds did. It\'s unfortunate,"'
                                                         '"but younger people listen to far less rock and more pop and hip-hop. What\'s your favorite rock song to listen to?"')
df.add_user_transition(State.ROCKANS, State.NOAGING, '[#ONT(no)]')
df.add_system_transition(State.NOAGING, State.ROCKSONG, '"Hmm, the statistics would disagree, but it\'s interesting that you might believe that. Most young people now are"'
                                                        '"listening to more pop and hip-hop, and less rock is being played on the radio. What\'s your favorite rock song?"')
df.add_user_transition(State.ROCKANS, State.AGINGIDK, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.add_system_transition(State.AGINGIDK, State.ROCKSONG, '"Well, a survey conducted in 2018 reported that almost 60% of respondents over the age of 50 listened to rock"'
                                                         '"music within the past month, while less than 35% of 18 to 29-year-olds did. What\'s your favorite rock song to listen to?"')
# Error
df.set_error_successor(State.ROCKANS, State.ROCK_ERROR9)
df.add_system_transition(State.ROCK_ERROR9, State.ROCKANS2, '"Sorry, I didn\'t catch that. Do you think the rock is now associated with an aging listener demographic?"')
df.add_user_transition(State.ROCKANS2, State.YESAGING, '[#ONT(yes)]')
df.add_user_transition(State.ROCKANS2, State.NOAGING, '[#ONT(no)]')
df.add_user_transition(State.ROCKANS2, State.AGINGIDK, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.set_error_successor(State.ROCKANS2, State.ROCK_ERROR10)
df.add_system_transition(State.ROCK_ERROR10, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')

# Turn 4
df.add_user_transition(State.ROCKSONG, State.SONGARTIST, '[$song=#NER(WORKOFART)]')
df.add_system_transition(State.SONGARTIST, State.SONGARTISTOPIN, '[!"Oh," $song "is by <INSERTARTIST>! I love listening to that song on vinyl. I would like to go to a concert though, wouldn\'t you?"]')
df.add_user_transition(State.ROCKSONG, State.SONGARTIST1, '[{bohemian rhapsody, Bohemian Rhapsody}]')
df.add_system_transition(State.SONGARTIST1, State.SONGARTISTOPIN, '[!"Oh, Bohemian Rhapsody is by Queen! I love listening to that song on vinyl. I would like to go to a concert though, wouldn\'t you?"]')
# Error
df.set_error_successor(State.ROCKSONG, State.ROCK_ERROR11)
df.add_system_transition(State.ROCK_ERROR11, State.ROCKSONG2, '"Sorry, I didn\'t catch that. What\'s your favorite rock song to listen to?"')
df.add_user_transition(State.ROCKSONG2, State.SONGARTIST, '[$song=#NER(WORKOFART)]')
df.add_user_transition(State.ROCKSONG2, State.SONGARTIST1, '[{bohemian rhapsody, Bohemian Rhapsody}]')
df.set_error_successor(State.ROCKSONG2, State.ROCK_ERROR12)
df.add_system_transition(State.ROCK_ERROR12, State.ERR, '"Sorry, I still didn\'t catch that. Let\'s start over."')


# Turn 5
df.add_user_transition(State.SONGARTISTOPIN, State.ROCKCONCERT, "/.*/")
df.add_system_transition(State.ROCKCONCERT, State.ROCKTICKETS, '"When we are able to stop social distancing, the first thing I\'m going to do is buy concert tickets."'
                                                               '"I think that rock music can still live on, if people continue to buy rock concert tickets, but that\'s also"'
                                                               '"much harder to do now, with Ticketmaster having a monopoly over ticket sales. Have you ever heard of Ticketmaster?"')

df.add_user_transition(State.ERR, State.START, '/.*/')

if __name__ == '__main__':
    df.run(debugging=False)

