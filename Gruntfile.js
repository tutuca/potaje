module.exports = function(grunt) {
  'use strict';
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      options: {
        includePaths: [
          './assets/lib/bootstrap-sass-official/assets/stylesheets',
          './assets/lib/slick.js/slick/'
        ]
      },
      dist: {
        options: {
          outputStyle: 'compact'
        },
        files: {
          './static/css/style.css': './assets/sass/style.scss'
        }        
      }
    },
    copy: {
      main: {
        files: [
          {
            flatten:true,
            cwd: './assets/images/',
            src: ['*.png', '*.jpg', '*.gif'],
            dest: './static/images/',
            expand: true
          },
          {
            cwd: './assets/lib/slick.js/slick/',
            src: ['*.gif', ],
            dest: './static/images/'
          },
          {
            cwd: './assets/lib/slick.js/slick/fonts/',
            src: ['*.eot', '*.svg','*.ttf','*.woff'],
            dest: './static/fonts/'
          }
        ]
      }
    },
    concat: {
      options: {
        separator: ';'
      },
      lib: {
        src: [
          './assets/lib/jquery/dist/jquery.js',
          './assets/lib/bootstrap-sass-official/assets/javascripts/bootstrap/scrollspy.js',
          './assets/lib/bootstrap-sass-official/assets/javascripts/bootstrap/affix.js',
          './assets/lib/jquery-pjax/jquery.pjax.js',
          './assets/lib/slick.js/slick/slick.js'
        ],
        dest: './static/js/lib.js'
      },
      main: {
        src: [
          'assets/js/main.js'
        ],
        dest: './static/js/main.js'
      }
    },
    uglify: {
      options: {
        mangle: true,
        sourceMap: true
      },
      lib: {
        files: {
          './static/js/lib.min.js': './static/js/lib.js'
        }
      },
      main: {
        files: {
          './static/js/main.min.js': './static/js/main.js'
        }
      }
    },
    watch: {
      scss: {
        files: [
         //watched files
          'assets/sass/*.scss',
          ],
        tasks: ['sass']
      },
      js : {
        files: [
          'assets/js/*.js',
        ],
        tasks: ['copy:main', 'concat:main']
      },
      config: {
        files: [
          'Gruntfile.js',
          'bower.json',
          'package.json'
        ],
        tasks: ['copy', 'concat', 'sass']
      }
    }
  });
  // Plugin loading
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');

  // Task definition
  grunt.registerTask('build', ['copy', 'sass', 'concat', 'uglify']);
  grunt.registerTask('default', ['build', 'watch']);

};
