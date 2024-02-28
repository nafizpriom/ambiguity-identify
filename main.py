import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def disambiguate_word(word, sentence):
    """
    Perform word sense disambiguation for a given word in the context of a sentence.
    """
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Tag parts of speech
    tagged_tokens = nltk.pos_tag(tokens)

    # Find the part of speech of the target word
    target_pos = None
    for token, pos in tagged_tokens:
        if token == word:
            target_pos = pos
            break

    print("Part of speech of the target word:", target_pos)

    # If the part of speech is found, disambiguate the word
    if target_pos:
        synsets = wordnet.synsets(word)
        for synset in synsets:
            # Check if any synset's POS matches the target POS
            if synset.pos() == get_wordnet_pos(target_pos):
                return synset.definition()

    # If no disambiguation is found, return the original word
    return 'There is no ambiguity.'

def get_wordnet_pos(treebank_tag):
    """
    Convert a Penn Treebank POS tag to a WordNet POS tag.
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        # Default to noun if no match is found
        return wordnet.NOUN

def main():
    word = input("Enter a word: ")
    sentence = input("Enter a sentence: ")
    disambiguated_word = disambiguate_word(word, sentence)
    print("Disambiguated word:", disambiguated_word)

if __name__ == "__main__":
    main()
