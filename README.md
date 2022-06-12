# misp-gateway

A Python ([FastAPI](https://github.com/tiangolo/fastapi)) based API gateway for MISP.

## What is for

- To prevent adding false positives
- To enrich an event / attribute

## How it works

The gateway works as a proxy for a MISP server.
You can intercept a request to a MISP server and transform it as you want.

You can set transform functions for the following API endpoints.

- `POST /events/add`
- `PUT /events/edit/{event_id}`
- `POST /events/edit/{event_id}`
- `POST /attributes/add/{event_id}`
- `PUT /attributes/edit/{attribute_id}`
- `POST /attributes/edit/{attribute_id}`

You can use all other MISP API endpoints via the gateway. But note that a request is just proxied to a server.

## Docs

- [Installation](https://github.com/ninoseki/misp-gateway/wiki/Installation)
- [Recipes](https://github.com/ninoseki/misp-gateway/wiki/Recipes)
