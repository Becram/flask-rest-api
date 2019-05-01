FROM python:3.6.1
MAINTAINER Bikram Dhoju <itsbecram@gmail.com>



# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# ENV C_FORCE_ROOT true
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /requirements.txt

# install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

# expose the app port
EXPOSE 8080

#Code ownership
RUN chown -R flask:flaskgroup /app

USER flask

# run the app server in development mode
ENTRYPOINT ["/app/entrypoint.sh"]
CMD [ "development" ]