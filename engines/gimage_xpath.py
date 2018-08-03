# coding: utf-8
import urllib.request as req
import urllib.parse as up
import lxml.html as lh
import html
from json import loads

def gisearch(query, ua):
  try:
    values = {
      'q': query,
    }
    s_url = 'http://www.google.co.jp/search?tbm=isch&gws_rd=cr&safe=active&' + up.urlencode(values)
    headers = {
          "User-Agent": ua,
          }
    request = req.Request(url=s_url, headers=headers)
    res = req.urlopen(request, timeout=10).read()
    root = lh.fromstring(res.decode('utf-8'))
    image_xpath = root.xpath('//div[@class="rg_meta notranslate"]//text()')
    results = []
    num = 0
    while num <= 0:
      try:
        imdata = loads(image_xpath[num])
        if len(imdata['ru']) > 30:
          d_url = imdata['ru'][:30] + '...'
        else:
          d_url = imdata['ru']
        results.append({'url': html.escape(imdata['ru'], quote=True),
                    'd_url': html.escape(d_url, quote=True),
                    'thumb_src': html.escape(imdata['tu'], quote=True),
                    'img_src': html.escape(imdata['ou'], quote=True),
                    })
      except:
        pass
      num+=1
    return results

  except:
    return []
