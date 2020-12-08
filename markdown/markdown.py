import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False

    for i in lines:
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + \
                   m.group(2) + '</strong>' + m.group(3)

        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + \
                   '</em>' + m.group(3)

        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'


        m_item = re.match(r'\* (.*)', i)  
        if m_item:
            if not in_list:
                in_list = True
                i = '<ul><li>' + m_item.group(1) + '</li>'
            else:
                i = '<li>' + m_item.group(1) + '</li>'
        else:
            m_item = re.match('<h|<ul|<p|<li', i)  # if there are not containers any text containers
            if not m_item:
                i = '<p>' + i + '</p>'

            if in_list:
                in_list = False
                i = '</ul>' + i

        res += i

    if in_list:
        res += '</ul>'
    return res