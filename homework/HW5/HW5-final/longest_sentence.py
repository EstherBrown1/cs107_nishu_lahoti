import sys
sys.setrecursionlimit(2000) 
from linked_list import LinkedList, Nil

def get_list_of_sentences(chapter1 = 'swansway-chapter1.txt'):
    def to_sentences(p):
        for delimiter in '.?!': p = p.replace(delimiter, '|')
        return [s.strip('\"') for s in p.split ('|')]
    with open(chapter1, 'r', encoding = 'UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)

    return list_of_sentences

def longest_sentence():
    
    list_of_sentences = get_list_of_sentences()

    # Defined word count function to split and return length of each sentence.
    def word_count(sentence):
        sentence_length = sentence.split()
        return len(sentence_length)
    
    # Created variable which captures the return of the word count function applied to each
    # sentence in the list_of_sentences.
    split_sentences = list_of_sentences.for_each(word_count)

    # Defined a function to find the longest sentence in the list.
    def longest(a, b): # our "combine" function
        return a if a > b else b

    # Created a variable to capture the longest sentence in split_sentences 
    total_words = split_sentences.reduce_right(longest)
    return total_words