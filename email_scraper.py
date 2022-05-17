import re
from requests_html import HTMLSession
import csv
import validators



def get_email(url):

    EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

    # initiate an HTTP session
    session = HTMLSession()
    # get the HTTP Response
    try:
        r = session.get(url, timeout=8)
    except BaseException:
        return print("error getting url")
    # for JAVA-Script driven websites
    # r.html.render()
    emails = []
    for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
        emails.append(re_match.group())

    return emails




# loads urls from csv
def load_urls(csvfile):
    urls = []
    with open(csvfile, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                if len(row) > 3:
                    urls.append(row[3])
    return urls

if __name__ == "__main__":
    print("don't run this file")
