import json
from enum import Enum, auto
from typing import Dict, Any, List

from emora_stdm import KnowledgeBase, DialogueFlow, Macro, Ngrams
from spotify_query import requester

# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    RES = auto()
    RES2 = auto()
    RES_ERROR = auto()
    RES_ERROR2 = auto()
    NO = auto()
    NO_ANS = auto()
    MUSIC_GOOD = auto()
    MUSIC_OPINION = auto()
    AGREE = auto()
    DISAGREE = auto()
    NEUT = auto()
    YES = auto()
    VERB = auto()
    VERBRES = auto()
    TIMERES = auto()
    VERB2 = auto()
    ACT_ERROR = auto()
    ACT_ERROR2 = auto()
    SERVICE = auto()
    STREAM = auto()
    OTHERSTREAM2 = auto()
    STREAM_ERROR = auto()
    STREAM_ERROR2 = auto()
    CDS = auto()
    VINYLS = auto()
    OTHERMED = auto()
    SERV_ERROR = auto()
    SERV_ERROR2 = auto()
    SERVICE2 = auto()
    ADJ = auto()
    POSITIVE = auto()
    NEGATIVE = auto()
    ADJ_ERROR = auto()
    ADJ2 = auto()
    ADJ_ERROR2 = auto()
    ARTIST = auto()
    PANDORA = auto()
    APPLE = auto()
    AMAZON = auto()
    YOUTUBE = auto()
    SPOTIFY = auto()
    OTHERSTREAM = auto()
    DISCOUNT = auto()
    PLAYLIST = auto()
    CONVENIENCE = auto()
    SELECTION = auto()
    SHOWS = auto()
    DOWNLOAD = auto()
    DISCOVERY = auto()
    END = auto()
    TERMINAL = auto()
    ERR = auto()
    ARTIST_ERROR = auto()
    NOUNRES = auto()
    PLACERES = auto()
    GENREQUESTION = auto()
    GENREQUESTION2 = auto()
    ARTISTTOMUSIC = auto()
    ROCK = auto()
    OTHERMUSIC = auto()
    ROCKDYING = auto()
    ROCKDYING2 = auto()
    ROCK_ERROR = auto()
    ROCK_ERROR2 = auto()
    ROCK_ERROR3 = auto()
    ROCK_ERROR4 = auto()
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
    ROCKDONTKNOW2 = auto()

sp_requester = requester()

class ARTIST_GENRE(Macro):

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        if 'fav_artist' in vars:
            fav_artist_name = vars['fav_artist']
            vars['artist_genre'] = sp_requester.get_artist_genres(fav_artist_name)[0]
            # returns the first genre in the artists' genre list
            return vars['artist_genre']

class ARTIST_QUALITIES(Macro):

    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        if 'fav_artist' in vars:
            fav_artist_name = vars['fav_artist']
            query_first_result = requester.search_for_artist(fav_artist_name)[0]
            artist_id = query_first_result['id']
            artist_features = requester.get_artist_avg_features(artist_id)
            # these next two lines are for testing. Remove once macro is up and running
            for key, val in artist_features:
                print(""+key+""+val)

            # TODO: build a way to turn artist feature metrics into qualitative descriptives

# TODO: create the ontology as needed
ontology = json.loads(open('ontology.json').read())

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"ARTIST_QUALITIES": ARTIST_QUALITIES(),
                          "ARTIST_GENRE": ARTIST_GENRE()})

df.add_system_transition(State.START, State.RES, '"Do you listen to music?"')


df.add_user_transition(State.RES, State.YES, '[#ONT(yes)]')
df.add_user_transition(State.RES, State.NO, '[#ONT(no)]')


# Error
df.set_error_successor(State.RES, State.RES_ERROR)
df.add_system_transition(State.RES_ERROR, State.RES2, '"Sorry, I didn\'t catch that. Do you listen to music?"')
df.add_user_transition(State.RES2, State.YES, '[#ONT(yes)]')
df.add_user_transition(State.RES2, State.NO, '[#ONT(no)]')
df.set_error_successor(State.RES2, State.RES_ERROR2)
df.add_system_transition(State.RES_ERROR2, State.VERB, '"Hmm, well I love listening to music because it makes me less stressed. When do you listen to music?"')


