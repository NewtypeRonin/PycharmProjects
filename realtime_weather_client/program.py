import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():

    # t = (1,7, 'cat', [1,2,3])
    # print(t) - prints 1, 7, cat, [1 2 3]
    # this is a tuple, it's basically a collection of different data types
    # very handy for working with this data we're pulling from the internet page
    # print(t[1]) - prints 7
    # n1, n2, s, l = t
    # print(n1, n2, s, l) -  prints 1 7 cat [1 2 3]
    # a way of assigning values to variable can be used with tuples like this


    print_the_header()

    code = input('What zipcode do you want the weather for (76521)? ')

    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_the_header():
    print('---------------------------------')
    print('     Weather App')
    print('---------------------------------')
    print()

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/tx/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code) checks status code of a given web page
    # print(response.text[0:250]) Grabs the first 250 characters from the html/xml file

    return response.text

def get_weather_from_html(html):
    # cityCss ='.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherTempCss = test-true wu-unit wu-unit-temperature is-degree-visible">
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
