import lxml.etree as ET
import datetime

from webpage.metadata import PROJECT_METADATA
from tei.partials import TEI_NSMAP, custom_escape

class MakeTeiDoc():
    def __init__(self, text, PROJECT_METADATA=PROJECT_METADATA):
        self.nsmap = TEI_NSMAP
        self.project_md = PROJECT_METADATA
        self.base = "https://id.acdh.oeaw.ac.at/mmp/archiv/text"
        self.text = text
        if self.text.get_prev():
            self.prev = f'prev="{self.base}{self.text.get_prev_id()}"'
        else:
            self.prev = ""
        if self.text.get_next():
            self.next = f'next="{self.base}{self.text.get_next_id()}"'
        else:
            self.next = ""
        self.text_url = f"{self.base}{self.text.get_absolute_url()}"
        # self.creators = " ".join(["#{}".format(x.username) for x in self.text.creators.all()])
        if self.text.jahrhundert:
            self.jarhhundert = self.text.jahrhundert
        else:
            self.jahrhundert = ""

    def not_before(self):
        if self.text.start_date is not None:
            return self.text.start_date

    def not_after(self):
        if self.text.end_date is not None:
            return self.text.end_date
        elif self.not_before is not None:
            return self.not_before()
                
    def populate_header(self):
        header = f"""
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="archesource-{self.res.id}" {self.prev} {self.next} xml:base="{self.base}">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main">{self.text.title}</title>
            <title type="sub">{self.project_md['subtitle']}</title>
            <principal ref="WP">Walter Pohl</principal>
            <principal ref="VW">Veronika Wieser</principal>
            <respStmt>
                <resp>Researcher</resp>
                <name ref="WP">Walter Pohl</name>
                <name ref="VW">Veronika Wieser</name> 
            </respStmt>
            <respStmt>
                <resp>TEI conform Transformation</resp>
                <name ref="PA">Peter Andorfer</name>
            </respStmt>
         </titleStmt>
         <publicationStmt>
            <publisher>Austrian Centre for Digital Humanities</publisher>
            <idno type="django_id">{self.text_url}</idno>
         </publicationStmt>
         <sourceDesc>
            <msDesc>
               <msIdentifier>
                    <repository>{}</repository>
                    <msName>{}</msName>
               </msIdentifier>
               <physDesc>
                    <typeDesc>
                        <p>{}</p>
                    </typeDesc>
               </physDesc>
            </msDesc>
         </sourceDesc>
      </fileDesc>
     <profileDesc>
        <creation>
            <date notBefore="{self.not_before()}" notAfter="{self.not_after()}">
                {self.jahrhundert}
            </date>
        </creation>
     </profileDesc>
  </teiHeader>
  <text>
      <body>
         <p></p>
      </body>
      <back>
         <listPerson>
            <head>Erwähnte Personen</head>
            <person/>
         </listPerson>
         <listPlace>
            <head>Erwähnte Orte</head>
            <place/>
         </listPlace>
         <listOrg>
            <head>Erwähnte Institutionen</head>
            <org/>
         </listOrg>
      </back>
  </text>
</TEI>
"""
        return header

