module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-browserify'); 
  
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    browserify: {
      all: {
        src: 'assets/js/app.js',
        dest: 'static/js/app.js'
      },
    },
    sass: {
      options: {
        includePaths: ['assets/sass'],
        sourceComments: 'none',
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'static/css/styles.css': 'assets/sass/styles.scss'
        }        
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },
      js: {
        files: 'assets/js/*.js',
        tasks: ['uglify', 'concat']
      },
      sass: {
        files: 'assets/scss/**/*.scss',
        tasks: ['sass']
      }
    }
  });

  grunt.registerTask('build', ['sass', 'browserify']);
  grunt.registerTask('default', ['build','watch']);
}