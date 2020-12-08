import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for i in lines:
        # First of all I removed all code repetitions
        # ------------------------------------------------- BOLD
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + \
                   m.group(2) + '</strong>' + m.group(3)
        # ------------------------------------------------- ITALICS
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + \
                   '</em>' + m.group(3)

        # ------------------------------------------------- HEADERS
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'

        # after removing repetitions list parse looks simply like below:
        # ------------------------------------------------- LIST
        m_item = re.match(r'\* (.*)', i)  # if there is list item
        if m_item:
            # -------------FIRST-----------
            if not in_list:  # is this is 1st list item: TODO
                in_list = True
                i = '<ul><li>' + m_item.group(1) + '</li>'
            else:
                i = '<li>' + m_item.group(1) + '</li>'
        else:  # ------------------- NOT LIST ITEM, JUST SOME TEXT
            m_item = re.match('<h|<ul|<p|<li', i)  # if there are not containers any text containers
            if not m_item:
                i = '<p>' + i + '</p>'

            if in_list:  # The ending of the list (previous i item was the last)
                in_list = False
                i = '</ul>' + i

        res += i

    if in_list:  # if list is open but that's the end of file
        res += '</ul>'
    return res