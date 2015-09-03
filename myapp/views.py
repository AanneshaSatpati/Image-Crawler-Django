# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import re
import time
import mechanize
import urlparse
import sys

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import redirect

def home(request):
    test = ['a', 'b', 'c']
    with open('imageUrls.txt', 'r') as fin:
        urls = fin.read().split('\n')
    print urls
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'test': urls})
    return render_to_response('myapp/home.html',context_instance=context)

def make_soup(url):
    try:
        #html = urllib.urlopen(url
        html = urlopen(url).read()
        return BeautifulSoup(html,'html.parser')
    except:
        print("no images in this url")
 
def get_images(url):

    try:
        imageUrls= open("imageUrls.txt","a")
        soup = make_soup(url)

        #this makes a list of bs4 element tags
        images = [img for img in soup.findAll('img')]
        print (str(len(images)) + "images found in:\n" + str(url))
        print ('Downloading images url to txt file.')
        #compile our unicode list of image links
        image_links = [each.get('src') for each in images]
        for link in image_links:
            imageUrls.write(str(link)+"\n")
        imageUrls.close()
        return image_links  
    except:
        print("no images in this url")

def scrapeStep(root):
    br = mechanize.Browser()
    result_urls = []
    for url in root:
        try:
            br.open(url)
            for link in br.links():
                newurl = urlparse.urljoin(link.base_url,link.url)
                #print (newurl+ "\n")

                result_urls.append(newurl)
                        
        except:
            print "error"

    return result_urls

def uinput(request):
    if request.GET.get('url'):
        url = request.GET.get('url')
        level = int(request.GET.get('depth'))
        # print name
        imageUrls = open("imageUrls.txt","w+")
        imageUrls.write("")
        imageUrls.close()

        urls= [url,]
        visited = [urls]
        br = mechanize.Browser()
        counter = 0

        while counter < level:
            for i in urls:
                 get_images(i)
            step_url = scrapeStep(urls)
            urls=[]
            for u in step_url:
                if u not in visited:
                    #print(u + "\n")
                     
                    urls.append(u)
                    visited.append(u)
            counter+=1
            
        return redirect('myapp.views.home')
    return render_to_response('myapp/uinput.html')