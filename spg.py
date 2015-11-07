#Every great project starts with... ENTERPRISE QUALITY.
#
# CODE OF CONDUCT THE SJWS HAVE INVADED
#  * be nice
#  * be accepting
#  * be civil
#  * install gentoo
#
#lets make a shitpost generator 
#ok 
#great idea
#this quality

#limiting this shit to prefixes is terrible we need shitposts generated so real that we could make an OP with them
#how could we do that?
#something along the lines of 'only niggers will use "thing" why are you still using "thing" /tech/?'
#we could remake the prefixes to something where you do like: "only [noun] will use [thing] like that
#that could work
#ill make a list of formats
#more grammar 
#how i end a function in python?
#you dont, you just let it be
#that upsets me
#yea python is a bit original with its syntax and it can be hard to get used to but its a really nice language
#i just use ruby and c
# its all fuckin in the tabs man let the tabs do all the work
# drop a tab drop a brace ezpz lemonsqueezy
#it lets you do things a lot of different ways

##############################################################
#         INDUSTRIAL GRADE SHITPOST GENERATOR                #
##############################################################

import random, re

prefixes = [
    'i hate', 'I hate', 'I fucking hate',
    'Hey guys', 'hey guys', 'hey guise',
    'fucking', 'Fucking', 'FUCKING',
    'the best meme is',
    'kill all',
    'the worst meme is',
    'the real botnet is',
    '>yfw',
    '>yrw',
    '>tfw',
    'smh tbh',
    'DAE le',
    '>implying',
    'Hey faggots,',
    'How do you',
    'It\'s like I\'m really',
    'Do you suck',
    'Slide thread,',
    'That',
    'now that the dust has settled, how do we feel about',
    'repost if you'
]

formats = [
    '[prefix] [adjective] [noun]',
    'fucking [noun] [noun] [noun] [noun]',
    'Nice try, [noun]',
    'Fucking [noun]fags',
    #'\n\n>2015 \n >still [adjective] [noun]\n >ISHYGDDT\n\n',
    'anyone have that [noun] webm?',
    '[noun] thread'
]


# if the prefix is singular then noun should be plural and vice versa
# could use a dictionary with word type and singularity
#we could just make 2 different prefixes tables, one which needs singular ones and one which needs plural, and with formatting we can just add s at the end idk
#that's probably easier
nouns = [
    'niggers','NIGGERS',
    'kikes','KIKES',
    'spics','SPICS',
    'maymays',
    'kek','keks',
    'penis','PENIS',
    'shitposts',
    'crash this plane',
    'troll','TROLL',
    'big guys',
    'CIA','NSA','FBI',
    '4chan',
    'cucks','CUCKS',
    'benis','BENIS',
    'shills','SHILLS',
    '/tech/',
    'systemd','SYSTEMD',
    'google chrome',
    'ubuntu',
    'Windows 7',
    'Windows XP',
    'Windows 10',
    'BSD',
    '/g/',
    'SJWs','feminist',
    'Gentoo',
    'the jews',
    'plebbit',
    '9gag',
    'apple', 
    'normie','Normies','NORMIES'
    'm80s',
    'anime',
    'os-tan',
    'CISC',
    'TPP',
    'CISA',
    'Shlomo',
    'RISC',
    'Arch',
    'cancer','CANCER','AIDS',
    'fam',
    'hacker',
    'hack',
    'anonymous',
    'mint',
    '[number] memers',
    'the [number]0000000 that died in the holocaust',
    'loli',
    'VN',
    'Lisp',
    'SICP'
] 

adjectives = [
    'shitposting',
    'fucking',
    'gay',
    'best',
    'with no survivors',
    'memeing',
    'ebin',
    'detected',
    'pleb detected',
    'memed',
    'epic',
    'thread',
    'feel',
    'trolling',
    'fat',
    '6,000,000',
    'hack'
]

# we need verbs
verbs = [
    
    
]


#!/usr/bin/env python
# Every great project starts with... ENTERPRISE QUALITY.

##############################################################
#         INDUSTRIAL GRADE SHITPOST MACHINERY                #
#                 "Oh my god, it's so lifelike"              #
# "I refuse to use linux if it doesnt have a shitpost        #
#  generator built-in and no sane person would either"       #
##############################################################

# CODE OF CONDUCT THE SJWS HAVE INVADED
#  * be nice
#  * be accepting
#  * be civil
#  * install gentoo

#lets make a shitpost generator
#ok
#great idea

# TODO:
#  post numbers
#  quoting
#  botnet implementation

