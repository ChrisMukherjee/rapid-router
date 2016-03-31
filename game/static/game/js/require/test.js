requirejs.config({
    //By default load any module IDs from js/lib
    baseUrl: 'game/js/require'
});

// Start the main app logic.
requirejs(['foo', 'bar'],
    function   (foo, bar) {
        //jQuery, canvas and the app/sub module are all
        //loaded and can be used here now.
        tellmeFoo();
        tellmeBar();
    });