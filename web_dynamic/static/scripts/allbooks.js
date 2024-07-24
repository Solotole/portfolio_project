function generateBookHtml(books) {
  const downloadUrl = `http://127.0.0.1:5001/api/v1/books/download/${books.id}`;
    return `
        <li>
          <div class="text-container">
            <span>Title: ${books.name}</span>
            <span>Author: ${books.author}</span>
            <span>Genre: ${books.genre}</span>
            <ul class="options">
              <li class="view" data-id="${books.id}">view</li>
              <li class="review" data-id="${books.id}">review</li>
            </ul>
            <button class="mark-read" data-id="${books.id}">Mark</button>
            <a href="${downloadUrl}" download>Download</a>
          </div>
        </li>
    `;
  }
  $(document).ready(function () {
    url = "http://127.0.0.1:5001/api/v1/books";
    const userId = $('ul.books').data('user-id');
    $.ajax({
      type: 'GET',
      url: url,
      contentType: 'application/json',
      dataType: 'json',
      success: (data) => {
        console.log('Data received:', data);
        data.forEach((books) => {
          const renderedHtml = generateBookHtml(books);
          $('ul.books').append(renderedHtml);
        });
      },
      error: (xhr, status, error) => {
        console.error('Error fetching data:', status, error);
      }
    });
  });
