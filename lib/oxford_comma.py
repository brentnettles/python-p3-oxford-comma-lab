def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


items = ['guitar', "bass", "drums", "sax", "bongos"]

oxford_comma(items)
print(len(items))
print(items[0:3])