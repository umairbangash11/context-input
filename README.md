# Input Message Agent

A Python application that demonstrates the use of AI agents with message history and context management using the OpenAI Agents framework and Gemini API.

## Features

- **AI Agent Integration**: Uses OpenAI Agents framework with Gemini 2.5 Flash model
- **Message History Management**: Supports conversation history and context
- **Environment-based Configuration**: Secure API key management using environment variables
- **Async Operations**: Built with asyncio for efficient asynchronous processing
- **Context Management**: Session-based context handling for multi-turn conversations

## Prerequisites

- Python 3.12 or higher
- UV package manager
- Gemini API key

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd input-message
   ```

2. **Install dependencies using UV**:
   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

### Running the Application

Execute the main script using UV:

```bash
uv run main.py
```

### Code Structure

The application consists of:

- **Agent Configuration**: Sets up an AI agent with Gemini 2.5 Flash model
- **Context Management**: Uses Pydantic models for structured context data
- **Message History**: Supports conversation history with system and user messages
- **Async Runner**: Utilizes the Runner class for executing agent operations

### Key Components

1. **Agent Setup**:
   ```python
   agent = Agent(
       name="InputInjectionAgent",
       instructions="you are a helpful assistant"
   )
   ```

2. **Context Management**:
   ```python
   class MyContext(BaseModel):
       session_id: str
   ```

3. **Message History**:
   ```python
   input_history = [
       {"role": "system", "content": "The user's name is Umair."},
       {"role": "user", "content": "What is the user's name?"}
   ]
   ```

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (required)

### Model Configuration

The application uses:
- **Model**: Gemini 2.5 Flash
- **Base URL**: Google's Generative Language API
- **Framework**: OpenAI Agents

## Project Structure

```
input-message/
├── main.py              # Main application file
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
├── uv.lock             # UV lock file
└── .env                # Environment variables (create this)
```

## Dependencies

- `openai-agents>=0.2.4`: OpenAI Agents framework
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation and settings management
- `openai`: OpenAI client library

## Development

### Adding New Features

1. **Extend the Agent**: Modify the agent instructions or add new tools
2. **Enhance Context**: Add new fields to the `MyContext` class
3. **Custom Messages**: Modify the message history structure

### Error Handling

The application includes basic error handling for:
- Missing API keys
- Network connectivity issues
- Invalid configurations

## Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure `GEMINI_API_KEY` is set in your `.env` file
2. **Network Issues**: Check your internet connection and firewall settings
3. **SSL Errors**: May occur due to certificate issues - check your system's SSL configuration

### Debug Mode

Enable verbose logging by uncommenting or adding:
```python
from agents import enable_verbose_stdout_logging
enable_verbose_stdout_logging()
```

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please [create an issue](link-to-issues) or contact [your-email].
