## IIS-Python-WebAPI
This respository has both fastapi and flask WebAPI deployed on IIS.

## Prerequisite Module for IIS
The <a href="https://www.iis.net/downloads/microsoft/httpplatformhandler" title="HttpPlatformHandler" target="_blank">HttpPlatformHandler</a>
is a module that proxy requests to fastapi or flask WebAPI.

## Deployment
1. Create a Python virtual environment for WebAPI.
2. Add an application on IIS and set the alias for WebAPI project name which was defined in fastapi or flask python file.
3. The web.config should be placed in the application physical file path.
