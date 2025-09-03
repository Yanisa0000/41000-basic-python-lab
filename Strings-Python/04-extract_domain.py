data = 'babababababanaaaaa@prc.ac.th vonguvogioehgihdsioghws'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)