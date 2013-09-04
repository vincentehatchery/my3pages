//Initialise
$("#progressbar").progressbar({value: 1});

$(function() {
	var percentComplete=0;
    var wordCounts = {};
    progressLabel = $( ".progress-label" );
    
    $("textarea").keyup(function() {
        var matches = this.value.match(/\b/g);
        wordCounts[this.id] = matches ? matches.length / 2 : 0;
        var finalCount = 0;
        $.each(wordCounts, function(k, v) {
            finalCount += v;
        });
        $('#finalcount').html(finalCount);
        percentComplete = finalCount/750*100;
        percentComplete = percentComplete.toFixed(2);
       // $('#percent_complete').html(percentComplete);
        
  
        $("#progressbar").progressbar("value", parseInt(percentComplete));
        $('.progress-label').text(percentComplete + '% complete');
        //progressLabel.text( progressbar( "value" ) + "% complete" );
        
    }).keyup();
});