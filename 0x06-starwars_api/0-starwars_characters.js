#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    printCharactersList(characterUrls, 0);
  }
});

function printCharactersList (characterUrls, index) {
  request(characterUrls[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characterUrls.length) {
        printCharactersList(characterUrls, index + 1);
      }
    }
  });
}
