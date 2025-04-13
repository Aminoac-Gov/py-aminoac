"""
Utility functions for PyAminoac.
"""

import re
from typing import List, Tuple

# Map of Chinese punctuation to English punctuation
PUNCTUATION_MAP = {
    '，': ',',
    '。': '.',
    '！': '!',
    '？': '?',
    '；': ';',
    '：': ':',
    '"': '"',
    '"': '"',
    ''': "'",
    ''': "'",
    '（': '(',
    '）': ')',
    '【': '[',
    '】': ']',
    # Remove book title marks completely instead of converting
    '《': '',
    '》': '',
    '、': ' ',
    '—': '-',
    '～': '~',
    '·': '.'
}

def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences.
    
    Args:
        text: Input text
        
    Returns:
        List of sentences
    """
    sentences = text.replace('\r\n','\n').split('\n')
    return sentences

def convert_punctuation(text: str) -> str:
    """
    Convert Chinese punctuation to English punctuation.
    
    Args:
        text: Input text with Chinese punctuation
        
    Returns:
        Text with English punctuation
    """
    for cn_punc, en_punc in PUNCTUATION_MAP.items():
        text = text.replace(cn_punc, en_punc)
    return text

def is_chinese_word(word: str) -> bool:
    """
    Check if a word contains Chinese characters.
    
    Args:
        word: Input word
        
    Returns:
        True if the word contains Chinese characters
    """
    # Check if the word contains any Chinese character
    for char in word:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

def is_punctuation(char: str) -> bool:
    """
    Check if a character is punctuation.
    
    Args:
        char: Input character
        
    Returns:
        True if the character is punctuation
    """
    # Consider both English and Chinese punctuation
    return (
        char in PUNCTUATION_MAP.keys() or 
        char in PUNCTUATION_MAP.values() or 
        re.match(r'[,.!?;:"\'\[\]\(\)\{\}-]', char)
    )

def is_paragraph_splitting_punctuation(char: str) -> bool:
    """
    Check if a character is paragraph-splitting punctuation.
    
    Args:
        char: Input character
        
    Returns:
        True if the character is paragraph-splitting punctuation
    """
    # These punctuation marks typically end a paragraph/sentence
    return char in ['.', '!', '?', ';', ':'] or char in ['。', '！', '？', '；', '：']

def reverse_word(word: str) -> str:
    """
    Reverse the characters of a word.
    
    Args:
        word: Input word
        
    Returns:
        Reversed word
    """
    return word[::-1]

def capitalize_first_letter(text: str) -> str:
    """
    Capitalize the first letter of a text.
    
    Args:
        text: Input text
        
    Returns:
        Text with first letter capitalized
    """
    if not text:
        return text
        
    result = list(text)
    for i in range(len(result) - 2):
        if result[i] in ['.', '!', '?'] and result[i+1] == ' ' and result[i+2].isalpha():
            result[i+2] = result[i+2].upper()
    
    if result and result[0].isalpha():
        result[0] = result[0].upper()
        
    return ''.join(result)


def amino(text: str) -> str:
    english_punctuation = ['.', '!', '?', ';', ':', ',']
    
    sentences = []
    current_sentence = ""
    for char in text:
        if char in english_punctuation:
            if current_sentence:
                current_sentence += char
                sentences.append(current_sentence)
                current_sentence = ""
        else:
            current_sentence += char
    if current_sentence:
        sentences.append(current_sentence)
    


    # print(sentences)

    res = []

    for sentence in sentences:
        if sentence[-1] in english_punctuation:
            sentence = sentence.strip()
            s = " ".join([word.strip() for word in sentence[:-1].split(' ')[::-1] if word])
            s += sentence[-1]
        else: 
            sentence = sentence.strip()
            s = " ".join([word.strip() for word in sentence.split(' ')[::-1] if word])
        # print(s)
        res.append(s)

    # print(res)

    return " ".join(res)