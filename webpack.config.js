const path = require('path');

module.exports = {
  entry: './assets/js/main.js',
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname, 'static/js/'),
    filename: 'main.js'
  }
};
