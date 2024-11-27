# gStream Documents

## Docker
Run this in Docker using docker-compose, e.g., 

```
AWS_ACCESS_KEY_ID=your_access_key_id \
AWS_SECRET_ACCESS_KEY=your_secret_access_key \
AWS_DEFAULT_REGION=your_default_region \
GDOC_ENV=prod \
docker-compose up -d
```

Then navigate to http://localhost to see the app

## Local
Or run the individual components (Nuxt and FastAPI) via two terminals:

### Nuxt (requires Node 18+)
1. `cd client`
2. `npm install`
3. `NUXT_PUBLIC_API_BASE=http://0.0.0.0:8000 npm run dev`

### FastAPI 
1. `cd server` 
2. `python -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `GDOC_ENV="prod" uvicorn api:app --host 0.0.0.0 --port 8000`

And you can see this operating on http://0.0.0.0:3000 (front-end) or http://0.0.0.0:8000 (back-end)