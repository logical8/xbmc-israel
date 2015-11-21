# -*- coding: utf-8 -*-
import urllib, urllib2, sys, re, xbmcplugin, xbmcgui, xbmcaddon, xbmc, os, json,random
import repoCheck

ADDON = xbmcaddon.Addon(id='plugin.video.israelsports')
libDir = os.path.join(ADDON.getAddonInfo("path").decode("utf-8"), 'resources')
sys.path.insert(0, libDir)

def update_view(url):

    ok=True        
    xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
    return ok

def CATEGORIES():
	repoCheck.UpdateRepo()
	repoCheck.UpdateRepo('http://abeksis.com/repo/repository.abeksis/repository.abeksis.zip','repository.p2p-streams.xbmc')
	repoCheck.UpdateRepo('http://abeksis.com/repo/plugin.video.SportsDevil/plugin.video.SportsDevil-2015.11.14.zip','plugin.video.SportsDevil')
	
	addDir('SPORTS DEVIL  *LIVE*','plugin://plugin.video.SportsDevil/?item=title%3dLive%2bSports%26url%3dlivesports.cfg%26definedIn%3dmainMenu.cfg%26director%3dSportsDevil%26genre%3dLive%2bSports%26type%3drss&mode=1 ',1,'http://xbmc-development-with-passion.googlecode.com/svn/branches/repo/plugin.video.SportsDevil/icon.png','')
	addDir('כל הסרטונים','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=147&page=',2,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTvo6GmRkhBMgJHX0DiWtikRpet97rNyCTsSi_OdsdF7Dp4K-96','1')
	addDir('     ,תקצירים    ליגת האלופות','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5813&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRf7mZyApMKwnQyHcJ5shoFE8OhLOlbmUIhytkWAP05suAGv9h8xA','1')
	addDir('  ליגת האלופות כתבות','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5935&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRf7mZyApMKwnQyHcJ5shoFE8OhLOlbmUIhytkWAP05suAGv9h8xA','1')

	addDir('ליגת העל בכדורגל','www.stam.com',6,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRpi-QusXtg3bBYigUFBxDmVj-nbBuPqJsGhWybwI8zx1Rlh2mw','')
	addDir('One-  ליגת העל','stam',9,'http://www.isramedia.net/images/tvshowpic/Ligat_winner.png','1')
	addDir('ליגה איטלקית','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5808&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ5MZPuGkXGn4XoaDo72fi0gKIOik_0GVZHgHXmkQ1avptCA4WS','1')
	addDir('ליגה אנגלית','http://svc.one.co.il/Cat/Video/?c=85&p=',4,'http://www.bettingexpert.com/deprecated/assets/images/blog/PremLeagueBettingAwards/premier-league-logo.jpg','1')
	addDir('EUROLEAGUE','http://svc.one.co.il/Cat/Video/?c=77&p=',4,'http://www.isramedia.net/images/tvshowpic/euroleague.jpg','1')
	addDir('בית"ר נורדיה ירושלים','open',14,'http://www.headstart.co.il/components/img.aspx?img=images%5C2(25).jpg','1')
	addDir('NBA','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5959&page=',2,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTMaYyCKAudTxqAh0YUsGGbL5axGDZV5YT-wL1-dYK25VfNNTzhKg','1')
	addDir('כדורסל ישראלי','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5845&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcROtyknPHO9KMMRBxTivXvWDngNdMzr5Mf5VMyJLyPEx_WEpxtk','1')
	addDir('כדורסל   נשים ישראלי','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=4979&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcROtyknPHO9KMMRBxTivXvWDngNdMzr5Mf5VMyJLyPEx_WEpxtk','1')
	addDir('חדשות הספורט','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=3968&page=',2,'http://www.nrg.co.il/images/archive/300x225/631/730.jpg','1')
	addDir('יציע העיתונות','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=5811&page=',2,'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRVDQaVdqH65g5IqYdUf1zqt_FMHSOsbJPYzLI6tC1lxyh_FS97','1')
	addDir('בובה של לילה 3','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=3473&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRjTjLnpK8ye6aN68h5HgcPo08Xtr1KJZd9iRSRQ3GlU9zB0pPViQ','1')
	addDir('בובה של לילה 2','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=3186&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRjTjLnpK8ye6aN68h5HgcPo08Xtr1KJZd9iRSRQ3GlU9zB0pPViQ','1')
	addDir('בובה של לילה 1','http://vod.sport5.co.il/Ajax/GetVideos.aspx?Type=B&Vc=3185&page=',2,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRjTjLnpK8ye6aN68h5HgcPo08Xtr1KJZd9iRSRQ3GlU9zB0pPViQ','1')


	xbmc.executebuiltin('Container.SetViewMode(500)')

	
def setupP2P():
	all_modules = [ 'http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/arenavision.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/livefootballvideo.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/livefootballws.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/onetorrenttv.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/rojadirecta.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/sopcastucoz.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/torrenttvruall.tar.gz','http://parsersforp2pstreams.googlecode.com/svn/trunk/%20parsersforp2pstreams/torrenttvrusports.tar.gz']

	for parser in all_modules:
		xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
		xbmc.sleep(1000)
		

	
def list_videos(url,page):
	url1=url+"1"
	url=url+str(page)
	link=OPEN_URL(url1)
	total=re.compile('total-pages="(.*?)"').findall(link)
	if total:
		total=int(total[0])
	else:
		total=1
   
	page=int(page)
	if page <= total:
		link=OPEN_URL(url)
		matches=re.compile('<li id.*?<a href="(.*?)"><img src="(.*?)" title="(.*?)"').findall(link)
		for  newurl ,image , title  in matches :
			title=title.decode('iso-8859-8').encode('utf-8')
			title=unescape(title)
			addDir(title,newurl,3,image,'')
		index=url.find('page=')
		url=url[0:index]
		page=page+ 1
		url=url+"page="
		list_videos(url,page)
	setView('movies', 'default')
		
def play_video(url,name,iconimage):	  
	link=OPEN_URL(url)
	clipid=re.compile('clipid=(.*?)&Width',re.M+re.I+re.S).findall(link)
	secondurl = "http://sport5-metadata-rr-d.nsacdn.com/vod/vod/" + str(clipid[0]) +"/HLS/metadata.xml?smil_profile=default"
	
	if  not ('delivery' in clipid[0]) :
		link=OPEN_URL(secondurl)
		highres=re.compile('http://s5-s.nsacdn.com/sport5_vod/(.*?)</FileURL>',re.M+re.I+re.S).findall(link)
		ip=re.compile('<Server priority=.*?>(.*?)<',re.M+re.I+re.S).findall(link)
		random.seed()
		ip=ip[random.randint(0, len(ip)-1)]
		direct=  "http://"+ip+"/sport5_vod/" + str (highres[-1])
	else:
		direct='http://sport5-vh.akamaihd.net/i/video/'+clipid[0]+'.csmil/master.m3u8'
	playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist.clear()
	liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title":name} )
	liz.setPath(direct)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
			  
def ligat_al():
	link = OPEN_URL('http://svc.one.co.il/Cat/Video/Reviews.aspx?c=28')
	#<a href="/Cat/Video/Reviews.aspx?tm=1"><img style="border:0;width:46px;height:49px;" src="http://images.one.co.il/Images/Teams/Logos_46x49/1.png" alt="הפועל חיפה" /></a>"
	list1=re.compile('<a href="(.*?)".*?src="http://images.one.co.il/Images/Teams/Logos(.*?)" alt="(.*?)" /></a>').findall(link)
	for url, image, name in list1:
		name=name.decode('iso-8859-8').encode('utf-8')
		name=unescape(name)
		url='http://svc.one.co.il'+url
		image='http://images.one.co.il/Images/Teams/Logos'+image
		addDir(name,url,4,image,'al')
	setView('movies', 'default')

def one_videopage(url,description):
	if description!='al' :
		murl=url+str(description)
	else:
		murl=url
					
	link = OPEN_URL(murl)
	list1=re.compile('"Image": "(.*?)".*?"Title": "(.*?)".*?"HQ":"(.*?)".*?"ID":(.*?)}').findall(link)
	#var page = 4;var pages = 8;
	page_total=re.compile('var page = (.*?);.*?var pages = (.*?);').findall(link)[0]
	current= page_total[0]
	total= page_total[1]
	current=int(current)
	total =int (total)
	
	for image,name,hq,Id in list1:
		image="http://images.one.co.il/images/video/segment377x285/"+image
		name=unescape(name)
		name=name.decode('windows-1255').encode('utf-8')
		addDir(name,str(Id),5,image,hq)
	if current < total :
		current+=1
		addDir("[COLOR yellow]לעמוד הבא[/COLOR]",url,4,'',str(current))
	addDir("[COLOR blue]חזרה לראשי [/COLOR]",'',None,'','')

	setView('movies', 'default')

def YoutubeUser(username):
	xbmc.executebuiltin('XBMC.Container.Update(plugin://plugin.video.youtube/user/{0}/)'.format(username))
	
def play_one(name,url,iconimage,description):
	url1="http://svc.one.co.il/cat/video/playlisthls.aspx?id="+url
	link = OPEN_URL(url1)
	regex='playlist(.*?)" label="(.*?)"'
	direct=re.compile(regex).findall(link)
	playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist.clear()
	liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title":name} )
	
	for item in direct:
			if description=='True':
				if item[1].find("HD")>0 :
					link="http://playlist"+str(item[0])
					liz.setPath(link)
					xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
			else:
				addLink(name,"http://playlist"+str(item[0]),iconimage,'')

def OPEN_URL(url,host=None):
	print url
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	if host:
			req.add_header('HOST',host)
	response = urllib2.urlopen(req,timeout=180)
	link=response.read()
	response.close()
	return link
	
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
						
	return param

def unescape(text):
	try:			
		rep = {"&nbsp;": " ",
			  "\n": "",
			  "\t": "",
			  "\r":"",
			  "&#39;":"",
			  "&quot;":"\""
			  }
		for s, r in rep.items():
			text = text.replace(s, r)
			
		# remove html comments
		text = re.sub(r"<!--.+?-->", "", text)	
			
	except TypeError:
		pass

	return text

def addDir(name,url,mode,iconimage,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
	if mode==1:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
	elif mode==3 or mode==5 or mode==9 or mode==14:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	
#same as above but this is addlink this is where you pass your playable content so you dont use addDir you use addLink "url" is always the playable content		
def addLink(name,url,iconimage,description):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
	liz.setProperty("IsPlayable","true")
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
	return ok 

#below tells plugin about the views				
def setView(content, viewType):
	# set content type so library shows more views and info
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
		xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type


params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:		
	mode=int(params["mode"])
except:
		pass
try:		
	description=urllib.unquote_plus(params["description"])
except:
	pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
		
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
	CATEGORIES()
elif mode==1:
	update_view(url)
elif mode==2:
	list_videos(url,description)
elif mode==3:
	play_video(url,name,iconimage)
elif mode==4:
	one_videopage(url,description)
elif mode==5:
	play_one(name,url,iconimage,description)
elif mode==6:
	ligat_al()
elif mode==8:
	LIVE()
elif mode==9:
	YoutubeUser('one')
elif mode==14:
	xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/?action=play_video&videoid=L2928xxYc7c)')
xbmcplugin.endOfDirectory(int(sys.argv[1]))

