from bs4 import BeautifulSoup

def confirmProperDiv(div):
    if len(div['class']) > 1:
        return False
    if div['class'][0] != 'body':
        return False
    return True

def parseDiv(div):
    return


filename = "messages.html"
f = open(filename, "r")
index = f.read()

print(index)
print()
print()

soup = BeautifulSoup(index, 'html.parser')
divs = soup.find_all('div', class_="body")

divs = list(filter(confirmProperDiv, divs))

print(len(divs))
print(divs[0])
print()
name = divs[0].find('div', class_='from_name')
print(name.contents[0].strip())
message = divs[0].find('div', class_='text')
print(message.contents[0].strip())
exit()

for idx in range(0, 10):
    print('div:', divs[idx])
    print('div-class:', divs[idx]['class'])
    print('div-contents:', divs[idx].contents)
    print('is class im lookingfor:', confirmProperDiv(divs[idx]))
    print('\n\n\n')


#hello()