#USER DOESNT LISTEN TO MUSIC
df.add_system_transition(State.NO, State.NO_ANS, '"That\'s a shame. Why do you not listen to music?"')

df.add_user_transition(State.NO_ANS, State.YES, '[{-not,-dont}, like, music]')
df.set_error_successor(State.NO_ANS, State.MUSIC_GOOD)

df.add_system_transition(State.MUSIC_GOOD, State.MUSIC_OPINION, "Scientists have actually found many benefits to listening "
                                                        "to music. Research shows music makes you happier, "
                                                        "it enhances workout performance and lowers stress. "
                                                        '"Have you heard about the benefits of music before?"')

df.add_user_transition(State.MUSIC_OPINION, State.AGREE, '[#ONT(yes)]')
df.add_user_transition(State.MUSIC_OPINION, State.DISAGREE, '[#ONT(no)]')
df.set_error_successor(State.MUSIC_OPINION, State.NEUT) # error handling

df.add_system_transition(State.AGREE, State.TERMINAL, '"Great! I hope this convinced you to listen to more music"')
df.add_system_transition(State.DISAGREE, State.TERMINAL, '"That\'s a shame, you should read up on it."')
df.add_system_transition(State.NEUT, State.TERMINAL, '"You should read up on it."')



#USER LISTENS TO MUSIC
df.add_system_transition(State.YES, State.VERB, '"When do you listen to music?"')

df.add_user_transition(State.VERB, State.VERBRES, '[-listen, $activity={#POS(verb), $activity=#POS(VBG)}]')
df.add_user_transition(State.VERB, State.TIMERES, '[$time=#NER(time)]')
df.add_user_transition(State.VERB, State.PLACERES, '[$place={in the}, {in my}]')

# Error
df.set_error_successor(State.VERB, State.ACT_ERROR)
df.add_system_transition(State.ACT_ERROR, State.VERB2, '"I don\'t understand. When do you listen to music?"')
df.add_user_transition(State.VERB2, State.VERBRES, '[-listen, $activity={#POS(verb), $activity=#POS(VBG)}]')
df.add_user_transition(State.VERB2, State.TIMERES, '[$time=#NER(time)]')
df.set_error_successor(State.VERB2, State.ACT_ERROR2)
df.add_system_transition(State.ACT_ERROR2, State.SERVICE, '"That\'s interesting! I prefer to listen to music in my car. What do you use to listen to music?"')



df.add_system_transition(State.VERBRES, State.SERVICE,
                         '[!"During" $activity "is a great time to listen to music! What do you use to listen to music? "]')
df.add_system_transition(State.TIMERES, State.SERVICE,
                         '[!$time "is a great time to listen to music! What do you use to listen to music?"]')

df.add_user_transition(State.SERVICE, State.CDS, '[-vinyl, $medium=#ONT(mediums)]')
df.add_user_transition(State.SERVICE, State.VINYLS, '[$medium=vinyl]')
df.add_user_transition(State.SERVICE, State.OTHERMED, '[$medium=#ONT(othermediums)]')

