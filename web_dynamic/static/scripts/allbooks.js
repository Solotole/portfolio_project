function generateBookHtml(books) {
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
            </div>
        </li>
    `;
  };
  $(document).ready(function () {
    // let selectedConstraint = {};
    // listen for changes on each input checkbox
    // $('input[type="search"]').change(function() {
      // const contraint = $(this).closest('li').text().trim();
      // if ($(this).is(':checked')) {
        // selectedConstaint[amenityName] = amenityName;
      // } else {
        // delete selectedConstraint[amenityName];
      // }
      // Update the h4 tag inside the div Amenities
      // let constraint = Object.values(selectedConstraint).join(', ');
      //$('div.search li').text(amenitiesList || '');
    // });
    const url = "http://127.0.0.1:5001/api/v1/books";
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
