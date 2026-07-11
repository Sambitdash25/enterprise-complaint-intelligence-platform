# ECIP Engineering Notebook

> Personal Engineering Notebook for the Enterprise Complaint Intelligence Platform (ECIP)

**Purpose**

This notebook is my personal engineering diary and interview preparation guide while building ECIP.

It is **not** project documentation.

It exists so that whenever I revisit this project after weeks or months, I can quickly recall:
- What I built.
- Why I built it.
- Important engineering concepts.
- Interview questions with answers.
- Mistakes I made.
- Key takeaways.

The objective is to understand the project deeply enough to confidently explain every engineering decision during interviews.

---

# Sprint 0

---

# Task 1 – Repository Setup & Project Foundation

## Objective

Before writing any business logic, establish a professional software engineering foundation for the project.

A good software project begins with proper planning, version control, folder organization, dependency isolation, and documentation. This reduces technical debt and makes future development easier.

---

## What We Built

- GitHub Repository
- Local Git Repository
- Standard Project Folder Structure
- Python Virtual Environment
- Initial Project Dependencies
- Problem Statement
- Initial Architecture Documents

---

## Concepts Learned

### Git

Git is a distributed version control system.

Instead of saving multiple copies of the project manually, Git stores snapshots of the project history.

Basic workflow:

Working Directory
↓
Staging Area
↓
Commit
↓
Remote Repository (GitHub)

---

### GitHub

GitHub is a cloud platform that hosts Git repositories.

Git manages version history locally.

GitHub stores it remotely for backup and collaboration.

---

### Virtual Environment

Purpose:

- Isolates project dependencies.
- Prevents package conflicts.
- Makes the project reproducible.

Every Python project should have its own virtual environment.

---

### Why create the folder structure first?

Folders should represent architectural responsibilities.

A clear folder structure makes the project easier to understand, extend, and maintain.

Architecture should drive implementation—not the other way around.

---

## Commands to Remember

### Check status

```bash
git status
```

### Stage files

```bash
git add .
```

### Commit

```bash
git commit -m "message"
```

### Push

