import json
from enum import Enum, auto
from typing import Dict, Any, List

from emora_stdm import KnowledgeBase, DialogueFlow, Macro, Ngrams
from spotify_query import requester


# TODO: Update the State enum as needed
class State(Enum):
    TMSTART = auto()
    CONCERT = auto()
    YESCONCERT = auto()
    NOCONCERT = auto()
    LIVEARTIST = auto()
    LIVERES = auto()
    KENDRICK = auto()
    ED = auto()
    CONCOP = auto()
    CONCADJ = auto()
    CONCADJS = auto()
    CONCADJSN = auto()
    FREQ = auto()
    NFREQ = auto()


ontology = json.loads(open('ontology.json').read())

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={"ARTIST_QUALITIES": ARTIST_QUALITIES(),
                          "ARTIST_GENRE": ARTIST_GENRE()})

df.add_system_transition(State.TMSTART, State.CONCERT, '"The good thing about pop artists is that they\'re always on tour! Have you been to any concerts\?"' )
df.add_user_transition(State.CONCERT, State.YESCONCERT, '[#ONT(yes)]')
df.add_user_transition(State.CONCERT, State.NOCONCERT, '[#ONT(no)]')

df.add_system_transition(State.YESCONCERT, State.LIVEARTIST, '"That\'s cool! Concerts are really fun. Who have you seen live\?"')
df.add_user_transition(State.LIVEARTIST, State.LIVERES, '[-Kendrick Lamar, -Ed Sheeran, $live_artist=#NER(person)]')
df.add_system_transition(State.LIVERES, State.CONCADJ, '"I\'ve always wanted to see $live_artist live! How was the concert?')
df.add_user_transition(State.CONCADJ, CONCADJS, '[#ONT(positive_response)]')
df.add_user_transition(State.CONCADJ, CONCADJSN, '[#ONT(negative_response)]')
df.add_system_transition(State.CONCADJS, State.CONCOP, '"That\'s great! I\'ve heard $live_artist is really good live! Do you go to concerts a lot?"')
df.add_system_transition(State.CONCADJSN, State.CONCOP, '"That\'s too bad. Some concerts just aren\'t that fun. Do you go to concerts a lot?"')

df.add_user_transition(State.LIVEARTIST, State.KENDRICK, '[$live_artist=Kendrick Lamar')
df.add_system_transition(State.KENDRICK, State.CONCOP, '"I saw him in 2018 and his concert was really fun, but he showed up about two hours late. Do you go to concerts a lot?"')
df.add_user_transition(State.LIVEARTIST, State.ED, '[$live_artist=Ed Sheeran')
df.add_system_transition(State.ED, State.CONCOP, '"I saw him in 2018 and his concert was really sweet. I saw someone propose there! Do you go to concerts a lot?"')


df.add_user_transision(State.CONCOP, State.FREQ, '[#ONT(yes)]')
df.add_user_transition(State.FREQ, State.TM)
df.add_user_transition(State.CONCOP, State.NFREQ, '[#ONT(no)]')




