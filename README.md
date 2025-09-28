# Pitch Desk Analyser

A production-grade, agent-oriented Python app for extracting, analyzing, and enriching company pitch decks (PDF, PPTX) for investment decision-making.

## Features

- **Multi-format Support**: Ingest pitch decks in PDF and PPTX formats
- **AI-Powered Analysis**: LLM-based enrichment via OpenRouter with configurable models
- **External Intelligence**: Fetches public profiles and news via DuckDuckGo HTML
- **Investment Insights**: Competitive landscape mapping with Mermaid charts
- **Risk Assessment**: Sentiment and hype analysis for investment decisions
- **Scoring System**: AI signal scoring across Product, Team, Market, and Investment Fit
- **Due Diligence**: Automated gap detection and diligence questions
- **Extensible Architecture**: Modular design for new agents and dashboards

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd boxone-pitchdeck-insights
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your OpenRouter API key:
   ```env
    OPENROUTER_API_KEY=sk-yourkeyhere
    ```

4. **Configure settings (optional)**
   Edit `config.yaml` to customize model and output settings:
   ```yaml
   llm_model: openai/gpt-3.5-turbo
   output_file: analysis_output.md
   ```
   
   Note: The `output_file` setting determines the file extension and base naming pattern. The actual filename will be unique with a timestamp (e.g., `your_pitchdeck_20241201_143022.md`).

5. **Run the analysis**
   ```bash
   python3 main.py your_pitchdeck.pdf
   ```
   
   The analysis will generate a unique output file named `your_pitchdeck_YYYYMMDD_HHMMSS.md` to avoid overwriting previous results.

## Configuration

### Supported LLM Models
- `deepseek-v3` 
- `openai/gpt-4o`
- `openai/gpt-3.5-turbo`
- `mixtral-8x7b`
- `gemini-2-5-flash`

### Output Sections
The analysis generates comprehensive reports including:
- Executive Summary
- Team Analysis
- Product Description
- Market Analysis
- Traction & Metrics
- Funding & Financials
- Competitive Landscape Map
- Sentiment & Hype Analysis
- AI Investment Signal Score
- Risks & Unique Strengths
- Missing Info & Diligence Questions

## Architecture

```
main.py                 # Application entry point
├── utils/
│   ├── agent.py        # High-level agent interface
│   ├── enrich.py       # Core AI enrichment engine
│   ├── pdf_parser.py   # PDF text extraction
│   ├── ppt_parser.py   # PowerPoint text extraction
│   ├── web_enrich.py   # External data gathering
│   └── markdown_writer.py # Output formatting
└── tests/              # Unit tests
```

## Future Enhancements

### High Priority
- **Multi-language Support**: Add support for pitch decks in different languages
- **Image Analysis**: Extract and analyze charts, graphs, and visual elements from pitch decks
- **Real-time Data Integration**: Connect to financial APIs (Alpha Vantage, Yahoo Finance) for live market data
- **Database Integration**: Store analysis results in PostgreSQL/MongoDB for historical tracking
- **Web Dashboard**: Create a React/Vue.js frontend for interactive analysis viewing
- **Batch Processing**: Support for analyzing multiple pitch decks simultaneously

### Analytics & Intelligence
- **Comparative Analysis**: Side-by-side comparison of multiple companies
- **Industry Benchmarking**: Compare metrics against industry standards
- **Trend Analysis**: Track company progress over time with multiple pitch deck versions
- **Investment Portfolio Integration**: Connect with portfolio management systems
- **Custom Scoring Models**: Allow users to define their own scoring criteria
- **Sentiment Tracking**: Monitor sentiment changes over time

### Technical Improvements
- **Async Processing**: Implement async/await for better performance
- **Caching Layer**: Add Redis caching for repeated API calls
- **Rate Limiting**: Implement intelligent rate limiting for API calls
- **Error Recovery**: Add robust error handling and retry mechanisms
- **Logging & Monitoring**: Comprehensive logging with structured data
- **API Documentation**: Auto-generated API docs with FastAPI/Flask

### Integration & Extensibility
- **Slack/Teams Integration**: Send analysis results to team channels
- **Email Reports**: Automated email delivery of analysis results
- **CRM Integration**: Connect with Salesforce, HubSpot, or Pipedrive
- **Webhook Support**: Real-time notifications for completed analyses
- **Plugin System**: Allow third-party plugins for custom analysis modules
- **REST API**: Expose functionality via REST API for external integrations

### Security & Compliance
- **Data Encryption**: Encrypt sensitive data at rest and in transit
- **Access Control**: Role-based access control for different user types
- **Audit Logging**: Track all analysis activities for compliance
- **Data Retention**: Configurable data retention policies
- **SOC 2 Compliance**: Implement security controls for enterprise use
- **GDPR Compliance**: Data privacy controls for European users

### Performance & Scalability
- **Horizontal Scaling**: Support for multiple worker processes
- **Load Balancing**: Distribute analysis workload across multiple servers
- **CDN Integration**: Serve static assets via CDN
- **Database Optimization**: Query optimization and indexing strategies
- **Memory Management**: Efficient memory usage for large pitch decks
- **Background Jobs**: Queue-based processing for long-running analyses

## Improvement Pointers

### Code Quality
- **Type Hints**: Add comprehensive type hints throughout the codebase
- **Unit Test Coverage**: Increase test coverage to 90%+ with comprehensive test cases
- **Integration Tests**: Add end-to-end integration tests
- **Code Linting**: Implement pre-commit hooks with black, flake8, and mypy
- **Documentation**: Add comprehensive API documentation and user guides

### Performance Optimization
- **Text Processing**: Implement more efficient text extraction algorithms
- **Memory Usage**: Optimize memory consumption for large files
- **API Efficiency**: Batch API calls where possible to reduce latency
- **Caching Strategy**: Implement intelligent caching for repeated operations
- **Parallel Processing**: Use multiprocessing for CPU-intensive tasks

### User Experience
- **Progress Indicators**: Add detailed progress bars for long-running operations
- **Error Messages**: Provide clear, actionable error messages
- **Configuration Validation**: Validate configuration files before processing
- **Output Customization**: Allow users to customize output format and sections
- **Interactive Mode**: Add interactive CLI for guided analysis

### Monitoring & Observability
- **Metrics Collection**: Track analysis success rates, processing times, and errors
- **Health Checks**: Implement health check endpoints for monitoring
- **Alerting**: Set up alerts for system failures or performance issues
- **Distributed Tracing**: Track requests across microservices
- **Performance Profiling**: Regular performance profiling and optimization

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security

- `.env` files are git-ignored - never commit your API keys
- Use environment variables for all sensitive configuration
- Regularly update dependencies to patch security vulnerabilities
- Implement proper input validation and sanitization

## Support

For questions, issues, or feature requests, please:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Contact the maintainers for urgent issues

---

