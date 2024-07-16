function booksSearched(books) {
    return (
        <li>
            <div class="text-container">
                <span>Title: ${books.name}</span>
                <span>Author: ${books.author}</span>
                <span>Genre: ${books.genre}</span>
                <ul class="options">
                    <li class="view" data-id="${books.id}">view</li>
                    <li class="review" data-id="${books.id}">review</li>
                </ul>
            </div>
        </li>
    );
}
$(document).ready(function() {
    $('#search-btn').on('click', function() {
        let criteria = $('input[name="search-criteria"]:checked').val();
        const term = $('#search-input').val();

        let url = "";
        if (!criteria || !term) {
            alert('Please select a search criterion and enter a search term.');
            return;
        }

        if (criteria === "Genre") {
            url = `http://127.0.0.1:5001/api/v1/books/genre/` + term;
        } else if (criteria === "Author") {
            url = `http://127.0.0.1:5001/api/v1/books/author/` + term;
        } else if (criteria === "Title") {
            url = `http://127.0.0.1:5001/api/v1/books/name/` + term;
        }
        $.ajax({
            type: 'GET',
            url: url,
            contentType: 'application/json',
            dataType: 'json',
            success: function(data) {
                console.log('Data received:', data);
                // emptying the current book list
                $('.books').empty();

                // Iterate through the response and add the books to the list
                data.forEach((book) => {
                    const searchedBooks = booksSearched(book);
                    $('ul.books').append(searchedBooks);
                });
            },
            error: function(xhr, status, error) {
                console.error('Error fetching books:', status, error);
            }
        });
    });
});