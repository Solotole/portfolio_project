$(document).ready(function() {
    $('ul.books').on('click', '.mark-read', function() {
        const bookId = $(this).data('id');
        console.log(bookId);
        const userId = $('ul.books').data('user-id');
        const value = {
            book_id: bookId
        }

        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5001/api/v1/users/${userId}/read`,
            contentType: 'application/json',
            data: JSON.stringify(value),
            success: function(response) {
                alert('Book marked as read!');
            },
            error: function(xhr, status, error) {
                console.error('Error marking book as read:', status, error);
            }
        });
    });
});
