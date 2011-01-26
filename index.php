<?
require_once('lib/slim/Slim.php');
require_once('lib/MustacheView.php');
require_once('lib/idiorm.php');
require_once('lib/flickr.php');
require_once('utils.php');
require_once('config.php');

Flickr::$api_key = $FLICKR_APIKEY;

ORM::configure('mysql:host=127.0.0.1;dbname='.$DATABASE_NAME);
ORM::configure('username', $DATABASE_USER);
ORM::configure('password', $DATABASE_PASS);

Slim::init('MustacheView');
Slim::config('log', true);
Slim::config('debug', $DEBUG);

Slim::get('/', 'home');
Slim::get('/nosotros/', 'about');
Slim::get('/trabajos/new', 'trabajo_form');
Slim::get('/trabajos/(:id)', 'trabajo_view');
Slim::post('/trabajos/', 'trabajo_add');
Slim::get('/contacto/', 'contact');
Slim::post('/contacto/', 'contact_send');
Slim::notFound('nada');

function home(){
    Slim::render('index.html', array('title'=>'- Bienvenido'));
}

function about(){
    Slim::render('about.html', array('title'=>'- ¿Qué es potaje?'));
}

function contact(){
    Slim::render('contact.html', array('title'=>'- Estemos en contacto'));
}

function contact_send(){
    Slim::render('index.html');
}

function nada() {
    Slim::render('404.html', array('title'=>'- 404, no encontrado'));
}

function trabajo_view($id=null){
    $trabajos = ORM::for_table('trabajo')->find_many();

    if ($id){
        $trabajo = ORM::for_table('trabajo')->find_one($id);
    }else{
        $trabajo = $trabajos[array_rand($trabajos)];
    }
    $params = array(
        'photoset_id'=> $trabajo->gallery_id,
        'extras'    => 'description,original_format,tags,url_m',
    );
    $result_list = Flickr::call('photosets.getPhotos', $params);
    Slim::log($result_list->stat);
    Slim::render( 
        'index.html',
        array(
            'trabajos' => $trabajos,
            'trabajo' => $trabajo,
            'photos' => $result_list->photoset->photo,
            'title'=>'- Trabajos '.$trabajo->name,
        )
    );
}

function trabajo_form(){
    $trabajos = ORM::for_table('trabajo')->find_many();

    Slim::render( 
        'trabajo_form.html',
        array(
            'trabajos' => $trabajos,
        )
    );
}

function trabajo_add(){
    $params = Slim::request()->post();
    $trabajo = ORM::for_table('trabajo')->create();
    $trabajo->name = $params['name'];
    $trabajo->slug = slugify($params['name']);
    $trabajo->gallery_id = $params['gallery_id'];
    $trabajo->description = $params['description'];
    $trabajo->save();
    Slim::redirect( 
        '/trabajos/',
        301
    );
}

Slim::run();

?>
