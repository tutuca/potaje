var webpack = require('webpack');
module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    lib: './node_modules',
    out: './assets/static/',
    src: './assets/',
    module_loaders: { 
      loaders: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel'
        },
        {
          test: /\.jsx$/,
          exclude: /node_modules/,
          loader: 'babel'
        }

      ]
    },
    sass: {
      options: {
        sourceMap: true,
        includePaths: [
          './assets/lib/bootstrap-sass-official/assets/stylesheets',
          './node_modules/slick-carousel/slick/'
        ]
      },
      dist: {
        options: {
          outputStyle: 'compact'
        },
        files: {
          '<%= out%>css/style.css': '<%= src%>sass/style.scss'
        }        
      }
    },
    copy: {
      main: {
        files: [
          {
            flatten:true,
            cwd: '<%= src%>images/',
            src: ['*'],
            dest: '<%= out%>images/',
            expand: true
          },
          {
            cwd: '<%= src%>lib/slick-carousel/slick/',
            src: ['*.gif'],
            dest: '<%= out%>images/',
            expand: true
          },
          {
            cwd: './assets/lib/slick.js/slick/fonts/',
            src: ['*.eot', '*.svg','*.ttf','*.woff'],
            dest: '<%= out%>fonts/',
            expand: true
          }
        ]
      }
    },
    webpack: {
      main: {
        entry: {
          main: "<%= src%>/js/main.js"
        },
        output: {
          path: "<%= out%>/js",
          filename: "main.js",
          sourceMapFilename: "main.js.map",
        },
        devtool: 'source-map',
        watch: true,
        module: "<%= module_loaders%>"
      },
      prod: {
        entry: {
          main: "<%= src%>/js/main.js"
        },
        output: {
          path: "<%= out%>/js",
          filename: "main.min.js",
        },
        module: "<%= module_loaders%>",
        plugins: [
          new webpack.optimize.UglifyJsPlugin(),
        ]
      }
    },
    watch: {
        scss: {
            files: [
                '<%= src%>sass/*.scss'
            ],
            tasks: ['sass']
        },
        config: {
            files: [
                'Gruntfile.js',
                'bower.json',
                'package.json'
            ],
            tasks: ['build']
        }
    },
  });
  // Plugin loading
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-webpack');
  // Task definition
  grunt.registerTask('build', ['webpack', 'copy', 'sass']);
  grunt.registerTask('default', ['build', 'watch']);

};
