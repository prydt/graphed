import requests # for a good HTTP client
from bs4 import BeautifulSoup # for parsing soup

URL = 'https://hac.friscoisd.org/HomeAccess'

def getData(username, password):
    s = requests.Session()

    # log in
    s.post(URL + '/Account/LogOn', data = {
        'Database': '10',
        'LogOnDetails.UserName': username,
        'LogOnDetails.Password': password
    })

    # get grades page
    res = s.get(URL + '/Content/Student/Assignments.aspx')

    print(res.text)
