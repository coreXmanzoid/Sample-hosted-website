# Sample Deployable Flask App

A basic Flask application ready for deployment.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser

## Deployment

### Heroku
```bash
heroku create
git push heroku main
heroku open
```

### Render
1. Connect your GitHub repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

### Railway
1. Connect your GitHub repository to Railway
2. Add a Python service
3. Deploy# Sample-hosted-website
