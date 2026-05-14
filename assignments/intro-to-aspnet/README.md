# 📘 Assignment: Intro to ASP.NET

## 🎯 Objective

Build a simple web application using ASP.NET Core. You will learn how to create a project, define routes, handle HTTP requests, and return responses from a web API controller.

## 📝 Tasks

### 🛠️ Create an ASP.NET Core Web API Project

#### Description
Set up a new ASP.NET Core Web API project and verify it runs with a default endpoint.

#### Requirements
Completed program should:

- Create a new ASP.NET Core Web API project using the `dotnet new webapi` command
- Successfully build and run the project with `dotnet run`
- Return a valid JSON response when the default endpoint is accessed

### 🛠️ Add a Custom Controller with GET Endpoints

#### Description
Create a new controller for a `Messages` resource and define endpoints to list and retrieve messages.

#### Requirements
Completed program should:

- Define a `MessagesController` class that inherits from `ControllerBase` with the `[ApiController]` and `[Route]` attributes
- Include a `GET /messages` endpoint that returns a list of at least three hardcoded messages
- Include a `GET /messages/{id}` endpoint that returns a single message by its index
- Return a `404 Not Found` response when the requested index does not exist

### 🛠️ Add a POST Endpoint to Accept User Input

#### Description
Extend the controller to accept new messages submitted by the client in the request body.

#### Requirements
Completed program should:

- Define a `POST /messages` endpoint decorated with `[HttpPost]`
- Accept a JSON request body containing a `text` field
- Append the new message to the in-memory list and return it with a `201 Created` response
