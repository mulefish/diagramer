
# diagramer
TODO: everything
# setup
0: 
1: python3 -m venv env 
2:  source env/bin/activate ( MacOS )
3: pip3 install -r requirements.txt  
4: make kittycat.py script
5: uvicorn kittcat:app --reload  
6: browser: http://localhost:8000/

# Some curls
A: curl1 - a simple get
curl --location --request GET 'localhost:8000'
B: curl2 - a post with a particular json pay load
curl --location --request POST 'localhost:8000/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}'


# requirements.txt follow 
asyncpg==0.20.1
databases[postgresql]==0.2.6
fastapi==0.48.0
SQLAlchemy==1.3.13
uvicorn==0.11.2
httpx==0.11.1