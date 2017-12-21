with open('files/write.txt','w') as fp:
    fp.write('lorem ipsum is some filler test')

# Now if we again perform the same operation withb the same file mode

quotes = ['\n I can resist everything if there is no ned ot more fuller',
'\n More give fucking awesome coders in World',
'\n Mercedez is one of my favorite car in India'
]

with open('files/write.txt','a') as fp:
    for quote in quotes:
        fp.write(quote)