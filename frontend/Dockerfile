FROM node:14

WORKDIR /var/app

COPY package.json /var/app/package.json
RUN yarn install

COPY . /var/app

RUN yarn build

CMD yarn start
