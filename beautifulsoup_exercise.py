import requests as client
from bs4 import BeautifulSoup


res = client.get("https://news.ycombinator.com/news")
print(res.text)

bs_hacker_news = BeautifulSoup(res.text, "html.parser")

print(type(bs_hacker_news.find_all("a")))

print(bs_hacker_news.body.contents)
print(bs_hacker_news.find(id="pagespace"))
print(bs_hacker_news.select(".score"))
print("select all score selectors\n")
print(bs_hacker_news.select(".score")[0])
print("select all votes\n")
votes = bs_hacker_news.select(".score")
links = bs_hacker_news.select(".titlelink")
print(votes[0].get("id"))


def sort_stories_by_votes(v, l):
    return sorted(v, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext_args):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get("href", None)
        vote = subtext_args[i].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn, links)


print(create_custom_hn(links, votes))
