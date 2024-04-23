var host = "cpsc484-03.stdusr.yale.internal:8888";
document.addEventListener("DOMContentLoaded", function() {
    sp2tx.start();
});

var sp2tx = {
    socket: null,

    start: function() {
        var url = "ws://" + host + "/sp2tx";
        this.socket = new WebSocket(url);
        this.socket.onmessage = function (event) {
            var text = event.data.toLowerCase();
            if (text !== "") {
                console.log("/sp2tx received: " + text);
        
                // Process all elements with data-speech-command attribute
                document.querySelectorAll('.mentor-card').forEach(function(element) {
                    var mentorName = element.getAttribute('data-speech-command');

                    // Check if the spoken text matches the mentor's name
                    if (text.includes(mentorName)) {
                        var name = element.querySelector('.mentor-name').textContent;
                        var email = element.querySelector('.mentor-email').textContent;
                        var description = element.querySelector('.mentor-description').textContent;
            
                        // Call selectMentor with the mentor's details
                        selectMentor(name, email, description);
                    }
                });
            }
        };
    }
};

function selectMentor(name, email, description) {
    // Update the form with the selected mentor's details
    document.getElementById('mentor-name').value = name;
    document.getElementById('mentor-email').value = email;
    document.getElementById('mentor-description').value = description;

    // Submit the form
    document.getElementById('contact-form').submit();
}
