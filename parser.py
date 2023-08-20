import nltk
from nltk.tokenize import word_tokenize


grammar_rules = """
VP -> V NP | V PP | V NP PP
NP -> N | Nom | Det N | Det Nom | NP PP
Nom -> J N | J Nom
PP -> P NP
Det -> 'the' | 'a' | 'an'
"""

# A set of words will be added to grammar_rules
# For example:
# N -> 'bed' | 'door' | 'key' | 'handle' | 'box' | 'window'
# V -> 'sit' | 'open' | 'close' | 'unlock' | 'go'
# P -> 'on' | 'in' | 'with' | 'to'
# J -> 'small' | 'big' | 'wooden' | 'heavy' | 'open' | 'closed' | 'round'
#
# This is achieved by passing a dictionary:
# language = {
#     'N': ['bed', 'door', 'key', 'handle', 'box', 'window'],
#     'V': ['sit', 'open', 'close', 'unlock', 'go'],
#     'P': ['on', 'in', 'with', 'to'],
#     'J': ['small', 'big', 'wooden', 'heavy', 'open', 'closed', 'round']
# }


class Parser():

    def __init__(self, language, grammar_rules=grammar_rules):
        self.language = language
        self.grammar_rules = grammar_rules
        self.grammar = self.build_grammar(language)
        self.parser = nltk.ChartParser(self.grammar)

    def build_grammar(self, language):
        grammar_string = self.grammar_rules.format()
        lines = []
        for key, words in language.items():
            word_str = ' | '.join(["'{:s}'".format(n) for n in words])
            lines.append(
                "{key:s} -> {word_str:s}".format(key=key, word_str=word_str)
            )
        grammar_string = grammar_string + '\n'.join(lines)
        return nltk.CFG.fromstring(grammar_string)

    def parse_sentence(self, sentence):
        words = word_tokenize(sentence)
        return self.parser.parse(words)
