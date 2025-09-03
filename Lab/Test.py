word = 'BB banana'

if word == 'banana':
    print ('All right,banana')


if word < 'banana':
    print ('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print ('Your word,' + word + ', comes after banana.')
else:
    print ('All right,banana')    

data = 'babababababababnaaaaa@nana.ac.th nndlbhrspjisjig'
atpos = data.find('@')
print(atpos)
sppos = data.find('',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

