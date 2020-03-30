FROM python:2.7.13-alpine

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pylint

COPY . .

# CMD [ "pylint", "./solution.py" ]
CMD [ "pylint", "./lint.py" ]
# CMD [ "python", "./scratch.py" ]
# CMD [ "python", "./solution.py" ]

