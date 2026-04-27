🚀 Logistics Tracking Microservice

🚀 Mini Logistics Brain API

A containerized logistics tracking system that simulates real-world package lifecycles with state transitions, metrics, and automated API workflows.

🧠 Overview

This project models a last-mile logistics backend where packages move through a controlled lifecycle:

CREATED → IN_TRANSIT → OUT_FOR_DELIVERY → DELIVERED

It’s designed to demonstrate:

backend architecture
API design
state management
containerization
workflow automation
⚙️ Tech Stack
Python (Flask) – REST API
MongoDB – NoSQL persistence
Docker + Docker Compose – containerized environment
Postman – automated API workflows & testing
📦 Features
✅ Package Lifecycle Management
Create packages with unique IDs
Enforce valid status transitions
Track timestamps and location
🔄 State Transition Engine

Prevents invalid flows:

❌ CREATED → DELIVERED (blocked)
✅ CREATED → IN_TRANSIT → ...
📊 Metrics & Analytics
Total package count
Aggregation by status
🔍 Filtering + Pagination
Filter by status
Paginated results for scalability
🧪 Automated Workflow (Postman)

One-click execution:

Create → Update → Fetch → Metrics
🐳 Run Locally (Zero Setup Chaos)
1. Clone the repo
git clone https://github.com/YOUR_USERNAME/mini-logistics-brain.git
cd mini-logistics-brain
2. Run with Docker
docker compose up --build
3. API is live at:
http://localhost:5000
📡 API Endpoints
Create Package
POST /packages
{
  "location": "Warehouse A"
}
Get Package
GET /packages/{id}
Update Status
PUT /packages/{id}/status
{
  "status": "IN_TRANSIT"
}
List Packages
GET /packages?status=CREATED&page=1&limit=10
Count
GET /packages/count
Metrics
GET /metrics
🔁 Automated Demo Flow (Postman)

This project includes a workflow-driven API demo:

Create package
Update status
Retrieve package
Fetch metrics

All executed in sequence using:

pm.execution.setNextRequest()

This simulates real backend workflows and state propagation.

🧱 Architecture
app/
 ├── routes/        # API endpoints
 ├── services/      # business logic
 ├── repositories/  # database access
 ├── utils/         # serialization
 └── extensions/    # Mongo connection

Separation of concerns:

Routes = HTTP layer
Services = logic
Repositories = data
🧪 Example Response
{
  "id": "2ab8a49b-faa3-4e21-9d75-66b61f77863e",
  "status": "IN_TRANSIT",
  "location": "Warehouse A",
  "updated_at": "2026-04-27T13:48:42Z"
}
🎯 Why This Project Matters

This isn’t just CRUD.

It demonstrates:

controlled state transitions
real-world domain modeling
containerized backend systems
automated API workflows
scalable query patterns
🚀 Future Improvements
JWT authentication
Event-driven architecture (Kafka / queues)
Frontend dashboard (React)
Swagger/OpenAPI docs
Deployment (AWS / GCP)
👤 Author

Gerin Wilde

💥 TL;DR

A production-style backend that:

enforces business rules
runs in Docker
exposes a clean API
demonstrates real engineering patterns