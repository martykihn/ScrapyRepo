NYC Data Science Academy
Submission #2

# WEB SCRAPING PROJECT

# PROJECT DESCRIPTION

My project used Scrapy to scrape text from a website called TheMovieSpoiler.com

The website contains thousands of fairly long (2K-word) plot summaries of major
motion pictures, documentaries and TV shows released in the past decade or so.
The summaries are contributed by civilians and they contain the endings of the movies
(thus the name 'Spoilers'). The summaries themselves include only the TITLE and
the SPOILER itself (text). Sometimes there is a YEAR - but no GENRE or BOXOFFICE.

In order to supplement the SPOILERS I also used an API to access GENRE for the titles
scraped. This API got data from TMDB.org, a public data source for movie info.

I also got boxoffice data from TheNumbers by scraping using the method demonstrated
in class. (I didn't include this in my scraping file since it was already demod.)

# MOTIVATION

I have been interested in movie plots for years, since studying screenwriting and
working in LA some time ago. My hypothesis is that there are linguistic patterns in
the plots of movies that can be found in summaries. In particular I was interested in
the difference between the plots and verbal patterns of:
	(1) Different GENRES (Action vs. Comedy)
	(2) HITS vs MISSES (successful vs less successful movies)
	
My audience was (potentially) production companies, producers and writers who are
interested in creating successful features. I assume they have a portfolio of projects
and want to know what makes a COMEDY different from an ACTION movie at the professional
level. Also - more importantly - what makes a SUCCESSFUL movie vs an ALSO-RAN.

# WEB SCRAPING

The website was a Wordpress blog with some customization - basically. It was quite
difficult to scrape since it used different formats. In particular, current movies
were captured on different page and format from older movies. I ended up having to
use three different scripts for three different formats of spoiler pages.

Also - YEARS were often missing for the titles. Luckily they were sometimes present
in the URLs or in the TITLES themselves - which required some use of RegEx and additional
parsing to bring out.

As I said, I used an API to get genres (matched by TITLE and YEAR).

# ANALYSIS

I was new to NLTK and text analysis so limited my explorations to basic techniques.
The general techniques I used were:
	(1) Word frequency
	(2) Bigrams and Trigrams
	(3) Wordclouds
	(4) Contexts/Similar words
	(5) Part of Speech frequencies
	
To focus my word, I compared:
	(1) Action vs Comedy -- assuming they would show differences
	(2) Action Hit vs Action Misses -- keeping genre constant
	
# FINDINGS

The findings are contained in the 6 i notebooks in the folder.

I found that the corpus itself was almost half Action and Drama films - i.e.,
29% Action and 22% Drama. Comedy was 18%. Crime was 11% and Horror only 8%.
So Action seems to be by far the most popular genre.

Plot spoilers were of similar lengths -- about 1,800 words each.

I looked at TOTAL SPOILERS (all film plots) first. The most frequent words were:
GET. TELL, GO, SEE, FIND, SAY, TAKE, TRY, BACK, MAKE, ASK, KILL, COME.

This was interesting because it showed the importance of interpersonal action words,
that is - words that are about an action that implies MOVEMENT or RELATIONSHIP.

Most frequent trigrams were:
(get, phone, call)       37
(make, look, like)       36
(tri, find, way)         26
(make, thing, worse,)    24
(return, home, find)     23
(say, doesn’t, want)     22
(see, look, like)        19
(new, york, citi)        19
(young, woman, name)     18

These were quite dramatic - showing importance of phone calls, deception and attempts.

# ACTION VS COMEDY

I compared genre spoilers for two different popular genres.

After calculating frequencies, I created a dataframe with words, frequencies
(based on frequency / total words in corpus) for the Genres.

These words were more relatively frequent in ACTION movies vs COMEDY:
	* find
	* back and take
	* one
	* kill
	* help
	* fight
	
Among trigrams, there were interesting patterns with the following standing out
to me:
	* More common in ACTION: gain-upper-hand and make-look-like and try-get-away were
	the most frequen trigrams -- all about manipulation and deception
	* More common in COMEDY: make-thing-worse, get-back-together, go-back-inside
	and get-phone-call were the most popular trigrams -- not about manipulation
	but rather indicating people getting together/communicating or consequences
	for actions that were unexpected
	
# HITS VS MISSES

I compared Action Genre films that were above-average boxoffice (HITS) vs those that
were below-average boxoffice (MISSES).

Word frequencies showed a similar list - but "KILL" was must less popular in the HITS
that in the MISSES. "FIGHT" was more frequent in HITS than MISSES. This could indicate
that FIGHTS are more popular at the boxoffice than lethal endings.

BIGRAMS showed that look-like was most frequent in HITS but not present at all in
MISSES. This indicates ambiguity/deception/confusion -- leading to suspense. On
the other hand, next-day and drive-away and two-men were in MISSES but not HITS.
These are relatively weak statements about retreat/time passing. Less active.

HYPOTHESIS: from the word analysis and word cloud, it seemed to me that HITS had
more verbs (action words) and proper nouns (specific people/things) that MISSES.
To test this, I looked at POS.

# PART OF SPEECH

I looked at Action Genre films that were HITS and MISSES tagged by Part of Speech (POS).

I generated a plot that showed frequency of POS for Action Hits and Misses. Overlaid,
there were remarkable agreement in the plots -- indicating that POS frequency may be
a function of the spoiler format or the genre as a whole.

But my hypothesis was to some extent affirmed -- action HITS did use more active
verbs and proper nouns (as well as Determinants like All/Any/Every) in their spoilers.

# SUMMARY

Text analysis is an art form and I have only made a dent here. There were differences
among the GENRES and between HITS and MISSES. In particular, I think my most interesting
findings were these:
> Comedy plots have more language about human interaction & consequences
> Action plots have more language about actions, named people and places (Proper Nouns)
> Hits focus on verbs, specific action, and deception/suspense
> Misses have more language that is passive/time-filling (e.g., "next-day")

Obviously, there is more to do. In particular, I would like to be able to add an
element of time to the analysis -- that is, what happens WHEN (early/middle/late) in
the Spoiler. The PACE of the story is important and I could include it here.

This project has certainly encouraged me to do more with text analysis.

[The End]
