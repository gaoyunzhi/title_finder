#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import title_finder
from title_finder import export, _formaturl, exportAllInText, getTitle
import os
import sys
from bs4 import BeautifulSoup
from telegram.ext import Updater
import album_sender

with open('bot_token') as f:
	bot_token = f.read().strip()
tele = Updater(bot_token, use_context=True)
chat = tele.bot.get_chat(420074357)

urls = [
	'https://mp.weixin.qq.com/s/Yc_X8jclGVTOMW2eK1ibDQ',
]

s = '''
'''

def testExportAllInText():
	soup = BeautifulSoup(s, features="lxml")
	print(exportAllInText(soup))

def testExport():
	for url in urls:
		print(title_finder.getTitle(url))
		# print('原文：', url)
		# r = title_finder.export(url, True, True, True)
		# print('导出：', r)
		# os.system('open ' + _formaturl(r) + ' -g')
		# print('')

def test():
	testExport()
	# testExportAllInText()

def testAlbum():
	album = title_finder.getAlbum(urls[0])
	print(album)
	album_sender.send_v2(chat, album)

if __name__=='__main__':
	testAlbum()