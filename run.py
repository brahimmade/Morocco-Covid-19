import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin, urlparse



def is_valid(url):
    """ Checks whether 'url' is a valid URL. """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_reports_url(url_1,url_2, headers=None):
    """ Returns all reports URLs on a single 'url' """
    if headers == None:
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    else:
        header = headers
        
    url = urljoin(url_1, url_2)
    # initialize the session
    session = HTMLSession()
    # make the HTTP request and retrieve response
    response = session.get(url, headers=header)
    # execute Javascript with a timeout of 20 seconds
    # response.html.render(timeout=20)   ## pyppeteer.errors.TimeoutError: Navigation Timeout Exceeded: 20000 ms exceeded.
    # construct the soup parser
    soup = BeautifulSoup(response.html.html, "html.parser")
    
    urls  = []
    table =  soup.find("table", class_="ms-rteTable-5")
    
    for report, name in zip(table.find_all("td", class_="ms-rteTableEvenCol-5"), table.find_all("td", class_="ms-rteTableOddCol-5")) :
        report_url = report.find("a").attrs.get("href")
        name       = ((''.join(name.text.split())).replace("/", "-")).replace(" ", "").replace("\u200b", "") 
        if not report_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        report_url = urljoin(url_1, report_url)
        try:
            pos = report_url.index("?")
            report_url = report_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(report_url):
            urls.append({'url':report_url, 'name':name})
    
    # close the session to end browser process
    session.close()
    # print total images found in URL
    print(f"Total {len(urls)} Reports Found!")
    return urls 
    
def download(url, pathname, headers=None,):
    """ Downloads a file given an URL and puts it in the folder 'pathname' """
    if headers == None:
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    else:
        header = headers
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url['url'], headers=header, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname,f"{url['name']}.{url['url'].split('.')[-1]}")
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
            
def get_all_reports(url_1,url_2, path):
    if not path:
        # if path isn't specified, use the domain name of that url as the folder name
        path = urlparse(urljoin(url_1, url_2)).netloc
    # get all reports
    reports = get_all_reports_url(url_1,url_2)
    # for each report, download it
    for report in reports:
        download(report, path)


# Test
if __name__ == '__main__' :
    base_URL    = "http://www.covidmaroc.ma"
    reports_URL = "/Pages/LESINFOAR.aspx"
    get_all_reports(base_URL, reports_URL, path='data')