## IIS-Python-WebAPI
This repository contains both FastAPI and Flask WebAPIs, which can be deployed on IIS.

## Prerequisite Module for IIS
The <a href="https://www.iis.net/downloads/microsoft/httpplatformhandler" title="https://www.iis.net/downloads/microsoft/httpplatformhandler" target="_blank">HttpPlatformHandler</a>
is a module that proxy requests to FastAPI or Flask WebAPI.

Download and install HttpPlatformHandler for python WebAPI deployment.

## Deployment
1. Create a python virtual environment for the WebAPI using either `venv` or `virtualenv`.
<pre lang="bash">
  pip install venv  #install venv
  cd X:\file_path  #change directory
  venv python_env  #create virtual environment
</pre>
<pre lang="bash">
  pip install virtualenv  #or install virtualenv
  cd X:\file_path  #change directory
  virtualenv python_env  #create virtual environment
</pre>
Change directory to the scripts folder of python virtual environment and activate to start the virtual environment. 
<pre lang="bash">
  cd X:\file_path\python_env\Scripts
  activate
</pre>
Packages for FastAPI
<pre lang="bash">
  pip install fastapi  #install fastapi
  pip install uvicorn  #install uvicorn
</pre>
Packages for Flask
<pre lang="bash">
  pip install flask  #install flask
  pip install flask-cors  #install flask-cors
  pip install waitress  #install waitress
</pre>
2. Add an application on IIS and set the `alias` for WebAPI `project name` which was defined in FastAPI or Flask python file.
3. The `web.config` should be placed in the application physical file path.
