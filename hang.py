#coding:utf8
#qpy:3
#qpy:console
import sys
import sl4a
reload(sys)
sys.setdefaultencoding('utf-8')
text = input("Text: ")
def pesan(t):
    droid = sl4a.Android()
    p = "\u200e\u200f" * 1000
    droid.setClipboard(t.replace(" "," "+p))
if __name__ == "__main__":
    pesan(text)
