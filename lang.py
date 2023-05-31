# Language model
import re

word_sets = {
    'verb': {'go', 'walk', 'climb', 'put', 'take'},
    'prep': {'north', 'south', 'east', 'west', 'on', 'off', 'up', 'down', 'upstairs', 'downstairs'},
    'noun': {'ladder', 'stairs', 'hill', 'hat'}
}

all_words = {w: k for k, ws in word_sets.items() for w in ws}

word_patterns = {k: f"{'|'.join(v)}" for k, v in word_sets.items()}

sentence_patterns = {
    'imp-v': 'verb',
    'imp-vp': 'verb+prep',
    'imp-vn': 'verb+noun',
    'imp-vpn-vnp': 'verb+(prep+noun)|(noun+prep)',
    'imp-vnpn': 'verb+noun+prep+noun'
}


def parse_sentence(text):
    words = text.split()
    words_lc = [w[0].lower() + w[1:] for w in words]
    tokens = [all_words.get(w, None) for w in words_lc]
    unmatched_words = [w for w, t in zip(words, tokens) if t is None]
    return words_lc, tokens, unmatched_words