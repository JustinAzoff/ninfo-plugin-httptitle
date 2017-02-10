from BeautifulSoup import BeautifulSoup
from ninfo import PluginBase
import requests

class httptitle_plug(PluginBase):
    """"""
    name          = 'httptitle'
    title         = 'Httptitle'
    description   = 'Fetch HTTP Titles'
    cache_timeout = 60*60
    types         = ['hostport', 'url']
    #local        = False
    remote       = False

    def setup(self):
        pass

    def get_title_from_url(self, url):
        resp = requests.get(url, verify=False, timeout=2)
        return BeautifulSoup(resp.content).title.string

    def get_title(self, arg):
        if arg.startswith('http'):
            return self.get_title_from_url(arg)

        schemes = 'http', 'https'
        if arg.endswith('443'): #443 or 8443
            schemes = 'https', 'http'

        for scheme in schemes:
            try :
                title = self.get_title_from_url("{0}://{1}".format(scheme, arg))
                return title
            except Exception, e:
                pass

    def get_info(self, arg):
        result = {}
        title = self.get_title(arg)
        if title:
            result['title'] = title.strip()
        return result
            

plugin_class = httptitle_plug
