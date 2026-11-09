"""Writes new_meta.json (title, description, tags) from the YouTube SEO bot's text and
ASSERTS there is no em/en dash anywhere. Check lengths: title <= 100, tags total <= 500."""
import json
t="Did the Hanging Gardens of Babylon Ever Exist? 🌿"
d="""Were the Hanging Gardens of Babylon real, or just a legend? One of the Seven Wonders of the Ancient World has never been found.

Greek writers described terraced gardens built by King Nebuchadnezzar II for his homesick queen Amytis, watered from the Euphrates. But no Babylonian text mentions them, and excavations at Babylon have found no clear trace.

Some historians, like Stephanie Dalley, argue the gardens were really in Nineveh, built by the Assyrian king Sennacherib. Others think they were pure legend.

What do you think? Comment below and subscribe for more ancient mysteries.

#hanginggardens #babylon #sevenwonders"""
tags=["hanging gardens of babylon","hanging gardens","babylon","nebuchadnezzar ii","nineveh","sennacherib","seven wonders of the ancient world","ancient wonders","mesopotamia","ancient mysteries","lost wonders","archaeology","ancient history","history facts"]
assert '—' not in d and '–' not in d
print(len(t),len(d),len(",".join(tags)),len(tags))
json.dump({"title":t,"description":d,"tags":tags},open("new_meta.json","w"),ensure_ascii=False)
