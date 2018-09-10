import os
import datetime

import feedparser
import yagmail

EMAIL = os.environ['WOKE_EMAIL']
RSS = {
    'https://www.sfgate.com/bayarea/feed/Bay-Area-News-429.php': 10,
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml': 10,
    'https://www.npr.org/rss/rss.php': 5,
    'https://www.npr.org/rss/rss.php?id=3': 5,
    'https://news.ycombinator.com/rss': 30,
    'https://feeds.feedburner.com/TechCrunch': 5,
    'https://techcrunch.com/startups/feed': 5,
    'https://www.recode.net/rss/index.xml': 5,
    'https://www.reddit.com/.rss': 10,
    'https://pitchfork.com/rss/reviews/best/albums/': 3,
    'https://www.merriam-webster.com/wotd/feed/rss2': 5,
}
LISTEN = {
    'https://www.kqed.org/radio': 'kqed: radio',
    'https://open.spotify.com/user/hypem/playlist/7nnyvG2CHYgiCOrUlh67v7': 'hypem: popular',
    'https://open.spotify.com/user/hypem/playlist/57sg1piOUnk203p1FYMpvJ': 'hypem: most blogged',
    'https://rainwave.cc/all/': 'rainwave: all',
    'https://rainwave.cc/game/': 'rainwave: game',
    'https://rainwave.cc/ocremix/': 'rainwave: ocremix',
    'https://open.spotify.com/user/npr_music?si=jb9O46H_R_yyy8jYNhRVVg': 'npr: music',
}

html = []

# NEWS
for url, limit in RSS.items():
    rss = feedparser.parse(url)
    html.append('<h3>%s<h3>' % rss['feed']['title'])
    for entry in rss['entries']:
        html.append('<a href="{link}" style="display:block;">{title}</a>'.format(**entry))
        limit -= 1
        if not limit:
            break
            
# LISTEN
html.append('<h3>Listen</h3>')
for url, source in LISTEN.items():
    html.append('<a href="{url}" style="display:block;">{source}</a>'.format(url=url, source=source))

# EMAIL
subject = datetime.datetime.now().strftime('%A, %B %-d, %Y')
yagmail.SMTP(EMAIL).send(EMAIL, subject, html)
