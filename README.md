# 🌱 The Sandbox: Multi-Agent AI Framework

![GitHub License](https://img.shields.io/github/license/Hams-Ollo/the_sandbox)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![React Version](https://img.shields.io/badge/react-19.0.0-blue)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

> 💭 "Technology should enhance human consciousness, not replace it."

## 🚀 Welcome to The Sandbox

The Sandbox is an open-source multi-agent AI framework designed for content creation, knowledge management, and workflow automation. It combines advanced AI agents, knowledge graph technology, and human-in-the-loop workflows to create a flexible system for both experimentation and production use cases.

This framework uses a custom implementation of the Batman & Alfred paradigm, where:

- 🦇 **Batman (You)** = The strategist, decision-maker, and consciousness guide
- 🤵 **Alfred (AI Assistant)** = The intelligent, consciousness-aware assistant that supports your mission

## 🧩 Core Components

The Sandbox framework consists of several integrated components:

### 1. 🎭 Multi-Agent System

- **Alfred Prime**: Central orchestrator agent that coordinates all specialized agents
- **Content Collector**: Extracts web content using FireCrawl and other sources
- **Insight Extractor**: Analyzes content to identify key insights and patterns
- **Content Generator**: Creates long-form content using multi-stage generation
- **Social Media Agent**: Formats content for different platforms and schedules posts

### 2. 🧠 Knowledge Infrastructure

- **ChromaDB**: Vector database for semantic search and content retrieval
- **Neo4j**: Graph database for representing relationships between content entities
- **Embedding Pipeline**: Converts content into vector representations for similarity search
- **Retrieval System**: Implements RAG (Retrieval-Augmented Generation) for context-aware responses

### 3. 🖥️ User Interface

- **Chat Interface**: Real-time communication with the AI system
- **Workflow Controls**: Visualization and management of automated processes
- **Content Review**: Human-in-the-loop content approval and editing
- **Knowledge Explorer**: Visualization of the knowledge graph

### 4. 🔌 Integrations

- **FireCrawl**: Web scraping and content extraction
- **Google Workspace**: Document storage and collaborative editing
- **Publishing Platforms**: WordPress, Medium, and social media publishing
- **Email System**: Newsletter distribution and notifications

## 📁 Project Structure

```curl
the_sandbox/
├── backend/                      # Backend Python application
│   ├── app/                      # Main application code
│   │   ├── agents/               # Agent implementations
│   │   ├── api/                  # API endpoints
│   │   ├── core/                 # Core infrastructure
│   │   ├── db/                   # Database connections
│   │   ├── services/             # External service integrations
│   │   ├── utils/                # Utility functions
│   │   └── main.py               # Application entry point
│   ├── tests/                    # Backend tests
│   └── requirements.txt          # Python dependencies
├── frontend/                     # React frontend application
│   ├── public/                   # Static assets
│   ├── src/                      # React source code
│   │   ├── components/           # UI components
│   │   ├── contexts/             # React contexts
│   │   ├── hooks/                # Custom hooks
│   │   ├── pages/                # Page components
│   │   ├── services/             # API and WebSocket services
│   │   ├── styles/               # CSS/Tailwind styles
│   │   ├── utils/                # Utility functions
│   │   ├── App.tsx               # Main application component
│   │   └── index.tsx             # Entry point
│   ├── package.json              # Node dependencies
│   └── tsconfig.json             # TypeScript configuration
├── docs/                         # Documentation
│   ├── architecture/             # System architecture docs
│   ├── implementation-guide.md   # Implementation guide
│   ├── api-credentials.md        # API credential setup
│   └── prompt-engineering.md     # Prompt engineering guide
└── scripts/                      # Utility scripts
    ├── setup.sh                  # Environment setup script
    └── seed_data.py              # Initial data setup
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Neo4j database
- API keys (see `docs/api-credentials.md`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hams-Ollo/the_sandbox.git
   cd the_sandbox
   ```

2. Set up the backend:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:

   ```bash
   cd ../frontend
   npm install
   ```

4. Configure your environment:

   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

5. Start the development servers:

   ```bash
   # In one terminal (backend)
   cd backend
   python -m app.main

   # In another terminal (frontend)
   cd frontend
   npm start
   ```

## 🏗️ Implementation Roadmap

The Sandbox is being built in stages:

1. **Project Setup & Environment Configuration** (Week 1)
   - Repository setup, authentication system, documentation

2. **Backend Core Infrastructure** (Week 2)
   - FastAPI backend, database connections, agent infrastructure

3. **React Frontend Foundation** (Week 3)
   - Chat interface, workflow sidebar, WebSocket integration

4. **Knowledge Graph & Storage System** (Week 4)
   - ChromaDB, Neo4j, Google Workspace integration

5. **Multi-Agent Orchestration** (Week 5)
   - Alfred Prime implementation, specialized agents, communication system

6. **Content Collection & Analysis** (Week 6)
   - FireCrawl integration, content normalization, insight extraction

7. **Content Generation System** (Week 7)
   - Multi-stage generation, human review interface, quality assurance

8. **Publishing & Distribution** (Week 8)
   - WordPress integration, social media posting, email distribution

9. **System Integration & Optimization** (Weeks 9-10)
   - Full integration, performance optimization, documentation

## 🧪 Use Cases

### Content Creation Pipeline

Automate the process of collecting content from various sources, extracting insights, generating new content with human review, and publishing across multiple platforms.

### Knowledge Management System

Create a dynamic knowledge graph of your domain, enabling powerful semantic search and context-aware content generation.

### Research Assistant

Build a system that can collect research, analyze findings, identify patterns, and generate comprehensive reports.

### Social Media Management

Automate content curation, creation, and scheduling across multiple social platforms with consistent messaging.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Documentation

- [Architecture Guide](docs/architecture/overview.md) - System architecture overview
- [Implementation Guide](docs/implementation-guide.md) - Detailed implementation instructions
- [API Credentials](docs/api-credentials.md) - Setup guide for required API keys
- [Prompt Engineering](docs/prompt-engineering.md) - Guide to effective prompt design

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

The Sandbox is built on the foundation of numerous open-source projects and research in AI, knowledge systems, and human-computer interaction. Special thanks to the communities behind these technologies and to all contributors.

---

> Built by Hans Havlik (@hams_ollo)
