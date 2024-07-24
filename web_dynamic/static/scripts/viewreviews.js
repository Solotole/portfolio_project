function generateReviewsHtml(reviews) {
  // genearates reviews of a specific book
  return `
    <li>
      <div class="text-container">
        <span class="reviewcomment">Review: ${reviews.text}</span>
        <span class="reviewrating">Rate: ${reviews.rating}</span>
        <ul class="options">
          <li class="delete" data-id="${reviews.id}">Delete</li>
          <li class="update" data-id="${reviews.id}">Update</li>
        </ul>
      </div>
    </li>
    `;
  }
$(document).ready(function () {
  const urlreviews = "http://127.0.0.1:5001/api/v1/reviews/";
  $('ul.books').on('click', '.view', function () {
    $('header').html('Reviews');
    // removing contentes of an element with class conatiner
    $('.container').remove();
    const bookId = $(this).data('id');
    console.log('Book ID:', bookId);
    $.ajax({
      type: 'GET',
      url: urlreviews + bookId,
      contentType: 'application/json',
      dataType: 'json',
      success: (data) => {
        console.log('Data received:', data);
        $('ul.books').empty();
        // looping over reviews data returned
          data.forEach((reviews) => {
            const renderedReviewsHtml = generateReviewsHtml(reviews);
            // appending a block of all reviews by a user
            $('ul.books').append(renderedReviewsHtml);
          });
      },
      error: (xhr, status, error) => {
        console.error('Error fetching data:', status, error);
      }
    });
  });
});