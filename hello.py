import speechd

client = speechd.SSIPClient("orca123")


languages = []
for item in client.list_synthesis_voices():
    if(item[1] not in languages):
        languages.append(item[1])

# Printing all the languages 
print(languages)

# Closing the SSIP connection
client.close()

print("Hai how are you? How is my new branch ?")
