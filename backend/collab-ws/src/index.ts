import express from "express";
import expressWebsockets from "express-ws";
import { Hocuspocus } from "@hocuspocus/server";

// Configure Hocuspocus
const hocuspocus = new Hocuspocus({});

// Setup your express instance using the express-ws extension
const { app } = expressWebsockets(express());

// A basic http route
app.get("/", (request, response) => {
  response.send("Hello World!");
});

// Add a websocket route for Hocuspocus
// You can set any contextual data like in the onConnect hook
// and pass it to the handleConnection method.

app.ws("/collaboration", (websocket, request) => {
  const context = {
    user: {
      id: 1234,
      name: "Jane",
    },
  };

  hocuspocus.handleConnection(websocket, request, context);
});

// Start the server
app.listen(process.env.PORT, () =>
  console.log("Listening on port " + process.env.PORT)
);
