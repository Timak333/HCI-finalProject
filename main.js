var host = "cpsc484-03.stdusr.yale.internal:8888";
$(document).ready(function() {
  sp2tx.start();
});

var sp2tx = {
  socket: null,

  start: function() {
    var url = "ws://" + host + "/sp2tx";
    sp2tx.socket = new WebSocket(url);
    sp2tx.socket.onmessage = function (event) {
      var text = event.data.toLowerCase(); // Convert to lower case for case-insensitive comparison
      if (text !== "") {
        console.log("/sp2tx received: " + text);
    
        // Get all elements with data-speech-command attribute
        document.querySelectorAll('[data-speech-command]').forEach(function(element) {
          // Get the commands for the current element
          var commands = element.getAttribute('data-speech-command').split(", ");
    
          // Check if any command matches the spoken text
          commands.forEach(function(command) {
            if (text.includes(command.trim())) {
              if (element.type === 'radio' || element.type === 'checkbox') {
                element.checked = true; // Check the radio or checkbox
                element.form.submit(); 
              }
            }
          });
        });
      }
    };
  }
};
