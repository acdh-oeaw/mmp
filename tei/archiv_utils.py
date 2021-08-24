import lxml.etree as ET
import re

from webpage.metadata import PROJECT_METADATA
from tei.partials import TEI_NSMAP


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
        if self.text.start_date:
            start_date = re.search(r'\d+', self.text.start_date).group()
            if len(start_date) == 3:
                return "notBefore='0" + start_date + "'"
            elif len(start_date) == 2:
                return "notBefore='00" + start_date + "'"
            elif len(start_date) == 1:
                return "notBefore='000" + start_date + "'"
            else:
                return "notBefore='" + start_date + "'"
        else:
            return ""

    def not_after(self):
        if self.text.end_date:
            end_date = re.search(r'\d+', self.text.end_date).group()
            if len(end_date) == 3:
                return "notAfter='0" + end_date + "'"
            elif len(end_date) == 2:
                return "notAfter='00" + end_date + "'"
            elif len(end_date) == 1:
                return "notAfter='000" + end_date + "'"
            else:
                return "notAfter='" + end_date + "'"
        else:
            return ""

    def text_lang(self):
        if self.text.text_lang:
            return self.text.text_lang
        else:
            return "lat"

    def populate_header(self):
        text_url = f"https://mmp.acdh-dev.oeaw.ac.at{self.text.get_absolute_url()}"
        header = f"""
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="archetext__{self.text.id}"
{self.prev} {self.next} xml:base="{self.base}">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title type="main">
                Digital Edition of cited texts
                from "{self.text.title}"
            </title>
            <title type="fullquote">
               <bibl>: {self.text.title}, {self.text.alt_title},
               in: {self.text.edition}</bibl>
            </title>
            <title type="sub">{self.project_md['subtitle']}</title>
            <principal ref="#WP">Walter Pohl</principal>
            <principal ref="#VW">Veronika Wieser</principal>
            <respStmt>
                <resp>Data Collection and Analysis</resp>
                <name ref="#WP">Walter Pohl</name>
                <name ref="#VW">Veronika Wieser</name>
            </respStmt>
            <respStmt>
                <resp>Digital Edition (WebApp) and Database</resp>
                <name ref="#PA">{self.project_md['author']}</name>
            </respStmt>
            <respStmt>
                <resp>TEI/XML conform markup</resp>
                <name ref="#DST">Daniel Stoxreiter</name>
            </respStmt>
         </titleStmt>
         <editionStmt>
            <edition>digital edition <date when="2021">2021</date></edition>
            <funder ref="https://www.oeaw.ac.at/foerderungen/innovationsfonds-forschung-wissenschaft-und-gesellschaft">
                OEAW Innovation Fund "Research, Science and Society"
            </funder>
         </editionStmt>
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
                    Attribution — You must give appropriate credit,
                    provide a link to the license, and indicate if changes were made.
                    You may do so in any reasonable manner,
                    but not in any way that suggests the licensor endorses you or your use.
                    No additional restrictions —
                    You may not apply legal terms or technological measures that legally
                    restrict others from doing anything the license permits.
                </p>
                <p>The text of the Digital Edition is available at <ref type="django_text_id">{text_url}</ref></p>
            </availability>
         </publicationStmt>
         <notesStmt>
            <note>{self.text.kommentar}</note>
         </notesStmt>
         <sourceDesc>
            <bibl xml:id="text__{self.text.id}" type="short">{self.text.edition}</bibl>
         </sourceDesc>
     </fileDesc>
     <encodingDesc>
        <projectDesc>
            <p>
                {self.project_md['description']}
            </p>
        </projectDesc>
        <editorialDecl>
            <p>
                {self.text.title} was found in 
                <rs type="bibl" ref="#text__{self.text.id}">{self.text.edition}</rs>.
                Various text passages (citations) were chosen and further analyzed.
                These original text passages (citations) were often but not always digitized.
            </p>
            <normalization>
                <p>Some text passages (citations) were translated in modern british english or german.</p>
                <p>Keywords of text passages were collected and origanized containing the keyword,
                    lemma (Wurzel) and different variants of the keyword.</p>
                <p>Person-Names in different languages, birth and death dates were collected.</p>
                <p>Place-Names in different languages, category and geographical information
                    like latitude and longitude were collected.</p>
            </normalization>
            <interpretation>
                <p>Some text passages (citations) were summarized.</p>
            </interpretation>
        </editorialDecl>
     </encodingDesc>
     <profileDesc>
        <textClass>
            <keywords scheme="http://www.w3.org/2004/02/skos/core#Concept">
                <term>{self.text.art}</term>
            </keywords>
        </textClass>
        <langUsage>
            <language ident="{self.text_lang()}"/>
            <language ident="de"/>
            <language ident="en"/>
        </langUsage>
        <creation>
            <date {self.not_before()} {self.not_after()}>
                {self.jahrhundert + " century"}
            </date>
        </creation>
     </profileDesc>
  </teiHeader>
  <text>
  </text>
</TEI>
"""
        return header

    def create_header_node(self):
        header = ET.fromstring(self.populate_header())
        return header

    def pop_mentions(self):
        cur_doc = self.create_header_node()

        text = cur_doc.xpath(".//tei:text", namespaces=self.nsmap)[0]
        if self.text.rvn_stelle_text_text.all():
            body = ET.Element("{http://www.tei-c.org/ns/1.0}body")
            for x in self.text.rvn_stelle_text_text.all():
                div = ET.Element("{http://www.tei-c.org/ns/1.0}div")
                div.attrib["{http://www.w3.org/XML/1998/namespace}id"] = "cite__" + str(x.id)
                index = ET.Element("{http://www.tei-c.org/ns/1.0}index")
                variantlist = []
                wurzellist = []
                keywordlist = []
                for k in x.key_word.all():
                    term = ET.Element("{http://www.tei-c.org/ns/1.0}term")
                    term.attrib["key"] = "keyword__" + str(k.id)
                    term.text = k.stichwort
                    keywordlist.append([str(k.id), k.stichwort])
                    if k.art:
                        term.attrib["type"] = k.art
                    if k.wurzel:
                        term.attrib["n"] = k.wurzel
                        wurzel = k.wurzel
                        wurzellist.append([str(k.id), wurzel])
                    index.append(term)
                    if k.name_gr:
                        termGr = ET.Element("{http://www.tei-c.org/ns/1.0}term")
                        termGr.text = k.name_gr
                        if k.art:
                            termGr.attrib["type"] = k.art
                        if k.wurzel:
                            termGr.attrib["ana"] = k.wurzel
                        index.append(termGr)
                    if k.varianten:
                        # indexVarianten = ET.Element("{http://www.tei-c.org/ns/1.0}index")
                        varianten = k.varianten.split(";")
                        for v in varianten:
                            termVarianten = ET.Element("{http://www.tei-c.org/ns/1.0}term")
                            termVarianten.attrib["type"] = "variant"
                            termVarianten.text = v
                            variantkey = v
                            # indexVarianten.append(termVarianten)
                            variantlist.append([str(k.id), variantkey])
                            term.append(termVarianten)
                div.append(index)
                # original citation in lang text_lang() default "lat"
                cite_text = x.zitat
                cit = ET.Element("{http://www.tei-c.org/ns/1.0}cit")
                cit.attrib["type"] = "original"
                if x.zitat:
                    # cite_text = x.zitat
                    # cite_text = re.sub(r"<", "[", cite_text, flags=re.IGNORECASE)
                    # cite_text = re.sub(r">", "]", cite_text, flags=re.IGNORECASE)
                    # annotate keywords within cite (Stelle) as <term>
                    # if k.wurzel:
                    #     for i, w in wurzellist:
                    #         cite_text = re.sub(rf"({w}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                    #                            "<term ref='#keyword__%s'>" % (i) + r"\1" + "</term>" + r"\2",
                    #                            cite_text,
                    #                            flags=re.IGNORECASE)
                        # for match in re.finditer(rf"{w}\w+?[\s,\\.,\\,,\\!,\\?]", cite_text, flags=re.IGNORECASE):
                        #     a,b = match.span()
                        #     t = cite_text
                        #     l = [t[:a], "<term ref='#keyword__%s'>" % (i), t[a:b], "</term>", t[b:]]
                    # else:
                    #     for i, v in variantlist:
                    #         cite_text = re.sub(rf"({v}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                    #                            "<term ref='#keyword__%s'>" % (i) + r"\1" + "</term>" + r"\2",
                    #                            cite_text,
                    #                            flags=re.IGNORECASE)
                        # for match in re.finditer(rf"{v}\w+?[\s,\\.,\\,,\\!,\\?]", cite_text, flags=re.IGNORECASE):
                        #     a,b = match.span()
                        #     t = cite_text
                        #     l = [t[:a], "<term ref='#keyword__%s'>" % (i), t[a:b], "</term>", t[b:]]
                        #     cite_text = "".join(l)
                        #     print(cite_text)
                    # for i, key in keywordlist:
                    #     cite_text = re.sub(rf"([“,,\",′,\s,\(,',‘])({key})([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                    #                        r"\1" + "<term ref='#keyword__%s'>" % (i) + r"\2" + "</term>" + r"\3",
                    #                        cite_text,
                    #                        flags=re.IGNORECASE)
                    # cit.append(ET.fromstring("<quote>" + cite_text + "</quote>"))
                    quote = ET.Element("{http://www.tei-c.org/ns/1.0}quote")
                    quote.text = x.zitat
                    cit.append(quote)
                    cit[0].attrib["{http://www.w3.org/XML/1998/namespace}lang"] = self.text_lang() 
                ref = ET.Element("{http://www.tei-c.org/ns/1.0}ref")
                ref.text = x.zitat_stelle
                cit.append(ref)
                div.append(cit)
                # translation of original citation in lang "?"
                if x.translation:
                    divTranslation = ET.Element("{http://www.tei-c.org/ns/1.0}div")
                    divTranslation.attrib["type"] = "translation"
                    t = x.translation
                    t = re.sub(r"<", "[", t, flags=re.IGNORECASE)
                    t = re.sub(r">", "]", t, flags=re.IGNORECASE)
                    if k.wurzel:
                        for i, w in wurzellist:
                            t = re.sub(rf"({w}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                       "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\1" + "</foreign>" + r"\2",
                                       t,
                                       flags=re.IGNORECASE)
                    else:
                        for i, v in variantlist:
                            t = re.sub(rf"({v}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                       "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\1" + "</foreign>" + r"\2",
                                       t,
                                       flags=re.IGNORECASE)
                    for i, key in keywordlist:
                        t = re.sub(rf"([“,,\",′,\s,\(,',‘])({key})([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                   r"\1" + "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\2" +
                                   "</foreign>" + r"\3",
                                   t,
                                   flags=re.IGNORECASE)
                    divTranslation.append(ET.fromstring("<p>" + t + "</p>"))
                    divTranslation[0].attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "mix"
                    div.append(divTranslation)
                # summary of original citation in lang "?"
                if x.summary:
                    divSummary = ET.Element("{http://www.tei-c.org/ns/1.0}div")
                    divSummary.attrib["type"] = "summary"
                    s = x.summary
                    s = re.sub(r"<", "[", s, flags=re.IGNORECASE)
                    s = re.sub(r">", "]", s, flags=re.IGNORECASE)
                    if k.wurzel:
                        for i, w in wurzellist:
                            s = re.sub(rf"({w}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                       "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\1" + "</foreign>" + r"\2",
                                       s,
                                       flags=re.IGNORECASE)
                    else:
                        for i, v in variantlist:
                            s = re.sub(rf"({v}\w+?)([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                       "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\1" + "</foreign>" + r"\2",
                                       s,
                                       flags=re.IGNORECASE)
                    for i, key in keywordlist:
                        s = re.sub(rf"([“,,\",′,\s,\(,',‘])({key})([′,\s,\.,\,,\!,\?,\),\",',’,”,;])",
                                   r"\1" + "<foreign xml:lang='%s'>" % (self.text_lang()) + r"\2" +
                                   "</foreign>" + r"\3",
                                   s,
                                   flags=re.IGNORECASE)
                    divSummary.append(ET.fromstring("<p>" + s + "</p>"))
                    divSummary[0].attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "mix"
                    div.append(divSummary)
                # adding all original, translation and summary quote to div
                note = ET.Element("{http://www.tei-c.org/ns/1.0}note")
                if x.kommentar:
                    note.text = x.kommentar
                    div.append(note)
                body.append(div)
            text.insert(1, body)

        if self.text.autor or self.text.ort:
            back = ET.Element("{http://www.tei-c.org/ns/1.0}back")
            text = cur_doc.xpath(".//tei:text", namespaces=self.nsmap)[0]
            text.append(back)

        if self.text.autor:
            author = cur_doc.xpath(".//tei:titleStmt/tei:title[@type='fullquote']", namespaces=self.nsmap)[0]
            back = cur_doc.xpath(".//tei:back", namespaces=self.nsmap)[0]
            listPerson = ET.Element("{http://www.tei-c.org/ns/1.0}listPerson")
            # autor = ET.Element("{http://www.tei-c.org/ns/1.0}author")
            for x in self.text.autor.all():
                persName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                if x.name:
                    persName.text = x.name
                else:
                    persName.text = " unknown"
                persName.attrib["ref"] = f"#person__{x.id}"
                # person for tei:back tei:listPerson
                person = ET.Element("{http://www.tei-c.org/ns/1.0}person")
                person.attrib["{http://www.w3.org/XML/1998/namespace}id"] = f"person__{x.id}"
                # persName in lang "de"
                if x.name:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "de"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                # persName in lang "lat"
                if x.name_lat:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name_lat.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "lat"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                # persName in lang "en"
                if x.name_en:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name_en.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                # persName in lang "fr"
                if x.name_fr:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name_fr.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                # persName in lang "it"
                if x.name_it:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name_it.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "it"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                # persName in lang "gr"
                if x.name_gr:
                    ListPersName = ET.Element("{http://www.tei-c.org/ns/1.0}persName")
                    forename = ET.Element("{http://www.tei-c.org/ns/1.0}forename")
                    surname = ET.Element("{http://www.tei-c.org/ns/1.0}surname")
                    names = x.name_gr.split(' ', 1)
                    if len(names) == 2:
                        forename.text = names[0]
                        surname.text = names[1]
                    else:
                        forename.text = names[0]
                        surname.text = ""
                    ListPersName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "gr"
                    ListPersName.append(forename)
                    ListPersName.append(surname)
                    person.append(ListPersName)
                if x.start_date:
                    birth = ET.Element("{http://www.tei-c.org/ns/1.0}birth")
                    date_b = ET.Element("{http://www.tei-c.org/ns/1.0}date")
                    date_b.text = x.start_date
                    date_att = re.search(r'\d+', x.start_date).group()
                    if len(x.start_date) == 3:
                        birth.attrib["when"] = "0" + date_att
                    elif len(x.start_date) == 2:
                        birth.attrib["when"] = "00" + date_att
                    elif len(x.start_date) == 1:
                        birth.attrib["when"] = "000" + date_att
                    else:
                        birth.attrib["when"] = date_att
                    birth.append(date_b)
                    person.append(birth)
                if x.end_date:
                    death = ET.Element("{http://www.tei-c.org/ns/1.0}death")
                    date_d = ET.Element("{http://www.tei-c.org/ns/1.0}date")
                    date_d.text = x.end_date
                    date_att = re.search(r'\d+', x.end_date).group()
                    if len(x.end_date) == 3:
                        death.attrib["when"] = "0" + date_att
                    elif len(x.end_date) == 2:
                        death.attrib["when"] = "00" + date_att
                    elif len(x.end_date) == 1:
                        death.attrib["when"] = "000" + date_att
                    else:
                        death.attrib["when"] = date_att
                    death.append(date_d)
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
                listPerson.append(person)
                if person is not None:
                    back.append(listPerson)
                author.insert(0, persName)
        if self.text.ort:
            back = cur_doc.xpath(".//tei:back", namespaces=self.nsmap)[0]
            listPlace = ET.Element("{http://www.tei-c.org/ns/1.0}listPlace")
            for x in self.text.ort.all():
                place = ET.Element("{http://www.tei-c.org/ns/1.0}place")
                place.attrib["{http://www.w3.org/XML/1998/namespace}id"] = "place__{}".format(
                    x.id
                )
                # placeName in lang "en"
                if x.name:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"
                    place.append(placeName)
                # persName in lang "antik"
                if x.name_antik:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name_antik
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "lat"
                    place.append(placeName)
                # persName in lang "de"
                if x.name_de:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name_de
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "de"
                    place.append(placeName)
                # persName in lang "fr"
                if x.name_fr:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name_fr
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"
                    place.append(placeName)
                # persName in lang "it"
                if x.name_it:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name_it
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "it"
                    place.append(placeName)
                # persName in lang "gr"
                if x.name_gr:
                    placeName = ET.Element("{http://www.tei-c.org/ns/1.0}placeName")
                    placeName.text = x.name_gr
                    placeName.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "gr"
                    place.append(placeName)
                if x.long or x.lat:
                    location = ET.Element("{http://www.tei-c.org/ns/1.0}location")
                    geo = ET.Element("{http://www.tei-c.org/ns/1.0}geo")
                    geo.text = str(x.lat) + ' ' + str(x.long)
                    geo.attrib['decls'] = "latLong"
                    location.append(geo)
                    place.append(location)
                if x.norm_id:
                    idno = ET.Element("{http://www.tei-c.org/ns/1.0}idno")
                    idno.text = x.norm_id
                    idno.attrib["type"] = "ID"
                    place.append(idno)
                if x.kommentar:
                    noteComment = ET.Element("{http://www.tei-c.org/ns/1.0}note")
                    noteComment.text = x.kommentar
                    noteComment.attrib["type"] = "comment"
                    place.append(noteComment)
                if f"{x.art}":
                    noteType = ET.Element("{http://www.tei-c.org/ns/1.0}note")
                    noteType.text = f"{x.art}"
                    noteType.attrib["type"] = "type"
                    place.append(noteType)
                if f"{x.kategorie}":
                    noteCategory = ET.Element("{http://www.tei-c.org/ns/1.0}note")
                    noteCategory.text = f"{x.kategorie}"
                    noteCategory.attrib["type"] = "category"
                    place.append(noteCategory)
                listPlace.insert(2, place)
                if place is not None:
                    back.insert(2, listPlace)

        return cur_doc

    def export_full_doc(self):
        return self.pop_mentions()

    def export_full_doc_str(self, file="temp.xml"):
        with open(file, 'wb') as f:
            f.write(ET.tostring(self.pop_mentions(), pretty_print=True, encoding='UTF-8'))
        return file
