import csv
from xml.etree.ElementTree import Element,ElementTree
import requests
from StringIO import StringIO
from xml_pretty import xml_pretty
def download(url):
    response = requests.get(url,timeout=3)
    if response.ok:
        return StringIO(response.content)
def csvToXml(scsv,fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h:h.replace(' ',''),headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag,text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)
    pretty(root)
    et = ElementTree(root)


def handle(sid):
    print 'Download...(%d)' % sid
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6,'0')
    rf = download(url)
    if rf is None: return

    print 'Convert to XML...(%d)' % sid
    fname = str(sid).rjust(6,'0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf,wf)

from threading import Thread
t = Thred(target=handle,ards=(1,))
t.start()

print 'main thread'

class MyThread(Thread):
    def __init__(self,sid):
        Thred.__init__(self)
        self.sid = sid
    def run(self):
        handle(self,sid)

# t = MyThread(1)
# t.start()
threads = []
for i in xrange(1,11):
    t = MyThread(i)
    threads.append(t)
    t.start
# t.join()
for i in threads:
    t.join(t)
print 'main thread'