# Eleos

Web automation testing framework using Python, Playwright, and pytest.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run tests
pytest
```

## Docker

```bash
docker-compose up test_chrome
docker-compose up test_firefox
```

## Structure

```
flows/      Test workflows
pages/      Page objects  
tests/      Test cases
data/       Test data generator
reports/    HTML test reports
```

Tests run against `https://demo.automationtesting.in` by default.
