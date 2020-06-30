from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

num_returned = num_stop = 10

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
def null_func(stock_url):
	return None

def scrapable(url_to_check):
	#print("SCRAPABLE: Checking "+url_to_check) 
	req = Request(url=url_to_check, headers=headers)
	readable = False
	try:
		html = urlopen(req).read()
		readable = True
		#print("\tStock is Good to Go Boss")
	except:
		print("\tCannot Scrape "+url_to_check)
	return readable

def search_google(search_query, num_to_search, key_phrase):
	found_url = None
	print("\tSearching |"+search_query+"| for |"+key_phrase+"|") 
	for result in search(search_query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = num_to_search,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = num_to_search,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
		print("\t\t--> "+result)
		if result.find(key_phrase) != -1 and scrapable(result):
			found_url = result
			break
	return found_url
	
def analyze_raw_links(stock_url):
	req = Request(url=stock_url, headers=headers) 
	html = urlopen(req).read() 

	soup = BeautifulSoup(html, 'html.parser')
	
	for link in soup.find_all('a'):
		link_txt = link.get('href')
		print(link_txt)

def get_link_text(stock_url):
	links = []

	req = Request(url=stock_url, headers=headers) 
	html = urlopen(req).read() 

	soup = BeautifulSoup(html, 'html.parser')
	
	for link in soup.find_all('a'):
		link_txt = link.get('href')
		if link_txt is not(None):
			links.append(link_txt)
		
	return links

def clean_link_list(article_list):
	
	#Remove duplicate Entries
	article_list = list(dict.fromkeys(article_list))
	
	#Make sure articles are scrapable and remove ones that are not
	new_article_list = []
	for article in article_list:
		if article.find('.') != -1:
			#Valid URL
			if get_source(article) != "seekingalpha":
				#Seeking alpha always gets blocked
				if scrapable(article):
					new_article_list.append(article)

	return new_article_list

def get_source(link_url):
	start_pos = link_url.find('://')+3
	end_pos = link_url.find('.com')
	
	if end_pos == -1:
		print(link_url+" ENDED WITH SOMETHING OTHER THAN .COM -> Returning Misc")
		return "Misc"
	
	name = link_url[start_pos:end_pos]
	if name.find('www.') != -1:
		name = name.split('www.')[1]

	return name

def get_motley_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if link_txt.find('/investing/20') != -1 and link_txt.find('/investing/2019/02/13/etfs-or-mutual') == -1 and link_txt.find('/investing/2018/07/26/how-to-build') == -1 and link_txt.find('fool.com') == -1:

			article_link = "https://www.fool.com"+link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles



def get_market_watch_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if (link_txt.find('/articles/') != -1 or link_txt.find('/story/') != -1) and True:# link_txt.find('wsj.com') == -1:
			#if you get rid of wsj constraint, wall street journal articles can also be accessed here
			article_link = link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles



def get_cnbc_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if (link_txt.find('/2020/') != -1 or link_txt.find('/2019/') != -1) and link_txt.find('cnbc.') != -1:
			article_link = link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles

def get_cnbc_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if (link_txt.find('/2020/') != -1 or link_txt.find('/2019/') != -1) and link_txt.find('cnbc.') != -1:
			article_link = link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles

def get_business_insider_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if link_txt.find('/news/stocks/') != -1:
			article_link = link_txt
			if link_txt.find('.com') == -1:
				article_link = "https://markets.businessinsider.com"+link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles

def get_wsj_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if link_txt.find('wsj.com/articles/') != -1 and link_txt.find('wsj.com/articles/PR') == -1 and link_txt.find('about-the-newsroom') == -1:
			article_link = link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles

def get_market_beat_articles(stock_url):
	news_articles = []

	for link_txt in get_link_text(stock_url):
		if (link_txt.find('/article/') != -1 or link_txt.find('/news/') != -1 or link_txt.find('/story/') != -1 or link_txt.find('finance.yahoo.com') != -1):
			article_link = link_txt
			news_articles.append(article_link)
	
	news_articles = clean_link_list(news_articles)

	return news_articles

def get_all_articles(base_search, key_phrase, article_functions):
	compiled_articles = []
	
	for i in range(1,len(base_search)):
		print("Checking for articles from "+base_search[i])
		query = base_search[i] + stock
		url = search_google(query, 10, key_phrase[i])

		if url is not(None):
			print("\tScraping "+url)

			temp_articles = article_functions[i](url)
			print("\tGot %d Articles!"%(len(temp_articles)))

			for article in temp_articles:
				compiled_articles.append(article)
		else:
			print('\tURL NOT FOUND')
	
	
	#Remove Duplicates between separate websites
	compiled_articles = list(dict.fromkeys(compiled_articles))
	
	print("Organizing List based on Source")
	organized_list = {}
	for article in compiled_articles:
		source_name = get_source(article)
		if source_name in organized_list.keys():
			#Source Exists already, append to list
			organized_list[source_name].append(article)
		else:
			#New Source, make a new key with a list started
			organized_list[source_name] = [article]

	#Lump keys with a single entry into Misc
	print("Reorganzing Single Elements to Misc")
	keys_to_delete = []
	misc_articles = []
	for key in organized_list.keys():
		if len(organized_list[key]) == 1:
			article = organized_list[key][0]
			misc_articles.append(article)
			keys_to_delete.append(key)
	
	for key in keys_to_delete:
		del organized_list[key]
	
	if "Misc" in organized_list.keys():
		for article in misc_articles:
			organized_list['Misc'].append(article)
	else:
		organized_list['Misc'] = misc_articles
	
	print("Organized List")
	for key in organized_list.keys():
		print("\n=============================================== Source: "+key+" ====================================================")
		article_list = organized_list[key]
		for article in article_list:
			print('\t'+article)

	print("\n%d Unique Articles found"%(len(compiled_articles)), end=" ")
	print("from %d Unique Sources\n"%(len(organized_list.keys())))

	return organized_list
		 


source_ind = -1
base = [
	"All",
	"Motley Fool ", 
	"Market Watch ", 
	"CNBC ", 
	"Market BusinessInsider News ",
	"WSJ ",
	"MarketBeat News "
	]

key_phrase = [
	"Please Don't Search This",
	"/quote/", 
	"/investing/stock/",
	"/quotes/", 
	"/news/",
	"/quotes/",
	"/news/"
	]

article_func = [
		null_func,
		get_motley_articles, 
		get_market_watch_articles,
		get_cnbc_articles,
		get_business_insider_articles,
		get_wsj_articles,
		get_market_beat_articles
		]

while (True):
	source_ind = -1
	print("Please Enter Number of source you would like to Scrape")
	for i,source in enumerate(base):
		print("\t%d. "%(i)+source)
	print('')
	source_ind = input("Source Number: ")
	try:
		source_ind = int(source_ind)
	except:
		print("Invalid Answer: Need a number")
		source_ind = -1
		continue
	
	if not(source_ind >= -1 and source_ind < len(base)):
		print("A NUMBER BETWEEN 0 and %d PLEASE"%(len(base)-1))
		continue

	while (source_ind > -1):
		articles = []

		print("\nAccessing news from "+base[source_ind])
		
		stock = input("Enter Stock: ")

		if source_ind == 0:
			all_articles = get_all_articles(base, key_phrase, article_func)
		
		else:
			if stock == "change":
				break
			query = base[source_ind] + stock
			url = search_google(query, 10, key_phrase[source_ind])

			if url is not(None):
				print("Here's the url :)")
				print("\t"+url)
				
				#analyze_raw_links(url)
				
				#articles = article_func[source_ind](url)
				
				print("Here's the scrapable articles")
				for article in articles:
					print('\t'+article)
				
			else:
				print("No Url boss :(")
		
