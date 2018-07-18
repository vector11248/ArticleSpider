import hashlib

def get_md5(url):

    #在py3中已经没有unicode关键字了,所有的str编码都是unicode,
    #所以，如果是unicode,就编码utf-8的格式
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    #生成摘要
    return m.hexdigest()

if __name__=="__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))