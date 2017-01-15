from tempfile import TemporaryFile,NamedTemporaryFile
f = TemporaryFile()
f.write('abcds'*100000)
f.seek(0)
print f.read(100)
############################
ntf = NamedTemporaryFile(delete=False)
print ntf.name