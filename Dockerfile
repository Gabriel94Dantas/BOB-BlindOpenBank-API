FROM python:3.6
WORKDIR /bob
COPY ./requirements.txt /bob/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /bob
ENTRYPOINT ["python"]
CMD ["__init__.py"]