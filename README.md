py -m venv venv\
activate venv: venv\Scripts\activate

build Docker image:
docker build -t my-python-app .
run image:
docker run -it --rm --name my-running-app my-python-app
