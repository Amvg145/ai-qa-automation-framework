# AI QA Automation Framework

An intelligent test automation framework that leverages AI/ML capabilities for test case generation, failure analysis, bug reporting, and self-healing test locators. This framework combines traditional QA automation with modern AI agents powered by Ollama and LLaMA3.

## 🎯 Overview

The AI QA Automation Framework is designed to reduce manual testing effort and improve test maintenance through:

- **AI-Powered Test Generation**: Automatically generate comprehensive test cases (positive, negative, edge, security)
- **Intelligent Failure Analysis**: Analyze pytest failures and suggest root causes and fixes
- **Automated Bug Reporting**: Generate structured bug reports from test failures
- **Self-Healing Tests**: Automatically suggest alternative locators when UI elements change
- **Test Validation**: Relevance validators to ensure generated tests are meaningful

## 🏗️ Architecture

### Components

#### AI Agents (`/agents/`)

- **TestCaseAgent**: Generates QA test cases for features with comprehensive coverage
- **FailureAnalyzer**: Analyzes pytest failure logs and provides root cause analysis, suggestions, and prevention strategies
- **BugReportAgent**: Creates structured bug reports from failures
- **SelfHealingAgent**: Suggests alternative element locators when tests break

#### Test Suites

- **API Tests** (`/api_tests/`): FastAPI endpoint testing
- **UI Tests** (`/ui_tests/`): End-to-end UI testing with Playwright
- **Generated Tests** (`/generated_tests/`): AI-generated test cases

#### Core Components

- **Backend** (`/backend/`): FastAPI application with chat endpoint
- **Pages** (`/pages/`): Page Object Model for UI tests (ChatPage)
- **Utilities** (`/utils/`): API client, logger, response models
- **Configuration** (`/config/`): Application settings and base URLs

#### Validators (`/ai_validators/`)

- **RelevanceValidator**: Validates that AI-generated tests are relevant and properly structured

## 🔧 Tech Stack

- **Python 3.x**: Core language
- **FastAPI**: Backend API framework
- **Playwright**: Browser automation for UI testing
- **Pytest**: Test framework
- **Ollama + LLaMA3**: Local AI model for intelligent agent processing
- **Requests**: HTTP client library
- **Jinja2**: Template engine

## 📁 Project Structure

```
ai-qa-automation-framework/
├── agents/                          # AI Agent implementations
│   ├── test_case_agent.py          # Generate test cases
│   ├── failure_analyzer.py          # Analyze test failures
│   ├── bug_report_agent.py          # Generate bug reports
│   └── self_healing_agent.py        # Fix broken locators
├── api_tests/                       # API test suites
│   └── test_chat_api.py             # Chat endpoint tests
├── ui_tests/                        # UI test suites
│   ├── test_chat_ui.py              # Chat UI tests
│   ├── test_chat_end_to_end.py      # E2E tests
│   └── test_self_healing_demo.py    # Self-healing demo
├── generated_tests/                 # AI-generated tests
│   ├── test_ai_generated.py         # Generated test cases
│   ├── test_failure_demo.py         # Failure demonstration
│   └── test_generator.py            # Test generation utilities
├── backend/                         # FastAPI backend
│   ├── app.py                       # Main application
│   └── templates/
│       └── index.html               # Chat UI template
├── pages/                           # Page Object Models
│   └── chat_page.py                 # Chat page POM
├── ai_validators/                   # AI validation logic
│   └── relevance_validator.py       # Test relevance validation
├── utils/                           # Utility functions
│   ├── api_client.py                # HTTP client wrapper
│   ├── logger.py                    # Logging utilities
│   ├── response_models.py           # Pydantic response models
│   └── generate_failure_log.py      # Failure log generation
├── config/                          # Configuration
│   └── config.py                    # App configuration
├── reports/                         # Test reports & artifacts
├── test_data/                       # Test data files
│   └── chat_payload.json            # Sample API payloads
├── conftest.py                      # Pytest configuration & fixtures
├── pytest.ini                       # Pytest settings
├── requirements.txt                 # Python dependencies
├── Jenkinsfile                      # CI/CD pipeline configuration
├── analyze_failure.py               # CLI for failure analysis
├── generate_bug_report.py           # CLI for bug report generation
├── run_self_healing.py              # CLI for self-healing agent
├── run_agent.py                     # General agent runner
└── README.md                        # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- LLaMA3 model installed in Ollama: `ollama pull llama3`
- Git

### Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd ai-qa-automation-framework
```

2. **Create virtual environment**

```bash
python -m venv venv
```

3. **Activate virtual environment**

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Start Ollama and LLaMA3 model**

```bash
ollama serve
# In another terminal:
ollama pull llama3
```

## ⚙️ Configuration

Edit `config/config.py` to configure:

```python
class Config:
    BASE_URL = "http://127.0.0.1:8000"  # Backend URL
    # Add more configuration as needed
```

## 🏃 Running Tests

### Run all tests

```bash
pytest
```

### Run API tests

```bash
pytest api_tests/
```

### Run UI tests

```bash
pytest ui_tests/
```

### Run specific test file

