/*
* On the client, poll for the timestamp file and check to see if a new timestamp has been deployed.
* If so, refresh the client.
*/

var reloadTimestamp = null;

var getTimestamp = function() {
    // get the timestamp on page load
    if (reloadTimestamp == null) {
        checkTimestamp();
    }
    
    // continually check the timestamp every three minutes
    setInterval(checkTimestamp, 180000);
}

var checkTimestamp = function() {
    $.ajax({
        'url': 'live-data/timestamp.json',
        // bust the browser cache
        'cache': false,
        'success': function(data) {
            var newTime = data['timestamp'];
            
            // if we haven't set a timestamp yet, set it
            if (reloadTimestamp == null) {
                reloadTimestamp = newTime;
            }
            
            // if the initial timestamp doesn't match the new one, refresh the page
            if (reloadTimestamp != newTime) {
                // set a cookie in case we need to do special things on this reload
                $.cookie('reload', true);
                
                window.location.reload(true);
            }
        }
    });
}

    getTimestamp();
    