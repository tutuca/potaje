const CopyWebpackPlugin = require('copy-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const path = require('path');

module.exports = {
  entry: './assets/js/main.js',
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname, 'static/'),
    filename: 'main.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.(ttf|otf|woff|woff2|eot|svg)$/,
        loader: 'file-loader',
        options: {
          name: './assets/[name].[ext]'
        }
      },
  
      {
        test: /\.(png|ico|jpe?g|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: './assets/[name].[ext]'
        }
      },
      {
        test: /\.(css|sass|scss)$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          publicPath: '../',
          use: [
            'css-loader',
            {
              loader: 'postcss-loader', // Run post css actions
              options: {
                plugins: function () { // post css plugins, can be exported to postcss.config.js
                  return [
                    require('precss'),
                    require('autoprefixer')
                  ];
                }
              }
            },
            'resolve-url-loader',
            'sass-loader?sourceMap',      
          ]})
        }
    ]

  },
  plugins: [
    new ExtractTextPlugin('css/style.css'),
    new CopyWebpackPlugin([{
      from: 'assets/images',
      to: path.resolve(__dirname, 'static/assets/')
      }
    ])
  ],  
  stats: {
      colors: true
  },
};