#Error
df.set_error_successor(State.SERVICE, State.SERV_ERROR)
df.add_system_transition(State.SERV_ERROR, State.SERVICE2, '"Hmm, I\'m not sure what that is. What do you use to listen to music?"')
df.add_user_transition(State.SERVICE2, State.CDS, '[-vinyl, $medium=#ONT(mediums)]')
df.add_user_transition(State.SERVICE2, State.VINYLS, '[$medium=vinyl]')
df.add_user_transition(State.SERVICE2, State.OTHERMED, '[$medium=#ONT(othermediums)]')
df.add_user_transition(State.SERVICE2, State.PANDORA, '[{pandora, pandora radio}]')
df.add_user_transition(State.SERVICE2, State.APPLE, '[{apple, iphone, siri}]')
df.add_user_transition(State.SERVICE2, State.AMAZON, '[{amazon, amazonplus, amazonpremium}]')
df.add_user_transition(State.SERVICE2, State.YOUTUBE, '[{YouTube, youtube}]')
df.add_user_transition(State.SERVICE2, State.SPOTIFY, '[{spotify, spotify music}]')
df.set_error_successor(State.SERVICE2, State.SERV_ERROR2)
df.add_system_transition(State.SERV_ERROR2, State.ADJ, '"Well, I\'ve never heard of that, but it\'s good that you like it. I use Spotify, which is a music streaming service."'
                                                     '"How do you think music streaming, such as Spotify, has impacted the music industry?"')


df.add_user_transition(State.SERVICE, State.PANDORA, '[{pandora, pandora radio}]')
df.add_system_transition(State.PANDORA, State.OTHERSTREAM,
                         '"Pandora is great for discovering new music, and the free version allows you unlimited skips but has ads! Why do you like pandora?"')
df.add_user_transition(State.SERVICE, State.APPLE, '[{apple, iphone, siri}]')
df.add_system_transition(State.APPLE, State.OTHERSTREAM,
                         '"Apple music is well integrated with Siri! Why do you like apple music?"')
df.add_user_transition(State.SERVICE, State.AMAZON, '[{amazon, amazonplus, amazonpremium}]')
df.add_system_transition(State.AMAZON, State.OTHERSTREAM,
                         '"Amazon music is well integrated with alexa! why do you like Amazon music?"')
df.add_user_transition(State.SERVICE, State.YOUTUBE, '[{YouTube, youtube}]')
df.add_system_transition(State.YOUTUBE, State.OTHERSTREAM,
                         '"You can watch thousands of music videos on youtube, all for free! Why do you like youtube?"')
df.add_user_transition(State.SERVICE, State.SPOTIFY, '[{spotify, spotify music}]')
df. add_system_transition(State.SPOTIFY, State.OTHERSTREAM, '"Spotify has really cool insights about your listening habits! Why do you like spotify?"')


discount = r"[#ONT(discount)]"
df.add_user_transition(State.OTHERSTREAM, State.DISCOUNT, discount)
df.add_system_transition(State.DISCOUNT, State.ADJ, '"You\'re right. It\'s pretty affordable and there might be discounts if you\'re a student. How do you think music streaming has impacted the music industry?"')

playlists = r"[#ONT(playlists)]"
df.add_user_transition(State.OTHERSTREAM, State.PLAYLIST, playlists)
df.add_system_transition(State.PLAYLIST, State.ADJ, '"It\'s cool to create and share playlists! How do you think music streaming has impacted the music industry?"')

convenient = r"[#ONT(convenience)]"
df.add_user_transition(State.OTHERSTREAM, State.CONVENIENCE, convenient)
df.add_system_transition(State.CONVENIENCE, State.ADJ, '"You\'re right. its a convenient service. How do you think music streaming has impacted the music industry?"')

selection = r"[#ONT(selection)]"
df.add_user_transition(State.OTHERSTREAM, State.SELECTION, selection)
df.add_system_transition(State.SELECTION, State.ADJ, '"There are thousands of songs on there! How do you think music streaming has impacted the music industry?"')

shows = r"[#ONT(shows)]"
df.add_user_transition(State.OTHERSTREAM, State.SHOWS, shows)
df.add_system_transition(State.SHOWS, State.ADJ, '"I love when streaming services come with perks like that! How do you think music streaming has impacted the music industry?"')

downloading = r"[#ONT(offline)]"
df.add_user_transition(State.OTHERSTREAM, State.DOWNLOAD, downloading)
df.add_system_transition(State.DOWNLOAD, State.ADJ, '"Downloading music is especially convenient for long plane rides. How do you think music streaming has impacted the music industry?"')

