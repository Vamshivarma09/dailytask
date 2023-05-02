txt = "lorem ipsum dolor sit amet"
txtToList = (txt.split())
arr = []

for i in range(0,len(txtToList)):
    txtToList[i] = txtToList[i].capitalize()
    arr.append(txtToList[i])
    a = (" ".join(map(str,txtToList)))
print(a)