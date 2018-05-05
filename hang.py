#coding:utf8
#qpy:3
#qpy:console

print("This is console module")
import sl4a
text = input("Text: ")
def pesan(t):
    droid = sl4a.Android()
    p = "\u200e\u200f" * 1000
    droid.setClipboard(t.replace(" "," "+p))
pesan(text)
