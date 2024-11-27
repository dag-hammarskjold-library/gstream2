# gStream Documents

Run this in Docker using docker-compose, e.g., 

`AWS_ACCESS_KEY_ID=your_access_key_id AWS_SECRET_ACCESS_KEY=your_secret_access_key AWS_DEFAULT_REGION=your_default_region GDOC_ENV=prod docker-compose up -d`

Then navigate to http://localhost to see the app

Or run the individual components (Nuxt and FastAPI)

1. `NUXT_PUBLIC_API_BASE=http://0.0.0.0:8000 npm run dev`
2. `GDOC_ENV="prod" uvicorn api:app --host 0.0.0.0 --port 8000`

And you can see this operating on http://0.0.0.0:3000