import random
class Codec:
    def __init__(self):
        self.db = {}
    def getRandom(self):
        a = ""
        while a=="" or a in self.db:
            a=""
            for i in range(5):
                a+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        return a

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        r = self.getRandom()
        self.db[r] = longUrl
        return "http://shorturl.com/"+r
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        r = shortUrl.split("/")[-1]
        return self.db[r]        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))