```bash
pytest ui_tests/test_chat_ui.py
```

### Run with detailed output

```bash
pytest -v -s
```

### Run with coverage report

```bash
pytest --cov=.
```

## 🤖 Using AI Agents

### 1. Generate Test Cases

```bash
python -c "
from agents.test_case_agent import TestCaseAgent

agent = TestCaseAgent()
test_cases = agent.generate_test_cases('Login Feature')
print(test_cases)
"
```

### 2. Analyze Test Failures

```bash
python analyze_failure.py
```

This reads `failure_log.txt` and provides:

- Root cause analysis
- Possible reasons for failure
- Suggested fixes
- Prevention strategies

### 3. Generate Bug Reports

```bash
python generate_bug_report.py
```

Generates structured bug reports including:

- Title and severity/priority
- Module affected
- Steps to reproduce
- Expected vs actual results
- Root cause analysis
- Recommendations

### 4. Self-Healing Locators

```bash
python run_self_healing.py
```

When a UI locator fails, the agent suggests alternative locators based on:

- Failed locator syntax
- Current HTML/DOM structure
- Best practices for locator strategies

## 🏗️ Backend API

Start the FastAPI backend:

```bash
uvicorn backend.app:app --reload
```

The backend provides:

- **GET /**: Chat UI interface
- **POST /chat**: Chat endpoint for processing messages

## 📊 Reports and Artifacts

Test reports are generated in the `reports/` directory:

- Container JSON files for test execution details
- Result JSON files with test outcomes
- Attachment files with logs and screenshots

## 🔍 Key Features

### Test Case Generation

- AI-powered generation of comprehensive test cases
- Includes positive, negative, edge, and security test cases
- Structured output ready for implementation

### Failure Analysis

- Automatic analysis of pytest failure logs
- Root cause identification
- Prevention strategy suggestions
- Fix recommendations

### Bug Reporting

- Automatic bug report generation
- Includes all necessary QA information
- Severity and priority assessment
- Structured format for issue tracking

### Self-Healing Capability

- Detects broken UI locators
- Suggests alternative locators using AI
- Reduces test maintenance burden
- Learns from DOM changes

### Logging

- Comprehensive logging for all API calls
- Structured logging with levels (INFO, ERROR, DEBUG)
- Easy troubleshooting and audit trails

## 🧪 Example Workflows

### Workflow 1: Generate and Run Tests

```bash
# 1. Generate test cases
python -c "from agents.test_case_agent import TestCaseAgent; agent = TestCaseAgent(); print(agent.generate_test_cases('User Registration'))"

# 2. Review and implement tests in generated_tests/

# 3. Run tests
pytest generated_tests/

# 4. If tests fail, analyze failures
python analyze_failure.py
```

### Workflow 2: Maintain UI Tests

```bash
# 1. Run existing UI tests
pytest ui_tests/test_chat_ui.py

# 2. If locator fails, use self-healing
python run_self_healing.py

# 3. Generate bug report if test is legitimately failing
python generate_bug_report.py
```

## 🔌 Integration Points

### CI/CD Integration

- Jenkins support via `Jenkinsfile`
- Easy integration with other CI/CD platforms
- Structured reports for pipeline consumption

### API Testing

- Built-in API client with logging
- Support for POST/GET requests
- Configurable base URL

### UI Testing

- Playwright for cross-browser testing
- Page Object Model for maintainability
- E2E testing support

## 📝 Development Guidelines

### Adding New Tests

1. Create test file in appropriate directory (api_tests, ui_tests, or generated_tests)
2. Use conftest.py fixtures for common setup
3. Follow naming convention: `test_<feature>.py`

### Extending AI Agents

1. Create new agent class in `/agents/`
2. Inherit from base pattern if needed
3. Use Ollama for LLM calls
4. Add CLI runner in root directory if needed

### Adding Validators

1. Create validator in `/ai_validators/`
2. Implement validation logic
3. Use in test generation pipeline

## 🐛 Troubleshooting

### Ollama Connection Issues

```bash
# Ensure Ollama is running
ollama serve

# Check if model is loaded
ollama list
```

### Test Locator Issues

- Use self-healing agent to suggest fixes
- Check browser dev tools for updated selectors
- Update page objects with new locators

### API Connection Issues

- Verify backend is running on configured URL
- Check firewall/network connectivity
- Review logs in utils/logger.py output

## 📚 Resources

- [Ollama Documentation](https://ollama.ai/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Documentation](https://playwright.dev/python/)

## 🤝 Contributing

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and add tests
3. Run full test suite: `pytest`
4. Commit with descriptive messages
5. Push and create pull request

## 📄 License

[Add license information here]

## 🎓 Future Enhancements

- Multi-model support (GPT-4, Claude, etc.)
- Enhanced test flakiness detection
- Visual regression testing with AI
- Performance testing automation
- Advanced test result analytics dashboard
- Integration with popular test management tools
- Parallel test execution optimization
- AI-powered test data generation

## 📞 Support & Questions

For issues and questions, please:

- Check existing documentation
- Review failure logs and analysis
- Use AI agents for root cause analysis
- Document issues with test logs and screenshots
