# AI Quiz Solver

An automated data science quiz solver that uses Gemini AI to scrape, analyze, and solve multi-step quiz challenges involving web scraping, data processing, file analysis, and more.

## Features

- **Automated Web Scraping**: Uses Playwright to extract data from quiz pages
- **Multi-Format Support**: Handles CSV, PDF, audio files, images, and linked pages
- **AI-Powered Solving**: Leverages Google's Gemini 2.5 Pro for intelligent answer generation
- **Chain Solving**: Automatically follows quiz chains by processing server responses
- **File Processing**: Downloads and analyzes various file types (CSV, PDF, audio)
- **Function Calling**: Uses Gemini's function calling to structure quiz submissions

## Prerequisites

- Python 3.8+
- Google Gemini API key
- Playwright browser drivers

## Installation

1. Clone the repository and navigate to the project directory

2. Install required dependencies:
```bash
pip install fastapi uvicorn python-dotenv google-genai playwright httpx
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

4. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET=your_secret_key_here
```

## Usage

### Starting the Server

Run the FastAPI server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

### Triggering a Quiz

Send a POST request to `/task` endpoint:

```bash
curl -X POST http://localhost:8000/task \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "secret": "your_secret_key",
    "url": "https://quiz-url.com/start"
  }'
```

### API Response

```json
{
  "message": "Secret Matches!",
  "status_code": 200
}
```

The quiz solving process runs in the background and continues automatically through quiz chains.

## How It Works

1. **Extraction Phase**: 
   - Loads the quiz page using Playwright
   - Extracts visible text, HTML, JSON payloads, and linked resources
   - Identifies submit URLs and downloads relevant files (CSV, PDF, audio)

2. **AI Analysis Phase**:
   - Sends extracted data to Gemini AI
   - Includes all relevant files as attachments
   - Uses function calling to get structured responses

3. **Submission Phase**:
   - Submits the AI-generated answer to the quiz endpoint
   - Processes server response for next quiz URL
   - Continues chain if more quizzes are available

## Supported Quiz Types

- Web scraping challenges
- API integration tasks
- Data cleansing and transformation
- PDF/CSV processing
- Audio transcription
- Image analysis
- Statistical analysis and ML tasks
- Geospatial and network analysis
- Data visualization

## Architecture

- **FastAPI**: Web framework for API endpoints
- **Playwright**: Headless browser automation
- **Gemini AI**: Language model for solving quizzes
- **httpx**: Async HTTP client for file downloads
- **Background Tasks**: Non-blocking quiz solving workflow

## Configuration

### CORS Settings

The application allows all origins by default. Modify in `app.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Browser Settings

Modify browser launch options in the `lifespan` function:
```python
app.state.browser = await app.state.playwright.chromium.launch(
    headless=True  # Set to False for debugging
)
```

## Troubleshooting

### Browser Not Launching
Ensure Playwright browsers are installed:
```bash
playwright install chromium
```

### API Key Errors
Verify your `.env` file contains a valid `GEMINI_API_KEY`

### JSON Parsing Errors
The system includes automatic JSON cleaning for malformed payloads. Check console logs for specific parsing issues.

### File Download Failures
Check network connectivity and ensure URLs are accessible. Review console logs for specific file download errors.

## Security Considerations

- Store API keys securely in `.env` file
- Never commit `.env` to version control
- Implement proper authentication in production
- Restrict CORS origins to trusted domains
- Use HTTPS in production environments

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
