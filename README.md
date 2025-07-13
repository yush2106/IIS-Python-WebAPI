## IIS-Python-WebAPI
This repository contains both FastAPI and Flask WebAPIs, which can be deployed on IIS.

## Prerequisite Module for IIS
The <a href="https://www.iis.net/downloads/microsoft/httpplatformhandler" title="https://www.iis.net/downloads/microsoft/httpplatformhandler" target="_blank">HttpPlatformHandler</a>
is a module that proxy requests to fastapi or flask WebAPI.
Download and install HttpPlatformHandler for python WebAPI deployment.

## Deployment
1. Create a python virtual environment for the WebAPI using either `venv` or `virtualenv`.
2. Add an application on IIS and set the `alias` for WebAPI `project name` which was defined in fastapi or flask python file.
3. The `web.config` should be placed in the application physical file path.
