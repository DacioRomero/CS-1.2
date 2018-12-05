# Code

This is all the source code for my the [Tweet Generator tutorial](http://www.make.sc/oa-tweet-generator).

Some code requires the system to be **UNIX-based** (such as MacOS) as it reads from `/usr/share/dict/words`.

These will have a `*` next to their name

# Tutorial Answers

These are in reverse order to show most recent developments.

## 12. Creating a Corpus

It can be any article, book, blog, etc.

1. Convert your corpus to at text file.

2. Clean it - remove anything that's not part of the narrative.

3. Place it in texts as `corpus.txt`.

## 10. Performance Analysis

**Not Done**.

## 9. Hash Table

### hashtable.py

A `HashTable` class implemented using a `LinkedList`.


## 8. Linked List

### linkedlist.py

A `LinkedList` class implemented using `Node` objects.

## 7. Generating Sentences


### markov.py

Run `python3 markov.py -h` for explanation.

## 6. Application Architecture

Improved `app.py` implementation.

### listogram.py

A `Histogram` implemented using a `list`.

Run `python3 dictogram.py` by itself or with a list of space-separated words.

### dictogram.py

A `Histogram` class implemented using a `dict`

Run `python3 dictogram.py` by itself or with a list of space-separated words.

## 5. Flask Web App

### app.py

This is the web app for the markov chain.

#### Usage

1. Install Flask and python-dotenv (preferably to a virtualenv)

2. Create a `.env` file with

```
FLASK_APP=app.py
FLASK_RUN_PORT=[your port]
FLASK_ENV=development
```

Read more on what you can do in [Flask's documentation](http://flask.pocoo.org/docs/dev/cli/#environment-variables-from-dotenv).

3. Run `flask run`

4. Navigate to `localhost:[your port]` in your browser.

This will generate psuedo-sentence based on the corpus, refresh for different  sentences.

## 4. Stochastic Sampling

### sample.py

This was my initial histogram sampling. It emulates `random.choices` as we weren't allowed to use that built-in method.

`python3 sample.py [words]` where `[words]` is a list of space-separated words.

## 3. Analyze Word Frequency in Text


### histogram.py

A `Histogram` implemented using with a `dict`, `list` of `list`s, or `list` of `tuple`s.


## 2. Random Dictionary Words

Improved anagram.py.

### autocomplete.py*

Generates a list of words that could complete the provided word.

Run `python3 autocomplete.py [word]`.

- `[word]` = a single word.

### dictionary_words.py*

Reads from `/usr/share/dict/words` and generates a list of random words from it.


## 1. Let's Get Started

### anagram.py*

Generates a list anagrams of a provided word.

Run `python3 anagram.py [word]` where `[word]` is one word.

### string_reversals.py

Reverses words or the order of words in sentences.


### rearrange.py

Shuffles the provided list.
