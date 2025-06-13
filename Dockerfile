FROM python:3.9-alpine3.13
LABEL maintainer="João"

ENV PYTHONUNBUFFERED 1 
# Disable output buffering, othrwise the output will not be displayed in real-time
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirement.dev.txt /tmp/requirement.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

#Virtual environment
# Create a virtual environment in /py, install the requirements, and clean up
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r /tmp/requirement.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user


# Add the virtual environment to the PATH
ENV PATH="/py/bin:$PATH"

USER django-user