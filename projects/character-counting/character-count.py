# using setdefault()
import pprint
message = "The quick brown fox jumped over the lazy dogs. So I wondered, how could the brown fox jump over the lazy dog. This was clearly just a folk tale formulated to contain all the letters of the alphabet"

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)