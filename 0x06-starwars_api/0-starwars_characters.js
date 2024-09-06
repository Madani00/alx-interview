#!/usr/bin/node
const request = require('request');
const argv = process.argv;

if (argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <film number>');
  process.exit(1);
}
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(name);
    }
  }
});
