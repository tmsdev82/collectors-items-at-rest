FROM python:3.6

RUN apt-get update || apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential  \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Create home directory for the new app user.
RUN mkdir -p /home/app

# Create an app user so our program doesn't run as root.
RUN groupadd -r appuser &&\
    useradd -r -g appuser -d /home/app -s /sbin/nologin -c "Docker image user" appuser

# Set the home directory to our app user's home.
ENV HOME=/home/app
WORKDIR $HOME

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt --ignore-installed

COPY . ./app
RUN pip install -e ./app

COPY ./config.py ./config.py
COPY ./manage.py ./manage.py

# Chown all the files to the app user.
RUN chown -R appuser:appuser $HOME

# Change to the app user.
USER appuser

CMD ["gunicorn", "--config", "config.py", "manage:app"]