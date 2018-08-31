import requests # for a good HTTP client
from bs4 import BeautifulSoup # for parsing soup

URL = 'https://hac.friscoisd.org/HomeAccess'

def getData(username, password):

    data = { 'classes': []}

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

    for c in classes:
        # single class object
        obj = { assignments: []}

        # eldritch horror that makes class names prettier
        obj['name'] = c.find('a', class_='sg-header-heading').string.split('-')[1][2:].strip()

        # TODO add average grade for class

        rows = c.find_all(class_='sg-asp-table-data-row')

        # TODO add assignments to class
        for r in rows:
            assignment = {}
            #assignment[]

        # adding class to collection of classes
        data['classes'].append(obj)

    print(data)
