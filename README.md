# SriLankan-singers
Search engine for a small database of singers in Sri Lanka using Sinhala.
This search engine contains 127 of famous singers in Sri Lanka.
Elasticsearch library is used for the search engine.
## Data fields in the corpus:
* *Name
* *Birth Date
* *City
* Biography
* Lyrics of a song
* Songs
* email

I added new indexing through BulkAPI to the Elasticsearch by the help of the Postman.
Removed stop words from queries. 
Consisted of the similar words.

## Query examples:
### By entering the name of the singer - 
Ex: - රෝහණ වීරසිංහ
### By entering the city -
Ex: - මාතර
### By entering some part of a lyrics
Ex: - තනි වෙන්නට මගේ ලොවේ පුරුදු පාළුවෙන්

# Set up the program
## Clone the repository
## Run Elasticsearch
## Create indexing by running bulkdata.py
## Run the index.html in UI 
## Search info. about singers in Sri Lanka in Sinhala
