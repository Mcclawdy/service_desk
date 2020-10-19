from lxml import etree
from io import BytesIO


def parseXML(file, data):
    with open(file, 'r+') as f:
        f = f.read()
        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(f, parser)
        name = [name.text for name in tree.iter('name')]
        value = [value.text for value in tree.iter('value')]
        data_dict = dict(zip(name, value))
        for name in tree.iter('name'):
            if name in data.keys():
                name.text = data.get(name)

    return data