discovery = r"[#ONT(discovery)]"
df.add_user_transition(State.OTHERSTREAM, State.DISCOVERY, discovery)
df.add_system_transition(State.DISCOVERY, State.ADJ, '"I like finding new music too! How do you think music streaming has impacted the music industry?"')

#Error
df.set_error_successor(State.OTHERSTREAM, State.STREAM_ERROR)
df.add_system_transition(State.STREAM_ERROR, State.OTHERSTREAM2, '"Sorry, I didn\'t catch that. What do you like about your streaming service?"')
df.add_user_transition(State.OTHERSTREAM2, State.DISCOUNT, discount)
df.add_user_transition(State.OTHERSTREAM2, State.PLAYLIST, playlists)
df.add_user_transition(State.OTHERSTREAM2, State.CONVENIENCE, convenient)
df.add_user_transition(State.OTHERSTREAM2, State.SELECTION, selection)
df.add_user_transition(State.OTHERSTREAM2, State.SHOWS, shows)
df.add_user_transition(State.OTHERSTREAM2, State.DOWNLOAD, downloading)
df.add_user_transition(State.OTHERSTREAM2, State.DISCOVERY, discovery)
df.set_error_successor(State.OTHERSTREAM2, State.STREAM_ERROR2)
df.add_system_transition(State.STREAM_ERROR2, State.ADJ, '"Well, I like using Spotify because I can get a family discount plan. How do you think that music streaming services have impacted the music industry?"')


df.add_system_transition(State.CDS, State.ADJ,
                         '[!$medium "s are dead. How do you think music streaming services have impacted the music industry?"]')

df.add_system_transition(State.VINYLS, State.ADJ,
                         '"Vinyls are great. I exclusively listen to vinyls because I think the music quality is much better. How do you think music streaming services have impacted the music industry?"')

df.add_system_transition(State.OTHERMED, State.ADJ, '"oh you use" $medium "? I prefer the sound quality of vinyls. How do you think music streaming services have impacted the music industry?"')


df.add_user_transition(State.ADJ, State.POSITIVE, '[#ONT(positive_response)]')
df.add_user_transition(State.ADJ, State.NEGATIVE, '[#ONT(negative_response)]')

# Error
df.set_error_successor(State.ADJ, State.ADJ_ERROR)
df.add_system_transition(State.ADJ_ERROR, State.ADJ2, '"I don\'t understand. What?"')
df.add_user_transition(State.ADJ2, State.POSITIVE, '[#ONT(positive_response)]')
df.add_user_transition(State.ADJ2, State.NEGATIVE, '[#ONT(negative_response)]')
df.set_error_successor(State.ADJ2, State.ADJ_ERROR2)
df.add_system_transition(State.ADJ_ERROR2, State.ARTIST, '"I think that music streaming is good for the public, but artists only get a small percent of the profit. Who\'s your favorite artist? Maybe their music is on a streaming service."')


df.add_system_transition(State.POSITIVE, State.ARTIST,
                         '"Yes sometimes it can be good, but Spotify has caused artists to create albums with more songs but theyre shorter songs, since artists are paid by song. Who\'s your favorite artist?"')
df.add_system_transition(State.NEGATIVE, State.ARTIST,
                         '"I agree, streaming services like Spotify only give artists a small percent of the profit. Who\'s your favorite artist?"')
df.add_user_transition(State.ARTIST, State.END, '[$fav_artist=#NER(person)]')


df.add_system_transition(State.END, State.ARTISTTOMUSIC,
                         '[!$fav_artist "is a great" #ARTIST_GENRE "artist!"]')


df.set_error_successor(State.ARTIST, State.ARTIST_ERROR)
#df.add_system_transition(State.ARTIST_ERROR, State.ARTISTTOMUSIC, '"Hmm, I\'ve never heard of them. Guess I\'ll go listen to their music now!"')
#TODO: connect artist to genre, then go into genres

