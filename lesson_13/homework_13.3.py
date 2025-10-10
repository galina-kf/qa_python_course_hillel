import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

tree = ET.parse('groups.xml')
root = tree.getroot()


def find_incoming_by_number(file, my_number):
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        numbers = group.findall('number')
        if numbers.__len__() != 0:
            for item in numbers:
                if item.text == my_number:
                    timingExbytes = group.find('timingExbytes')
                    if timingExbytes is not None:
                        incoming = timingExbytes.find('incoming')
                        logging.info(f" Incoming value: {incoming.text}")


find_incoming_by_number('groups.xml', '4')
