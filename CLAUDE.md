# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Purpose**: A minimal Flask application that proxies RSS feeds from Substack with proper headers and encoding.

**Architecture**: Simple single-endpoint Flask app that fetches and returns XML content with proper content-type headers.

**Target RSS Feed**: `https://natesnewsletter.substack.com/feed`

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (development)
python app.py
# Access at: http://localhost:8080/proxy

# Run with gunicorn (production-like)
gunicorn app:app
# Access at: http://localhost:8000/proxy

# Test the endpoint
curl http://localhost:8080/proxy

# Check response headers
curl -I http://localhost:8080/proxy
```

## Core Application Architecture

**Single File Structure** (`app.py` - 23 lines):
- Flask route: `/proxy` 
- HTTP client: `requests` library
- Error handling: Basic try/catch with 500 responses
- Encoding: Explicitly set to UTF-8 using `r.text`
- Headers: Uses Mozilla User-Agent to avoid blocking
- Response: Returns XML with `application/xml; charset=utf-8` content-type

**Dependencies**:
- `flask` - Web framework
- `requests` - HTTP client for fetching feeds  
- `gunicorn` - Production WSGI server

## Code Patterns

### Response Pattern
```python
return Response(
    r.text,                                    # UTF-8 decoded content
    status=r.status_code,                      # Preserve original status
    content_type='application/xml; charset=utf-8'  # Explicit XML+charset
)
```

### Error Handling Pattern
```python
try:
    # HTTP request
    return Response(...)
except Exception as e:
    return Response(f'Error fetching feed: {e}', status=500)
```

## Deployment

**Platform**: Configured for Heroku via `Procfile`
**Command**: `web: gunicorn app:app`
**Port**: Uses environment `$PORT` or defaults

## Recent Changes Context

- **Latest**: Improved encoding by using `r.text` and setting charset
- **Previous**: Fixed content-type to include `charset=utf-8`
- **Initial**: Basic Flask proxy implementation

## Current Limitations

1. **Hardcoded URL**: Target Substack feed is not configurable
2. **No Caching**: Each request fetches fresh content from upstream
3. **No Tests**: No automated testing suite
4. **No Logging**: No structured logging implementation
5. **No Rate Limiting**: No protection against abuse

## Security Notes

- Application fetches from hardcoded URL (reduces SSRF risk)
- No user input validation needed (no parameters accepted)
- User-Agent spoofing is intentional for access (not malicious)