import sys
import urllib
import datetime
import time
from elementtree.ElementTree import parse

API_KEY = "your_key"


def parse_last_chart(metro, country, chart):

  def getXml(url):

    try:
      myxml = parse(urllib.urlopen(url)).getroot()
      return myxml
    except Exception, e:
      print 'could not retrieve feed: ' + str(e)
      return 0

  items = []
  html = 0
  params = urllib.urlencode({'method': chart, 'country': country, 'metro': metro, 'api_key': API_KEY})
  url = 'http://ws.audioscrobbler.com/2.0/?%s' % params
  myxml = getXml(url)
  if not myxml:
    return 0
  for element in myxml.findall('topartists/artist'):
    if element.keys:
      images = element.findall('image')
      items.append({'text': element.findtext('name'),
                    'url': element.findtext('url'),
                    'image': images[0].text,
                    'artist': element.findtext('artist/name')})
  for element in myxml.findall('toptracks/track'):
    if element.keys:
      items.append({
              'text': element.findtext('name'),
              'url': element.findtext('url'),
              'artist': element.findtext('artist/name'),
          })
  html = '<ol>'
  for a in items:
    html += '<li><a href="' + a['url'] + '">' + a['text'] + '</a></li>'
  html += '</ol><!-- ' + datetime.datetime.now().ctime() + ' -->'

  if html:
    try:
      file_name = '%s_%s.txt' % (metro, chart)
      myfile = open(file_name, 'w')
      myfile.write(html.encode('utf-8'))
      myfile.close()
      print 'wrote file %s' % file_name
    except:
      print 'ERROR creating: %s' % file_name
  return 1


if __name__ == "__main__":
  if not len(sys.argv) == 4:
    CITIES = ['new york'
              'los angeles',
              'san francisco',
              'chicago',
              'atlanta',
              'boston',
              'dallas',
              'detroit',
              'houston',
              'philadelphia',
              'tampa',
              'washington',
              'las vegas']
    print "running US test cities...\ncmd usage: PYTHON parse_last_chart.py what-city what-chart path-to-snippet"
    for c in CITIES:
      parse_last_chart(c, 'united states', 'geo.getmetroartistchart')
      time.sleep(1)
      parse_last_chart(c, 'united states', 'geo.getmetrotrackchart')
      time.sleep(1)
  else:
    city = sys.argv[1]
    country = sys.argv[2]
    chart = sys.argv[3]
    parse_last_chart(city, country, chart)
