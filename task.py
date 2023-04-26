#Task 2

text= '/content/news.txt'
f = open(text, 'r')
final = f.read()

x = [i for i in final]
x.reverse()
x
"".join(x)

#Task 2

text= '/content/news.txt'
f = open(text, 'r')
final = f.read()

def rev_all(x):
  return x[::-1]

if __name__ == '__main__':
  print(rev_all(final))


#Task 3

text= '/content/news.txt'
f = open(text, 'r')
final = f.read()
final[::-1]


#TASK 3

text= '/content/news.txt'
f = open(text, 'r')
final = f.read()
dev = final.split('(.)')
dev

def rev(x):
  print(dev[x][::-1])

for index, c in enumerate(dev):
  if index <= len(dev):
    print(rev(index))


#Task 4

text= '/content/news.txt'
f = open(text, 'r')
final = f.read()
dev = final.split(' ')
dev

def rev(x):
  print(dev[x][::-1])

newrev= [rev(index) for index in dev]
for index, c in enumerate(dev):
      str(rev(index))
