import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

URL_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


def split_to_sentences(phrase: str) -> "List[str]":
    sentences = []
    matches = re.split(r"([.?!]+)", phrase)
    matches_enum = enumerate(matches)
    for _, match in matches_enum:
        sentence = re.sub(r"['\"]", "", match)
        sentence = sentence.strip().capitalize()
        try:
            _, punctuation = next(matches_enum)
            sentence += punctuation
        except StopIteration:
            pass
        if sentence:
            sentences.append(sentence)
    return sentences


def capitalize(phrase: str) -> str:
    return " ".join(split_to_sentences(phrase))


def split_list_to_sentences(phrases: "List[str]") -> "List[List[str]]":
    start_idx = 0
    sentences = []
    for idx, word in enumerate(phrases):
        if word[:1] in ".?!" or idx == len(phrases) - 1:
            sentences.append(phrases[start_idx:idx + 1])
            start_idx = idx + 1
    return sentences


def strip_phrase(phrase: str) -> str:
    # Strip URLs, mentions and superfluous whitespace
    phrase = re.sub(URL_REGEX, "", phrase.lower())
    phrase = re.sub(r"@\w+", "", phrase)
    phrase = re.sub(r"\s{2,}", " ", phrase)
    return phrase.strip()
