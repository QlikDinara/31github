 from urllib.request import urlopen
 url = "http://olympus.realpython.org/profiles/aphrodite"
 page = urlopen(url)
 
 html_bytes = page.read()
 html = html_bytes.decode("utf-8")
 
 pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

print(title)