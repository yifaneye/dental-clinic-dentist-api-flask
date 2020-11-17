From alpine:latest

RUN apk add --no-cache py-pip
RUN pip3 install --upgrade pip

COPY ./dentistAPI /dentistAPI
WORKDIR /dentistAPI

RUN pip3 install -r requirements.txt

EXPOSE 5001

WORKDIR /dentistAPI/dentistAPI
ENTRYPOINT ["python3"]
CMD ["__init__.py"]