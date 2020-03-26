from furl import furl
f = furl('http://www.google.com/?one=1&two=2')
for args in (f.args):
  print(args)

del f.args['two']
f.args['three'] = 'ooo'
print(f.url)