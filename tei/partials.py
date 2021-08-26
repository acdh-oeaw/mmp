from xml.sax.saxutils import escape, unescape


TEI_NSMAP = {
    'tei': "http://www.tei-c.org/ns/1.0",
    'xml': "http://www.w3.org/XML/1998/namespace",
}


PERS_TO_TEI_DICT = {
    'name': "{http://www.tei-c.org/ns/1.0}surname",
    'first_name': "{http://www.tei-c.org/ns/1.0}forename",
    'start_date': "{http://www.tei-c.org/ns/1.0}birth",
    'end_date': "{http://www.tei-c.org/ns/1.0}death",
}


def custom_escape(somestring):
    un_escaped = unescape(somestring)
    return escape(un_escaped)
