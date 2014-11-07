module.exports = function(grunt) {
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-browserify'); 
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        browserify: {
            all: {
                src: ['assets/js/main.js'],
                dest: 'static/js/app.js'
            },
            options: {
                transforms: ['hbsfy'],
                extensions: ['.hbs']
            }
        },
        uglify: {
            all: {
                options: {
                    sourceMap: true,
                },
                files: {
                    'static/js/app.min.js': ['static/js/app.js'],
                },
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
            grunt: { files: ['Gruntfile.js'], tasks: ['build']},
            js: {
                files: ['assets/js/*.js', 'assets/js/**/*.js'],
                tasks: ['browserify', 'uglify']
            },
            sass: {
                files: 'assets/scss/**/*.scss',
                tasks: ['sass']
            }
        }
    });

    grunt.registerTask('build', ['sass', 'browserify', 'uglify']);
    grunt.registerTask('default', ['build','watch']);
};