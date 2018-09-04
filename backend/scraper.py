import requests # for a good HTTP client
from bs4 import BeautifulSoup # for parsing soup

import json
import pprint
import os

URL = 'https://hac.friscoisd.org/HomeAccess'

def getDataWithLogin(username, password):
    s = requests.Session()

    # log in
    s.post(URL + '/Account/LogOn', data = {
        'Database': '10',
        'LogOnDetails.UserName': username,
        'LogOnDetails.Password': password
    })

    return getData(s)

def getDataWithToken(session_id, auth_cookie):
    return getData(requests.Session(), session_id, auth_cookie)

def getData(session, session_id=None, auth_cookie=None):

    data = { 'classes': [], 'session_id': '', 'auth_cookie': '' }

    # get grades page
    if session_id is None or auth_cookie is None:
        res = session.get(URL + '/Content/Student/Assignments.aspx')

    else:
        res = session.get(URL + '/Content/Student/Assignments.aspx', cookies={
            '.AuthCookie': auth_cookie,
            'ASP.NET_SessionId': session_id
        })

    # for auth cookies
    data['session_id'] = session.cookies['.AuthCookie']
    data['auth_cookie'] = session.cookies['ASP.NET_SessionId']

    # for parsing html
    soup = BeautifulSoup(res.text, 'html.parser')

    classes = soup.find_all(class_='AssignmentClass')

    avgnum = 0 # for getting averages

    for c in classes:
        # single class object
        obj = { 'assignments': [] }

        # eldritch horror that makes class names prettier
        obj['name'] = c.find('a', class_='sg-header-heading').string.split('-')[1][2:].strip()

        # average grade for class
        obj['average'] = float(c.find('span', id='plnMain_rptAssigmnetsByCourse_lblHdrAverage_{}'.format(avgnum)).string[14:-1])
        avgnum = avgnum + 1

        rows = c.find('table', class_='sg-asp-table').find_all(class_='sg-asp-table-data-row')

        # add assignments to class
        for row in rows:
            assignment = {}

            # filling out assignment attributes
            columns = row.find_all('td')
            assignment['date_due'] = columns[0].string.strip()
            assignment['date_assigned'] = columns[1].string.strip()
            assignment['name'] = columns[2].find('a').string.strip()
            assignment['category'] = columns[3].string.strip()

            # CAN be None, so check
            if len(columns[4].string.strip()) > 0:
                assignment['score'] = float(columns[4].string.strip('\n %'))
            else:
                assignment['score'] = None

            if len(columns[5].string.strip()) > 0:
                assignment['total_points'] = float(columns[5].string.strip('\n %'))
            else:
                assignment['total_points'] = None

            obj['assignments'].append(assignment)

        # adding class to collection of classes
        data['classes'].append(obj)

    return json.dumps(data)

# only for testing purposes as this will never be used as a
if __name__ == '__main__':
    getData(os.environ['HUSERNAME'], os.environ['HPASSWORD'])