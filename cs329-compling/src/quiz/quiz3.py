# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import ssl
from typing import Set, Optional, List

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk
from nltk.corpus.reader import Synset

nltk.download('wordnet')

from nltk.corpus import wordnet as wn


def antonyms(word: str, pos: Optional[str] = None) -> Set[str]:
    res = []
    for s in wn.synsets(word, pos):
        for l in s.lemmas():
            if l.antonyms():
                res.append(l.antonyms()[0].name())

    return set(res)


def lch_paths(word_0: str, word_1: str) -> List[List[Synset]]:
    res = []

    s_0 = wn.synsets(word_0)
    s_1 = wn.synsets(word_1)

    for sense_0 in s_0:
        for sense_1 in s_1:
            lch = sense_0.lowest_common_hypernyms(sense_1)

            for hypernym in lch:
                res.extend(hypernym.hypernym_paths())

    return res


if __name__ == '__main__':
    print(antonyms('buy', pos='v'))
    for path in lch_paths('dog', 'cat'):
        print(path)
