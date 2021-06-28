import requests
from bs4 import BeautifulSoup
base_site = 'https://editorial.rottentomatoes.com/guide/140-essential-action-movies-to-watch-now/'
response = requests.get(base_site)
print(response)
html = response.content
# print(html)
soup = BeautifulSoup(html, 'lxml')
with open('Rotten_tomatoes_test_page.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

# Now environment is setup. Now we'll extract the title, year and score of each of the movie
divs = soup.find_all('div', {'class':'col-sm-18 col-full-xs countdown-item-content'})
# print(len(divs))    # This gives all the info and now we need to extract the heading tags from these 'div '
headings = [div.find("h2") for div in divs]
# print(headings)  # This gives para also not just the title
movie_names = [heading.find('a').string for heading in headings]    # coz all headings are under 'a'
print(movie_names)

years = [heading.find('span', class_ = 'start-year').string for heading in headings]
years = [year.strip('()') for year in years]
years = [int(year) for year in years]
print(years)