# ROCK MUSIC
df.add_system_transition(State.ARTIST_ERROR, State.GENREQUESTION, '"What\'s your favorite music genre?"')
df.add_user_transition(State.GENREQUESTION, State.ROCK, '[{rock, Rock}]')
df.set_error_successor(State.GENREQUESTION, State.ROCK_ERROR)
# Error
df.add_system_transition(State.ROCK_ERROR, State.GENREQUESTION2, '"Sorry, I didn\'t catch that. What\'s your favorite music genre?"')
df.add_user_transition(State.GENREQUESTION2, State.ROCK, '[{rock, Rock}]')
df.set_error_successor(State.GENREQUESTION2, State.ROCK_ERROR2)
df.add_system_transition(State.ROCK_ERROR2, State.ERR, '"Sorry, I still didn\'t catch that. Bye!"')

# Turn 1
df.add_system_transition(State.ROCK, State.ROCKDYING, '"So you like rock music?! I don\'t know about that."'
                                                      '"I heard the genre is dying out; wouldn\'t you agree?"')
df.add_user_transition(State.ROCKDYING, State.ROCKAGREE, '[#ONT(yes)]')
df.add_user_transition(State.ROCKDYING, State.ROCKDISAGREE, '[#ONT(no)]')
# Error
#df.set_error_successor(State.ROCKDYING, State.ROCK_ERROR3)
#df.add_system_transition(State.ROCK_ERROR3, State.ROCKDYING2, '"Sorry, I didn\'t catch that. Don\'t you agree?"')
#df.add_user_transition(State.ROCKDYING2, State.ROCKAGREE, '[#ONT(yes)]')
#df.add_user_transition(State.ROCKDYING2, State.ROCKDISAGREE, '[#ONT(no)]')
df.set_error_successor(State.ROCKDYING, State.ROCK_ERROR4)
df.add_system_transition(State.ROCK_ERROR4, State.POPULARITY, '"Well, it\'s true! In 2017, hip-hop surpassed rock as the favored genre among music fans. What do you think led to this decline in popularity?"')
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
df.add_system_transition(State.ROCK_ERROR5, State.POPULARITY2, '"Sorry, I don\'t understand. Why do you think rock is losing its popularity?"')
df.add_user_transition(State.POPULARITY2, State.ROCKIMAGE, '[{image, brand}]')
df.add_user_transition(State.POPULARITY2, State.ROCKREPRESENT, '[#ONT(rockrepresentation)]')
df.add_user_transition(State.POPULARITY2, State.ROCKCOSTLY, '[#ONT(discount)]')
df.add_user_transition(State.POPULARITY2, State.DIFFSOUND, '[{sound, tone, beat, beats}]')
df.add_user_transition(State.POPULARITY2, State.ROCKDONTKNOW, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.set_error_successor(State.POPULARITY2, State.ROCK_ERROR6)
df.add_system_transition(State.ROCK_ERROR6, State.ROCKANS, '"I think it\'s due to a lot of reasons, mostly because rock music doesn\'t sound like it did before. Some say that rock listeners have aged with their songs. Do you agree?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKARTISTS, '[{artists, people, musicians, band, bands}]')
df.add_system_transition(State.ROCKARTISTS, State.ROCKANS, '"Yes, some artists like Metallica are still very true to the genre,"'
                                                           '"but other supposedly rock bands like Coldplay or Fall Out Boy are leaning more towards pop."'
                                                            '"Do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKSTORY, '[{story, meaning, lyrics}]')
df.add_system_transition(State.ROCKSTORY, State.ROCKANS, '"That\'s true, a lot of unwavering rock fans love the genre because every song has a story they can relate to."'
                                                             '"But do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKINSTRUMENTS, '[{sound, instruments, guitar, bass drums, beat, beats, tone}]')
df.add_system_transition(State.ROCKINSTRUMENTS, State.ROCKANS, '"Yes, rock music is known for its instruments, but some say that there\'s only"'
                                                               '"so much you can do with an electric guitar or bass until it gets repetitive."'
                                                               '"Do you think that rock music is now associated with an aging demographic of listeners?"')
df.add_user_transition(State.POPROCKBANDS, State.ROCKDONTKNOW2, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.add_system_transition(State.ROCKDONTKNOW2, State.ROCKANS, '"Well some people still love the way rock artists tell stories through their music and its distinctive sound."'
                         '"Do you think that rock music is now associated with an aging demographic of listeners?"')
# Error
df.set_error_successor(State.POPROCKBANDS, State.ROCK_ERROR7)
df.add_system_transition(State.ROCK_ERROR7, State.POPROCKBANDS2, '"I don\'t think I understand. Why do you think rock music is still so popular?"')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKARTISTS, '[{artists, people, musicians, band, bands}]')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKSTORY, '[{story, meaning}]')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKINSTRUMENTS, '[{sound, instruments, guitar, drums, beat, beats, tone}]')
df.add_user_transition(State.POPROCKBANDS2, State.ROCKDONTKNOW2, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.set_error_successor(State.POPROCKBANDS2, State.ROCK_ERROR8)
df.add_system_transition(State.ROCK_ERROR8, State.ROCKANS, '"Well some people still love the way rock artists tell stories through their music and its distinctive sound."'
                         '"Do you think that rock music is now associated with an aging demographic of listeners?"')

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
df.add_system_transition(State.ROCK_ERROR9, State.ROCKANS2, '"Sorry, let me reword my question. Do you think the rock is now associated with an aging listener demographic?"')
df.add_user_transition(State.ROCKANS2, State.YESAGING, '[#ONT(yes)]')
df.add_user_transition(State.ROCKANS2, State.NOAGING, '[#ONT(no)]')
df.add_user_transition(State.ROCKANS2, State.AGINGIDK, '[{''dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain,[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],'
            '[!{cant,cannot,dont} {think,remember,recall}]'
            '}]')
df.set_error_successor(State.ROCKANS2, State.ROCK_ERROR10)
df.add_system_transition(State.ROCK_ERROR10, State.ROCKSONG, '"The most popular rock songs are from the 70s. What\'s your favorite rock song?"')

# TODO: Create macro that associates song with artist
df.add_user_transition(State.ROCKSONG, State.SONGARTIST, '[$song=#NER(WORKOFART)]')
df.add_system_transition(State.SONGARTIST, State.SONGARTISTOPIN, '[!"Oh," $song "is by <INSERTARTIST>! I love listening to that song on vinyl. I would like to go to a concert though, wouldn\'t you?"]')
df.add_user_transition(State.ROCKSONG, State.SONGARTIST1, '[{bohemian rhapsody, Bohemian Rhapsody}]')
df.add_system_transition(State.SONGARTIST1, State.SONGARTISTOPIN, '[!"Oh, Bohemian Rhapsody is by Queen! I love listening to that song on vinyl. I would like to go to a concert though, wouldn\'t you?"]')
# Error
df.set_error_successor(State.ROCKSONG, State.ROCK_ERROR11)
df.add_system_transition(State.ROCK_ERROR11, State.SONGARTISTOPIN, '"Hmm, I\'ve never heard of that song, but I\'ll definitely listen to it now. I\'d prefer to listen to music live though, wouldn\'t you?"')

# Turn
df.add_user_transition(State.SONGARTISTOPIN, State.ROCKCONCERT, "/.*/")
df.add_system_transition(State.ROCKCONCERT, State.ROCKTICKETS, '"When we are able to stop social distancing, the first thing I\'m going to do is buy concert tickets."'
                                                               '"I think that rock music can still live on, if people continue to buy rock concert tickets, but that\'s also"'
                                                               '"much harder to do now, with Ticketmaster having a monopoly over ticket sales. Have you ever heard of Ticketmaster?"')

df.add_user_transition(State.ERR, State.TERMINAL, '/.*/')

if __name__ == '__main__':
    df.run(debugging=False)