#limiting this shit to prefixes is terrible we need shitposts generated so real that we could make an OP with them
#how could we do that?
#something along the lines of 'only niggers will use "thing" why are you still using "thing" /tech/?'
#we could remake the prefixes to something where you do like: "only [noun] will use [thing] like that
#that could work
#ill make a list of formats
#more grammar
#how i end a function in python?
#you dont, you just let it be
#that upsets me
#yea python is a bit original with its syntax and it can be hard to get used to but its a really nice language
#i just use ruby and c
# its all fuckin in the tabs man let the tabs do all the work
# drop a tab drop a brace ezpz lemonsqueezy
#it lets you do things a lot of different ways

import random, re, os, signal, sys

prefix = prefixes = [
    'i hate', 'I hate', 'I fucking hate',
    'Hey guys', 'hey guys', 'hey guise',
    'fucking', 'Fucking', 'FUCKING',
    'the best meme is',
    'kill all',
    'the worst meme is',
    'the real botnet is',
    '>yfw',
    '>yrw',
    '>tfw',
    'smh tbh',
    'DAE le',
    '>implying',
    'Hey faggots,',
    'How do you',
    'It\'s like I\'m really',
    'Do you suck',
    'Slide thread,',
    'That',
    'now that the dust has settled, how do we feel about',
    'repost if you',
    'op is a faggot'
]

formats = [
    '[prefix] [adjective] [noun]',
    'fucking [noun] [noun] [noun] [noun]',
    'Nice try, [noun]',
    'Fucking [noun]fags',
    '\n\n>2015 \n >still [verb] [noun]\n >ISHYGDDT\n\n',
    'anyone have that [noun] webm?',
    '[noun] thread',
    '[adjective] [noun] detected',
    '[verb] [adjective] [noun] detected',
    'Can\'t [verb] the [noun]',
    'Nice try you [verb] [noun]',
    '>>>/[place]/',
    '>[year] + [number]\n>[verb] the [noun]',
    'as a [noun]fag i feel like [noun]\'s are [adjective]..', #idk
    'I kind of like [adjective] [noun] tbh fam.',
    '>[verb] the [adjective] jew',
    'If you see this shitpost while scrolling, you\'ve been visited by the [adjective] [noun] of [verb]. [noun] and [adjective] [noun] will be yours, but only if you post [noun] [verb] [noun].',
    '>Posting in a [noun] thread'
    'What did you [verb] did you just [adjective] about me, you [little] [noun]? I\'ll have you know I [verb] top of my [noun] in the [place], and I\'ve been involved in numerous secret raids on [noun], and I have over [number]'
]

# if the prefix is singular then noun should be plural and vice versa
# could use a dictionary with word type and singularity
#we could just make 2 different prefixes tables, one which needs singular ones and one which needs plural, and with formatting we can just add s at the end idk
#that's probably easier

noun = nouns = [
 'AIDS',
 'Arch',
 'Bait', 'BAIT', 'bait',
 'BENIS',
 'BSD',
 'CANCER',
 'CIA',
 'CISA',
 'CISC',
 'CUCKS',
 'dicks', 'DICKS',
 'FBI',
 'Gentoo',
 'Goy','Goys','Goyim',
 'KIKES','KIKE',
 'Lisp',
 'NIGGERS',
 'NORMIES',
 'mate', 'm8', 'm80s',
 'NSA',
 'Normies',
 'PENIS',
 'RISC',
 'SHILLS',
 'SICP',
 'SJWs',
 'SPICS',
 'SYSTEMD',
 'Shlomo',
 'TPP',
 'TROLL',
 'VN',
 'Windows 10',
 'Windows 7',
 'Windows XP',
 'Windows [number]',
 '[number] memers',
 'anime',
 'anonymous',
 'apple',
 'archfags',
 'benis',
 'big guys',
 'cancer',
 'cock',
 'cucks',
 'faggot',
 'fam',
 'feel',
 'feminist',
 'google chrome',
 'hack',
 'hacker',
 'kek',
 'keks',
 'kikes',
 'loli',
 'maymays',
 'mint',
 'niggers',
 'newfag', 'newfriend',
 'normie',
 'os-tan',
 'penis',
 'plebbit',
 'ruse',
 'shills',
 'shitposts',
 'shazbot',
 'spics',
 'systemd',
 'the [number]0000000 that died in the holocaust',
 'the jews',
 'thread',
 'troll',
 'ubuntu',
 'neghole',
 'pozhole',
 'shekel'
]


adjective = adjectives = [
    'gay',
    'the best',
    'with no survivors',
    'ebin',
    'qt 3.1415926535897932384626433832795',
    'memed',
    'epic',
    'poz',
    'fat',
    'dank',
    '6,000,000',
    'hack',
    'stupid',
    'retarded',
    'hand-rubbing', 'hook-nosed'
]

