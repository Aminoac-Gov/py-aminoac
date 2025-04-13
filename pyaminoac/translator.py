"""
Translation functionality for PyAminoac.
"""

import jieba
import logging
from pypinyin import pinyin, Style
import re
from typing import List
from zhconv import convert as zh_convert

from .utils import (
    split_sentences,
    convert_punctuation,
    is_chinese_word,
    reverse_word,
    capitalize_first_letter,
    amino
)

def translate_text(text: str) -> str:
    """
    Translate Chinese text to Aminoac format (reversed pinyin according to the specified rules).
    
    Args:
        text: Input Chinese text
        
    Returns:
        Translated text in Aminoac format
    """
    # Convert traditional Chinese to simplified Chinese
    text = zh_convert(text, 'zh-hans')
    
    # Convert Chinese punctuation to English (including removing book title marks)
    text = convert_punctuation(text)
    
    # Split into sentences
    sentences = split_sentences(text)
    
    translated_sentences = []

    jieba.setLogLevel(logging.ERROR)
    
    for sentence in sentences:
        # Check if this is a separator (punctuation with spaces)
        if re.match(r'\s*[.!?;:]+\s*', sentence):
            translated_sentences.append(sentence)
            continue
        
        # Use jieba to cut the sentence into words
        words = list(jieba.cut(sentence, cut_all=False))
        
        # Get pinyin for each word
        pinyin_words = []
        for word in words:
            # If it's a space or punctuation, keep it as is
            if not word.strip() or re.match(r'[,."\'\[\]\(\)\{\}-]+', word):
                pinyin_words.append(word)
                continue
                
            # Get pinyin for the word
            word_pinyin = pinyin(word, Style.NORMAL, strict=False)
            
            # Flatten the list and join with empty string
            word_pinyin_str = ''.join([''.join(p) for p in word_pinyin])
            
            # If it's a Chinese word, reverse it
            if is_chinese_word(word):
                word_pinyin_str = reverse_word(word_pinyin_str)
                
            pinyin_words.append(word_pinyin_str)
        
        # Join the pinyin words to form a sentence
        translated_sentence = ' '.join(pinyin_words)
        # 去掉标点符号前后的空格
        # 去掉,.:;?!}])前面的空格
        translated_sentence = re.sub(r'\s+([,.:;?!}\]\)])', r'\1', translated_sentence)
        # 去掉({[后面的空格
        translated_sentence = re.sub(r'([({[\[])\s+', r'\1', translated_sentence)
                
        # Capitalize the first letter of the sentence
        translated_sentence = capitalize_first_letter(amino(translated_sentence))
        
        translated_sentences.append(translated_sentence)
    
    # print(translated_sentences)
    
    # Join all translated sentences
    translated_text = ''.join(translated_sentences)
    return translated_text