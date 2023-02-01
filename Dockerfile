FROM osgeo/gdal:ubuntu-full-latest

WORKDIR /home/app/web

RUN apt update \
    && apt install -y gettext python3 python3-pip python3-venv python3-dev libpq-dev curl


COPY ./requirements.txt .
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

COPY . .

RUN chmod +x /home/app/web/scripts/entrypoint.sh

ENTRYPOINT ["sh", "/home/app/web/scripts/entrypoint.sh"]