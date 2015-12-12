function prepCountdown() {
    $.ajax({url: "http://127.0.0.1:8000/api/nextgame"}).done(function(data){
        updateCountdown(new Date(data.date + " " + data.time))
    })
}

function diffDays(d1, d2) {
    return Math.floor((d2-d1) / (1000 * 60 * 60 * 24));
}

function diffHours(d1, d2) {
    return Math.floor((d2-d1) / (1000 * 60 * 60)) % 24;
}

function diffMinutes(d1, d2) {
    return Math.floor((d2-d1) / (1000 * 60)) % 60;
}

function diffSeconds(d1, d2) {
    return Math.floor((d2-d1)/ 1000) % 60;
}

function updateField(id, content) {
    var child = $(id).find("small");
    $(id).text(content);
    $(id).append(child);
}

function updateCountdown(date) {
    var now = new Date(Date.now());
    updateField("#countdown-days", diffDays(now, date));
    updateField("#countdown-hours", diffHours(now, date));
    updateField("#countdown-mins", diffMinutes(now, date));
    updateField("#countdown-secs", diffSeconds(now, date));
    window.setTimeout(updateCountdown, 1000, date);
}

$(document).ready(prepCountdown);


/*
$(document).ready(function updateCountdown(cnt) {
    var secsText = "<small>secs</small>";
    console.log("A");
    console.log(cnt);
    if(typeof cnt != "number") {
        cnt = 0;
    }
    console.log(cnt);
    var secs = $("#countdown-secs");
    var tmp = secs.find("small");
    secs.text(cnt);
    secs.append(tmp);
    cnt++;
    console.log("B");
    window.setTimeout(updateCountdown, 1000, cnt);
    console.log("C");
})
*/
