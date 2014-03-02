expHashtag="#\w+" #Expresion regular hashtag
expUsur="@\w+"    #Expresion regular usuario


def buscaUser(listTwit):
	listUsu=[]
	for i in range (len(listTwit)):
		if re.match(expUsur,listTwit[i]):
			listUsu.append(listTwit[i])
	return listUsu

def buscaHashtag(listTwit):
	listHash=[]
	for i in range (len(listTwit)):
		if re.match(expHashtag,listTwit[i]):
			listHash.append(listTwit[i])
	return listHash
