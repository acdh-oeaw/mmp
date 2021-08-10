import lxml.etree as ET

from webpage.metadata import PROJECT_METADATA
from tei.partials import TEI_NSMAP, custom_escape

class MakeTeiDoc():
    def __init__(self, text, PROJECT_METADATA=PROJECT_METADATA):
        self.nsmap = TEI_NSMAP
        self.project_md = PROJECT_METADATA
        self.base = "https://id.acdh.oeaw.ac.at/mmp/archiv/text"
        self.text = text
        if self.text.get_prev():
            self.prev = f'prev="{self.base}/{self.text.get_prev_id()}"'
        else:
            self.prev = ""
        if self.text.get_next():
            self.next = f'next="{self.base}/{self.text.get_next_id()}"'
        else:
            self.next = ""
        self.text_url = f"{self.base}/{self.text.get_absolute_url()}"
        if self.text.jahrhundert:
            self.jahrhundert = self.text.jahrhundert
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

    def text_lang(self):
        if self.text.text_lang is not None:
            return self.text.text_lang
        else:
            return "lat"

    def populate_header(self):
        text_url = f"https://mmp.acdh-dev.oeaw.ac.at{self.text.get_absolute_url()}"
        header = f"""
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="textid-{self.text.id}" {self.prev} {self.next} xml:base="{self.base}">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main">{self.text.title}</title>
            <title type="alt">{self.text.alt_title}</title>
            <principal ref="#WP">Walter Pohl</principal>
            <principal ref="#VW">Veronika Wieser</principal>
            <respStmt>
                <resp>Researcher</resp>
                <name ref="#WP">Walter Pohl</name>
                <name ref="#VW">Veronika Wieser</name> 
            </respStmt>
            <respStmt>
                <resp>TEI conform Transformation</resp>
                <name ref="#PA">Peter Andorfer</name>
            </respStmt>
         </titleStmt>
         <editionStmt>
            <p>{self.text.edition}</p>
         </editionStmt>
         <notesStmt>
            <note>{self.text.kommentar}</note>
         </notesStmt>
         <publicationStmt>
            <publisher>Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH)</publisher>
            <pubPlace>Vienna</pubPlace>
            <date when="2021">2021</date>
            <availability>
                <licence target="https://creativecommons.org/licenses/by/4.0"/>
                <p>The Creative Commons Attribution 4.0 International (CC BY 4.0) License applies to this document.</p>
                <p>Copyright (c) 2021 Austrian Centre for Digital Humanities at the Austrian Academy of Sciences</p>
                <p>
                    You are free to:
                    Share — copy and redistribute the material in any medium or format
                    Adapt — remix, transform, and build upon the material
                    for any purpose, even commercially.
                </p>
                <p>
                    Under the following terms:
                    Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
                    You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.       
                    No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
                </p>
            </availability>
            <idno type="django_id">{text_url}</idno>
         </publicationStmt>
         <sourceDesc>
            <bibl>
                <title type="main">{self.project_md['title']}</title>
                <title type="sub">{self.project_md['subtitle']}</title>
                <author ref="#PA">{self.project_md['author']}</author>
                <publisher>Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH)</publisher>
                <date when="2021">2021</date>
                <decoNote type="abstract">
                    <p>
                        {self.project_md['description']}
                    </p>
                </decoNote>
            </bibl>
            <msDesc>
               <msIdentifier>
                    <repository>ARCHE - A Resource Centre for Humanities Related Research in Austria</repository>
                    <msName>Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH)</msName>
               </msIdentifier>
               <msContents>
                    <textLang mainLang="{self.text_lang()}"/>
               </msContents>
               <physDesc>
                    <typeDesc>
                        <p>{self.text.art}</p>
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
            <head>Autor/en</head>
         </listPerson>
         <listPlace>
            <head>Erwähnte Orte</head>
         </listPlace>
      </back>
  </text>
</TEI>
"""
        return header

    def create_header_node(self):
        header = ET.fromstring(self.populate_header())
        return header

    def pop_mentions(self):
        cur_doc = self.create_header_node()

        if self.text.autor:        
            titleStmt = cur_doc.xpath(".//tei:titleStmt", namespaces=self.nsmap)[0]
            listPerson = cur_doc.xpath(".//tei:listPerson", namespaces=self.nsmap)[0]
            autor = ET.Element("{http://www.tei-c.org/ns/1.0}author")            
            for x in self.text.autor.all():
                person = ET.Element("{http://www.tei-c.org/ns/1.0}person")
                persName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                forename.text = x.name.split(' ', 1)[0]
                surname.text = x.name.split(' ', 1)[1]                
                persName.text = x.name
                persName.attrib["ref"] = "#person__{}".format(
                    x.id
                )
                autor.append(persName)
                person.attrib["{https://www.w3.org/XML/1998/namespace}id"] = "person__{}".format(
                    x.id
                )
                ListPersName.attrib["{https://www.w3.org/XML/1998/namespace}lang"] = "de"
                ListPersName.append(forename)
                ListPersName.append(surname)
                person.append(ListPersName)
                if x.start_date:
                    birth = ET.Element("{http://www.tei-c.org/ns/1.0}birth")
                    date = ET.Element("{http://www.tei-c.org/ns/1.0}date")
                    date.text = x.start_date
                    birth.attrib["when"] = x.start_date
                    birth.append(date)
                    person.append(birth)
                if x.end_date:
                    death = ET.Element("{http://www.tei-c.org/ns/1.0}death")
                    date = ET.Element("{http://www.tei-c.org/ns/1.0}date")
                    date.text = x.end_date
                    death.attrib["when"] = x.end_date
                    death.append(date)
                    person.append(death)
                if x.gnd_id:
                    idno = ET.Element("{http://www.tei-c.org/ns/1.0}idno")
                    idno.text = x.gnd_id
                    idno.attrib["type"] = "GND"
                    person.append(idno)
                if f"{x.ort}":
                    residence = ET.Element("{http://www.tei-c.org/ns/1.0}residence")
                    residence.text = f"{x.ort}"
                    person.append(residence)
                if x.kommentar:
                    note = ET.Element("{http://www.tei-c.org/ns/1.0}note")
                    note.text = x.kommentar
                    person.append(note)
                listPerson.insert(2, person)
            titleStmt.insert(2, autor)
            


        return cur_doc

    def export_full_doc(self):
        return self.pop_mentions()

    def export_full_doc_str(self, file="temp.xml"):
        with open(file, 'wb') as f:
            f.write(ET.tostring(self.pop_mentions(), pretty_print=True, encoding='UTF-8'))
        return file
