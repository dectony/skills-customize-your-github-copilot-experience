// MessagesController.cs
// Starter code for the Intro to ASP.NET assignment

using Microsoft.AspNetCore.Mvc;

namespace MessagesApi.Controllers;

[ApiController]
[Route("[controller]")]
public class MessagesController : ControllerBase
{
    // In-memory list of messages
    private static readonly List<string> _messages = new()
    {
        "Hello, world!",
        "Welcome to ASP.NET Core.",
        "Keep coding!"
    };

    // Task 2: GET /messages
    // TODO: Add an endpoint that returns all messages in _messages

    // Task 2: GET /messages/{id}
    // TODO: Add an endpoint that returns a single message by index.
    //       Return 404 if the index is out of range.

    // Task 3: POST /messages
    // TODO: Add an endpoint that accepts a JSON body with a "text" field,
    //       appends it to _messages, and returns 201 Created with the new message.
}
