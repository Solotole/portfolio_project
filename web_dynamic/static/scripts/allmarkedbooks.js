$(document).ready(function() {
    // accessing user id
    const userId = $('ul.read-books-list').data('user-id');

    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:5001/api/v1/users/${userId}/read`,
        contentType: 'application/json',
        success: function(data) {
            const readBooksList = $('ul.read-books-list');
            // looping over the data returned
            data.forEach((book) => {
                const bookItem = `
                    <li>
                        <div class="text-container">
                            <span>Title: ${book.name}</span>
                            <span>Author: ${book.author}</span>
                            <span>Genre: ${book.genre}</span>
                        </div>
                    </li>
                `;
                readBooksList.append(bookItem);
            });
        },
        // addressing an error
        error: function(xhr, status, error) {
            console.error('Error fetching read books:', status, error);
        }
    });
});
