function generateBookRecHtml(books) {
    return `
        <li>
        <div class="text-container">
          <span>Title: ${books.name}</span>
                <span>Author: ${books.author}</span>
                <span>Genre: ${books.genre}</span>
          <ul class="options">
            <li class="view" data-id="${books.id}">view</li>
          </ul>
            </div>
        </li>
    `;
  };
  $(document).ready(function () {
    const userId = $('ul.books').data('user-id');
    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:5001/api/v1/recommendations/${userId}`,
        contentType: 'application/json',
        dataType: 'json',
        success: (data) => {
          console.log('Data received:', data);
          data.forEach((books) => {
            const renderedHtml = generateBookRecHtml(books);
            $('ul.books').append(renderedHtml);
          });
        },
        error: (xhr, status, error) => {
          console.error('Error fetching data:', status, error);
        }
    });
  });