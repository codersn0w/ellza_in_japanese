# coding: utf-8
from engines.random_ua import generate_ua
from engines.google_xpath import gsearch
from engines.bnews_xpath import bnsearch
from engines.gimage_xpath import gisearch
from engines.chatbot_engine import make_reply
import re
def generate_reply(query):
    if len(query) > 70:
      query = query[:70]
    if query == 'help:':
       results = [{
                   'title':'Ellpedia Chat',
                   'help': '[ Ver.1.0 beta  ©2018 Ellpedia ]<br>'\
                   'Ellpedia ChatはWeb検索サイト<a href="https://www.ellpedia.com" target="_blank">Ellpedia.com</a>のチャット版です。<br>'\
                   '標準ではWeb検索モードになっています。<br>オプションとして、<br>'\
                   '・Wikipediaを検索する際は「w:」<br>・ニュースを検索する際は「n:」<br>'\
                   '・画像を検索する際は「i:」<br>・YouTubeを検索する際は「y:」<br>'\
                   '・Ellza (Bot) と会話する際は「b:」<br>を検索ワードの先頭に入れてください。<br>'\
                   '[<a href="https://blog.ellpedia.com/term_and_privacy_policy/" target="_blank">規約・プライバシーポリシー</a>]<br>'\
                   '[<a href="https://github.com/thunderra1n/ellza_in_japanese" target="_blank">ソースコード</a>]',
       }]
       return results

    elif re.match('w:', query):
      query = query.lstrip('w:')
      query = 'site:wikipedia.org ' + query
      ua = generate_ua()
      ggl = gsearch(query, ua)
      results = ggl[0] + [{}]
      return results

    elif re.match('n:', query):
      query = query.lstrip('n:')
      ua = generate_ua()
      results = bnsearch(query, ua)
      return results

    elif re.match('i:', query):
      query = query.lstrip('i:')
      ua = generate_ua()
      results = gisearch(query, ua)
      return results

    elif re.match('y:', query):
      query = query.lstrip('y:')
      query = 'site:youtube.com ' + query
      ua = generate_ua()
      ggl = gsearch(query, ua)
      results = [{}] + ggl[1]
      return results

    elif re.match('b:', query):
      query = query.lstrip('b:')
      results = make_reply(query)
      return results

    else:
      ua = generate_ua()
      ggl = gsearch(query, ua)
      results = ggl[0] + ggl[1]
      return results