```bash
git push
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

---

## Interview Questions

### Q. Why Git?

Git provides version control by tracking project history. It enables collaboration, allows developers to restore previous versions, and helps manage changes safely.

---

### Q. Why GitHub?

GitHub stores Git repositories online, making collaboration, backup, and code sharing possible.

---

### Q. Why use a Virtual Environment?

A virtual environment isolates project dependencies so that different Python projects can use different versions of libraries without conflicts.

---

### Q. Why create the project structure before implementation?

Professional engineering teams define architecture and project structure before writing code. This ensures modularity, maintainability, and scalability from the beginning.

---

## Mistakes Made

Forgot to save the architecture document before committing.

Git committed the saved version (empty file) instead of the content open in the editor.

---

## Lessons Learned

Always follow this workflow:

Save

↓

git status

↓

git add

↓

git commit

↓

git push

---

## Quick Revision

- Git manages project history.
- GitHub stores repositories online.
- Virtual environments isolate dependencies.
- Folder structure should reflect architecture.
- Build the foundation before writing business logic.

---

# Task 2 – System Architecture

## Objective

Design the complete system architecture before implementing any code.

The objective of architecture is to define how different components interact and how a complaint moves through the system.

A well-designed architecture reduces coupling, improves maintainability, and makes future enhancements easier.

---

## Architecture Flow

Complaint Received

↓

Preprocessing

↓

Language Detection

↓

Translation (if required)

↓

PII Detection & Masking

↓

LLM Intelligence Engine

↓

Business Rules Engine

↓

Confidence Evaluation

↓

Human Review Decision

↓

Assignment Engine

↓

Database

↓

Logs & Metrics

---

## Important Concepts

### Architecture vs Workflow

Architecture describes the major components of the system.

Workflow describes the journey of a single complaint through those components.

Architecture = Structure

Workflow = Execution

---

### Single Responsibility Principle (SRP)

Every module should have one clearly defined responsibility.

Example:

Business Rules Engine

Only applies business rules.

It should not perform database operations or call the LLM.

---

### Modular Design

Every component should be independent.

Benefits:

- Easier maintenance
- Easier testing
- Easier replacement
- Better scalability

---

### Business Rules vs LLM

LLM:

Generates intelligent predictions.

Business Rules:

Apply deterministic organizational policies.

Keeping them separate makes the system more explainable and reliable.

---

### Human Review

Not every AI prediction should be accepted automatically.

Human review is required when:

- Confidence is low.
- Complaint is high-risk.
- Business policy requires manual approval.

---

### Folder Mapping

app/api/

REST APIs

app/agents/

LLM Intelligence Engine

app/services/

Business Services

app/rules/

Business Rules

app/database/

Database Layer

app/evaluation/

Confidence Evaluation

app/config/

Configuration

app/utils/

Reusable Utilities

---

## Interview Questions

### Q. Why create architecture before implementation?

Architecture provides a blueprint for development. It defines responsibilities, interactions, and system flow before code is written, reducing future redesign.

---

### Q. Why keep Business Rules separate from the LLM?

LLMs are probabilistic and may produce different outputs for similar inputs.

Business Rules are deterministic and enforce organizational policies.

Separating them improves reliability, maintainability, and explainability.

---

### Q. Why Human Review?

Enterprise AI systems should assist humans rather than completely replace them.

Low-confidence or high-risk predictions require manual validation.

---

### Q. What is the advantage of modular architecture?

Each module can evolve independently.

For example, the OpenAI model can be replaced with another LLM without affecting preprocessing, database, or business rules.

---

### Q. Difference between Architecture and Workflow?

Architecture describes the system components.

Workflow describes how a complaint moves through those components.

---

## Lessons Learned

Good architecture makes implementation easier.

Poor architecture makes every future feature harder.

Think about responsibilities before writing code.

---

## Quick Revision

- Architecture before implementation.
- Workflow follows architecture.
- One responsibility per module.
- AI predicts.
- Business Rules validate.
- Human Review builds trust.
- Folder structure follows architecture.

---

# Progress Tracker

✅ Repository Setup

✅ Git & GitHub

✅ Virtual Environment

✅ Project Structure

✅ Problem Statement

✅ System Architecture

🟨 Database Design (Next)


## Prediction Table

### Why separate Prediction from Complaint?

Complaint = Original business record.

Prediction = AI-generated insights.

Keeping them separate supports:

- Model versioning
- Historical comparison
- Reprocessing
- Better auditability

---

### Important Fields

model_version

→ Know which AI model generated the prediction.

confidence_score

→ Used to decide Human Review.

explanation

→ Makes AI output explainable.

---

### Interview Question

Q. Why store model_version?

Answer:

Different AI models produce different predictions. Storing the model version allows historical tracking, auditing, comparison, and safe model upgrades.

---

Q. Difference between Severity and Confidence?

Answer:

Severity measures business impact.

Confidence measures how certain the AI is about its prediction.

A complaint can have high severity but low confidence, requiring manual review.


## Employee

Purpose:
Store only the information required for complaint assignment.

Remember:
ECIP is not an HR system.

---

## Assignment

Purpose:
Maintain assignment history.

Complaint and Assignment are separate because ownership can change over time.

---

## Audit Log

Purpose:
Maintain complete traceability.

Enterprise systems should always be able to answer:

Who?

What?

When?

---

## Interview Questions

### Why separate Assignment from Complaint?

Assignments can change multiple times during the complaint lifecycle. A separate Assignment table preserves history and supports auditing.

### Why keep an Audit Log?

Audit logs provide traceability, debugging support, compliance, and operational visibility. They allow the system to record every significant event without modifying business records.

### Why doesn't the Employee table store HR information?

ECIP only stores information required for complaint routing. Additional employee details belong to dedicated HR systems.


# Task 3 – Database Design

## Objective

Design the database around business entities instead of application screens or code.

---

## Core Entities

Complaint

↓

Prediction

↓

Assignment

↓

Employee

↓

Audit Log

---

## Key Concepts

### Complaint vs Prediction

Complaint = Original business record

Prediction = AI generated data

Never mix them.

---

### Why Assignment Table?

Complaint ownership changes.

History should never be overwritten.

---

### Why Audit Log?

Enterprise systems require complete traceability.

Every major event should be recorded.

---

### Why UUID?

- Globally unique
- Better for distributed systems
- Difficult to guess
- Industry standard

---

### Why Business Rules decide Priority?

AI provides recommendations.

Business Rules apply organizational policies.

Final priority should always reflect business decisions.

---

## Interview Questions

### Why separate Complaint and Prediction?

Complaint data is immutable business information.

Predictions are derived AI outputs that may change as models evolve.

Keeping them separate supports versioning, auditing, and reprocessing.

---

### Why Assignment History?

Assignments change over time.

Maintaining history improves traceability and operational analysis.

---

### Why Audit Logs?

Audit logs support debugging, compliance, monitoring, and historical tracking.

---

### Difference between Severity and Priority?

Severity represents the impact predicted by AI.

Priority represents the final business urgency after applying organizational rules.

---

## Quick Revision

Remember:

Business Entity

↓

Table

↓

Relationships

↓

Implementation




## Interviewer's Thought Process

If I were interviewing a candidate, I would expect them to explain:

- Why Complaint and Prediction are separate.
- Why AI doesn't directly decide Priority.
- Why Business Rules exist.
- Why model_version is stored.
- Difference between Severity and Priority.

If I can explain these confidently, I understand the database design—not just the schema.


## Database Relationships

### Remember

PK

↓

Unique row

FK

↓

Relationship

---

### Cardinality

Complaint

↓

Many Predictions

↓

Many Assignments

↓

Many Audit Logs

Employee

↓

Many Assignments

---

### Index

Purpose:

Improve search performance.

Don't index everything.

Index frequently searched columns.

---

### Interview Questions

#### Why Foreign Keys?

Maintain referential integrity.

Prevent orphan records.

---

#### Why One Complaint → Many Predictions?

Supports:

- Model upgrades
- Reprocessing
- Historical comparison

---

#### Why indexes?

Indexes improve query performance by reducing full table scans.

---

### Quick Revision

PK

↓

Identity

FK

↓

Relationship

Index

↓

Performance



# Sprint 0 Summary

## What I Learned

- Think about business entities before database tables.
- Architecture should be completed before implementation.
- Every module should have a single responsibility.
- AI predictions and business decisions should remain separate.
- Documentation is part of engineering, not an afterthought.

---

## Biggest Takeaways

Problem Statement

↓

Architecture

↓

Database Design

↓

Implementation

Never start from implementation.

---

## If asked to explain ECIP

1. Explain the problem.
2. Explain the architecture.
3. Explain the database.
4. Explain the implementation.
5. Explain future improvements.

Always follow this order.



# Sprint 1

## Task 1 – FastAPI Application

### Objective

Build the backend foundation of ECIP.

FastAPI serves as the entry point of the application and exposes REST APIs for external clients.

### Concepts

FastAPI

↓

ASGI

↓

REST API

↓

JSON Response

### Interview Questions

Q. Why FastAPI instead of Flask?

Answer:

FastAPI provides better performance, automatic request validation using Pydantic, built-in OpenAPI/Swagger documentation, asynchronous support through ASGI, and excellent type hint integration. These features make it well-suited for modern AI and backend applications.

---

Q. What is an API?

Answer:

An API is a contract that allows two applications to communicate. Clients send HTTP requests to the server, and the server processes those requests and returns structured responses, typically in JSON format.

---

Q. What is ASGI?

Answer:

ASGI (Asynchronous Server Gateway Interface) is a modern Python interface that enables asynchronous request handling. It allows FastAPI to process multiple requests concurrently, improving performance for I/O-intensive applications.

### Quick Revision

Client

↓

API

↓

Business Logic

↓

Database

↓

Response


## FastAPI Application

### What is FastAPI?

FastAPI is the entry point of the backend application.

It receives HTTP requests, calls the required business logic, and returns responses.

It does not contain business logic itself.

---

### Why FastAPI?

- High performance
- Built-in Swagger documentation
- Automatic request validation
- Async support
- Excellent type hint support

---

### What is app = FastAPI()?

It creates the FastAPI application object.

Everything in the backend (routes, middleware, exception handlers, logging, etc.) is attached to this object.

---

### Interview Question

Q. What is the purpose of `app = FastAPI()`?

Answer:

It creates the FastAPI application instance, which acts as the central object of the backend. All routes, middleware, event handlers, and application configuration are registered with this instance.

---

### Quick Revision

Client

↓

FastAPI

↓

Business Logic

↓

Database / AI

↓

Response




## First API Endpoint

### What is an API Route?

A route maps an HTTP request to a Python function.

Example:

GET /health

↓

health_check()

---

### Why Health Check?

A health endpoint verifies that the application is running correctly.

It is commonly used by:

- Load Balancers
- Kubernetes
- Docker
- Monitoring tools
- Developers

---

### What is a Decorator?

A decorator tells FastAPI which URL should execute a specific function.

Example:

@app.get("/health")

↓

GET request to /health

↓

Execute health_check()

---

### Why GET?

GET is used to retrieve information without modifying server data.

Health check only returns application status.

---

### What is Uvicorn?

Uvicorn is the ASGI server that runs FastAPI applications.

---

### Interview Questions

#### Q. What is an API endpoint?

An API endpoint is a URL that exposes a specific functionality of an application. Each endpoint is mapped to a function that processes the request and returns a response.

---

#### Q. Why is a health endpoint important?

Health endpoints allow monitoring systems, load balancers, container orchestration platforms, and developers to verify that the application is running correctly.

---

#### Q. Why use `--reload`?

The `--reload` option automatically restarts the server whenever source code changes are detected. It is useful during development but should not be used in production.

---

### Quick Revision

Client

↓

GET /health

↓

FastAPI Route

↓

Python Function

↓

JSON Response

## APIRouter

### What is APIRouter?

APIRouter is used to group related API endpoints into separate modules.

Instead of placing every endpoint in `main.py`, routes are organized by responsibility.

This improves readability, maintainability, and scalability.

---

### Why not keep everything in `main.py`?

As the application grows, `main.py` would become difficult to maintain.

Keeping routes in separate modules follows the Single Responsibility Principle and aligns with modular architecture.

---

### What does `include_router()` do?

`include_router()` registers all routes defined in an `APIRouter` instance with the main FastAPI application.

It allows the application to discover and expose those endpoints.

---

### Interview Questions

#### Q. What is APIRouter?

**Answer**

`APIRouter` is a FastAPI component used to organize related endpoints into reusable modules. It helps keep the codebase modular and easier to maintain.

---

#### Q. Why use `include_router()`?

**Answer**

It registers a router with the FastAPI application, making all endpoints defined in that router available without placing them directly in `main.py`.

---

### Quick Revision

FastAPI App

↓

include_router()

↓

APIRouter

↓

Endpoint

↓

Response

FastAPI App
      │
      ▼
include_router()
      │
      ▼
Router (Department)
      │
      ▼
Route
(Method + URL)
      │
      ▼
Endpoint Function
      │
      ▼
Business Logic
      │
      ▼
Response

## Configuration Management

### Why use a .env file?

Sensitive information such as API keys and database credentials should never be hardcoded into the source code.

A `.env` file stores environment-specific configuration separately from the application.

---

### Why use settings.py?

The application should have a single place responsible for reading configuration.

Other modules import the `settings` object instead of reading environment variables directly.

This improves maintainability and makes it easier to change how configuration is managed in the future.

---

### What does load_dotenv() do?

It loads variables from the `.env` file into the application's environment.

---

### What does os.getenv() do?

It retrieves the value of an environment variable by name.

---

### Interview Questions

#### Q. Why should API keys not be hardcoded?

Hardcoding secrets exposes them in source code and version control. Using environment variables improves security and allows different configurations for development, testing, and production.

---

#### Q. Why centralize configuration?

A centralized configuration layer avoids duplication, improves maintainability, and provides a single source of truth for application settings.

---

### Quick Revision

.env

↓

load_dotenv()

↓

settings.py

↓

Entire Application

## Pydantic Settings

### Why not use os.getenv()?

`os.getenv()` works, but it does not validate configuration.

Missing or incorrect environment variables may only cause failures later during execution.

---

### Why BaseSettings?

`BaseSettings` automatically:

- Reads values from `.env`
- Validates configuration
- Supports type conversion
- Provides default values
- Fails fast when required configuration is missing

---

### What is "Fail Fast"?

Fail Fast means detecting configuration errors immediately when the application starts instead of allowing them to surface later during execution.

This makes debugging easier and prevents applications from running in an invalid state.

---

### Interview Questions

#### Q. Why use Pydantic Settings instead of os.getenv()?

**Answer**

Pydantic Settings provides automatic validation, type conversion, default values, and centralized configuration management. It also detects missing or invalid configuration early during application startup.

---

#### Q. What is Fail Fast?

**Answer**

Fail Fast is the practice of validating critical configuration and dependencies during startup so that the application stops immediately if something is wrong, rather than failing unpredictably later.

---

### Quick Revision

.env

↓

Pydantic Settings

↓

Validated Configuration

↓

Entire Application


## Centralized Configuration

### Concept

The application should read configuration from a single source instead of hardcoding values.

Flow:

.env

↓

settings.py

↓

Application

---

### Single Source of Truth (SSOT)

A configuration value should exist in only one place.

Example:

APP_NAME

↓

settings.py

↓

Entire Application

This avoids duplication and reduces maintenance effort.

---

### Why import `settings` instead of creating `Settings()` everywhere?

The application should use one shared configuration object.

Creating multiple instances is unnecessary and makes configuration management harder.

---

### Interview Questions

#### Q. What is a Single Source of Truth?

**Answer**

A Single Source of Truth (SSOT) means that a piece of information is maintained in one authoritative location. All parts of the application reference that location instead of duplicating the same value in multiple places.

---

#### Q. Why centralize configuration?

**Answer**

Centralized configuration improves maintainability, consistency, and security. Changes can be made in one place and automatically reflected throughout the application.

# Sprint 1 – Database Design

## Why Design Before Coding?

The database defines the structure of the entire application.

Every API, AI model, business rule, and dashboard depends on the underlying data model.

Designing the schema first ensures consistency, avoids major refactoring later, and reflects how enterprise software projects are planned.

---

## Key Principle

Model the business domain first.

Implement the code second.

A well-designed database simplifies application development, while a poor design leads to duplicated logic, inconsistent data, and difficult maintenance.

# Sprint 1 – Task 2

## Domain Modeling

### What is Domain Modeling?

Domain Modeling is the process of identifying the key business entities and their relationships before designing the database.

It focuses on representing the real-world business rather than immediately creating tables or writing code.

---

### Core Design Principle

Separate **business data** from **AI-generated data**.

Business data is the source of truth.

AI outputs are derived data and should evolve independently.

---

### Core Entities

1. Complaint
   - Original complaint information.

2. Prediction
   - AI-generated insights such as severity, category, sentiment, confidence, and model version.

3. Employee
   - Employee details, skills, and workload.

4. Assignment
   - Maps complaints to employees and tracks assignment lifecycle.

5. Audit Log
   - Records significant events for traceability and compliance.

---

### Interview Questions

#### Q. What is Domain Modeling?

**Answer**

Domain Modeling identifies the core business entities, their responsibilities, and relationships before implementing the database. It ensures that the data model reflects the business accurately and remains maintainable as the application evolves.

---

#### Q. Why separate Complaint and Prediction?

**Answer**

The complaint is immutable business data and acts as the source of truth. Predictions are AI-generated insights that may change as models improve. Separating them supports model versioning, reprocessing, and a more stable database schema.

---

### Quick Revision

Complaint

↓

Prediction

↓

Assignment

↓

Audit Trail


# Complaint Entity Design

## Design Principle

The Complaint entity stores only original business data.

It does **not** store AI-generated insights.

The complaint is the source of truth and should remain immutable except for lifecycle fields such as status and timestamps.

---

## Fields

### Complaint ID

- Unique identifier.
- Generated by the system.
- Never changes.

---

### Customer ID

- References the customer.
- Avoids duplicating customer information.
- Supports normalization.

---

### Complaint Text

- Original customer complaint.
- Never modified by AI.

---

### Source

- Origin of the complaint.
- Examples: Email, Web Portal, Mobile App, Call Center.

---

### Language

- Original complaint language.
- Used for translation and analytics.

---

### Status

Represents the complaint lifecycle.

Example:

Received

↓

Processing

↓

Assigned

↓

Resolved

↓

Closed

---

### External Reference

Stores identifiers from external systems such as CRM or ticketing platforms.

---

### Created At

Creation timestamp.

Never changes.

---

### Updated At

Updated whenever the complaint record changes.

---

## Interview Questions

### Q. Why keep Complaint Text immutable?

**Answer**

The original complaint is the source of truth. AI models can be rerun in the future, so preserving the original input ensures reproducibility, auditing, and consistent model evaluation.

---

### Q. What is database normalization?

**Answer**

Normalization reduces data duplication by storing each type of information in its appropriate entity and linking entities through identifiers instead of repeating data.

---

### Q. What is YAGNI?

**Answer**

"You Aren't Gonna Need It" is a software engineering principle that advises against adding features or fields before they are actually required. It keeps systems simpler, easier to maintain, and avoids unnecessary complexity.


# Prediction Entity Design

## Purpose

The Prediction entity stores AI-generated insights derived from a complaint.

It contains interpretations, recommendations, and confidence scores rather than original business data.

---

## Fields

### Prediction ID

- Unique identifier.
- Generated by the system.

---

### Complaint ID

- Links the prediction to its complaint.

---

### Severity Score

- Numeric score from 0 to 100.
- Represents the seriousness of the complaint.

---

### Priority

- Business urgency.
- Examples: Low, Medium, High, Critical.

---

### Category

- Business classification of the complaint.
- Should remain configurable for different industries.

---

### Root Cause

- AI's best estimate of the underlying issue.

---

### Sentiment

- Overall customer sentiment.
- Positive, Neutral, or Negative.

---

### Suggested Resolution

- Recommended next action for reviewers.

---

### Explanation

- Human-readable reasoning behind the prediction.

---

### Confidence Score

- AI confidence in its prediction.
- Used to support human review decisions.

---

## Interview Questions

### Q. Why separate Severity and Priority?

**Answer**

Severity measures the seriousness of the issue, while Priority represents the urgency of business action. A complaint can have medium severity but high priority due to compliance or operational requirements.

---

### Q. Why store a confidence score?

**Answer**

Confidence allows the system to determine when AI predictions are reliable and when a complaint should be escalated for human review.

# Employee Entity Design

## Purpose

The Employee entity stores operational information required by the Assignment Engine.

It is not an HR database.

Only information relevant to complaint routing is stored.

---

## Fields

### Employee ID

- Unique employee identifier.

---

### Employee Name

- Display name.

---

### Department

- Business function.

Examples:

- Payments
- Cards
- Loans
- Fraud

---

### Skills

- Employee expertise.

Used for intelligent complaint assignment.

---

### Current Workload

- Number of active complaints.

Helps balance work across employees.

---

### Availability

Examples:

- Available
- Busy
- On Leave
- Offline

---

### Experience Level

Examples:

- Junior
- Mid
- Senior
- SME

---

## Interview Questions

### Q. Why store skills separately from department?

**Answer**

Department identifies organizational ownership, while skills identify specific expertise. Intelligent assignment requires both dimensions.

---

### Q. Why shouldn't Complaint contain Employee ID directly?

**Answer**

Assignments change over time. Separating Assignment into its own entity preserves assignment history, supports reassignment, and improves auditability.

---

### Quick Revision

Complaint

↓

Assignment

↓

Employee

# Sprint 1 – Task 3

## What is an ORM?

ORM (Object Relational Mapper) is a software layer that maps Python objects to database tables.

It allows developers to work with Python classes and objects instead of writing SQL for every database operation.

---

## Why use an ORM?

Advantages:

- Cleaner code
- Better maintainability
- Database abstraction
- Easier CRUD operations
- Improved readability
- Reduced boilerplate SQL

---

## Does ORM replace SQL?

No.

An ORM generates SQL automatically for common operations.

Developers still need SQL knowledge for optimization, reporting, and complex queries.

---

## Why SQLAlchemy?

SQLAlchemy is the industry-standard ORM for Python applications.

It is widely used with FastAPI because it is flexible, powerful, and production-ready.

---

## Architecture

FastAPI

↓

Service Layer

↓

SQLAlchemy

↓

PostgreSQL

---

## Interview Questions

### Q. What is an ORM?

**Answer**

An ORM maps programming language objects to relational database tables, allowing developers to interact with databases using objects instead of writing SQL for every operation.

---

### Q. Why use SQLAlchemy?

**Answer**

SQLAlchemy provides a robust ORM and SQL toolkit for Python. It improves maintainability, supports multiple databases, integrates well with FastAPI, and allows developers to combine ORM features with raw SQL when needed.


# Database Layer Architecture

## Why separate the database layer?

Enterprise applications separate responsibilities to improve maintainability.

The database layer is divided into:

- Base
- Session
- Models
- Repositories

Each component has a single responsibility.

---

## Base

Defines the parent class inherited by all database models.

---

## Session

Responsible for creating database sessions and managing connections.

---

## Models

Represent database tables.

Each model maps one Python class to one database table.

---

## Repository

Contains all database access logic.

Repositories isolate SQLAlchemy from the rest of the application.

---

## Layered Architecture

Client

↓

API

↓

Service

↓

Repository

↓

Database

---

## Interview Questions

### Q. What is the Repository Pattern?

**Answer**

The Repository Pattern separates database access logic from business logic by providing a dedicated layer responsible for interacting with the database. This improves maintainability, testability, and separation of concerns.

---

### Q. Why not query the database directly from FastAPI?

**Answer**

Keeping database queries inside repositories prevents tight coupling between the API and the database, making the application easier to maintain, test, and modify.

# SQLAlchemy Base

## What is Base?

The Base class is the parent class for all SQLAlchemy ORM models.

Every database table is represented as a Python class that inherits from Base.

---

## What is Declarative Mapping?

Declarative Mapping is SQLAlchemy's approach of defining database tables using Python classes.

Instead of writing SQL manually, developers define classes and SQLAlchemy maps them to relational tables.

---

## Why use DeclarativeBase?

`DeclarativeBase` is the modern SQLAlchemy 2.x approach for creating the base ORM class.

It replaces the older `declarative_base()` API and provides improved typing support and cleaner syntax.

---

## Interview Questions

### Q. Why inherit from Base?

**Answer**

Inheriting from Base registers the class with SQLAlchemy's ORM system, enabling it to map the class to a database table and manage its metadata.

---

### Q. What is Declarative Mapping?

**Answer**

Declarative Mapping is the process of defining database tables as Python classes, allowing SQLAlchemy to automatically map objects to relational database records.

---

## Quick Revision

Python Class

↓

Inherit Base

↓

SQLAlchemy Model

↓

Database Table


