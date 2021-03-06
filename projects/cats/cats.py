"""Typing test implementation"""

from cgitb import small
from os import stat_result
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime
from operator import add
###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    count = 0
    index = 0
    # print("DEBUG:k:",k)
    while index < len(paragraphs):
        if select(paragraphs[index]):
            count += 1
        if count == k+1:
            # found enough
            return paragraphs[index]
        index += 1
    return ''
    # while 1:
    #     print("DEBUG:count:",count)
    #     print("DEBUG:index:",index)
    #     # not enough
    #     if index==len(paragraphs) and count<k:
    #         return ''
    #     # found
    #     if count-1==k:
    #         print("DEBUG:found",count,index)
    #         return paragraphs[index]
    #     # found one
    #     if select(paragraphs[index]):
    #         count+=1
    #     index+=1
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2

    def selection(paragraph):
        # process paragraph into no-punctuation lower case words list
        paragraph = remove_punctuation(paragraph)
        # print("DEBUG:paragraph without punctuation:",paragraph)
        paragraph = lower(paragraph)
        word_list = split(paragraph)
        topic_index = 0
        wordlist_index = 0
        # print("DEBUG:",word_list)
        # try find topic
        while topic_index < len(topic):
            # print("DEBUG:",topic_index)
            while wordlist_index < len(word_list):
                # print("DEBUG:comparision between:",topic[topic_index],word_list[wordlist_index])
                if topic[topic_index] == word_list[wordlist_index]:
                    return True
                wordlist_index += 1
            wordlist_index = 0    # remember to reset the wordlist_index to 0
            topic_index += 1
        return False
    # return selection
    return selection
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    # print("DEBUG:begin")
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    # edge cases, when typed or reference is empty
    # print("DEBUG:",len(typed))
    if len(typed_words) == 0 and len(reference_words) == 0:
        return 100.0
    if len(typed_words) == 0 and len(reference_words) != 0:
        return 0.0
    if len(typed_words) != 0 and len(reference_words) == 0:
        return 0.0

    total = len(typed_words)
    index = 0
    count = 0
    while index < len(typed_words):
        # if reference is shorter than typed, stop counting
        if index == len(reference_words):
            # print("DEBUG:break")
            break
        if typed_words[index] == reference_words[index]:
            # print("DEBUG:count add one")
            count += 1
        index += 1
    return count*100/total  # don't forget *100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    # edge case
    if len(typed) == 0:
        return 0.0
    return (len(typed)/5)/(elapsed/60)
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    index = 0
    insteadword = ''
    insteadword_diff = diff_function(
        typed_word, word_list[0], limit)+1  # initial diff is important
    while index < len(word_list):
        if typed_word == word_list[index]:
            return typed_word
        tempdiff = diff_function(typed_word, word_list[index], limit)
        if tempdiff < insteadword_diff:
            insteadword = word_list[index]
            insteadword_diff = tempdiff
        index += 1
    if insteadword_diff > limit:
        return typed_word
    else:
        return insteadword
    # END PROBLEM 5


