$(document).ready(function () {
    const userId = $('div.chat-window').data('user-id');
    
    // Function to fetch messages
    function fetchMessages() {
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5001/api/v1/messages',
            contentType: 'application/json',
            success: function(data) {
                $('#chat-messages').empty();
                data.forEach(message => {
                    let messageClass = message.user_id === userId ? 'message-sent' : 'message-received';
                    $('#chat-messages').append(`<div class="${messageClass}">${message.message} - ${message.username}</div>`);
                });
            },
            error: function(xhr, status, error) {
                console.error('Error fetching messages:', status, error);
            }
        });
    }

    // Fetch messages every 5 seconds
    setInterval(fetchMessages, 5000);

    // Send message
    $('#send-button').on('click', function() {
        const message = $('#chat-input').val();

        if (!message) {
            alert('Please enter a message');
            return;
        }

        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5001/api/v1/messages',
            contentType: 'application/json',
            data: JSON.stringify({ user_id: userId, message: message }),
            success: function() {
                $('#chat-input').val('');
                fetchMessages();
            },
            error: function(xhr, status, error) {
                console.error('Error sending message:', status, error);
            }
        });
    });
});
