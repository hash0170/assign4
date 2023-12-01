# dockerfile, Image, Container

FROM python:3.9


WORKDIR /app


COPY main.py /app

CMD ["python", "main.py"]
