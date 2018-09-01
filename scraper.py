import requests # for a good HTTP client
from bs4 import BeautifulSoup # for parsing soup

import pprint

URL = 'https://hac.friscoisd.org/HomeAccess'

def getData(username, password):

    data = { 'classes': [] }

    s = requests.Session()

    # log in
    s.post(URL + '/Account/LogOn', data = {
        'Database': '10',
        'LogOnDetails.UserName': username,
        'LogOnDetails.Password': password
    })

    # get grades page
    res = s.get(URL + '/Content/Student/Assignments.aspx')

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

    pprint.pprint(data)
