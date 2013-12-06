/*
 jQuery autoSave v1.0.0 - 2013-04-05
 (c) 2013 Yang Zhao - geniuscarrier.com
 license: http://www.opensource.org/licenses/mit-license.php
 
 Edited: Vincent Alcantara
 Comment: added autosaveName to allow to pass in a variable name to save to local storage.

 */
(function($) {
    $.fn.autoSave = function(callback, ms, autosaveName) {
        return this.each(function() {
            var timer = 0, 
                $this = $(this),
                delay = ms || 1000;
            $this.keyup(function() {
                clearTimeout(timer);
                var $context = $this.val();
                if(localStorage) {
                	localStorage.setItem(autosaveName, $context);
                   // alert('Auto save name is in jquery is:' + autosaveName);
                }
                timer = setTimeout(function() {
                    callback();
                }, delay);
            });
        });
    };
})(jQuery);