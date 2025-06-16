# Socket.IO and Celery

we used WebSockets and Broadcaster to get task status updates without server polling

## Objectives


1. Add Socket.IO support to a FastAPI application
2. Emit Socket.IO messages in a Celery worker

## Background

Socket.IO is library that simplifies the building of real-time, event-based applications. 