function addingUserComment(userId, bookId, addingData) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/books/${userId}>/${bookId}/reviews`,
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(addingData),
      success: function(result) {
        // Handle success (e.g., update the review in the UI)
        console.log('Review updated:', result);
      },
      error: function(xhr, status, error) {
        // Handle error
        console.error('Error adding review:', status, error);
      }
    });
};
$(document).ready(function () {
    $('ul.books').on('click', '.review', function () {
        const userId = $('ul.books').data('user-id');
        const bookId = $(this).data('id');
        const addingComment= prompt('Enter review comment:');
        const addingRating = prompt('Enter rating:');
        if (addingRating && addingComment) {
          const addingReview = {
            rating: addingRating,
            text: addingComment
          };
          addingUserComment(userId, bookId, addingReview);
        };
    });
});