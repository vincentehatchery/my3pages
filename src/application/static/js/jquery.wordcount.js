$(function() {
    var wordCounts = {};
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
        $('#perecent_complete').html(percentComplete);
        
        //$('#finalcount').html(finalCount + " words written and " + perecentComplete +"% complete");
        
        
    }).keyup();
});