# Substack Feed Proxy

This is a tiny Flask application that exposes a single endpoint for proxying
the RSS feed from [natesnewsletter.substack.com](https://natesnewsletter.substack.com/).
The app was originally created to provide an easy way to access this feed with
a consistent `User-Agent` header and proper XML content type.

## Current State

The project consists of a single `app.py` file containing the Flask app, a
`Procfile` for deploying with a process manager such as Heroku, and a
`requirements.txt` listing the Python dependencies.

The latest commit improves encoding handling by returning `r.text` and ensuring
responses are served with the `application/xml; charset=utf-8` content type.

## Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The dependencies are:

- **Flask** – the web framework used to create the application
- **Requests** – used to fetch the Substack RSS feed
- **Gunicorn** – optional production server referenced in the `Procfile`

## Running Locally

```bash
python app.py
```

The app listens on port `8080` and exposes a single route at `/proxy`. When you
access `http://localhost:8080/proxy`, the service fetches the Substack RSS feed
and returns it directly.

For production deployments you can run it via gunicorn:

```bash
gunicorn app:app
```

## Repository Structure

```
├── app.py           # Flask application with /proxy endpoint
├── requirements.txt # Python package requirements
└── Procfile         # Defines gunicorn command for platforms like Heroku
```

This repository currently does not include automated tests or CI configuration.
