FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY app/requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY app .
CMD ["python","manage.py","migrate"]