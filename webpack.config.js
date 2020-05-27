const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const autoprefixer = require('autoprefixer');
const path = require('path');


const styleConfig = {
  test: /\.(css|sass|scss)$/,
  use: [
    MiniCssExtractPlugin.loader,
    {
      loader: 'css-loader',
      options: {
        importLoaders: 2,
        sourceMap: true
      }
    },
    {
      loader: 'postcss-loader',
      options: {
        plugins: () => [
          autoprefixer
        ],
        sourceMap: true
      }
    },
    {
      loader: 'sass-loader',
      options: {
        sourceMap: true
      }
    }
  ]
};


module.exports = {
  entry: './assets/js/main.js',
  devtool: 'source-map',
  output: {
    path: path.resolve(__dirname, 'static/'),
    publicPath: '/static/',
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
          name: 'assets/[name].[ext]'
        }
      },
  
      {
        test: /\.(png|ico|jpe?g|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: 'assets/[name].[ext]'
        }
      },
      styleConfig
    ]

  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/style.css',
    }),
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
