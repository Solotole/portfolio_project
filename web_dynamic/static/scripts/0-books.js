function generateBookHtml(books) {
    return `
        <li>
        <div class="text-container">
          <span>id: ${books.id}</span>
          <span>title: ${books.name}</span>
                <span>author: ${books.author}</span>
                <span>genre: ${books.genre}</span>
          <ul class="options">
            <li class="view" data-id="${books.id}">view</li>
            <li class="review" data-id="${books.id}">review</li>
          </ul>
            </div>
        </li>
    `;
  }
  function generateReviewsHtml(reviews) {
    return `
        <li>
            <div class="text-container">
                <span class="reviewcomment">review: ${reviews.text}</span>
          <span class="reviewrating">rate: ${reviews.rating}</span>
          <ul class="options">
                  <li class="delete" data-id="${reviews.id}">Delete</li>
            <li class="update" data-id="${reviews.id}">Update</li>
          </ul>
            </div>
        </li>
    `;
  }
  // function to delete review
  function deleteReview(reviewId) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/reviews/${reviewId}`,
      type: 'DELETE',
      success: function(result) {
        // Handle success (e.g., remove the deleted review from the UI)
        console.log('Review deleted:', result);
        $(`li[data-id=${reviewId}]`).remove();
      },
      error: function(xhr, status, error) {
        // Handle error
        console.error('Error deleting review:', status, error);
      }
    });
  };
  function updateReview(reviewId, updatedData) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/reviews/${reviewId}`,
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify(updatedData),
      success: function(result) {
        // Handle success (e.g., update the review in the UI)
        console.log('Review updated:', result);
        const $reviewItem = $(`li[data-id=${reviewId}]`);
        $reviewItem.find('.reviewcomment').text(`review: ${updatedData.text}`);
        $reviewItem.find('.reviewrating').text(`rate: ${updatedData.rating}`);
      },
      error: function(xhr, status, error) {
        // Handle error
        console.error('Error updating review:', status, error);
      }
    });
  }
  $(document).ready(function () {
    let selectedConstraint = {};
    // listen for changes on each input checkbox
    $('input[type="search"]').change(function() {
      const contraint = $(this).closest('li').text().trim();
      if ($(this).is(':checked')) {
        selectedConstaint[amenityName] = amenityName;
      } else {
        delete selectedConstraint[amenityName];
      }
      // Update the h4 tag inside the div Amenities
      let constraint = Object.values(selectedConstraint).join(', ');
      $('div.search li').text(amenitiesList || '');
    });
    const url = "http://127.0.0.1:5001/api/v1/books";
    const urlreviews = "http://127.0.0.1:5001/api/v1/reviews/";
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
    $('ul.books').on('click', '.view', function () {
      $('header').html('Reviews');
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
          data.forEach((reviews) => {
            const renderedReviewsHtml = generateReviewsHtml(reviews);
            $('ul.books').append(renderedReviewsHtml);
          });
        },
        error: (xhr, status, error) => {
          console.error('Error fetching data:', status, error);
        }
      });
    });
    $('ul.books').on('click', '.delete', function () {
      const reviewId = $(this).data('id');
      deleteReview(reviewId);
    });
    $('ul.books').on('click', '.update', function () {
      let reviewId = $(this).closest('li').data('id');
      const newComment= prompt('Enter new review comment:');
      const newRating = prompt('Enter new rating:');
      if (newRating && newComment) {
        const updatedReview = {
          rating: newRating,
          text: newComment
        };
        updateReview(reviewId, updatedReview);
      }
    });
  });
  