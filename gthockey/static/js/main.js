function getDate(date) {
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    var post = "th";
    if (date.getDate() == 1) {
        post = "st";
    }

    if (date.getDate() == 2) {
        post = "nd";
    }
    return months[date.getMonth()] + " " + date.getDate() + post;
}

function getTime(date) {
    var hours = date.getHours() % 12;
    if (hours == 0) {
        hours = 12;
    }
    var mins = date.getMinutes();
    if (mins < 10) {
        mins = "0" + mins;
    }
    var am = date.getHours() < 12 ? "am" : "pm";
    return hours + ":" + mins + " " + am;
}

function prepCountdown() {
    $.ajax({url: "/api/nextgame"}).done(function(data){
        if (data.exists) {
            // Brittle Firefox fix to parse date
            data.date = data.date.replace("-", "/");
            data.date = data.date.replace("-", "/");

            var date = new Date(data.date + " " + data.time);
            $(".countdown-date").text(getDate(date));
            $(".countdown-team").text(data.team);
            console.log(data.logo);
            if (data.logo.length > 0) {
                $(".countdown-logo").attr("src", data.logo); // TODO Make this so it wont break
            }
            $(".countdown-location").text("@ " + data.location);
            $(".countdown-starttime").text("Puck Drop " + getTime(date))

            updateCountdown(date)
        } else {
            displayAltMessage();
        }
    }).fail(function(data) {
        displayAltMessage();
    });
}

function diffDays(d1, d2) {
    return Math.max(Math.floor((d2-d1) / (1000 * 60 * 60 * 24)), 0);
}

function diffHours(d1, d2) {
    return Math.max(Math.floor((d2-d1) / (1000 * 60 * 60)) % 24, 0);
}

function diffMinutes(d1, d2) {
    return Math.max(Math.floor((d2-d1) / (1000 * 60)) % 60, 0);
}

function diffSeconds(d1, d2) {
    return Math.max(Math.floor((d2-d1)/ 1000) % 60, 0);
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


function displayAltMessage() {
    $("#countdown-primary").addClass("hidden");
    $("#countdown-alt").removeClass("hidden");
}