# we need verbs
#then make a format with verbs you faggot
verb = verbs = [
    'crash this plane',
    'crashing',
    'fucking',
    'shitposting',
    'memeing',
    'trolling',
    'flaming',
    'cucked',
    'detect','pleb detected',
    'sperging',
    'stumped',
    'niggin'
]

#what if we put synonymns on the same line -- ok
place = places = [
    'g',
    'tech', 'Church of RMS',
    'leftypol', 'r9k', 'fem', 'mgtow', 'pol',
    '4chan', 'cuckchan', '4chad', 'halfchan',
    '9gag', '9shit', '9fag',
    'plebbit',
    'tumblr',
    'voat',
    'jewbook', 'kikebook','gaschamber','auschwitz',
    'Twatter'
]

year = years = [
    '3000 BC'
    '1990'
    'Y2K',
    'Y2K38',
    '2014',
    '2015',
    '2016',
    'CURRENT_YEAR',
    '2014 + 1',
    'The year of our lord, 2015'
]

#function just in case
def shitpost():
    c = random.choice
    format = c(formats)
    
    filters = {
        "[prefix]": lambda: c(prefixes),
        "[adjective]": lambda: c(adjectives),
        "[verb]": lambda: c(verbs),
        "[noun]": lambda: c(nouns).replace("[number]", str(random.randrange(-1000, 1000))),
        "[place]": lambda: c(places),
        "[number]": lambda: str(random.randrange(-1000, 1000)),
        "[year]": lambda: c(years)
    }

    split = format.split(" ")
    
    for index, word in enumerate(split):
        for filter, func in filters.items():
            if filter in word:
                split[index] = word.replace(filter, func())
    
    format = " ".join(split)
    return format

# now we just need to push this onto a web server (github-pages? django?)
def htmlwrapper():
    full = "<html><head><title>Welcome to the Shitposting Machinery</title></head><body> "
    for i in range(10):
        full += "<p>" + shitpost() + "</p>"
    full += "</body> </html>"
    return full

def shitpost_by_amount(amount):
    for i in range(amount): # fucking py3 whatever
        print(shitpost())

amount = -1
while amount == -1:
    try:
        amount = int(input("Amount of shitposts: "))
        if amount < 0:
            raise ValueError("penis lol xD")
    except ValueError:
        amount = -1

shitpost_by_amount(amount)

#whats the point of this? we already fixed the bug
#lisp memes
#ah i never programmed in lisp
def parse_sexp(string):
    sexp = [[]]
    atom = ''
    in_str = False

    LIST_OPEN = '('
    LIST_CLOSE = ')'
    QUOTE = '"'
    WHITESPACE = ' \n\t'
    
    for c in string:
        if c == LIST_OPEN and not in_str:
            sexp.append([])
        elif c == LIST_CLOSE and not in_str:
            if(len(atom) > 0):
                #determine the data
                has_decimal = False
                is_number = True
                for ch in atom:
                    if not (ch in '0123456789' and has_decimal):
                        has_decimal = ch == '.'
                        if not has_decimal:
                            is_number = False
                            break
                if is_number:
                    if has_decimal:
                        sexp[-1].append(float(atom))
                    else:
                        sexp[-1].append(int(atom))                        
                else:
                    sexp[-1].append(atom)

                atom = ''
            temp = sexp.pop()
            sexp[-1].append(temp)
        elif c in WHITESPACE and not in_str:
            sexp[-1].append(atom)
            atom = ''
        elif c == QUOTE:
            in_str = not in_str
        else:
            atom += c
    return sexp[0]

#test
print('S-Expression Test \n--------------')
print(parse_sexp('(+ 5 3 (* 4.5 4))'))

#excuse my shitty code
#im gonna do a raw_input thing
#function this and pass input
def shitpost_by_amount(amount):
    for i in range(amount): # fucking py3 whatever
        print(shitpost())

use_input = True

if use_input:
    amount = -1
    
    while amount == -1:
        try:
            amount = int(input("Amount of shitposts: "))
        except ValueError:
            amount = -1
    
    shitpost_by_amount(amount)


# TODO:
# post numbers
# quoting
# botnet implementation

#now what
#im gonna paste this to the main one, it looks like the autism cleared up
#nah
#anyone want contrib to the git
#over here
#we need to add a new feature to our sick ass shitposting machinery
#this all started with "lets make a shitpost generator"
# and we made it something more
#a shitposting robot
# a shitposting algorithm
