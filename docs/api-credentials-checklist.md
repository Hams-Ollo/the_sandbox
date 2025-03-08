# API Keys & Credentials Checklist for The Sandbox Multi-Agent AI Framework (Revised)

## LLM API Keys

- [ ] OpenAI API Key (primary for GPT-4o)
- [ ] Anthropic API Key (backup option)
- [ ] HuggingFace API Key (for embedding models)

## Google Workspace Integration

- [ ] Google Cloud Project Setup
  - [ ] Create a new project in Google Cloud Console
  - [ ] Enable required APIs:
    - [ ] Google Drive API
    - [ ] Google Docs API
    - [ ] Google Sheets API
    - [ ] Google Calendar API
    - [ ] Gmail API
  - [ ] Create OAuth 2.0 Client ID credentials
    - [ ] Configure OAuth consent screen
    - [ ] Add required scopes:
      - [ ] <https://www.googleapis.com/auth/drive>
      - [ ] <https://www.googleapis.com/auth/docs>
      - [ ] <https://www.googleapis.com/auth/spreadsheets>
      - [ ] <https://www.googleapis.com/auth/calendar>
      - [ ] <https://www.googleapis.com/auth/gmail.send>
    - [ ] Download JSON credentials file
  - [ ] Create Service Account (for background processing)
    - [ ] Grant necessary permissions
    - [ ] Download JSON key file
    - [ ] Share necessary Google Drive folders with service account email

## Web Scraping & Content Collection

- [ ] FireCrawl API Key (primary web scraping solution)
- [ ] Backup scraping setup:
  - [ ] Selenium/BeautifulSoup configuration
  - [ ] Proxy service credentials (if needed)
- [ ] RSS Feed URLs (for content monitoring)

## Database & Storage

- [ ] ChromaDB Configuration
  - [ ] Directory Path for vector database storage
  - [ ] Collection Name configuration
- [ ] Neo4j Database Credentials
  - [ ] Database URL
  - [ ] Username
  - [ ] Password
- [ ] Local storage configuration for document caching

## Social Media Integration

- [ ] Twitter/X
  - [ ] Create Developer Account
  - [ ] Register App
  - [ ] Get API Key and API Secret
  - [ ] Generate Access Token and Access Token Secret
  - [ ] Configure app permissions for posting

- [ ] LinkedIn
  - [ ] Create Developer Account
  - [ ] Register App
  - [ ] Get Client ID and Client Secret
  - [ ] Configure redirect URIs
  - [ ] Request necessary permissions:
    - [ ] r_liteprofile
    - [ ] r_emailaddress
    - [ ] w_member_social

- [ ] Facebook/Meta (if needed)
  - [ ] Create Developer Account
  - [ ] Register App
  - [ ] Get App ID and App Secret
  - [ ] Generate long-lived access token

## Publishing Platforms

- [ ] WordPress
  - [ ] Generate Application Password
  - [ ] Site URL
  - [ ] Username
  - [ ] XML-RPC endpoint

- [ ] Medium
  - [ ] Get Integration Token
  - [ ] Configure publication settings

- [ ] Substack (if applicable)
  - [ ] API credentials or email integration details

## Email Integration

- [ ] SMTP Server Configuration
  - [ ] Server hostname
  - [ ] Port
  - [ ] Username
  - [ ] Password
  - [ ] TLS/SSL settings
- [ ] Email Templates Setup
  - [ ] Notification templates
  - [ ] Newsletter templates

## Monitoring & Analytics

- [ ] LangSmith API Key (for LLM tracing)
- [ ] Basic analytics setup (internal tracking)
- [ ] Logging configuration

## Development & Deployment

- [ ] GitHub API Key (for repository integration)
- [ ] Environment variables configuration for:
  - [ ] Development
  - [ ] Testing
  - [ ] Production
- [ ] Continuous Integration setup

## Security Configuration

- [ ] JWT Secret Key (for authentication)
- [ ] Secret Key (for application security)
- [ ] Create secure .env file with all credentials
- [ ] Set up credential rotation schedule
- [ ] Configure backup for credential files
- [ ] API key usage limits and monitoring
- [ ] Rate limiting configuration

## Personal Information for Alfred Prime

- [ ] Personal Gmail address
- [ ] Google Drive folder structure for knowledge base
- [ ] Batman (Hans Havlik) profile document
- [ ] Content topics and preferences document
- [ ] Ethical boundaries and guidelines

## Implementation Best Practices

- [ ] Store all API keys in environment variables, not code
- [ ] Implement credential manager in the backend for secure access
- [ ] Use credential rotation for sensitive keys
- [ ] Implement exponential backoff for API rate limits
- [ ] Set up usage monitoring to avoid unexpected costs
- [ ] Keep a backup of credentials in a secure password manager
- [ ] Document each API's rate limits and quotas

## Cost Management

- [ ] Set up billing alerts for OpenAI API
- [ ] Configure usage caps where supported
- [ ] Implement token counting and tracking
- [ ] Create cost estimation reports

## Setup Priority Order

1. Core LLM Access (OpenAI API)
2. Storage (ChromaDB)
3. Content Collection (FireCrawl)
4. Google Workspace Integration
5. Publishing Platforms
6. Social Media Integration
7. Email Integration
8. Monitoring Tools

*Note: Focus on implementing the minimum viable credentials first, then expand as functionality grows. Start with development keys with restricted usage before moving to production credentials.*
