
from lxml import etree

class SchemaValidationLibrary:
    @staticmethod
    def validate_xml(xml_file, xsd_file):

        with open('C:\\Users\\HP\\PycharmProjects\\Automation\\pythonProject1\\TestCases\\schema.xsd', 'rb') as xsd_f, open('C:\\Users\\HP\\PycharmProjects\\Automation\\pythonProject1\\TestCases\\test.xml', 'rb') as xml_f:
            schema_root = etree.XML(xsd_f.read())
            schema = etree.XMLSchema(schema_root)
            parser = etree.XMLParser(schema=schema)

            try:
                etree.fromstring(xml_f.read(), parser)
                return "XML is valid against XSD"
            except etree.XMLSyntaxError as e:
                return f"XML is invalid: {str(e)}"
