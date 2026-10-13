a = "/cat/dog/hog/log"
a = a[::-1]

a = a[0:a.index("/")]
a = a[::-1]
print(a)
