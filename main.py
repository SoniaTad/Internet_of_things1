import morse 

if __name__ == "__main__":
    e = morse.encode('us')
    print('%s' % e)
    d = morse.decode(str(e))
    #testing the encode and decode functions 
    assert morse.encode('us') == '..- ... ', "Should be ..-"
    assert morse.decode('..- ...') == 'US', "Should be ..-"