def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    # return a short version of str, get rid of the first letter
    # def shorten(str):
    #     letterlist=list(str)    # turn word into list of letters
    #     index=1
    #     while index<len(str):
    #         # print("DEBUG:",index)
    #         letterlist[index-1]=letterlist[index]
    #         index+=1
    #     return ''.join(letterlist)

    # already abondon, just use str[1:]
    # return first letter and rest
    # def first_and_rest(str):
    #     strlist=list(str)
    #     firstletter=strlist[0]  # get the first letter
    #     # get the rest part
    #     reststr=''
    #     def newstr(index,reststr,str):
    #         if len(reststr)==len(str)-1:
    #             return reststr
    #         reststr+=str[index]
    #         return newstr(index+1,reststr,str)
    #     reststr=newstr(1,reststr,str)
    #     return firstletter,reststr

    # if len(start)==0 or len(goal)==0:
    if min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))    # length difference
    # if not equal
    if start[0] != goal[0]:
        limit -= 1
        if limit < 0:
            return 1
        return sphinx_swaps(start[1:], goal[1:], limit)+1
    return sphinx_swaps(start[1:], goal[1:], limit)
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # assert False, 'Remove this line'
    # if start=="sith":
    #     return 4

    # if start=="jeans":
    #     return 3

    if start == goal:
        return 0

    if limit == 0:
        return 1

    # if goal.count(start)==1:
    #     return len(goal)-len(start)

    # if start in goal:
    #     return len(goal)-len(start)

    # if goal in start:
    #     return len(start)-len(goal)

    # add tail
    if min(len(start), len(goal)) == 0:
        return max(len(start), len(goal))

    if len(start) == 1 and len(goal) == 1:
        return 1

    if start[0] == goal[0]:
        return minimum_mewtations(start[1:], goal[1:], limit)
    # elif len(start)>1 and len(goal)>1 and start[1]==goal[1]: # substitution
    #     print("DEBUG:sub")
    #     return minimum_mewtations(start[1:],goal[1:],limit-1)+1
    # elif len(start)>1 and start[1]==goal[0]: # remove
    #     print("DEBUG:remove")
    #     return minimum_mewtations(start[1:],goal,limit-1)+1
    # elif len(goal)>1 and start[0]==goal[1]: # add
    #     print("DEBUG:add")
    #     return minimum_mewtations(start,goal[1:],limit-1)+1
    # else:
    #     #35 59
    #     print("DEBUG:else")
    #     return minimum_mewtations(start[1:],goal[1:],limit-1)+1

    # print("DEBUG:no result")
    # return 0

    # for _ in range(3):
    # [x+1 for x in list0 if x % 5 == 0]
    # def divisor(n):
    #   return [1]+[x for x in range(2,n) if n % x == 0]
    add = minimum_mewtations(start, goal[1:], limit-1)
    remove = minimum_mewtations(start[1:], goal, limit-1)
    substitute = minimum_mewtations(start[1:], goal[1:], limit-1)
    return min(add, remove, substitute)+1


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    # count til the first wrong word
    index = 0
    count = 0
    # don't forget to check index first
    while index < len(sofar) and sofar[index] == prompt[index]:
        count += 1
        index += 1
    # compute ratio
    progress = count/len(prompt)
    # use upload function
    upload({'id': user_id, 'progress': progress})
    # return ratio
    return progress
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    # compute time
    for timesperplayer in times_per_player:
        index = 0
        while index+1 < len(timesperplayer):
            timesperplayer[index] = timesperplayer[index+1] - \
                timesperplayer[index]
            index += 1
        # remove last item
        # don't know why this method doesn't work
        # timesperplayer=timesperplayer[:(len(timesperplayer)-1)]
        print("DEBUG:", type(timesperplayer))
        timesperplayer.pop()

    # return a dictionary
    return match(words, times_per_player)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(
        len(match["times"]))  # contains an *index* for each player
    # contains an *index* for each word
    word_indices = range(len(match["words"]))
    # BEGIN PROBLEM 10
    # make an 2d list
    # outputlist = []
    # for x in player_indices:
    #     outputlist.append([])
    # # for every word in word list
    # for wordindex in word_indices:
    #     # initialize index need add word on
    #     newindex = match["times"][0][wordindex]
    #     for playerindex in player_indices:
    #         if match["times"][playerindex][wordindex] < newindex:
    #             newindex = playerindex
    #     outputlist[newindex].append(word_at(match, wordindex))
    # return outputlist

    # make a list contains fastest player'index for every word in order
    fastestplayerlist=[]
    for wi in word_indices:
        # let the smallest be the first player's time 
        smallest_player=0
        print("DEBUG:initial smallest_player",smallest_player)
        for pi in player_indices:
            print("DEBUG:pi",pi)
            # smallest_player can't be zero
            if match["times"][pi][wi] < match["times"][smallest_player][wi]:
                smallest_player=pi
                print("DEBUG:change smallest_player to",smallest_player)
        fastestplayerlist.append(smallest_player)
    
    print("DEBUG:fastestplayerlist",fastestplayerlist)

    outputlist=[]
    for p in player_indices:
        aplist=[]
        for index,t in enumerate(fastestplayerlist):
            if p==t:
                aplist.append(match["words"][index])
        print("DEBUG:aplist",aplist)
        outputlist.append(aplist)

    return outputlist
    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
               for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return {"words": words, "times": times}


def word_at(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(
        match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(
        match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
